from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    SPECIES = (
        ('Sutemizuvchilar', 'Sutemizuvchilar'),
        ('Qushlar', 'Qushlar'),
        ('Baliqlar', 'Baliqlar'),
        ('Amfibiyalar', 'Amfibiyalar'),
        ('Sudralib yuruvchilar', 'Sudralib yuruvchilar'),
        ('Artropodlar', 'Artropodlar'),
        ('Mollyuskalar', 'Mollyuskalar'),
        ('Echinodermlar', 'Echinodermlar'),
        ('Qurtlar', 'Qurtlar'),
        ('Gubkalar', 'Gubkalar'),
        ('Cnidarians', 'Cnidarians'),
    )
    name = models.CharField(choices=SPECIES, blank=True, max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='articles_cat')
    image = models.ImageField(upload_to='article/%Y/%m/%d')
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='articles_user')
    published = models.DateField(auto_now_add=True)
    body = models.TextField()
    tag = models.ManyToManyField(Tag, related_name='articles_tag')

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    comment = models.TextField()
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.article.slug)


class Reply_Comment(models.Model):
    for_comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='reply_comments')
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    replay_comment = models.TextField()
    published = models.DateField(auto_now_add=True)
