from django.utils import timezone
from .models import SocialNetwork

def get_socials(request):
    return {'social_net': SocialNetwork.objects.filter(is_active=True).order_by('order'),
            'current_year': timezone.now().year }