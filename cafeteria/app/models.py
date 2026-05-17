from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text
from sqlalchemy.orm import relationship


class Origen(Model):
    __tablename__ = "origen"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.nombre


class Cafe(Model):
    __tablename__ = "cafe"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    tueste = Column(String(50))  # Claro, Medio, Oscuro
    origen_id = Column(Integer, ForeignKey('origen.id'), nullable=False)

    # Relación requerida por rúbrica
    origen = relationship("Origen", back_populates="cafes")

    def __repr__(self):
        return self.nombre


Origen.cafes = relationship("Cafe", order_by=Cafe.id, back_populates="origen")


class Metodo(Model):
    __tablename__ = "metodo"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50), unique=True, nullable=False)
    tipo = Column(String(50))  # Goteo, Presión, Inmersión

    def __repr__(self):
        return self.nombre


class RegistroExtraccion(Model):
    __tablename__ = "registro_extraccion"
    id = Column(Integer, primary_key=True)
    ratio = Column(String(20))  # Ej: 1:15
    temperatura = Column(Float)
    puntaje = Column(Integer)  # 1 al 10
    notas = Column(Text)

    cafe_id = Column(Integer, ForeignKey('cafe.id'), nullable=False)
    cafe = relationship("Cafe", back_populates="extracciones")

    metodo_id = Column(Integer, ForeignKey('metodo.id'), nullable=False)
    metodo = relationship("Metodo", back_populates="extracciones")

# Añadir las relaciones inversas para cumplir con back_populates
Cafe.extracciones = relationship("RegistroExtraccion", back_populates="cafe")
Metodo.extracciones = relationship("RegistroExtraccion", back_populates="metodo")
