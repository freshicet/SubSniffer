# 🕵️‍♂️ SubSniffer: The Subdomain Detective 🔍

Welcome to SubSniffer, your trusty sidekick in the thrilling world of cybersecurity! 🦸‍♀️🦸‍♂️

Born from the brilliant minds of a human and their AI assistant, SubSniffer is here to sniff out those sneaky stale subdomains that could be ripe for takeover. It's like a bloodhound, but for the digital realm! 🐕‍🦺💻

## 🌟 Features That'll Make You Go "Wow!"

- 📚 Devours subdomain lists like a bookworm on a binge
- 🔎 Scrutinizes DNS A records with the precision of a master detective
- 🏃‍♂️ Sprints through HTTP/HTTPS requests to check if IPs are still kicking
- 🕵️‍♀️ Digs deep with WHOIS lookups on those suspiciously quiet IPs
- 📊 Serves up results in a neat CSV file, because who doesn't love a good spreadsheet?

## 🛠️ Installation: Let's Get This Party Started!

1. Clone this repo faster than you can say "subdomain takeover"!
2. Make sure you've got Python 3.7+ (we're not living in the digital stone age here)
3. Install the dependencies with a magical incantation:
   ```
   pip install -r requirements.txt
   ```

## 🚀 Usage: Time to Unleash the Sniffer!

Fire up your terminal and let's roll:

```
python stale_subdomain_checker.py input_file.txt -o output_file.csv
```

- `input_file.txt`: Your list of subdomains (one per line, like a well-behaved queue)
- `-o output_file.csv`: Where you want the juicy results (default: `stale_records.csv`)

## 📊 Output: The Treasure Trove

SubSniffer will conjure up a CSV file with these golden columns:

- Subdomain (The suspect)
- IP (The last known address)
- Status (Alive, or... not so much)
- WHOIS Info (The backstory)
- Timestamp (When we caught 'em)

## 🎭 License and Usage: With Great Power...

SubSniffer is free as a bird! Use it, tweak it, share it – but remember, with great power comes great responsibility. Always get permission before you go snooping around others' domains!

## 📝 Note: Keep It Clean, Folks!

While SubSniffer is available to all, it's mainly for the cybersecurity pros and curious learners out there. Stay ethical, stay legal, and happy sniffing!

## 🗺️ Roadmap: The Future is Bright!

- [ ] Expand our sensory range beyond the usual 80/443 ports. Who knows what we might find?
- [ ] More features coming soon! Got ideas? We're all ears! 👂

Remember, in the world of cybersecurity, it's better to be the SubSniffer than the sub-sniffed! Happy hunting! 🕵️‍♂️🔍
