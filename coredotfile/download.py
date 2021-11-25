import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def download_file(url: str, apikey: str, filename: str):
    if not filename.endswith('.zip'):
        filename += '.zip'
    # NOTE the stream=True parameter below
    with requests.post(url, data={"apikey": apikey}, stream=True, verify=False) as r:
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk:
                f.write(chunk)
    return filename
