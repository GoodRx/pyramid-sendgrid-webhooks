# -*- coding: utf-8 -*-
"""
Parses webhook events from request
"""

from . import events
from . import errors


def parse_event_data(request, event_data):
    """ Returns a single BaseWebhookEvent instance """
    event_type = event_data['event']
    try:
        event_cls = events.event_mapping[event_type]
    except KeyError:
        raise errors.UnknownEventError(event_type)

    return event_cls(request, event_data)


def webhooks_from_request(request):
    """
    Generates a sequence of BaseWebhookEvent instances
    """
    for event_data in request.json_body:
        yield parse_event_data(request, event_data)
