CHANGES
=======

0.6 (2018-12-28)
----------------

Proxy information is added to scrapy stats:

* proxies/unchecked
* proxies/reanimated
* proxies/dead
* proxies/good
* proxies/mean_backoff

0.5 (2017-10-09)
----------------

* ``ROTATING_PROXY_LIST_PATH`` option allows to pass file name
  with a proxy list.

0.4 (2017-06-06)
----------------

* ``ROTATING_PROXY_BACKOFF_CAP`` option allows to change max backoff time
  from the default 1 hour.

0.3.2 (2017-06-05)
------------------

* fixed proxy authentication issue.

0.3.1 (2017-03-20)
------------------

* fixed OverflowError during backoff computation.

0.3 (2017-03-14)
----------------

* redirects with empty bodies are no longer considered bans
  (thanks Diga Widyaprana).
* ``ROTATING_PROXY_BAN_POLICY`` option allows to customize ban detection
  for all spiders.

0.2.3 (2017-03-03)
------------------

* ``max_proxies_to_try`` request.meta key allows to override
  ``ROTATING_PROXY_PAGE_RETRY_TIMES`` option per-request.

0.2.2 (2017-03-01)
------------------

* Update default ban detection rules: scrapy.exceptions.IgnoreRequest
  is not a ban.

0.2.1 (2017-02-08)
------------------

* changed ``ROTATING_PROXY_PAGE_RETRY_TIMES`` default value - it is now 5.

0.2 (2017-02-07)
----------------

* improved default ban detection rules;
* log ban stats.

0.1 (2017-02-01)
----------------

Initial release
