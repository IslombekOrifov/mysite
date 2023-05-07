from django.utils import timezone
from django.db.models import Count

from .models import Category

def get_categories(request):
    return {'categories': Category.objects.filter(is_active=True).annotate(posts_count=Count('posts')).order_by('custom_order')}