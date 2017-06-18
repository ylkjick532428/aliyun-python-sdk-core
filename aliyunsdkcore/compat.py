try:
    from urllib.request import pathname2url  # @UnusedImport
    from urllib.parse import urlencode  # @UnusedImport
    import http.client as httplib  # @UnusedImport
except:
    from urllib import pathname2url, urlencode
    import httplib

