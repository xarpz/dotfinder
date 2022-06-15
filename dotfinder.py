import argparse
import sys
from extractors.crtsh import get_crtsh
from extractors.urlscan import get_urlscan
from extractors.waybackarchive import get_wba
from extractors.hackertarget import get_hackertarget
from extractors.virustotal import get_virustotal
from extractors.threatcrowd import get_threatcrowd
from extractors.bufferover import get_bufferover

version = 1.0

list = []

def banner():
    print(f"""
     _       _     __ _           _           
    | |     | |   / _(_)         | |          
  __| | ___ | |_ | |_ _ _ __   __| | ___ _ __ 
 / _` |/ _ \| __||  _| | '_ \ / _` |/ _ \ '__|
| (_| | (_) | |_ | | | | | | | (_| |  __/ |   
 \__,_|\___/ \__||_| |_|_| |_|\__,_|\___|_| v{version}
\n    made by ~ github.com/Miguel-Galdin0\n""")

parser = argparse.ArgumentParser(description="dotfinder is a subdomain enumerator.")
parser.add_argument("-d", "--domain", help="Domain to enumerate.")
parser.add_argument("-s", "--silent", help="Only subs in output.", action='store_true')
parser.add_argument("-v", "--version", help="Show program version.", action='store_true')
args = parser.parse_args()

if args.version == True:
  print(f"dotfinder in version: {version}")
  sys.exit()

if args.silent != True:
    banner()

if args.domain != None:
  domain = args.domain
else:
  print("\033[31m[-]\033[m Program exiting! No input recived.")
  sys.exit()


if "http://" in domain:
  domain = domain.replace("http://", "")
elif "https://" in domain:
  domain = domain.replace("https://", "")


def main ():

  if args.silent != True:
    print(f"\033[35m[*]\033[m Enumerating subdomains from {domain}")

  try:
    virustotal_list = get_virustotal(domain)
    for sub in virustotal_list:
      if sub not in list:
        list.append(sub)
        print(sub)

    urlscan_list = get_urlscan(domain)
    for sub in urlscan_list:
      if sub not in list:
        list.append(sub)
        print(sub)
        
    crtsh_list = get_crtsh(domain)
    for sub in crtsh_list:
      if sub not in list:
        list.append(sub)
        print(sub)

    wba_list = get_wba(domain)
    for sub in wba_list:
      if sub not in list:
        list.append(sub)
        print(sub)

    haclertarget_list = get_hackertarget(domain)
    for sub in haclertarget_list:
      if sub not in list:
        list.append(sub)
        print(sub)

    bufferoverget_list = get_bufferover(domain)
    for sub in bufferoverget_list:
      if sub not in list:
        list.append(sub)
        print(sub)
        
    threatcrowd_list = get_threatcrowd(domain)
    for sub in threatcrowd_list:
      if sub not in list:
        list.append(sub)
        print(sub)

  except KeyboardInterrupt:
    print("\033[31m[-]\033[m Program exiting!")

  if args.silent != True:
    print(f"\033[32m[+]\033[m {len(list)} subdomains found from {domain}!")

if __name__ == '__main__':
  if domain == "pipe":
    pipe = sys.stdin.read().split()
    for url in pipe:
      domain = url
      main()
  else:
    main()
