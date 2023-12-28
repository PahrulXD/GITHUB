import requests, os

def masuk():
	os.system ("clear")
	target = input ("- username : ")
	url = "https://api.github.com/users/"+target
	data = requests.get(url).json()
	print ("")
	print ("- login :", data["login"])
	print ("- id :", data["id"])
	print ("- name :", data["name"])
	print ("- bio :", data["bio"])
	print ("- public repos :", data["public_repos"])
	print ("- followers :", data["followers"])
	print ("- following :", data["following"])
	print ("- created :", data["created_at"])
	print ("- updated :", data["updated_at"])
	print ("")
	
masuk()