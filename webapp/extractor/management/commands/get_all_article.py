#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by abhilash on 29/10/16  
# File Name: get_all_article.py


from django.core.management.base import BaseCommand, CommandError
from extractor.models import NewsPaper, Article, Author
import newspaper
class Command(BaseCommand):
    help = 'Get all article urls and save it '


    def handle(self, *args, **options):
        for model in NewsPaper.objects.filter(is_enable=True):
            newspaperobject = newspaper.build(model.url)

            for article in newspaperobject.articles:
                article.download()
                article.nlp()
                print(article.text)
                print(article.top_image)
                print(article.authors)
                print(article.title)
                print(article.images)
                print(article.movies)
                article_model, c = Article.objects.get_or_create(newspaper=model, original_url=article.canonical_link)

                if c:
                    article_model.text = article.text
                    article_model.title = article.title
                    article_model.summary = article.summary

                    for author in article.authors:
                        author_model, c = Author.objects.get_or_create(name=author, )

            #self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))