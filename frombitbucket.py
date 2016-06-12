import json
import os

user = raw_input("Enter your username from bitbucket: ");
url = "https://api.bitbucket.org/1.0/user/repositories"
os.system("curl -k --user "+user+" "+url+" > repoinfo");
json_data=open("./repoinfo").read()
data = json.loads(json_data)
for repo in data:
    print "Cloning repository " + repo["name"]
    os.system(repo["scm"]+" clone https://bitbucket.org/" + repo["owner"] + "/" + repo["slug"])
os.system("rm repoinfo");
