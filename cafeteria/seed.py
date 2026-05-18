import logging
import random
from app import app, db
from app.models import Origen, Cafe, Metodo, RegistroExtraccion

# Configurar logging para ver qué pasa
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def seed_data():
    with app.app_context():
        print("Iniciando carga de datos...")
        
        # 1. Crear Orígenes
        origenes_nombres = ["Bolivia", "Etiopía", "Colombia", "Brasil", "Kenia"]
        origenes = {}
        for nombre in origenes_nombres:
            origen = db.session.query(Origen).filter_by(nombre=nombre).first()
            if not origen:
                origen = Origen(nombre=nombre)
                db.session.add(origen)
                db.session.flush() # Para obtener el ID
                print(f"Origen creado: {nombre}")
            origenes[nombre] = origen

        # 2. Crear Cafés
        cafes_data = [
            ("Geisha Caranavi", "Claro", origenes["Bolivia"]),
            ("Yirgacheffe", "Claro", origenes["Etiopía"]),
            ("Huila Reserva", "Medio", origenes["Colombia"]),
            ("Santos", "Oscuro", origenes["Brasil"]),
            ("Kenia AA", "Claro", origenes["Kenia"]),
        ]
        cafes = []
        for nombre, tueste, origen in cafes_data:
            cafe = db.session.query(Cafe).filter_by(nombre=nombre).first()
            if not cafe:
                cafe = Cafe(nombre=nombre, tueste=tueste, origen=origen)
                db.session.add(cafe)
                db.session.flush()
                print(f"Café creado: {nombre}")
            cafes.append(cafe)

        # 3. Crear Métodos
        metodos_data = [
            ("V60", "Goteo"),
            ("Chemex", "Goteo"),
            ("Prensa Francesa", "Inmersión"),
            ("AeroPress", "Presión"),
            ("Espresso", "Presión"),
        ]
        metodos = []
        for nombre, tipo in metodos_data:
            metodo = db.session.query(Metodo).filter_by(nombre=nombre).first()
            if not metodo:
                metodo = Metodo(nombre=nombre, tipo=tipo)
                db.session.add(metodo)
                db.session.flush()
                print(f"Método creado: {nombre}")
            metodos.append(metodo)

        # 4. Crear Registros de Extracción (Carga Masiva)
        ratios = ["1:15", "1:16", "1:18", "1:2"]
        
        print("Generando extracciones aleatorias...")
        for _ in range(30):
            cafe = random.choice(cafes)
            metodo = random.choice(metodos)
            registro = RegistroExtraccion(
                cafe=cafe,
                metodo=metodo,
                ratio=random.choice(ratios),
                temperatura=round(random.uniform(88.0, 96.0), 1),
                puntaje=random.randint(6, 10),
                notas="Nota generada automáticamente para pruebas de analítica."
            )
            db.session.add(registro)

        try:
            db.session.commit()
            print("\n¡ÉXITO! Se han cargado 30 registros de prueba.")
            print("Ahora puedes revisar las gráficas en el sistema.")
        except Exception as e:
            db.session.rollback()
            print(f"Error al guardar en base de datos: {e}")

if __name__ == "__main__":
    seed_data()
