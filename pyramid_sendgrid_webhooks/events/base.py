# -*- coding: utf-8 -*-
"""
Base classes for webhook events
"""

import logging
import datetime

try:
    STR_TYPE = basestring
except NameError:
    STR_TYPE = str

LOGGER = logging.getLogger(__name__)


class BaseWebhookEvent(object):
    """
    Interface shared by all webhook events
    """

    RESERVED_NAMES = {'event', 'email', 'timestamp', 'ip', 'tls', 'cert_error',
                      'smtp-id', 'useragent', 'category', 'reason', 'type',
                      'status', 'url', 'asm_group_id'}

    def __init__(self, request, data):
        LOGGER.debug("Received data %r", data)
        self.request = request
        self.data = dict(data)
        self.event = self.data['event']
        self.email = self.data['email']
        self.timestamp = self.data['timestamp']

        self.ip = self.data.get('ip')
        self.tls = self.data.get('tls')
        self.cert_error = self.data.get('cert_error')

        self.category = self.data['category']

        self.unique_arguments = self.extract_unique_params(self.data)

    @classmethod
    def extract_unique_params(cls, data):
        """
        Returns a dictionary of all unique arguments provided

        Unique arguments are considered to be any provided arguments that
        aren't known Sendgrid names
        """
        return {k: v for k, v in data.items()
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
        elif isinstance(self.category, STR_TYPE):
            return [self.category]
        else:
            return list(self.category)


__all__ = ['BaseWebhookEvent']
