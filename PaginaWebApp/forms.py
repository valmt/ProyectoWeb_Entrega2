from django import forms 
from .models import Cliente

class FormularioCliente(forms.ModelForm) :
   """
    xd

  """
class Meta :
    model = Cliente
    fields = ('nombre', 'apellido', 'rut')
    