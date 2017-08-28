# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Startup(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()
    description = models.TextField()
    founded_date = models.DateField()
    contact = models.EmailField()
    website = models.URLField()

class NewsLink(models.Model):
    title = models.CharField(max_length=63)
    pub_date = models.DateField()
    link = models.URLField()

class Tag(models.Model):
    name = models.CharField(
        max_length = 31, unique = True)
    slug = models.SlugField(
        max_length = 31,
        unique = True,
        help_text='A label for URL config')

class Startup(models.Model):
    name = models.CharField(
        max_length=31, db_index = True)
    slug = models.SlugField(
        max_length = 31,
        unique = True,
        help_text = 'A label for URL config',
    )
    description = models.TextField()
    founded_date = models.DateField(
        'date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

class Post(models.Model):
    
