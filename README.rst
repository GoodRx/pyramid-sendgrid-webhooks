===============================
Pyramid Sendgrid Webhooks
===============================

.. image:: https://img.shields.io/pypi/v/pyramid_sendgrid_webhooks.svg
        :target: https://pypi.python.org/pypi/pyramid_sendgrid_webhooks

.. image:: https://img.shields.io/travis/GoodRx/pyramid-sendgrid-webhooks.svg
        :target: https://travis-ci.org/GoodRx/pyramid-sendgrid-webhooks

.. image:: https://readthedocs.org/projects/pyramid_sendgrid_webhooks/badge/?version=latest
        :target: https://readthedocs.org/projects/pyramid_sendgrid_webhooks/?badge=latest
        :alt: Documentation Status


Parses incoming Sendgrid Webhooks in Pyramid  apps

* Free software: MIT license
* Documentation: https://pyramid_sendgrid_webhooks.readthedocs.org.

Features
--------

To use this app, add a configuration statement with your intended webhook
callback path:

.. code:: python

    config.include('pyramid_sendgrid_webhooks', '/sendgrid/webhooks')

Then, set up subscribers for any events that you want to be notified of:

.. code:: python

    from pyramid_sendgrid_webhooks import events

    def handle_bounce(event):
        request = event.request
        print event.reason

    ...
    config.add_subscriber(handle_bounce, events.BounceEvent)


Credits
---------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-pypackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
