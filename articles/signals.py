from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from articles.models import Article

"""
    We manually assigning the slug field to the new instance before
    it is created with [pre_save], so that once it is saved. The new instance 
    can have its own unique slug
"""
@receiver(pre_save, sender=Article)
def add_slug_to_question(sender, instance, *args, **kwargs):

    if instance:# and not instance.slug:
        slug = slugify(instance.title)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string

# https://learndjango.com/tutorials/django-slug-tutorial