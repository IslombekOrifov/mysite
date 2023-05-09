from django.db.models.signals import post_save
from django.dispatch import receiver

from firebase_admin.messaging import Message, Notification
from fcm_django.models import FCMDevice

from .models import Post


@receiver(post_save, sender=Post)
def handle_new_post(sender, instance, **kwargs):
    message_obj = Message(
    notification=Notification(title=instance.title, body=instance.body[:30] + '...', image=instance.image.url),
    topic="Optional topic parameter: Whatever you want",
)

    # You can still use .filter() or any methods that return QuerySet (from the chain)
    device = FCMDevice.objects.all()
    # send_message parameters include: message, dry_run, app
    device.send_message(message_obj)