import requests
from tkinter import *
#define window
ws = Tk()
#define window title
ws.title("DDNS")
#define window size
ws.geometry('300x400')
#define window background
ws['bg'] = '#ffbf00'

#command to run when button is pressed
def printValue():
    subdomain1 = subdomain.get()
    domain1 = domain.get()
    username1 = username.get()
    password1 = password.get()
    Label(ws, text=f'{subdomain1}.{domain1}, Registered!', pady=20, bg='#ffbf00').pack()
    if subdomain1=="":
        API_ENDPOINT = "https://infomaniak.com/nic/update?hostname="+domain1+"&username="+username1+"&password="+password1
    else:
        API_ENDPOINT = "https://infomaniak.com/nic/update?hostname="+subdomain1+"."+domain1+"&username="+username1+"&password="+password1
    print(API_ENDPOINT)
    r = requests.post(url = API_ENDPOINT) 
    
    pastebin_url = r.text 
    print("The pastebin URL is:%s"%pastebin_url) 

    
#label 
lblsubdomain=Label(ws, text="Enter your subdomain (leave blank if none)", fg='black', font=("Helvetica", 10))
lblsubdomain.pack(pady=5)
#entry
subdomain = Entry(ws)
subdomain.pack(pady=5)
lbldomain=Label(ws, text="Enter your domain", fg='black', font=("Helvetica", 10,))
lbldomain.pack(pady=5)	
domain = Entry(ws)
domain.pack(pady=5)
lblusername=Label(ws, text="Enter your username", fg='black', font=("Helvetica", 10))
lblusername.pack(pady=5)
username = Entry(ws)
username.pack(pady=5)
lblpassword=Label(ws, text="Enter your password", fg='black', font=("Helvetica", 10))
lblpassword.pack(pady=5)
password = Entry(ws)
password.pack(pady=5)

#button
Button(
    ws,
    text="Register", 
    padx=10, 
    pady=5,
    command=printValue
    ).pack()

ws.mainloop()

#source : 
#https://pythonguides.com/how-to-take-user-input-and-store-in-variable-using-python-tkinter/
#https://www.tutorialsteacher.com/python/create-gui-using-tkinter-python
#https://fr.acervolima.com/requetes-get-et-post-avec-python/