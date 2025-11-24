from django.forms import ModelForm

from bboard.models import Bboard


class BoardForm(ModelForm):
    class Meta:
        model = Bboard
        fields = ('title', 'content', 'price', 'rubric')
