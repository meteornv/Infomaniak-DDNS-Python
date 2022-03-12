import requests
subdomain=input("Enter your Subdomain (leave blank if none):") #this is your subdomain
domain=input("Enter your domain:") #this is your main domain
username=input("Enter your DDNS username:")#this is your dynamic DNS username
password=input("Enter your DDNS password:") #this is your dynamic DNS password
if subdomain=="":
    API_ENDPOINT = "https://infomaniak.com/nic/update?hostname="+domain+"&username="+username+"&password="+password
else:
    API_ENDPOINT = "https://infomaniak.com/nic/update?hostname="+subdomain+"."+domain+"&username="+username+"&password="+password

print(API_ENDPOINT)
r = requests.post(url = API_ENDPOINT) 
  
pastebin_url = r.text 
print("The pastebin URL is:%s"%pastebin_url) 