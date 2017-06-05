# -*- coding: utf-8 -*-
from rotating_proxies.expire import Proxies, exp_backoff


def test_proxies():
    proxy_list = ['foo', 'bar', 'baz']
    p = Proxies(proxy_list)
    proxy = p.get_random()
    assert proxy in proxy_list

    proxy = p.get_proxy('foo')
    assert proxy in proxy_list
    proxy = p.get_proxy('wom')
    assert not proxy

    p.mark_dead('bar')
    p.mark_dead('baz')

    assert p.get_random() == 'foo'

    p.mark_dead('foo')
    assert p.get_random() is None

    p.mark_good('bar')
    assert p.get_random() == 'bar'


def test_auth_proxies():
    proxy_list = ['http://foo:bar@baz:1234', 'http://egg:1234']
    p = Proxies(proxy_list)

    proxy = p.get_proxy('http://baz:1234')
    assert proxy in proxy_list

    proxy = p.get_proxy('http://egg:1234')
    assert proxy in proxy_list


def test_reanimate_reset():
    p = Proxies(['foo', 'bar', 'baz'])
    p.mark_dead('foo', 1000)
    p.mark_dead('bar', 1)
    p.mark_dead('baz', 1)
    assert not p.good and not p.unchecked
    n_reanimated = p.reanimate(1000)
    assert n_reanimated == 2
    assert all(proxy.failed_attempts > 0 for proxy in p.proxies.values())
    assert p.unchecked == {'bar', 'baz'}
    assert p.dead == {'foo'}

    p.reset()
    assert len(p.unchecked) == 3
    assert len(p.good) == len(p.dead) == 0
    assert all(proxy.failed_attempts > 0 for proxy in p.proxies.values())


def test_exp_backoff():
    assert exp_backoff(0, 3600.0, 300.0) == 300
    assert exp_backoff(1, 3600.0, 300.0) == 600
    assert exp_backoff(2, 3600.0, 300.0) == 1200
    assert exp_backoff(3, 3600.0, 300.0) == 2400
    assert exp_backoff(4, 3600.0, 300.0) == 3600
    assert exp_backoff(10, 3600.0, 300.0) == 3600


def test_exp_backoff_overflow():
    assert exp_backoff(100000, 3600.0, 300.0) == 3600
