from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from django.db.models import Avg
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
    body = QuillField()
    tag = models.ManyToManyField(Tag, related_name='articles_tag')
    view = models.PositiveIntegerField(default=0)
    like = models.PositiveIntegerField(default=0)

    @property
    def average_rating(self):
        rating = self.rating.all().aggregate(Avg('value'))['value__avg']
        if rating:
            return str(rating)
        else:
            return 0

    def __str__(self):
        return self.title

    def update_like_plus(self):
        self.like += 1
        self.save()
    

    def update_view(self):
        self.view += 1
        self.save()

    class Meta:
        ordering = ["-id"]


class Rating(models.Model):
    value = models.PositiveIntegerField(default=0)
    product = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="rating")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)


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
