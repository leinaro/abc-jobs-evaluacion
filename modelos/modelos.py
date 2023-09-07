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
    respuestas = db.relationship("Respuesta")

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