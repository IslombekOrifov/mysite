from typing import Iterable, Optional
from django.db import models

from .services import (
    upload_sertificate_path, upload_coding_lang_path,
    upload_quote_path, upload_cv_path
)


class SocialNetwork(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(max_length=200)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.name
    

class Education(models.Model):
    edu_name = models.CharField(max_length=250, unique=True) 
    year = models.CharField(max_length=50) 
    specialty = models.CharField(max_length=50)
    about = models.CharField(max_length=50)

    def __str__(self):
        return self.edu_name
    

class Experience(models.Model):
    company = models.CharField(max_length=250, unique=True) 
    year = models.CharField(max_length=50) 
    specialty = models.CharField(max_length=50)
    about = models.CharField(max_length=50)

    def __str__(self):
        return self.company
    

class Sertificate(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=upload_sertificate_path)
    image = models.ImageField(upload_to=upload_sertificate_path)
    year = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.name
    

class CodingLanguage(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to=upload_coding_lang_path)
    is_active = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['order',]

    def __str__(self):
        return self.name


class Quote(models.Model):
    author = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    from_where = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_quote_path)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} -> {self.from_where}"
    

class FunFact(models.Model):
    projects = models.PositiveSmallIntegerField(default=1)
    clients = models.PositiveSmallIntegerField(default=1)
    work_hour = models.PositiveSmallIntegerField(default=0)
    posts = models.PositiveSmallIntegerField(default=0)
    cv = models.FileField(upload_to=upload_cv_path, blank=True, null=True)
    about_me = models.CharField(max_length=350, blank=True)

    def save(self, *args, **kwargs):
        if FunFact.objects.exists():
            raise ValueError("You can add only one item for this model")
        else:
            super().save(self, *args, **kwargs)

class Contact(models.Model):
    tel = models.CharField(max_length=20, blank=True)
    tel1 = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)

    def __str__(self):
        return self.tel
    

class UserLetter(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.full_name} -> {self.subject}"