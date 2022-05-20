from rotating_proxies.utils import extract_proxy_hostport


def test_extract_proxy_hostport():
    """Test extra_proxy_hostport."""
    assert extract_proxy_hostport('example.com') == 'example.com'
    assert extract_proxy_hostport('http://www.example.com') == 'www.example.com'
    assert extract_proxy_hostport('127.0.0.1:8000') == '127.0.0.1:8000'
    assert extract_proxy_hostport('127.0.0.1') == '127.0.0.1'
    assert extract_proxy_hostport('localhost') == 'localhost'
    assert extract_proxy_hostport('zot:4321') == 'zot:4321'
    assert extract_proxy_hostport('http://foo:bar@baz:1234') == 'baz:1234'
