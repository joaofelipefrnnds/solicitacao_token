from django.forms import ModelForm
from .models import Servidor


class ServidorForm(ModelForm):
    class Meta:
        model = Servidor
        fields = ['nome', 'cpf', 'rg', 'telefone','email', 'fk_cargo','fk_coordenadoria', 'fk_departamento']