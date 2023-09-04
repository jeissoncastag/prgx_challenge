from pydantic import BaseModel
from typing import List

class Address(BaseModel):
    id: int
    direccion_1: str
    direccion_2: str
    ciudad: str
    estado: str
    codigo_postal: str
    pais: str

class User(BaseModel):
    id: int
    nombre: str
    apellidos: str
    correo_electronico: str
    contrasena: str
    direcciones: List[Address]
