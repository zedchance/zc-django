from django.db import models
from django.shortcuts import redirect
from django.utils.safestring import mark_safe

from .md import markdownify


class Entry(models.Model):
    title = models.CharField(max_length=300)
    range_text = models.CharField(max_length=40, blank=True)
    description = models.TextField(blank=True)
    weight = models.IntegerField(name='entry_weight', default=5)
    link = models.URLField(blank=True)
    image = models.ImageField(blank=True, null=True)
    is_short_entry = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Entries'

    def get_description_as_md(self):
        return markdownify(self.description)

    def get_sections(self):
        return list(Section.objects.filter(entries=self))

    def get_links_to_sections(self):
        sections = self.get_sections()
        links = ['<a href="{}">{}</a>'.format(
            redirect('admin:resume_section_change', i.id).url,
            i.title,
        ) for i in sections]
        return mark_safe(', '.join(links))

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

    def get_links_to_entries(self):
        entries = self.get_entries_by_weight()
        links = ['<code>{}   <a href="{}">{}</a></code>'.format(
            i.entry_weight,
            redirect('admin:resume_entry_change', i.id).url,
            i.title,
        ) for i in entries]
        return mark_safe('<br>'.join(links))

    def __str__(self):
        return self.title


class ResumeFile(models.Model):
    file = models.FileField(upload_to='uploads/', null=True, blank=True)
