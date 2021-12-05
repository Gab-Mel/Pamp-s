from django.db.models.fields.files import ImageField
from django.forms import ModelForm, fields
from django.forms import widgets
from inicio.models import dados_usuario, agendas
from django.forms.widgets import ClearableFileInput, TextInput, Widget

class novo_user(ModelForm):
    class Meta:
        model = dados_usuario
        fields = ['nome_a', 'nascimento_a', 'email_a', 'senha_a']

class nova_pendencia(ModelForm):
    class Meta:
        model = agendas
        fields = ['pendencia_a', 'inicio_a', 'fim_a']

#class fotofx(ModelForm):
#    foto = ImageField(Widget=ClearableFileInput)
#
#    class Meta:
#        model = fotog
#        fields = '__all__'
#        widgets = {
#           'nome': TextInput(attrs={
#                'class': 'from-control',
#                'maxlength': 255,
#                'placeholder': 'Digite o nome do produto'
#            })
#        }


