from types_db import ICliente;

clientes: list[ICliente] = [  # Mock de clientes
    {
        'nome': 'cliente1',
        'email': 'cliente1@gmail.com',
        'senha': '1234',
        'telefone': '123456789',
        'cpf': '123456789',
        'cep': '123456789',
        'bikes': [
            {
                'modelo': 'Caloi X98',
                'valor': 1399.80,
                'modificacoes': ["GPS", "Lanterna dianteira"],
                'chassi': '0000001',
                'fotos': '111111'
            },
            {
                'modelo': 'TREK 9800RP',
                'valor': 2000.90,
                'modificacoes': [],
                'chassi': '0000002',
                'fotos': ''
            }
        ]
    },
    {
        'nome': 'teste',
        'email': 'teste@email.com',
        'senha': '1234',
        'telefone': '123456789',
        'cpf': '123456789',
        'cep': '123456789',
        'bikes': []
    },
    {
        'nome': 'admin',
        'email': 'admin@porto.com',
        'senha': '1234',
        'telefone': '123456789',
        'cpf': '123456789',
        'cep': '123456789',
        'bikes': [],
    }
]
