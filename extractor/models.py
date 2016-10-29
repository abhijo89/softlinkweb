#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by abhilash on 29/10/16  
# File Name: models.py

from extractor import ModelBase
from sqlalchemy import Column, Integer, String


class NewsPaperUrls(ModelBase):
    __tablename__ = 'news_papper_urls'

    id = Column(Integer, primary_key=True)
    url = Column(String)

    def __repr__(self):
        return "<NewsPaperUrls(url=%s" % self.url


