from django import forms
from .models import Movie

class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    title_en = forms.CharField(max_length=100)
    audience = forms.IntegerField()
    open_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={'type':'date'})
        ) # 속성 중 type을 date로 바꿔줌.
    genre = forms.CharField(max_length=100)
    watch_grade = forms.IntegerField()
    score = forms.IntegerField()
    poster_url = forms.CharField(max_length=100)
    description = forms.CharField(
        widget=forms.Textarea()
        )
    
class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'open_date':forms.DateInput(attrs={'type':'date'})
        }