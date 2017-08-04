from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.urlresolvers import reverse
from tag.models import Tag


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(allow_unicode=True, unique=True)
    # todo: change the text into the area with words and images
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:single", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-created_date"]



