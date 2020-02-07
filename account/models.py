from django.db import models
from django.contrib.auth.models import User

from addressbook.models import Address


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    addresses = models.ManyToManyField(Address)

    def __unicode__(self):
        return self.user.email

    @property
    def address(self):
        return self.addresses.latest()
