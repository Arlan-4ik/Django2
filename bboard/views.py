from django.template import loader

from django.http import HttpResponse
from django.shortcuts import render

from bboard.models import Bboard, Rubric


def index(request):
    template = loader.get_template('index.html')
    bbs = Bboard.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}


    return render(request, 'index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bboard.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'create.html'
    form_class = BForm
    success_url = '/'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
