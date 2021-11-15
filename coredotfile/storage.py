"""Main module."""
import requests


coredot_storage_url = "https://tool.core.today/v1/storage/object/url"


def get_presigned_upload_url(key):
    r = requests.put(coredot_storage_url, params={"key": key})
    result = r.json()
    return result


def get_presigned_download_url(key):
    r = requests.get(coredot_storage_url, params={"key": key})
    result = r.json()
    return result


def put_object_storage(key, content):
    if type(content) is not bytes:
        return {'status': '500', 'message': 'Use bytes type content'}

    info = get_presigned_upload_url(key)
    result = requests.put(info['url'], data=content)
    return {'status': result.status_code, 'message': 'Upload successful'}


def get_object_storage(key, target_file=None, filename=None):
    if not filename:
        filename = key
    if not target_file:
        target_file = key

    info = get_presigned_download_url(key)
    result = requests.get(info['url'])
    with open(target_file, 'wb') as f:
        f.write(result.content)
    return {'status': result.status_code, 'message': 'Download successful', 'content': result.content}

