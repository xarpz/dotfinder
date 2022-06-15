from http.client import EXPECTATION_FAILED
import requests
import yaml
from yaml import Loader

def get_virustotal(domain):
    yaml_file = open('extractors/apiKeys/keys.yaml', 'r')
    data = yaml.load(yaml_file, Loader=Loader)
    apikey = data['virustotal']
    list = []
    resp = requests.get(f"https://www.virustotal.com/vtapi/v2/domain/report?domain={domain}&apikey={apikey}")
    for numb in range(99): 
        try:
            sub = resp.json()["subdomains"][numb]
            list.append(sub)
        except IndexError:
            break
        except Exception:
            break
    return list