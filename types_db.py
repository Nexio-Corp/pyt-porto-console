from typing import Optional, TypedDict


class IBike(TypedDict):
    modelo: str
    valor: float
    modificacoes: list[str]
    chassi: str
    fotos: str
    relatorio: Optional[str]


class IUsuario(TypedDict):
    nome: str
    email: str
    senha: str
    telefone: str
    cpf: str
    cep: str
    bikes: list[IBike]
