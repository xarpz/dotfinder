import requests

def get_hackertarget(domain):
    list = []
    resp = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}")
    for line in resp.text.split():
        sub = line[:line.find(',')]
        if domain in sub:
            list.append(sub)
    return(list)