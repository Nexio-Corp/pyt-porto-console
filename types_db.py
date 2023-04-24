from typing import TypedDict


class IBike(TypedDict):
    modelo: str
    valor: float
    modificacoes: list[str]
    chassi: int
    fotos: str


class ICliente(TypedDict):
    nome: str
    email: str
    senha: str
    telefone: str
    cpf: str
    cep: str
    bikes: list[IBike]
