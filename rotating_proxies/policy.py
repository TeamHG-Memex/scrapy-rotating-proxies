# -*- coding: utf-8 -*-
from scrapy.exceptions import IgnoreRequest
from scrapy.extensions.httpcache import DummyPolicy


class BanAwareCachePolicy(DummyPolicy):
    """
    This policy is for scrapy http caching that will prevent caching banned responses
    Usage, in settings.py:
        HTTPCACHE_POLICY = 'rotating_proxies.policy.BanAwareCachePolicy'
    """

    def should_cache_response(self, response, request):
        if request.meta.get('_ban', False):
            return False
        return super().should_cache_response(response, request):


class BanDetectionPolicy(object):
    """ Default ban detection rules. """
    NOT_BAN_STATUSES = {200, 301, 302}
    NOT_BAN_EXCEPTIONS = (IgnoreRequest,)

    def response_is_ban(self, request, response):
        if response.status not in self.NOT_BAN_STATUSES:
            return True
        if response.status == 200 and not len(response.body):
            return True
        return False

    def exception_is_ban(self, request, exception):
        return not isinstance(exception, self.NOT_BAN_EXCEPTIONS)
