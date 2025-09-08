import http.client
import json

conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
conn.request("GET", "/posts/1")

response = conn.getresponse()
print("Status:", response.status)
data = response.read()

# レスポンスはバイナリなので、デコードしてJSONに変換
print(json.loads(data.decode("utf-8")))

conn.close()
