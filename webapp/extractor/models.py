from django.db import models


class BaseModel(models.Model):

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100)


class NewsPaper(BaseModel):
    url = models.URLField(max_length=200)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    is_enable = models.BooleanField(default=False)


class Author(BaseModel):
    name = models.CharField(max_length=100)


class Article(BaseModel):

    news_paper = models.ForeignKey(NewsPaper)
    original_url = models.URLField(db_index=True)
    title = models.CharField(max_length=240, null=True)
    summary = models.TextField(null=True)
    text = models.TextField(null=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(Author, null=True)


class Image(BaseModel):
    file = models.ImageField(upload_to="%Y/%m/%d/")
    is_top_image = models.BooleanField(default=False)
    article = models.ForeignKey(Article)


class Video(BaseModel):
    url = models.URLField()
    article = models.ForeignKey(Article)


class Tag(BaseModel):

    name = models.CharField(max_length=240, db_index=True)
    article = models.ForeignKey(Article)