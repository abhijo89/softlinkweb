#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by abhilash on 29/10/16  
# File Name: get_all_article.py


from django.core.management.base import BaseCommand, CommandError
from extractor.models import NewsPaper, Article, Author, Image, Tag, Video
import newspaper
import urllib3

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
class Command(BaseCommand):
    help = 'Get all article urls and save it '


    def handle(self, *args, **options):
        http = urllib3.PoolManager()
        for model in NewsPaper.objects.filter(is_enable=True):
            newspaperobject = newspaper.build(model.url, memoize_articles=True)

            for article in newspaperobject.articles:
                try:
                    article.download()
                    article.parse()
                    article.nlp()
                except Exception:
                    continue
                self.stdout.write(self.style.SUCCESS('Parsing %s' % article.title))

                article_model, c = Article.objects.get_or_create(news_paper=model, original_url=article.canonical_link)

                if c:
                    article_model.text = article.text
                    article_model.title = article.title
                    article_model.summary = article.summary
                    try:
                        article_model.save()
                    except Exception:
                        continue
                """
                if article.top_image:
                    img_temp = NamedTemporaryFile(delete=True)
                    img_temp.write(http.request('GET', article.top_image).data)
                    img_temp.flush()
                    Image.objects.get_or_create(file=File(img_temp), article=article_model, is_top_image=True)
                """
                for author in article.authors:
                    a, c = Author.objects.get_or_create(name=author)
                    a.article = article_model
                    a.save()

                for keyword in article.keywords:
                    t, c = Tag.objects.get_or_create(name=keyword, article=article_model)
                    t.article = article_model
                    t.save()
                """
                for image in article.images:
                    img_temp = NamedTemporaryFile(delete=True)
                    img_temp.write(img_temp.write(http.request('GET', image).data))
                    img_temp.flush()
                    Image.objects.get_or_create(file=File(img_temp), article=article_model)
                """

                for video in article.movies:
                    Video.objects.get_or_create(url=video, article=article_model)


