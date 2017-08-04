from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tags:tag_post", kwargs={"pk": self.pk})
