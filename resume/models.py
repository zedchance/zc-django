from django.db import models

from .md import markdownify


class Entry(models.Model):
    title = models.CharField(max_length=300)
    range_text = models.CharField(max_length=40, blank=True)
    description = models.TextField(blank=True)
    weight = models.IntegerField(name='entry_weight', default=5)
    link = models.URLField(blank=True)
    image = models.ImageField(blank=True, null=True)
    is_short_entry = models.BooleanField(default=False)

    def get_description_as_md(self):
        return markdownify(self.description)

    def __str__(self):
        return self.title


class Section(models.Model):
    title = models.CharField(max_length=100, name='title')
    description = models.TextField(blank=True)
    weight = models.IntegerField(name='section_weight', default=5)
    entries = models.ManyToManyField(Entry, name='entries', blank=True)

    def get_entries_by_weight(self):
        return self.entries.order_by('entry_weight')

    def get_description_as_md(self):
        return markdownify(self.description)

    def __str__(self):
        return self.title


