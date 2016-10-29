#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by abhilash on 29/10/16  
# File Name: base.py


class AsyncConnection(object):
    pass


class BaseExtractor(object):

    def __int__(self):
        self.url = None

    def start(self):
        pass
