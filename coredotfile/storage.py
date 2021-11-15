"""Main module."""
import requests


coredot_storage_url = "https://tool.core.today/v1/storage/object/url"


def get_presigned_url(key):
    r = requests.put(coredot_storage_url, params={"key": key})
    result = r.json()
    return result


def put_object_storage(key, content):
    if type(content) is not bytes:
        return {'status': '500', 'message': 'Use bytes type content'}

    info = get_presigned_url(key)
    result = requests.put(info['url'], data=content)
    return {'status': result['status_code'], 'message': 'Upload successful'}
