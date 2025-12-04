import requests
class Github:
    def __init__(self):
        self.api_url="https://api.github.com"
    def getUser(self,username):
        response=requests.get(self.api_url+"/users/"+username)
        return response.json()
    def getRepositories(self,username):
        response=requests.get(self.api_url+"/users/"+username+"/repos")
        return response.json()
github=Github()
while True:
    secim=input("1-Find user\n2-Get repositoeries\n3-Create repositoeries\n4-Exit\nSeçiminiz: ")

    if secim=="4":
        break
    else:
        if secim=="1":
            username=input("Kullanıcı adı giriniz: ")
            result=github.getUser(username)
            print(f"Name:{result["name"]}\nPublic repos: {result["public_repos"]}")
        elif secim=="2":
            username=input("Kullanıcı adı giriniz: ")
            result=github.getRepositories(username)
            for repo in result:
                print(repo["name"])
        elif secim=="3":
            pass
        else:
            pass