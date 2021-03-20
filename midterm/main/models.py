from datetime import datetime

from django.db import models


class BookJournalBase(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(default=0.0)
    description = models.TextField(default='')
    created_at = models.DateField(auto_created=True, default=datetime.now())

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0)
    genres = models.CharField(max_length=255)


class Journal(BookJournalBase):
    TYPE = [(1, "Bullet"), (2, "Food"), (3, "Travel"), (4, "Sport")]
    type = models.IntegerField(choices=TYPE, default=1)
    publisher = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Journal'
        verbose_name_plural = 'Journals'
