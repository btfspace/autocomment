# Telegram Autocommenting Script
![](https://img.shields.io/badge/Telethon-v1.24.0-%230088cc)
### Setup
```
$ git clone https://github.com/btfspace/autocomment
$ cd autocomment
$ pip3 install telethon
```
After that, you need to create an application in Telegram.  
To do this, go to [My TG](https://my.telegram.org), log in to your account and make the application, then copy api_id and api_hash to `config.ini`.  
Then set up the channels:  
Copy the names of the desired channels in `config.ini` to the channels variable. If you have several channels, write them separated by commas.  
To configure the messages to be sent, configure the messages variable. If you have one channel, just write a message, if you have several channels, write messages in the order of channels for each channel. Example:
```
[posthandler]
channels=Example,Example 2
api_id=1337
api_hash=fe78fv7ev78f6vrf78vb6
messages=Message for Example,Message for Example 2
```
This completes the setup.
### Using
```
$ python3 main.py
```
Wait for the channel names to be checked and leave the script enabled.  
That's it, autocommenting is running.
### License
THERE IS NO LICENSE
