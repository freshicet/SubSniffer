# Subdomain Checker

I made this tool, with the help of AI, to help with finding stale subdomains can be used to subdomain takeover since I work in the cyber security field. Anyone is free to use this!

This Python script checks for stale DNS A records by verifying the activity status of subdomains and performing WHOIS lookups on inactive IP addresses.

## Features

- Reads subdomains from a file
- Checks DNS A records for each subdomain
- Verifies if the IP is active using HTTP/HTTPS requests
- Performs WHOIS lookups on inactive IPs
- Outputs results to a CSV file

## Installation

1. Clone this repository or download the script files.

2. Ensure you have Python 3.7+ installed.

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script from the command line:

```
python stale_subdomain_checker.py input_file.txt -o output_file.csv
```

- `input_file.txt`: Path to a file containing a list of subdomains (one per line)
- `-o output_file.csv`: (Optional) Path to the output CSV file (default: stale_records.csv)

## Output

The script will generate a CSV file with the following columns:

- Subdomain
- IP
- Status
- WHOIS Info
- Timestamp

## License and Usage

This tool is free for anyone to use, modify, and distribute. However, please use it responsibly and ensure you have permission to scan and analyze the domains and IP addresses you're targeting.

## Note

While this tool is freely available, it is primarily intended for educational and professional use in the cybersecurity field. Always adhere to ethical guidelines and applicable laws when conducting security research or assessments.

## Roadmap

- [ ] looking at other ports than 80/443 to see if active.
