from django.shortcuts import render

from .models import Section, Entry


def home(request):
    template = 'resume/home.html'
    sections = Section.objects.order_by('section_weight')

    return render(request, template, {
        'sections': sections,
    })
