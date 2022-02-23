from django.shortcuts import render

from .models import Section, ResumeFile


def home(request):
    template = 'resume/home.html'
    sections = Section.objects.order_by('section_weight')
    resume_file = ResumeFile.objects.get(pk=1)

    return render(request, template, {
        'sections': sections,
        'resume_file': resume_file,
    })
