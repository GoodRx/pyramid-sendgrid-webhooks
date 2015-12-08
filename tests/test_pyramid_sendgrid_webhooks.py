#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyramid_sendgrid_webhooks
----------------------------------

Tests for `pyramid_sendgrid_webhooks` module.
"""

from __future__ import unicode_literals

import json
import unittest
from pyramid import testing

import pyramid_sendgrid_webhooks as psw
from pyramid_sendgrid_webhooks import events


class EventGrabber(object):
    """ Grabs events as they're dispatched """
    def __init__(self):
        self.events = []

    def __call__(self, event):
        self.events.append(event)


class WebhookTestBase(unittest.TestCase):
    def setUp(self):
        self.request = testing.DummyRequest()
        self.config = testing.setUp(request=self.request)

    def tearDown(self):
        testing.tearDown()

    def _createGrabber(self, event_cls):
        grabber = EventGrabber()
        self.config.add_subscriber(grabber, event_cls)
        return grabber

    def _createRequest(self, json_body):
        self.request.json_body = json.loads(json_body)
        return self.request


class TestBaseEvents(WebhookTestBase):

    def _makeOne(self, n=1, single_category=False):
        return json.dumps([{
            'asm_group_id': 1,
            'category': 'c' if single_category else ['c1', 'c2'],
            'cert_error': '0',
            'email': 'email@example.com',
            'event': 'bounce',
            'ip': '127.0.0.1',
            'reason': '500 No Such User',
            'sg_event_id': 'sendgrid_internal_event_id',
            'sg_message_id': 'sendgrid_internal_message_id',
            'smtp-id': '<original-smtp-id@domain.com>',
            'status': '5.0.0',
            'timestamp': 1249948800,
            'tls': '1',
            'type': 'bounce',
            'unique_arg_key': 'unique_arg_value',
        }] * n)

    def test_event_parsed(self):
        grabber = self._createGrabber(events.BaseWebhookEvent)
        request = self._createRequest(self._makeOne())
        psw.receive_events(request)

        self.assertEqual(len(grabber.events), 1)


class TestDeliveryEvents(WebhookTestBase):
    def _makeOne(self):
        return json.dumps([{
            'asm_group_id': 1,
            'category': ['category1', 'category2'],
            'cert_error': '0',
            'email': 'email@example.com',
            'event': 'bounce',
            'ip': '127.0.0.1',
            'reason': '500 No Such User',
            'sg_event_id': 'sendgrid_internal_event_id',
            'sg_message_id': 'sendgrid_internal_message_id',
            'smtp-id': '<original-smtp-id@domain.com>',
            'status': '5.0.0',
            'timestamp': 1249948800,
            'tls': '1',
            'type': 'bounce',
            'unique_arg_key': 'unique_arg_value',
        }])


class TestEngagementEvents(WebhookTestBase):
    def _makeOne(self):
        return json.dumps([{
            'asm_group_id': 1,
            'category': ['category1', 'category2'],
            'email': 'email@example.com',
            'event': 'click',
            'ip': '255.255.255.255',
            'newsletter': {'newsletter_id': '1943530',
            'newsletter_send_id': '2308608',
            'newsletter_user_list_id': '10557865'},
            'sg_event_id': 'sendgrid_internal_event_id',
            'sg_message_id': 'sendgrid_internal_message_id',
            'timestamp': 1249948800,
            'unique_arg_key': 'unique_arg_value',
            'url': 'http://yourdomain.com/blog/news.html',
            'useragent': 'Example Useragent',
        }])


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
