import requests as req

res = req.get("http://api.ipify.org")

print(res.status_code)
print(res.request.method)
print(res.request.headers)
print(res.raw)