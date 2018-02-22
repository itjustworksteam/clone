import json
import os

orgs = raw_input("Enter organization from github: ")
os.system("curl -k https://api.github.com/orgs/"+orgs+"/repos?per_page=200 > repoinfo")
json_data = open("./repoinfo").read()
data = json.loads(json_data)
for repo in data:
	os.system("git clone "+repo["clone_url"])
os.system("rm repoinfo")