# Infomaniak Dynamic DNS via HTTP POST request

This code is for those of you who are just like me: a simple guy juste trying to make infomaniak ddns work automatically.
I already did a repository of this in Nodejs but it's more accessible using python so here it is.

I recently add a notification system with Pushbullet so you can keep track of what's happening with this code.

To get started you will need the python module request. You can install by typing:
```
pip install requests
pip install pushbullet
```

Don't forget to put your username, your password and your the domains you want to update.

Finally you can put your script in cron or for windows in a schedule task.

![image](https://user-images.githubusercontent.com/47923266/158037700-b77e3fcc-f60b-40fd-b819-58780b6d8fc2.png)
