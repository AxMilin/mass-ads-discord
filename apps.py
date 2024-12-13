import requests, time, json, random, threading, os
from colorama import Fore
from config import message, token, delay, thread

banner = f'''{Fore.LIGHTCYAN_EX}
  __  __                             _     
 |  \/  |                   /\      | |     
 | \  / | __ _ ___ ___     /  \   __| |___  
 | |\/| |/ _` / __/ __|   / /\ \ / _` / __| 
 | |  | | (_| \__ \__ \  / ____ \ (_| \__ \ 
 |_|  |_|\__,_|___/___/ /_/    \_\__,_|___/ 
    \__ https://ax-milin.netlify.app
     \__ Made By Ax_Milin <3
'''
print(banner)
print(" ")
print("Message: \n"+message)
print("Thread: "+str(thread))
print("Delay: "+str(delay))
print(" ")
time.sleep(1)
os.system("cls||clear")
print(banner)
print(" ")
print("Getting Ready...")
time.sleep(1)
os.system("cls||clear")
print(banner)

with open('channels.txt', 'r') as file:
    content = file.readlines()

chs = [item.strip() for item in content]

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text

def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

def send(channel):

    url = 'https://discord.com/api/v10/channels/' + channel + '/messages'
    payload = {"content": message, "tts": False}
    header = mainHeader(token)

    while True:
        try:
            src = requests.post(url, headers=header, json=payload)

            if src.status_code == 429:
                ratelimit = json.loads(src.content)
                print(f"{Fore.LIGHTRED_EX} DELAY",
                        str(float(ratelimit['retry_after'])) + " seconds")

            elif src.status_code == 200:
                print(f'{Fore.GREEN}[*]{Fore.GREEN} SUCCEED {channel}')
        except:
            pass
        time.sleep(delay)

for i in range(thread):
    time.sleep(0.5)
    print(f"{Fore.YELLOW}Thread {i+1} Sent!")
    for item in chs:
        try:
            threading.Thread(target=send,args=(item,)).start()
        except:
            send(item)
