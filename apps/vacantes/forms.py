from django import forms
from .models import Perfil

class PerfilForm(forms.ModelForm):
    genero = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-inputs'}),
        choices=Perfil.opcionesGenero
    )

    class Meta:
        model = Perfil
        fields = ["genero"]
