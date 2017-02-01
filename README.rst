scrapy-rotating-proxies
=======================

.. image:: https://img.shields.io/pypi/v/scrapy-rotating-proxies.svg
   :target: https://pypi.python.org/pypi/scrapy-rotating-proxies
   :alt: PyPI Version

.. image:: https://travis-ci.org/TeamHG-Memex/scrapy-rotating-proxies.svg?branch=master
   :target: http://travis-ci.org/TeamHG-Memex/scrapy-rotating-proxies
   :alt: Build Status

.. image:: http://codecov.io/github/TeamHG-Memex/scrapy-rotating-proxies/coverage.svg?branch=master
   :target: http://codecov.io/github/TeamHG-Memex/scrapy-rotating-proxies?branch=master
   :alt: Code Coverage

This package provides a Scrapy_ middleware to use rotating proxies,
check that they are alive and adjust crawling speed.

.. _Scrapy: https://scrapy.org/

License is MIT.

Installation
------------

::

    pip install scrapy-rotating-proxies

Usage
-----

Add ``ROTATING_PROXY_LIST`` option with a list of proxies to settings.py::

   ROTATING_PROXY_LIST = [
      'proxy1.com:8000',
      'proxy2.com:8031',
      # ...
   ]

You can load it from file if needed::

   def load_lines(path):
      with open(path, 'rb') as f:
         return [line.strip() for line in
                 f.read().decode('utf8').splitlines()
                 if line.strip()]

   ROTATING_PROXY_LIST = load_lines('/my/path/proxies.txt')

Then add rotating_proxies middlewares to your DOWNLOADER_MIDDLEWARES::

   DOWNLOADER_MIDDLEWARES = {
      # ...
      'rotating_proxies.middlewares.RotatingProxyMiddleware': 610,
      'rotating_proxies.middlewares.BanDetectionMiddleware': 620,
      # ...
   }

Concurrency
-----------

By default, all default Scrapy concurrency options (``DOWNLOAD_DELAY``,
``AUTHTHROTTLE_...``, ``CONCURRENT_REQUESTS_PER_DOMAIN``, etc) become
per-proxy for proxied requests when RotatingProxyMiddleware is enabled.
For example, if you set ``CONCURRENT_REQUESTS_PER_DOMAIN=2`` then
spider will be making at most 2 concurrent connections to each proxy,
regardless of request url domain.

Customization
-------------

``scrapy-rotating-proxies`` keeps track of working and non-working proxies,
and re-checks non-working from time to time.

Detection of a non-working proxy is site-specific.
By default, ``scrapy-rotating-proxies`` uses a simple heuristic:
if a response status code is not 200, response body is empty or if
there was an exception then proxy is considered dead.
To customize this with site-specific rules define ``response_is_ban``
and/or ``exception_is_ban`` spider methods::

   class MySpider(scrapy.spider):
      # ...

      def response_is_ban(self, request, response):
         return b'banned' in response.body

      def exception_is_ban(self, request, exception):
         return None

It is important to have these rules correct because action for a failed
request and a bad proxy should be different: if it is a proxy to blame
it makes sense to retry the request with a different proxy.

Non-working proxies could become alive again after some time.
``scrapy-rotating-proxies`` uses a randomized exponential backoff for these
checks - first check happens soon, if it still fails then next check is
delayed further, etc. Use ``ROTATING_PROXY_BACKOFF_BASE`` to adjust the
initial delay (by default it is random, from0 to 5 minutes).

Settings
--------

* ``ROTATING_PROXY_LIST``  - a list of proxies to choose from;
* ``ROTATING_PROXY_LOGSTATS_INTERVAL`` - stats logging interval in seconds,
  30 by default;
* ``ROTATING_PROXY_CLOSE_SPIDER`` - When True, spider is stopped if
  there are no alive proxies. If False (default), then when there is no
  alive proxies all dead proxies are re-checked.
* ``ROTATING_PROXY_PAGE_RETRY_TIMES`` - a number of times to retry
  downloading a page using a different proxy. After this amount of retries
  failure is considered a page failure, not a proxy failure. Default: 15.
* ``ROTATING_PROXY_BACKOFF_BASE`` - base backoff time, in seconds.
  Default is 300 (i.e. 5 min).

Contributing
------------

* source code: https://github.com/TeamHG-Memex/scrapy-rotating-proxies
* bug tracker: https://github.com/TeamHG-Memex/scrapy-rotating-proxies/issues

To run tests, install tox_ and run ``tox`` from the source checkout.

.. _tox: https://tox.readthedocs.io/en/latest/
