from flask_appbuilder import IndexView, expose
from .models import RegistroExtraccion
from . import db

class MyIndexView(IndexView):
    @expose("/")
    def index(self):
        # Fetch dynamic data: last 5 extractions
        last_extractions = db.session.query(RegistroExtraccion).order_by(RegistroExtraccion.id.desc()).limit(5).all()
        
        # Modules for quick access
        modules = [
            {"name": "Orígenes", "icon": "fa-globe", "url": "/origenview/list", "description": "Gestiona los países y regiones de origen."},
            {"name": "Cafés", "icon": "fa-coffee", "url": "/cafeview/list", "description": "Administra los diferentes granos de café."},
            {"name": "Métodos", "icon": "fa-flask", "url": "/metodoview/list", "description": "Configura los métodos de extracción."},
            {"name": "Mis Extracciones", "icon": "fa-list", "url": "/registroextraccionview/list", "description": "Registra y consulta tus experiencias."},
            {"name": "Estadísticas", "icon": "fa-bar-chart", "url": "/registrostatsview/chart", "description": "Visualiza el análisis de tus datos."}
        ]
        
        return self.render_template("index.html", 
                                  last_extractions=last_extractions,
                                  modules=modules)
