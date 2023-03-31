from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=30, blank=False)
    titles = models.IntegerField(blank=True, null=True, default=0)
    top_scorer = models.CharField(max_length=50, blank=False)
    fifa_code = models.CharField(max_length=3, blank=False, unique=True)
    first_cup = models.DateField(blank=True, null=True)

    def __repr__(self) -> str:
        return f"<[{self.id}] {self.name} - {self.fifa_code}>"
