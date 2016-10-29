#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by abhilash on 29/10/16  
# File Name: connection.py

from sqlalchemy import create_engine
engine = create_engine('mysql://root:root@localhost/softlinkweb', pool_size=20, max_overflow=0)
