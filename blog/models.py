from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.urls import reverse


from accounts.models import CustomUser

from .services import upload_image_path


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    custom_order = models.PositiveSmallIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['custom_order',]
    
    def __str__(self) -> str:
        return self.name

    
class PublishedManager(models.Manager):
    def get_queryset(self):
            return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    category = models.ForeignKey(
        Category, 
        related_name='posts', 
        on_delete=models.PROTECT
    )
    image = models.ImageField(
        upload_to=upload_image_path, 
        blank=True, 
        null=True
    )
    body = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    status = models.CharField(
        max_length=2, 
        choices=Status.choices, 
        default=Status.DRAFT
    )
    author = models.ForeignKey(CustomUser, on_delete=models.PROTECT, related_name='blog_posts')

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
    def save(self, *args, **kwargs):
        self.title = ' '.join(self.title.strip().split())
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "blog:post_detail", 
            args=[self.publish.year,
                  self.publish.month,
                  self.publish.day,
                  self.slug])
    
