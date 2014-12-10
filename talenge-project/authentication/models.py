from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('s', 'Student'),
        ('c', 'Company' ),
    )
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    type_user = models.CharField(max_length=20, default='s',choices=USER_TYPE_CHOICES)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
