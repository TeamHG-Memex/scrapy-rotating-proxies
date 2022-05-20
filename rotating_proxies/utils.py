from urllib.request import _parse_proxy


def extract_proxy_hostport(proxy):
    """
    Return the hostport component from a given proxy:
    """
    return _parse_proxy(proxy)[3]
