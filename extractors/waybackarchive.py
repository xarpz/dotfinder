import requests
from urllib.parse import urlparse

def get_wba(domain):
    list = []
    resp = requests.get(f"http://web.archive.org/cdx/search/cdx?url=*.{domain}/*&output=json&fl=original&collapse=urlkey")
    for (key,value) in enumerate(resp.json()):
        if value[0] != "original" and f".{domain}" in value[0]:
            clean_url = urlparse(value[0]).hostname.lower()
            if ":" not in clean_url:
                if clean_url not in list:
                    list.append(clean_url)
    return(list)