# -*- coding: utf-8 -*-
"""
Classes for incoming engagement webhook events

ClickEvent
OpenEvent
SpamReportEvent
UnsubscribeEvent
GroupUnsubscribeEvent
GroupResubscribeEvent
"""

from .base import BaseWebhookEvent


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
        self.useragent = self.data.get('useragent')


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
