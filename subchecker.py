import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# список для перебора
wordlist = [
    "www", "mail", "ftp", "admin", "api", "dev", "test", "staging",
    "portal", "vpn", "blog", "shop", "cdn", "app", "dashboard",
    "login", "auth", "beta", "old", "support", "docs", "git",
    "jenkins", "jira", "monitor", "status", "internal", "secure"
]

def check(sub, domain):
    url = f"http://{sub}.{domain}"
    try:
        r = requests.get(url, timeout=4, allow_redirects=True)
        return url, r.status_code
    except:
        return None

domain = input("domain: ").strip()
print(f"checking {len(wordlist)} subdomains...\n")

found = []
with ThreadPoolExecutor(max_workers=20) as pool:
    futures = {pool.submit(check, s, domain): s for s in wordlist}
    for fut in as_completed(futures):
        res = fut.result()
        if res:
            url, code = res
            print(f"{url}  {code}")
            found.append(res)

print(f"\nfound: {len(found)}")
