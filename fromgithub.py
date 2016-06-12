import json
import os

user = raw_input("Enter your username from github: ")
os.system("curl -k -u "+ user + " https://api.github.com/users/"+user+"/repos > repoinfo")
json_data = open("./repoinfo").read()
data = json.loads(json_data)
for repo in data:
	os.system("git clone "+repo["clone_url"])
os.system("rm repoinfo")
