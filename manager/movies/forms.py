from django.forms import ModelForm
from .models import MovieDB

class MovieClass(ModelForm):
    class Meta:
        model = MovieDB
        fields='__all__'
        