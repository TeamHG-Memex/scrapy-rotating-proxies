# -*- coding: utf-8 -*-
from scrapy.http import Response, Request
from rotating_proxies.policy import BanDetectionPolicy
import pytest


request = Request('http://example.com')


@pytest.fixture()
def policy():
    return BanDetectionPolicy()


def get_response(**kwargs):
    return Response(request.url, request=request, **kwargs)


def test_default_ban_policy(policy):
    resp = get_response(body=b'hello')
    assert policy.response_is_ban(request, resp) is False

    resp = get_response(body=b'hello', status=302)
    assert policy.response_is_ban(request, resp) is False

    resp = get_response(body=b'hello', status=500)
    assert policy.response_is_ban(request, resp) is True


def test_default_ban_policy_empty_body(policy):
    resp = get_response(body=b'')
    assert policy.response_is_ban(request, resp) is True

    resp = get_response(body=b'', status=301)
    assert policy.response_is_ban(request, resp) is False

    resp = get_response(body=b'', status=500)
    assert policy.response_is_ban(request, resp) is True


def test_default_ban_policy_exception(policy):
    assert policy.exception_is_ban(request, ValueError()) is True

