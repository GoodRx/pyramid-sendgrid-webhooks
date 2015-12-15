========
Usage
========

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
