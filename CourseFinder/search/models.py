from django.db import models


# Create your models here.
class base(models.Model):

    keyword = models.TextField(default="C++")
    name = models.TextField(max_length=100)
    description = models.TextField(max_length=300)
    Link = models.URLField(max_length=100)
    Duration = models.DurationField()
    KeyDuration = models.IntegerField(default=1)

    def __str__(self):
        return f"File id: {self.id}"
