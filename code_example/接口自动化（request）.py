import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
data = response.json()

# 状态码断言
assert response.status_code == 200, "状态码错误"

assert data["userId"] == 1

print("测试通过")