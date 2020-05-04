from django.db import models
from django_extensions.db.fields import AutoSlugField
# Create your models here.
class Tag(models.Model):
    name=models.CharField(max_length=31,unique=True)
    #slug=models.SlugField(max_length =31,unique=True, help_text="A label for URL config." )
    slug=AutoSlugField(help_text='A label for URL config.',max_length=31,populate_from=['name'])
    class Meta:
        ordering= ["name"]

    def __str__(self):
        return self.name


class Startup(models.Model):
    name = models.CharField(max_length=31,db_index=True)
    slug= AutoSlugField(max_length=31,unique=True,help_text="A label for URL config.",populate_from=['name'])
    description=models.TextField()
    founded_date=models.DateField("Date founded")
    contact = models.EmailField()
    website=models.URLField(max_length=255)
    tags=models.ManyToManyField(Tag)

    class Meta:
        ordering=["name"]
        get_latest_by ="founded_date"

    def __str__(self):
        return self.name

class Newslink(models.Model):
    title = models.CharField(max_length=31)
    slug = AutoSlugField(max_length=31,populate_from=['title'])
    pub_date = models.DateField("Date published")
    link = models.URLField(max_length=255)
    startup=models.ForeignKey(Startup,on_delete=models.CASCADE)

    class Meta:
        get_latest_by="pub_date"
        ordering=["-pub_date"]
        unique_together=['slug','startup']
        verbose_name="news article"

    def __str__(self):
        return f"{self.startup}: {self.title}"
