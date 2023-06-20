from typing import Optional

from pydantic import BaseModel


class Chave(BaseModel):
    """Simple message model."""

    idUsuario: str
    email: Optional[str]
    senha: Optional[str]
    nome: Optional[str]
    urlfoto: Optional[str]

