import requests
a = {"token": "61d1f5b7ef20dacafcf93addf4c1fc0c" , "github" : "https://github.com/CYJ001/Code2040app"}
#key-pair = {"token" : "61d1f5b7ef20dacafcf93addf4c1fc0c", "github" : "https://github.com/CYJ001/Code2040app"}
r = requests.post("http://challenge.code2040.org/api/register", json=a)
