import requests


def post_request(url, data, auth):
    resp = requests.post(url, json=data, auth=auth)
    return resp


if __name__ == '__main__':
    post_request(url=None, json={}, auth=('admin', 'admin'))
