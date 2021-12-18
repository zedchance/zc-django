from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin

from .models import Section, Entry


class EntryAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('title', 'entry_weight', 'get_links_to_sections', )
    search_fields = ('title', 'id', )
    fields = ('get_links_to_sections', 'title', 'range_text', 'description', 'entry_weight', 'link', 'image',
              'is_short_entry', )
    readonly_fields = ('get_links_to_sections', )


class SectionAdmin(ImportExportModelAdmin, ImportExportActionModelAdmin):
    list_display = ('title', 'section_weight', )
    fields = ('title', 'description', 'section_weight', 'entries', 'get_links_to_entries', )
    filter_vertical = ('entries', )
    readonly_fields = ('get_links_to_entries', )


admin.site.register(Section, SectionAdmin)
admin.site.register(Entry, EntryAdmin)
