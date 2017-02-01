# -*- coding: utf-8 -*-
from rotating_proxies.expire import Proxies


def test_proxies():
    proxy_list = ['foo', 'bar', 'baz']
    p = Proxies(proxy_list)
    proxy = p.get_random()
    assert proxy in proxy_list

    p.mark_dead('bar')
    p.mark_dead('baz')

    assert p.get_random() == 'foo'

    p.mark_dead('foo')
    assert p.get_random() is None

    p.mark_good('bar')
    assert p.get_random() == 'bar'


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
