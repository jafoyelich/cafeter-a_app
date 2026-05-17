import unittest
from app import app, db
from app.models import Origen, Cafe, Metodo, RegistroExtraccion

class TestModels(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        # Use a separate test database or just test within the current context
        # For simplicity in this environment, we'll assume the DB is ready
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            # Careful with drop_all if using a production DB, but here it's okay for testing
            # db.drop_all()

    def test_create_origen(self):
        with app.app_context():
            origen = Origen(nombre="Bolivia")
            db.session.add(origen)
            db.session.commit()
            
            queried_origen = db.session.query(Origen).filter_by(nombre="Bolivia").first()
            self.assertEqual(queried_origen.nombre, "Bolivia")
            
            # Cleanup
            db.session.delete(queried_origen)
            db.session.commit()

    def test_create_cafe(self):
        with app.app_context():
            origen = Origen(nombre="Etiopía")
            db.session.add(origen)
            db.session.commit()
            
            cafe = Cafe(nombre="Yirgacheffe", tueste="Claro", origen=origen)
            db.session.add(cafe)
            db.session.commit()
            
            queried_cafe = db.session.query(Cafe).filter_by(nombre="Yirgacheffe").first()
            self.assertEqual(queried_cafe.nombre, "Yirgacheffe")
            self.assertEqual(queried_cafe.origen.nombre, "Etiopía")
            
            # Test back_populates
            self.assertIn(cafe, origen.cafes)
            
            # Cleanup
            db.session.delete(cafe)
            db.session.delete(origen)
            db.session.commit()

    def test_create_metodo(self):
        with app.app_context():
            metodo = Metodo(nombre="V60", tipo="Goteo")
            db.session.add(metodo)
            db.session.commit()
            
            queried_metodo = db.session.query(Metodo).filter_by(nombre="V60").first()
            self.assertEqual(queried_metodo.nombre, "V60")
            
            # Cleanup
            db.session.delete(queried_metodo)
            db.session.commit()

    def test_create_registro(self):
        with app.app_context():
            origen = Origen(nombre="Colombia")
            db.session.add(origen)
            cafe = Cafe(nombre="Huila", origen=origen)
            db.session.add(cafe)
            metodo = Metodo(nombre="Prensa Francesa", tipo="Inmersión")
            db.session.add(metodo)
            db.session.commit()
            
            registro = RegistroExtraccion(
                cafe=cafe, 
                metodo=metodo, 
                ratio="1:15", 
                temperatura=92.5, 
                puntaje=9
            )
            db.session.add(registro)
            db.session.commit()
            
            queried_registro = db.session.query(RegistroExtraccion).first()
            self.assertEqual(queried_registro.ratio, "1:15")
            self.assertEqual(queried_registro.cafe.nombre, "Huila")
            self.assertEqual(queried_registro.metodo.nombre, "Prensa Francesa")
            
            # Test back_populates
            self.assertIn(registro, cafe.extracciones)
            self.assertIn(registro, metodo.extracciones)
            
            # Cleanup
            db.session.delete(registro)
            db.session.delete(metodo)
            db.session.delete(cafe)
            db.session.delete(origen)
            db.session.commit()

if __name__ == '__main__':
    unittest.main()
