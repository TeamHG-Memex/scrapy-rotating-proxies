CHANGES
=======

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
