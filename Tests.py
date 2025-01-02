import requests
from requests.adapters import HTTPAdapter
from urllib3.util.ssl_ import create_urllib3_context

class TLSAdapter(HTTPAdapter):
    def __init__(self, tls_version, **kwargs):
        self.tls_version = tls_version
        super().__init__(**kwargs)

    def init_poolmanager(self, *args, **kwargs):
        kwargs['ssl_context'] = create_urllib3_context()
        super().init_poolmanager(*args, **kwargs)

# Force TLSv1.2 or TLSv1.3
session = requests.Session()
session.mount("https://", TLSAdapter("TLSv1.2"))

try:
    response = session.get(url)
    print(response.status_code)
    print(response.text)
except requests.exceptions.SSLError as e:
    print(f"SSL Error: {e}")


