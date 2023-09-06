import enum
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema


db = SQLAlchemy()


#class Evaluacion(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    nombre = db.Column(db.String(100))
#    preguntas = db.relationship("Preguntas", foreign_keys=[pregunta_id])

class Pregunta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enunciado = db.Column(db.String(128))
    respuestas = db.relationship("Solucion")

class Respuesta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Numeric)
    pregunta_id = db.Column(db.Integer, db.ForeignKey("pregunta.id")) 
    es_correcta = db.Column(db.Boolean)


class RespuestaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Respuesta
        load_instance = True

    id = fields.String()
    pregunta_id = fields.String()
    descripcion = fields.String()
    pregunta = fields.String()


class PreguntaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Pregunta
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.String()
    enunciado = fields.String()
    respuestas = fields.List(fields.Nested(RespuestaSchema()))




class RecetaIngredienteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = RecetaIngrediente
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.String()
    cantidad = fields.String()
    ingrediente = fields.String()


class RecetaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Receta
        include_relationships = True
        include_fk = True
        load_instance = True

    id = fields.String()
    duracion = fields.String()
    porcion = fields.String()
    ingredientes = fields.List(fields.Nested(RecetaIngredienteSchema()))


class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

    id = fields.String()


class MenuRecetaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MenuReceta
        include_relationships = True
        include_fk = True
        load_instance = True

    receta = fields.String()


class MenuSemanaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = MenuSemana
        include_relationships = True
        load_instance = True

    id = fields.String()
    nombre = fields.String()
    fecha_inicial = fields.Date()
    fecha_final = fields.Date()
    recetas = fields.List(fields.Nested(MenuRecetaSchema()))
