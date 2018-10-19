import json

import requests


def post_request(url, data, auth):
    resp = requests.post(url, json=data, auth=auth)
    json_obj = json.loads(resp.text)
    return json_obj


if __name__ == '__main__':
    post_request(url=None, json={}, auth=('admin', 'admin'))
