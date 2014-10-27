from django.db import models
from django.utils.timezone import now
from django.core.urlresolvers import reverse
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(default=now)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk, 'post_slug': slugify(self.title)})
