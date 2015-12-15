# -*- coding: utf-8 -*-
"""
Pyramid plugin to receive, parse, and dispatch Sendgrid Webhook events

To use this app, add a configuration statement with your intended webhook
callback path:

    config.include('pyramid_sendgrid_webhooks', '/sendgrid/webhooks')

Then, set up subscribers for any events that you want to be notified of:

    from pyramid_sendgrid_webhooks import events

    def handle_bounce(event):
        request = event.request
        print event.reason

    ...
    config.add_subscriber(handle_bounce, events.BounceEvent)

Currently the app adds a single endpoint at '{PREFIX}/receive'.  This will be
the webhook path to give to Sendgrid.
"""

from . import parser

__author__ = 'Kyle Stark'
__email__ = 'kyle@goodrx.com'
__version__ = '1.2.1'


def receive_events(request):
    for event in parser.webhooks_from_request(request):
        request.registry.notify(event)
    return request.response


def includeme(config):
    """
    Adds route and view configuration
    """
    config.add_route('sendgrid-webhook-receive', '/receive')
    config.add_view(receive_events, route_name='sendgrid-webhook-receive')
