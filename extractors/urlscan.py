import requests

def get_urlscan(domain):
    list = []
    resp = requests.get(f"https://urlscan.io/api/v1/search/?q=domain:{domain}")
    for numb in range(99):
        try:
            sub = resp.json()["results"][numb]["task"]["domain"]
            if f".{domain}" in sub:
                if sub not in list:
                    list.append(sub)
        except IndexError:
            break
    return list