import sys
from random import randint

from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify

from blog.models import CustomUser, Post, Category


class Command(BaseCommand):
    help = 'Add users'

    def handle(self, count=1000, *args, **options):

        title = "Lorem ipsum dolor sit amet,\
                'consectetur adipiscing elit,\
                sed do eiusmod tempor incididunt\
                ut labore et dolore magna aliqua."
        body = "Lorem ipsum dolor sit amet,\
                'consectetur adipiscing elit,\
                sed do eiusmod tempor incididunt\
                'consectetur adipiscing elit,\
                sed do eiusmod tempor incididunt\
                'consectetur adipiscing elit,\
                sed do eiusmod tempor incididunt\
                'consectetur adipiscing elit,\
                sed do eiusmod tempor incididunt\
                'consectetur adipiscing elit,\
                sed do eiusmod tempor incididunt\
                'consectetur adipiscing elit,\
                sed do eiusmod tempor incididunt\
                ut labore et dolore magna aliqua."

        admin = CustomUser.objects.get(is_superuser=True)
        categories = Category.objects.filter(is_active=True)

        for _ in categories:
            # you can pass params explicitly
            posts = list((Post(title=title + str(randint(1, 500)), slug=slugify(title + str(randint(1, 500))), body=body, author=admin, category=_, status=Post.Status.PUBLISHED) for i in range(27)))
            Post.objects.bulk_create(posts)