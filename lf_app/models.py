'''Model definition for the `loc` application.'''

from django.core.exceptions import ValidationError
from django.conf import settings
from django.urls import reverse
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy

from taggit.managers import TaggableManager

class Link(models.Model):
    url = models.URLField(
        max_length=1024,
        default='')

    title = models.CharField(
        max_length=1024,
        default='')

    notes = models.TextField(
        default='',
        blank=True)

    created_on = models.DateTimeField(auto_now_add=True)

    updated_on = models.DateTimeField(auto_now=True)

    follow_count = models.PositiveIntegerField(default=0)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)

    tags = TaggableManager()

    def __str__(self):
        return f'Link: {self.title}'


    def get_absolute_url(self):
        return reverse('lf:link', args=[self.id])


    def get_tags(self):
        return self.tags.order_by('name')
