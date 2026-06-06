# pentools

small scripts i use for recon and testing. nothing fancy.

---

**nmap_ai.py** — runs nmap on a target and sends output to groq ai, gets back a report in russian

```
pip install groq
sudo python3 nmap_ai.py
```

needs sudo for syn scan. free api key at console.groq.com

---

**subchecker.py** — checks a list of subdomains and shows which ones are alive

```
pip install requests
python3 subchecker.py
```

---

**headers.py** — checks http security headers on a site, shows what's missing

```
pip install requests
python3 headers.py
```

---

> only for authorized testing
