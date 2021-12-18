from django import forms

from .models import Entry


class EntryChangeListForm(forms.ModelForm):
    entries = forms.ModelMultipleChoiceField(
        queryset=Entry.objects.all(),
        required=False,
    )
