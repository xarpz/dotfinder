import requests

def get_crtsh(domain):
    list = []
    resp = requests.get(f"https://crt.sh/?q=%.{domain}&output=json")
    for (key,value) in enumerate(resp.json()):
        if "*" not in value['name_value']:
            separate = value['name_value'].split("\n")
            for sub in separate:
                if sub not in list:
                    list.append(sub)
    return(list)