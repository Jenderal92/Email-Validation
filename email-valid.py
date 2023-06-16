# -*- coding: utf-8 -*
#!/usr/bin/python
#Email Validator
# Coded Shin_Code
#My Friendo : JametKNTLS -  h0d3_g4n - Moslem And All Coders
# Blog : https://www.blog-gan.org          
#Buy coffee :
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
#CONTACT ME :(
       # ICQ : https://icq.im/Shin403
       # Telegram : https://t.me/Shin_code
       # Youtube : Smile Of Beauty 
# Apakah kamu hanya bisa melakukan recode dengan mengganti nama author?
# Can you only recode by changing the author name?
############# [ Module ] #############
import requests,time,os,base64
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, init
init(autoreset=True)



#email = ""

def verifer_email(email):
	try:
		resp = requests.get('https://api.hunter.io/v2/email-verifier?email='+email+'&api_key='+base64.b64decode('YTQzNWM2NjVjYTU5NjViNDYxNTFhM2I0MGI1ZTY3MjllZmQ0NTBlMQ=='),timeout=10,headers={'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'})
		if '"status": "valid"' in resp.content:
			print (Fore.YELLOW + "[+]" + Fore.RESET + email + ' - ' + Fore.GREEN + "[VALID]" + Fore.RESET)
			open('email_valid.txt','a').write(email+'\n')
		else:
			print (Fore.YELLOW + "[+]" + Fore.RESET + email + ' - ' + Fore.RED + "[INVALID]" + Fore.RESET)
    
	except:
		pass
if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	print "{} Email Validator  | {}Shin Code\n".format(Fore.YELLOW,Fore.CYAN)
	email = open(raw_input('List:~# '),'r').read().replace('http://','').replace('https://','').splitlines()
	pool = ThreadPool(int(20))
	pool.map(verifer_email, email)
	pool.close()
	pool.join()
