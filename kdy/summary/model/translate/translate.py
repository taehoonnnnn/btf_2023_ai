import os
import sys
import urllib.request
import json  # JSON module import

client_id = "jEPij9MsZqUVIRtH6wyh"  # Client ID 발급받은 값
client_secret = "UVL7kT1zvT"  # Client Secret 발급받은 값
encText = urllib.parse.quote("반갑습니다")
data = "source=ko&target=en&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if (rescode == 200):
    response_body = response.read()
    response_body = response_body.decode('utf-8')  # Decode from bytes to string
    response_body = json.loads(response_body)  # Parse string to JSON
    print(response_body["message"]["result"]["translatedText"])  # Access fields
else:
    print("Error Code:" + str(rescode))
