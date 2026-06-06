import requests

# заголовки которые должны быть
good_headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
]

# заголовки которые лучше не светить
bad_headers = [
    "Server", "X-Powered-By", "X-AspNet-Version", "X-Generator"
]

url = input("url: ").strip()
if not url.startswith("http"):
    url = "https://" + url

try:
    r = requests.get(url, timeout=8, headers={"User-Agent": "Mozilla/5.0"})
except Exception as e:
    print(f"error: {e}")
    exit(1)

h = {k.lower(): v for k, v in r.headers.items()}

print(f"\n--- security headers ---")
score = 0
for header in good_headers:
    if header.lower() in h:
        print(f"[+] {header}: {h[header.lower()]}")
        score += 1
    else:
        print(f"[-] {header}: missing")

print(f"\n--- info leak ---")
for header in bad_headers:
    if header.lower() in h:
        print(f"[!] {header}: {h[header.lower()]}")

print(f"\nscore: {score}/{len(good_headers)}")
