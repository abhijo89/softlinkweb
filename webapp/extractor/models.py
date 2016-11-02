from django.db import models


class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class NewsChanel(BaseModel):
    name = models.CharField(max_length=100)


class NewsPaper(BaseModel):
    url = models.URLField(max_length=200, unique=True)
    name = models.CharField(max_length=100)
    chanel = models.ForeignKey(NewsChanel)
    is_enable = models.BooleanField(default=False)


class Article(BaseModel):

    news_paper = models.ForeignKey(NewsPaper)
    original_url = models.URLField( unique=True)
    title = models.CharField(max_length=240, null=True)
    summary = models.TextField(null=True)
    text = models.TextField(null=True)
    is_published = models.BooleanField(default=False)


class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    article = models.ForeignKey('Article')


class Author(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    article = models.ForeignKey(Article, null=True)


class Image(BaseModel):
    file = models.ImageField(upload_to="%Y/%m/%d/")
    is_top_image = models.BooleanField(default=False)
    article = models.ForeignKey(Article, null=True)


class Video(BaseModel):
    url = models.URLField()
    article = models.ForeignKey(Article)


class Tag(BaseModel):

    name = models.CharField(max_length=240)
    article = models.ForeignKey(Article, null=True)