import requests
import os
import sys
import yaml
from yaml import Loader

def get_virustotal(domain):
    if os.path.dirname(sys.argv[0]) == "":
        dir = ""
    else:
        dir = f"{os.path.dirname(sys.argv[0])}/"
    yaml_file = open(f'{dir}extractors/apiKeys/keys.yaml', 'r')
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
