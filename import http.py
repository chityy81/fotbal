import http.client

conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "7a3b548e77mshbb0c62108b7c16fp160c79jsn02ef1add7889",
    'X-RapidAPI-Host': "api-football-v1.p.rapidapi.com"
    }

conn.request("GET", "/v3/timezone", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))