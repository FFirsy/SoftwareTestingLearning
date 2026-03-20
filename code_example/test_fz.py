from request_util import RequestUtil

def test_users():
    req = RequestUtil()
    response = req.send_request(
        "get",
        "https://jsonplaceholder.typicode.com/users")

    assert response.status_code == 200