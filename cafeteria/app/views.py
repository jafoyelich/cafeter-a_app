from flask import current_app, render_template

from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from . import appbuilder, db
from .models import Origen, Cafe, Metodo, RegistroExtraccion

class OrigenView(ModelView):
    datamodel = SQLAInterface(Origen)
    list_columns = ["nombre"]
    # Forzamos a que solo pida el nombre al agregar/editar para evitar dependencia circular
    add_columns = ["nombre"]
    edit_columns = ["nombre"]
    show_columns = ["nombre", "cafes"]
    label_columns = {"nombre": "Región/País", "cafes": "Cafés Asociados"}
    search_columns = ["nombre"]

class CafeView(ModelView):
    datamodel = SQLAInterface(Cafe)
    list_columns = ["nombre", "tueste", "origen"]
    add_columns = ["nombre", "tueste", "origen"]
    edit_columns = ["nombre", "tueste", "origen"]
    label_columns = {"nombre": "Nombre del Grano", "tueste": "Tipo de Tueste", "origen": "Origen"}
    search_columns = ["nombre", "tueste"]

class MetodoView(ModelView):
    datamodel = SQLAInterface(Metodo)
    list_columns = ["nombre", "tipo"]
    add_columns = ["nombre", "tipo"]
    edit_columns = ["nombre", "tipo"]
    label_columns = {"nombre": "Método", "tipo": "Categoría"}

class RegistroExtraccionView(ModelView):
    datamodel = SQLAInterface(RegistroExtraccion)
    list_columns = ["cafe", "metodo", "ratio", "puntaje"]
    # No incluimos relaciones inversas aquí para mantenerlo limpio
    add_columns = ["cafe", "metodo", "ratio", "temperatura", "puntaje", "notas"]
    edit_columns = ["cafe", "metodo", "ratio", "temperatura", "puntaje", "notas"]
    
    label_columns = {
        "cafe": "Café Utilizado",
        "metodo": "Método de Extracción",
        "ratio": "Ratio (Gr/Ml)",
        "temperatura": "Temp. Agua (ºC)",
        "puntaje": "Puntaje (1-10)",
        "notas": "Notas de Sabor"
    }
    
    # Esto asegura que solo usuarios logueados vean/editen (Requisito 4)
    base_permissions = ['can_add', 'can_show', 'can_edit', 'can_delete', 'can_list']

# Registrar las vistas en el menú
appbuilder.add_view(OrigenView, "Orígenes", icon="fa-globe", category="Configuración")
appbuilder.add_view(CafeView, "Cafés", icon="fa-coffee", category="Configuración")
appbuilder.add_view(MetodoView, "Métodos", icon="fa-flask", category="Configuración")
appbuilder.add_view(RegistroExtraccionView, "Mis Extracciones", icon="fa-list", category="Diario")

@current_app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )
