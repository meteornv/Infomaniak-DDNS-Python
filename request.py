import requests
from pushbullet import Pushbullet
import time
API_KEY=""
pb = Pushbullet(API_KEY)

def refresh_IP(domain, retry=3):
    api_endpoint = "https://infomaniak.com/nic/update?hostname="+domain+"&username=username&password=password"
    r = requests.post(url = api_endpoint) 
    pastebin_url = r.text
    if pastebin_url.startswith("nochg"):
        print(" No change for ",domain," The pastebin URL is:%s"%pastebin_url)
    elif pastebin_url.startswith("no_change"):
        print(" No change for ",domain," The pastebin URL is:%s"%pastebin_url)
    elif pastebin_url.startswith("good"):
        ip=pastebin_url.replace("good ",'')
        push = pb.push_note("Changement d'IP", "L'IP de "+domain+" est maintenant "+ip)
        print("Good for ",domain," The pastebin URL is:%s"%pastebin_url)
    else:
        if retry > 1:
            print("Retrying for ", domain," ...:",pastebin_url)
            time.sleep(600)
            refresh_IP(domain, retry=retry - 1)
        else:
            push = pb.push_note("Changement d'IP","Un problème est survenu lors du check de changement d'IP pour le domaine "+domain+" avec le message suivant: " + pastebin_url)
            print("Error. The pastebin URL is: %s" % pastebin_url)


domains=[""]
for x in domains:
    refresh_IP(x)

