import requests

def get_threatcrowd(domain):
    list = []
    resp = requests.get(f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}")
    for numb in range(499):
        try:
            sub = resp.json()["subdomains"][numb]
            if f".{domain}" not in sub:
                if sub not in list:
                    list.append(sub.lower())
        except IndexError:
            break
        except Exception:
            break
    return list