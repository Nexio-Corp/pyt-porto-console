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
                'modelo': 'modelo1',
                'valor': 100,
                'modificacoes': [],
                'chassi': 1234,
                'fotos': '111111'
            },
            {
                'modelo': 'modelo2',
                'valor': 100,
                'modificacoes': [],
                'chassi': 1234,
                'fotos': '111111'
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
