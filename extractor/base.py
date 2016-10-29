#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by abhilash on 29/10/16  
# File Name: base.py


class AsyncConnection(object):
    pass


class Extractor(object):

    def __init__(self):
        pass

    def get_url_from_db(self):
        pass


class BaseExtractor(object):

    def __int__(self):
        self.url = None

    def start(self):
        pass

