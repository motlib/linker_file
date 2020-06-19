'''Model definition for the `loc` application.'''

from django.core.exceptions import ValidationError
from django.urls import reverse
from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
