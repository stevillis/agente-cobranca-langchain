INSERT INTO negociadores (nome, data_admissao, status)
VALUES ('João Silva', '2023-01-15', TRUE),
    ('Maria Santos', '2023-03-20', TRUE),
    ('Pedro Oliveira', '2023-06-10', TRUE),
    ('Ana Costa', '2023-08-01', FALSE);
INSERT INTO devedores (nome, cpf_cnpj)
VALUES ('Carlos Mendes', '123.456.789-00'),
    ('Empresa XYZ Ltda', '12.345.678/0001-90'),
    ('Mariana Souza', '987.654.321-00'),
    ('José Pereira', '456.789.123-00'),
    ('Amanda Lima', '789.123.456-00'),
    ('Roberto Almeida', '234.567.890-11'),
    ('Fernanda Castro', '345.678.901-22'),
    ('Supermercado ABC Ltda', '23.456.789/0001-12'),
    ('Paulo Ribeiro', '456.789.012-33'),
    ('Lucia Ferreira', '567.890.123-44');
INSERT INTO dividas (devedor_id, valor, data_venc, descricao)
VALUES (1, 1500.00, '2023-12-15', 'Empréstimo pessoal'),
    (1, 800.00, '2023-11-30', 'Cartão de crédito'),
    (2, 5000.00, '2023-10-20', 'Fornecedores'),
    (3, 2300.00, '2023-12-01', 'Financiamento'),
    (4, 1200.00, '2023-11-15', 'Empréstimo pessoal'),
    (5, 3500.00, '2023-12-10', 'Cartão de crédito'),
    (6, 4200.00, '2024-01-15', 'Empréstimo comercial'),
    (6, 1800.00, '2024-02-10', 'Cartão de crédito'),
    (
        7,
        3500.00,
        '2024-01-20',
        'Financiamento pessoal'
    ),
    (
        8,
        12000.00,
        '2024-02-01',
        'Dívida com fornecedores'
    ),
    (
        8,
        8500.00,
        '2024-01-25',
        'Empréstimo capital de giro'
    ),
    (9, 2800.00, '2024-02-05', 'Empréstimo pessoal'),
    (
        10,
        5600.00,
        '2024-01-30',
        'Financiamento veículo'
    );
INSERT INTO acordos (
        divida_id,
        negociador_id,
        valor_acordo,
        qtd_parcelas,
        data_acordo,
        cancelado
    )
VALUES (1, 1, 1200.00, 6, '2024-01-10', FALSE),
    (2, 2, 700.00, 3, '2024-01-15', FALSE),
    (3, 1, 4500.00, 10, '2024-01-05', FALSE),
    (4, 3, 2000.00, 5, '2024-01-20', TRUE),
    (5, 2, 1000.00, 4, '2024-01-25', FALSE);
