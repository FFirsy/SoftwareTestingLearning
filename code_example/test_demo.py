import requests

def test_users():
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    assert res.status_code == 200

def test_posts():
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert res.status_code == 200