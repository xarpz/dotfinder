from webbrowser import get
import requests

def get_bufferover(domain):
    list = []
    resp = requests.get(f"https://dns.bufferover.run/dns?q=.{domain}")
    numb = 0
    while True:
        try:
            sub = resp.json()["FDNS_A"][numb]
            numb = numb+1
            if sub != None:
                if sub[sub.find(',')+1:] not in list:
                    list.append(sub[sub.find(',')+1:])
        except IndexError:
            break
        except TypeError:
            break
        except Exception:
            break
    return list