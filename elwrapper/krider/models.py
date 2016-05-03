from django.db import models


class Series(models.Model):

    name = models.CharField(max_length=100, unique=True)
    year = models.IntegerField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Series: {0} - Year: {1}".format(self.name, self.year)
