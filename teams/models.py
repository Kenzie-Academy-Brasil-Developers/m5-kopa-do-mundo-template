from django.db import models


# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=30)
    titles = models.IntegerField(default=0, null=True)
    top_scorer = models.CharField(max_length=50)
    fifa_code = models.CharField(max_length=3, unique=True)
    first_cup = models.DateField(null=True)

    def __repr__(self):
        return f"<[{self.id}] {self.name} - {self.fifa_code}>"
