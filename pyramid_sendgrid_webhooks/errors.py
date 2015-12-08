# -*- coding: utf-8 -*-
""" Exception classes raised when parsing fails """


class UnknownEventError(KeyError):
    """ Raised when an unfamiliar event is received """
