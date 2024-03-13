import random
import string
from .models import Usuario, Compra, Ingreso, Egreso
import base64

def obtener_user(user_id):
    try:
        # Busca el usuario en la base de datos por su ID
        usuario = Usuario.query.filter_by(user_Id=user_id).first()
        imagen_codificada = base64.b64encode(usuario.user_Img).decode('utf-8')
        return {
            'id': usuario.user_Id,
            'imagen': imagen_codificada,  # Asegúrate de devolver la imagen codificada 
        }
    except Exception as e:
        print(f"Error al obtener información del perfil del administrador: {e}")
    return None

def obtener_compra(user_id):
    try:
        # Busca los egresos en la base de datos asociados al usuario
        compras = Compra.query.filter_by(usuario_user_Id=user_id).all()
        lista_compras = []
        for compra in compras:
            # Formatear el campo compra_Total con comas para separador de miles
            total_formateado = "{:,}".format(int(compra.compra_Total))
            info_compra = {
                'id': compra.compra_Id,
                'detalle': compra.compra_Detalle,
                'precio': "{:,}".format(int(compra.compra_Precio)),
                'tipo': compra.compra_Tipo,
                'cantidad': compra.compra_Cantidad,
                'total': total_formateado,
                'fecha': compra.compra_Fecha,
            }
            lista_compras.append(info_compra)
        return lista_compras
    except Exception as e:
        print(f"Error al obtener información de los egresos: {e}")
        return None

def obtener_ingreso(user_id):
    try:
        # Busca los egresos en la base de datos asociados al usuario
        ingresos = Ingreso.query.filter_by(usuario_user_Id=user_id).all()
        lista_ingresos = []
        for ingreso in ingresos:
            info_ingreso = {
                'id': ingreso.ingreso_Id,
                'detalle': ingreso.ingreso_Detalle,
                'precio': "{:,}".format(int(ingreso.ingreso_Precio)),
                'tipo': ingreso.ingreso_Tipo,
                'cantidad': ingreso.ingreso_Cantidad,
                'total': "{:,}".format(int(ingreso.ingreso_Total)),
                'fecha': ingreso.ingreso_Fecha,
            }
            lista_ingresos.append(info_ingreso)
        return lista_ingresos
    except Exception as e:
        print(f"Error al obtener información de los egresos: {e}")
        return None

def obtener_egreso(user_id):
    try:
        # Busca los egresos en la base de datos asociados al usuario
        egresos = Egreso.query.filter_by(usuario_user_Id=user_id).all()
        lista_egresos = []
        for egreso in egresos:
            info_egreso = {
                'id': egreso.egreso_Id,
                'detalle': egreso.egreso_Detalle,
                'precio': "{:,}".format(int(egreso.egreso_Precio)),
                'tipo': egreso.egreso_Tipo,
                'cantidad': egreso.egreso_Cantidad,
                'total': "{:,}".format(int(egreso.egreso_Total)),
                'fecha': egreso.egreso_Fecha,
            }
            lista_egresos.append(info_egreso)
        return lista_egresos
    except Exception as e:
        print(f"Error al obtener información de los egresos: {e}")
        return None
