import requests
from fake_email import Email
import time,random
import re
import requests
import uuid
import random
import time
from datetime import datetime
import base64
import urllib.parse
import json
import base64
import json
import hashlib
import os
from faker import Faker
import string
import spintax
def generate_uuid(prefix: str = '', suffix: str = '') -> str:
    return f'{prefix}{uuid.uuid4()}{suffix}'
def generate_android_device_id() -> str:
    return "android-%s" % hashlib.sha256(str(time.time()).encode()).hexdigest()[:16]
def generate_useragent():
    with open("ua.txt", "r")as file:
        agents = file.read().splitlines()
        a = random.choice(agents)
        user = a.split(",")
    return f'Instagram 261.0.0.21.111 Android ({user[7]}/{user[6]}; {user[5]}dpi; {user[4]}; {user[0]}; {user[1]}; {user[2]}; {user[3]}; en_US; {user[9]})'

def get_mid():
    params = None
    api_url = f"https://i.instagram.com/api/v1/accounts/login"
    response = requests.get(api_url, params=params)
    mid = response.cookies.get("mid")
    if mid != None:
        return mid
    else:
        u01 = 'QWERTYUIOPASDFGHJKLZXCVBNM'
        us1 = str("".join(random.choice(u01)for k in range(int(8))))
        return f'Y4nS4g{us1}zwIrWdeYLcD9Shxj'

def Username():
    fake = Faker()
    name = fake.name()
    return str(name)
def generate_jazoest(symbols: str) -> str:
    amount = sum(ord(s) for s in symbols)
    return f'2{amount}'
BlockVersion = 'a399f367a2e4aa3e40cdb4aab6535045b23db15f3dea789880aa0970463de062'
App_ID = '567067343352427'
def getcode(topic):
	number = re.search(r'\d+', topic).group()
	return number
def gene():
 email=nm+'@'+dm
 emaill = Email().Mail()
 return email,emaill
def getmsg(emaill):
 headers = {'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36",'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",'Accept-Encoding': "gzip, deflate, br, zstd",'upgrade-insecure-requests': "1",'sec-fetch-site': "same-origin",'sec-fetch-mode': "navigate",'sec-fetch-user': "?1",'sec-fetch-dest': "document",'sec-ch-ua': "\"Chromium\";v=\"130\", \"Google Chrome\";v=\"130\", \"Not?A_Brand\";v=\"99\"",'sec-ch-ua-mobile': "?1",'sec-ch-ua-platform': "\"Android\"",'accept-language': "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ar;q=0.6",'priority': "u=0, i",'Cookie': f"_ga=GA1.2.263727456.1729523197; _gid=GA1.2.356737544.1729523197; __gads=ID=e508f22c61782ce8:T=1729523197:RT=1729523197:S=ALNI_MYHEnL2-Ev8UZcsoBpvV2uyGZ81Jw; __gpi=UID=00000f1126b59e8e:T=1729523197:RT=1729523197:S=ALNI_ManCa1sPXx2CsHXsUWlGGYnhZlFwQ; __eoi=ID=c84bc14508c1e954:T=1729523197:RT=1729523197:S=AA-Afjb22XugHUO2KpfGQ5vcBaUU; _ga_YDXL47LYFV=GS1.1.1729523196.1.1.1729523198.58.0.0; FCNEC=%5B%5B%22AKsRol9EGsTPSvv7V7JT6ZoV7ivqqHrFXLEzlrpd3TP5Vo8YMtH3SKi8cVpeWTMKlkzD6xRLvAGhBlyNg4gzByvYmGXRou0DixpobRsC2pipVhi3TB892b97qLa0zU05frTGg5Ulm3P-POle-grx3EtTI4S8Y_tfGQ%3D%3D%22%5D%5D; surl={dm}%2F{nm}"}
 while True:
  response = requests.get("https://emailfake.com/channel9/",headers=headers).text
  try:
   code=(response.split('"e7m subj_div_45g45gg">')[1].split(' ')[0])
   return code
  except:
   print('waiting code')
Device_ID = generate_uuid()
Family_ID = generate_uuid()
Android_ID = generate_android_device_id()
UserAgent = generate_useragent()
X_Mid = get_mid()
adid = str(uuid.uuid4())
water = str(uuid.uuid4())
username = Username()
def test():
	global Device_ID,Family_ID,Android_ID,UserAgent,X_Mid,adid,water,username
	enc = 'Ac0nwrH7FRN9YJogXOkAAVvzKZcofY8HdNLdLBh7scbGj/7D5OQM/nfsFHuz/RuTO8yEvCVYQqbJnXpTnpEzLrs0mY5tJuBLmdIGRKl/D8ILo5eyTT6SBYs7bIu5bM9H8IkvHGtVre9sBp2bKEB0513wDLqhav4zDnklPKjZr4MnxIgosPQNjEpPCXbydfyC+pccn2gYUgZWEE0ceYiwMrQR4oQChxH2cW8Keq2/SqZvOIR8nr8lmhkOSQCq2i6gE7NGqbMa3M1h8LSMvheG4gFrabUeoRMdEOn8x9F0IvKNMO6dcPkfJJKQhJaxPJk0v3KSCfHf6awdeD49yakDafhPkDHzGZlh8RIgi8fXotIwq/RWUs/wPFmuaUoAv15SCdz79JBac08='
	password = 'plplokok'
	jazoest = generate_jazoest(Family_ID)
	try:
		email,emaill=gene()
	except:
#		time.sleep(2)
		test()
	headers = {

    'Host': 'i.instagram.com',

    'X-Ig-App-Locale': 'en_US',

    'X-Ig-Device-Locale': 'en_US',

    'X-Ig-Mapped-Locale': 'en_US',

    'X-Pigeon-Session-Id': generate_uuid('UFS-', '-1'),

    'X-Pigeon-Rawclienttime': str(round(time.time(), 3)),

    'X-Ig-Bandwidth-Speed-Kbps': str(random.randint(2500000, 3000000) / 1000),

    'X-Ig-Bandwidth-Totalbytes-B': str(random.randint(5000000, 90000000)),

    'X-Ig-Bandwidth-Totaltime-Ms': str(random.randint(2000, 9000)),

    'X-Bloks-Version-Id': BlockVersion,

    'X-Ig-Www-Claim': '0',

    'X-Bloks-Is-Layout-Rtl': 'false',

    'X-Ig-Device-Id': Device_ID,

    'X-Ig-Family-Device-Id': Family_ID,

    'X-Ig-Android-Id': Android_ID,

    'X-Ig-Timezone-Offset': '16500',

    'X-Fb-Connection-Type': 'WIFI',

    'X-Ig-Connection-Type': 'WIFI',

    'X-Ig-Capabilities': '3brTv10=',

    'X-Ig-App-Id': App_ID,

    'Priority': 'u=3',

    'User-Agent': UserAgent,

    'Accept-Language': 'en-US',

    'X-Mid': X_Mid,

    'Ig-Intended-User-Id': '0',

    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',

    'X-Fb-Http-Engine': 'Liger',

    'X-Fb-Client-Ip': 'True',

    'X-Fb-Server-Cluster': 'True',

    'Connection': 'close',

}
	url = "https://i.instagram.com/api/v1/accounts/send_verify_email/"
	data = {
    "phone_id": Family_ID,
    "guid": Device_ID,
    "device_id": Android_ID,
    "email": email,
    "waterfall_id": water,
    "auto_confirm_only": "false"
}
	json_data = json.dumps(data)
	encoded_body = urllib.parse.quote(json_data)
	signature = "46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b"
	payload = f"signed_body={signature}.{encoded_body}"
	#print(payload)
	response = requests.post(url, data=payload, headers=headers)
	#print(response.text)
	status=(response.json().get("status"))
	#print(status)
	if status=='ok':
		
		code=(getmsg(emaill))
		url = "https://i.instagram.com/api/v1/accounts/check_confirmation_code/"
		data = {

    'signed_body': '46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b.{"code":"'+code+'","email":"'+email+'","device_id":"' + Android_ID + '","waterfall_id":"'+water+'"}',

}

		response = requests.post(url, data=data, headers=headers)
		#print(response.json())
		try:signup=(response.json().get("signup_code"))
		except:
			print("Fail Get SignUp Code")
			signup=None
		url = "https://i.instagram.com/api/v1/accounts/create/"
		urname=''.join(random.choice("qwertyuiopasdfghjklzxcvbnm") for i in range(1))
		usrname=''.join(random.choice("qwertyuiopasdfghjklzxcvbnm1234567890") for i in range(5))
		username=urname+usrname+str(random.randint(10000,999999))
		sig=(Device_ID.replace('-',''))
		url = "https://i.instagram.com/api/v1/si/fetch_headers/"
		params = {
  'guid': sig,
  'challenge_type': "signup"
}
		response = requests.get(url, params=params, headers=headers)
		current_time = str(int(time.time()))
		url = "https://i.instagram.com/api/v1/accounts/create/"
		data={'is_secondary_account_creation': 'false', 'jazoest': jazoest, 'tos_version': 'row', 'suggestedUsername': '', 'sn_result': "API_ERROR: class X.2mY:7: ", 'do_not_auto_login_if_credentials_match': 'true', 'phone_id': Family_ID, 'enc_password': f'#PWD_INSTAGRAM:4:1728908491:{enc}', 'username': username, 'first_name':Username(), 'day': '14', 'adid': adid, 'guid': Device_ID, 'year': '1993', 'device_id': Android_ID, '_uuid': Device_ID, 'email': email, 'month': '10', 'sn_nonce': 'a2ViaXM2MDI2OEByb3dwbGFudC5jb218MTcyODkwODQ3NXyBPBJ8K71vVMwEQVMtMK5xS+RnKq3bxo8=', 'force_sign_up_code':signup, 'waterfall_id':water, 'qs_stamp': '', 'one_tap_opt_in': 'true'}
		json_data = json.dumps(data)
		encoded_body = urllib.parse.quote(json_data)
		signature = "SIGNATURE"
		payload = f"signed_body={signature}.{encoded_body}"

#		try:
		response = requests.post(url, data=payload, headers=headers)
#			print(response.text)
		if 'account_created":true'  in response.text:
				current_time = str(int(time.time()))
				password = password
				data = {
    "_csrftoken": "missing",
    "adid": adid,
    "country_codes": "[{\"country_code\":\"7\",\"source\":[\"default\",\"uig_via_phone_id\"]}]",
    "device_id": Android_ID,
    "google_tokens": "[]",
    "guid": Device_ID,
    "login_attempt_count": 0,
    "jazoest": "22072",
    "phone_id": Family_ID,
    "username": username,
    "enc_password": f"#PWD_INSTAGRAM:0:{current_time}:{password}"
}
				response = requests.post("https://i.instagram.com/api/v1/accounts/login/", data={"signed_body": f"'46024e8f31e295869a0e861eaed42cb1dd8454b55232d85f6c6764365079374b.{json.dumps(data)}"}, headers=headers)
				response_json = response.json()
				if "logged_in_user" in response_json:
					token = response.headers.get("ig-set-authorization")
					y=(f'[√] Registered [ {email} | {password} | {username} | {token} ]')
					print(y)
					with open("accounts.txt",'a') as f:
						f.write(f'{email}:{password}:{username}:{token}\n')
#					time.sleep(25)
		else:
				y=(f'[×] Error : {email} : {password} : {username}')
				print(y)
				print(response.text)
#				time.sleep(60)
#		except:
#			print("Except")
try:
	count = int(input('[+] How Many Accounts : '))
except :
	count = 0
for i in range(count):
 domain=['clonekhoe.com','aenomail.com','konterkulo.com','otpku.com','hotrometa.com','izhowto.com','gustopizza.es','coffeepancakewafflebacon.com','shopbantkclone.com','remaild.com','luonglanhlung.com','24hinbox.com','filevino.com','ebarg.net','pemberontakjaya88.com','getcode1.com','jagomail.com','meetingpoint-point.com','cggup.com','kreasianakkampoeng.com','kimgmail.com','otpku.com','flybyinbox.cam','hieuclone.com','gmailbrt.com','h0tmal.com','dmxs8.com','681mail.com','htmail.store','suksesboss.com']
 dm=random.choice(domain)
 nm=Username().replace(' ','')+str(random.randint(100,999))
 test()
