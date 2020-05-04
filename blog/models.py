from django.db import models
from organizer.models import Startup , Tag
from django_extensions.db.fields import AutoSlugField #new
class Post(models.Model):
    title=models.CharField(max_length=75)
    slug=models.SlugField(max_length=75)
    text=models.TextField()
    pub_date=models.DateField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    startup=models.ManyToManyField(Startup)

    class Meta:
        get_latest_by="pub_date"
        ordering=["-pub_date","title"]
        verbose_name="Blog post"


    def __str__(self):
        date_string=self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"
