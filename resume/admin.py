from django.contrib import admin
from django.db import models
from django import forms
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from .models import Section, Entry


class EntryInline(admin.StackedInline):
    model = Section.entries.through
    extra = 1


class EntryAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('title', )


class SectionAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('title', 'section_weight', )
    filter_horizontal = ('entries', )
    # formfield_overrides = {
    #     models.ManyToManyField: {
    #         'widget': forms.CheckboxSelectMultiple
    #     },
    # }
    # inlines = [EntryInline]


admin.site.register(Section, SectionAdmin)
admin.site.register(Entry, EntryAdmin)
