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
        Category, on_delete=models.PROTECT, related_name='articles')
    image = models.ImageField(upload_to='article/%Y/%m/%d')
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='articles')
    published = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title
