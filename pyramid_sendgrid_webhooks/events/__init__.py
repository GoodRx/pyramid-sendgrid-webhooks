# -*- coding: utf-8 -*-
"""
Classes for incoming webhook events
"""

# pylint: disable=unused-import
from .base import BaseWebhookEvent  # NOQA
from .delivery import (
    BounceEvent,
    DeferredEvent,
    DeliveredEvent,
    DroppedEvent,
    ProcessedEvent,
)
from .engagement import (
    ClickEvent,
    OpenEvent,
    SpamReportEvent,
    UnsubscribeEvent,
    GroupUnsubscribeEvent,
    GroupResubscribeEvent,
)

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
