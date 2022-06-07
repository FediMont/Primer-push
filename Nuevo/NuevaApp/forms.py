from django import forms
from NuevaApp.models import Bibliotecas

# class Biblio_form(forms.Form):
#     nombre = forms.CharField(max_length=40)
#     provincia = forms.CharField(max_length=40)
#     localidad = forms.CharField(max_length=40)
#     direccion = forms.CharField(max_length=60)
#     apertura = forms.CharField(max_length=100)
#     link = forms.URLField(max_length=100)
#     imagen = forms.URLField(max_length=100)

class Biblio_form(forms.ModelForm):
    class Meta:
        model = Bibliotecas
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'provincia': forms.TextInput(attrs={'class':'form-control'}),
            'localidad': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'apertura': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control'}),
            'imagen': forms.URLInput(attrs={'class':'form-control'}),
        }