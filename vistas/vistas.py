from flask import request
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_restful import Resource
import hashlib
from datetime import datetime
from sqlalchemy.orm import joinedload
import random

from modelos import (
    db,
    Pregunta,
    PreguntaSchema,
    Respuesta,
    RespuestaSchema,
)

pregunta_schema = PreguntaSchema()
respuesta_schema = RespuestaSchema()


class VistaPregunta(Resource):
   # @jwt_required()
    def get(self, id_receta):
        receta = Receta.query.get_or_404(id_receta)
        ingredientes = Ingrediente.query.all()
        resultados = receta_schema.dump(Receta.query.get_or_404(id_receta))
        recetaIngredientes = resultados["ingredientes"]
        for recetaIngrediente in recetaIngredientes:
            for ingrediente in ingredientes:
                if str(ingrediente.id) == recetaIngrediente["ingrediente"]:
                    recetaIngrediente["ingrediente"] = ingrediente_schema.dump(
                        ingrediente
                    )
                    recetaIngrediente["ingrediente"]["costo"] = float(
                        recetaIngrediente["ingrediente"]["costo"]
                    )

        return resultados
    


class VistaRespuesta(Resource):
   # @jwt_required()
    def get(self, id_pregunta, id_respuesta):
        #pregunta = Pregunta.query.get_or_404(id_pregunta)
        respuesta = Respuesta.query.get_or_404(id_respuesta)
        #ingredientes = Ingrediente.query.all()
        #resultados = receta_schema.dump(Receta.query.get_or_404(id_receta))
        #recetaIngredientes = resultados["ingredientes"]
        match(self.random.randrange(5)) :
            case 0:
                return { "mensaje": "No encontramos la respuesta" }, 404
            case 1:
                return { "mensaje": "No tiene permisos" }, 403
            case 2:
                return { "mensaje": "No autorizado" }, 401
            case 3:
                return { "mensaje": "No sabemos que paso" }, 500
            case _:
                return { "mensaje": "la respuestaz es correcta respuesta es correcta" }


        
