import dns.resolver
import concurrent.futures
import argparse
from tqdm import tqdm
import csv
from datetime import datetime
from ipwhois import IPWhois
import json
import requests
from requests.exceptions import SSLError


def check_ip(ip):
    try:
        # First, try HTTP
        response = requests.get(
            f"http://{ip}", timeout=5, allow_redirects=False)
        active_codes = {200, 301, 302, 307, 308, 401, 403, 404, 426, 503}
        if response.status_code in active_codes:
            return "Active (HTTP)"
    except requests.RequestException:
        pass  # If HTTP fails, we'll try HTTPS

    try:
        # Try HTTPS
        response = requests.get(
            f"https://{ip}", timeout=5, allow_redirects=False, verify=False)
        active_codes = {200, 301, 302, 307, 308, 401, 403, 404, 426, 503}
        if response.status_code in active_codes:
            return "Active (HTTPS)"
    except SSLError as e:
        # Check if it's a certificate error
        if "SSL_ERROR_BAD_CERT_DOMAIN" in str(e):
            return "Active (HTTPS with cert error)"
    except requests.RequestException:
        pass

    return "Inactive"


def get_subdomains_from_file(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def get_whois_info(ip):
    try:
        obj = IPWhois(ip)
        results = obj.lookup_rdap(depth=1)
        return json.dumps({
            "asn_description": results.get("asn_description"),
            "country": results.get("asn_country_code"),
            "org": results.get("network", {}).get("name")
        })
    except Exception as e:
        return f"Whois lookup failed: {str(e)}"


def check_subdomain(subdomain):
    try:
        answers = dns.resolver.resolve(subdomain, 'A')
        results = []
        for rdata in answers:
            ip = rdata.to_text()
            status = check_ip(ip)
            whois_info = get_whois_info(ip) if "Inactive" in status else ""
            results.append((subdomain, ip, status, whois_info))
        return results
    except dns.resolver.NXDOMAIN:
        return [(subdomain, "N/A", "No such domain", "")]
    except dns.resolver.NoAnswer:
        return [(subdomain, "N/A", "No A record", "")]
    except Exception as e:
        return [(subdomain, "N/A", f"Error - {str(e)}", "")]


def main(subdomain_file, output_file):
    print(f"Reading subdomains from file: {subdomain_file}")
    subdomains = get_subdomains_from_file(subdomain_file)

    if not subdomains:
        print("No subdomains found in the file.")
        return

    print(
        f"Found {len(subdomains)} subdomains. Checking A records and performing Whois lookups...")

    stale_records = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_subdomain = {executor.submit(
            check_subdomain, subdomain): subdomain for subdomain in subdomains}
        for future in tqdm(concurrent.futures.as_completed(future_to_subdomain), total=len(subdomains)):
            subdomain = future_to_subdomain[future]
            try:
                results = future.result()
                for result in results:
                    subdomain, ip, status, whois_info = result
                    print(f"{subdomain}: {ip} ({status})")
                    if "Inactive" in status:
                        print(
                            f"Potential stale record found: {subdomain}: {ip}")
                        stale_records.append(result)
            except Exception as exc:
                print(f"{subdomain} generated an exception: {exc}")

    print(
        f"Writing {len(stale_records)} potential stale records to {output_file}")
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Subdomain', 'IP', 'Status',
                        'Whois Info', 'Timestamp'])
        for record in stale_records:
            writer.writerow(list(record) + [datetime.now().isoformat()])

    print("Scan complete. Results saved to file.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check for stale DNS A records and perform Whois lookups")
    parser.add_argument(
        "input_file", help="Path to file containing list of full subdomain names (one per line)")
    parser.add_argument("-o", "--output", default="stale_records.csv",
                        help="Path to output CSV file for stale records (default: stale_records.csv)")
    args = parser.parse_args()

    main(args.input_file, args.output)
