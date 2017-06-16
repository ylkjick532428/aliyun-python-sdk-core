try:
    from urllib.request import pathname2url
    from urllib.parse import urlencode
    import http.client as httplib
except:
    from urllib import pathname2url, urlencode
    import httplib

