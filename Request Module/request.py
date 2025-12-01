import requests
result=requests.get("https://jsonplaceholder.typicode.com/todos")
result=result.text
print(result)