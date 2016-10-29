import requests
a = {"token" : "61d1f5b7ef20dacafcf93addf4c1fc0c"}
reqOne = requests.post('http://challenge.code2040.org/api/reverse', json=a)
reqTwo = requests.get('http://challenge.code2040.org/api/reverse')
#print(reqTwo.text)
newString = reqTwo.text[::-1]
b = {"token" : "61d1f5b7ef20dacafcf93addf4c1fc0c", "string" : newString}
reqThree = requests.post('http://challenge.code2040.org/api/reverse/validate', json=b)
