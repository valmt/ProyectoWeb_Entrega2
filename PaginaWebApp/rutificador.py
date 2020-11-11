from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_rutificador(rut):
    if validar_rut(rut) == False :
        raise ValidationError(
            _('El rut "%(valor)s" no es valido'),
             code='invalid',
             params={'valor' : rut}
        )
def validar_rut(rut):
    rut_partes = rut.split('-')
    if not rut_partes[0].isnumeric() :
        return False
    rut_como_int = int(rut_partes[0])
    dv_calculado = verificar_dv(rut_como_int)
    dv_ingresado = rut_partes[1]
    if dv_calculado == dv_ingresado.upper() :
        return True
    return False

def verificar_dv(rut_sin_dv) :
    contador = 2
    suma = 0
    while rut_sin_dv != 0 :
        multiplo = (rut_sin_dv % 10) * contador 
        suma = suma + multiplo
        rut_sin_dv = rut_sin_dv // 10 
        contador = contador + 1
        if contador == 8 :
            contador = 2
    digito = 11 - (suma % 11)
    if digito == 10 :
        dv = 'K'
    elif digito == 11 :
        dv = '0'
    else :
        dv = str(digito)
    return dv


