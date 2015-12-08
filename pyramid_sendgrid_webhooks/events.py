# -*- coding: utf-8 -*-
"""
Classes for incoming webhook events
"""

import datetime


class BaseWebhookEvent(object):
    """
    Interface shared by all webhook events
    """

    RESERVED_NAMES = {'event', 'email', 'timestamp', 'ip', 'tls', 'cert_error',
                      'stmp-id', 'useragent', 'category', 'reason', 'type',
                      'status', 'url'}

    def __init__(self, request, data):
        self.request = request
        self.data = dict(data)
        self.event = self.data['event']
        self.email = self.data['email']
        self.timestamp = self.data['timestamp']
        self.ip = self.data['ip']
        self.tls = self.data['tls']
        self.cert_error = self.data['tls']

        self.category = self.data['category']

        self.unique_arguments = self.extract_unique_params(self.data)

    @classmethod
    def extract_unique_params(cls, data):
        """
        Returns a dictionary of all unique arguments provided

        Unique arguments are considered to be any provided arguments that
        aren't known Sendgrid names
        """
        return {k: v for k, v in data.iteritems()
                if k not in cls.RESERVED_NAMES}

    @property
    def dt(self):
        """ Naive UTC datetime corresponding to this event's timestamp """
        return datetime.datetime.utcfromtimestamp(self.timestamp)

    @property
    def categories(self):
        """ Returns categories as a list """
        if not self.category:
            return []
        elif isinstance(self.category, basestring):
            return [self.category]
        else:
            return list(self.category)


class BaseDeliveryEvent(BaseWebhookEvent):
    """
    Basic interface shared for all delivery events

    - bounce
    - deferred
    - delivered
    - dropped
    - processed
    """
    def __init__(self, request, data):
        super(BaseDeliveryEvent, self).__init__(request, data)
        self.smtp_id = self.data['smtp-id']


class BaseEngagementEvent(BaseWebhookEvent):
    """
    Basic interface shared for all engagement events

    - click
    - open
    - spamreport
    - unsubscribe
    """
    def __init__(self, request, data):
        super(BaseEngagementEvent, self).__init__(request, data)
        self.useragent = self.data['useragent']


class BounceEvent(BaseDeliveryEvent):
    def __init__(self, request, data):
        super(BounceEvent, self).__init__(request, data)
        self.status = self.data['status']
        self.reason = self.data['reason']
        self.type = self.data['type']


class DeferredEvent(BaseDeliveryEvent):
    def __init__(self, request, data):
        super(DeferredEvent, self).__init__(request, data)
        self.response = self.data['response']
        self.attempt = self.data['attempt']


class DeliveredEvent(BaseDeliveryEvent):
    def __init__(self, request, data):
        super(DeliveredEvent, self).__init__(request, data)
        self.response = self.data['response']


class DroppedEvent(BaseDeliveryEvent):
    def __init__(self, request, data):
        super(DroppedEvent, self).__init__(request, data)
        self.reason = self.data['reason']


class ProcessedEvent(BaseDeliveryEvent):
    pass


class ClickEvent(BaseEngagementEvent):
    def __init__(self, request, data):
        super(ClickEvent, self).__init__(request, data)
        self.url = self.data['url']


class OpenEvent(BaseEngagementEvent):
    pass


class SpamReportEvent(BaseEngagementEvent):
    pass


class UnsubscribeEvent(BaseEngagementEvent):
    pass


class GroupUnsubscribeEvent(BaseEngagementEvent):
    def __init__(self, request, data):
        super(GroupUnsubscribeEvent, self).__init__(request, data)
        self.asm_group_id = self.data['asm_group_id']


class GroupResubscribeEvent(BaseEngagementEvent):
    def __init__(self, request, data):
        super(GroupResubscribeEvent, self).__init__(request, data)
        self.asm_group_id = self.data['asm_group_id']


event_mapping = {
    'bounce': BounceEvent,
    'click': ClickEvent,
    'deferred': DeferredEvent,
    'delivered': DeliveredEvent,
    'dropped': DroppedEvent,
    'open': OpenEvent,
    'processed': ProcessedEvent,
    'spamreport': SpamReportEvent,
    'unsubscribe': UnsubscribeEvent,
    'group_unsubscribe': GroupUnsubscribeEvent,
    'group_resubscribe': GroupResubscribeEvent,
}
