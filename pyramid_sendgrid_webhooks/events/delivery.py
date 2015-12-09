# -*- coding: utf-8 -*-
"""
Classes for incoming delivery webhook events

BounceEvent
DeferredEvent
DeliveredEvent
DroppedEvent
ProcessedEvent
"""

from .base import BaseWebhookEvent


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


class BounceEvent(BaseDeliveryEvent):
    def __init__(self, request, data):
        super(BounceEvent, self).__init__(request, data)
        self.status = self.data['status']
        self.reason = self.data['reason']
        self.type = self.data.get('type')


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
