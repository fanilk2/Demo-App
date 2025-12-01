import requests,json
api_key="b637638cac2ad89d4b90c210" 
api_url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"
bozulandoviz=input("Bozulan döviz türünü giriniz: ")
alinandoviz=input("Alınan döviz türünü giriniz: ")
miktar=int(input(f"Kaç {bozulandoviz} bozuyorsunuz: "))                   
sonuc=requests.get(api_url+bozulandoviz)
sonuc_json=json.loads(sonuc.text)
result=miktar*sonuc_json["conversion_rates"][alinandoviz]

# print(sonuc_json["conversion_rates"])
print("1 {0} = {1} {2}".format(bozulandoviz,sonuc_json["conversion_rates"][alinandoviz],alinandoviz))
print(f"{miktar} {bozulandoviz} = {result} {alinandoviz}")