-- INSERINDO CLIENTES
INSERT INTO cliente (
    cpf,
    nome_cliente,
    email_cliente,
    rua_cliente,
    numero_cliente,
    bairro_cliente,
    cidade_cliente
) VALUES (
    14322795634,
    'Gabriel',
    'gabriel@stadtler.com',
    'Teles Junior',
    105,
    'Aflitos',
    'Recife'
);

INSERT INTO cliente (
    cpf,
    nome_cliente,
    email_cliente,
    rua_cliente,
    numero_cliente,
    bairro_cliente,
    cidade_cliente
) VALUES (
    14355634783,
    'Danilo',
    'danilo@franca.com',
    'Franca',
    105,
    'Jardim Baixo',
    'Paulista'
);

INSERT INTO cliente (
    cpf,
    nome_cliente,
    email_cliente,
    rua_cliente,
    numero_cliente,
    bairro_cliente,
    cidade_cliente
) VALUES (
    04655834793,
    'Moises',
    'moises@giorgio.com',
    'Giorgio',
    15,
    'Jardim São Paulo',
    'Recife'
);

INSERT INTO cliente (
    cpf,
    nome_cliente,
    email_cliente,
    rua_cliente,
    numero_cliente,
    bairro_cliente,
    cidade_cliente
) VALUES (
    94355634798,
    'Naruto',
    'naruto@konoha.com',
    'Uzumaki',
    125,
    'Konohagakure',
    'Konohagakure'
);

INSERT INTO cliente (
    cpf,
    nome_cliente,
    email_cliente,
    rua_cliente,
    numero_cliente,
    bairro_cliente,
    cidade_cliente
) VALUES (
    17355634485,
    'Marcela',
    'Marcela@silva.com',
    'Silva',
    18,
    'Camaragibe',
    'Recife'
);

-- INSERINDO TELEFONES DE CLIENTES
INSERT INTO telefone_cliente (
    cpf_cliente,
    telefone
) VALUES (
    14322795634,
    33442563
);

INSERT INTO telefone_cliente (
    cpf_cliente,
    telefone
) VALUES (
    14355634783,
    33552668
);

INSERT INTO telefone_cliente (
    cpf_cliente,
    telefone
) VALUES (
    04655834793,
    31452769
);

INSERT INTO telefone_cliente (
    cpf_cliente,
    telefone
) VALUES (
    94355634798,
    33665567
);

INSERT INTO telefone_cliente (
    cpf_cliente,
    telefone
) VALUES (
    17355634485,
    33445566
);

-- INSERINDO PRODUTOS
INSERT INTO produto (
    id_produto,
    nome,
    preco_venda,
    preco_compra,
    qtd_estoque
) VALUES (
    1,
    'cadeira gamer',
    2500,
    2000,
    100
);

INSERT INTO produto (
    id_produto,
    nome,
    preco_venda,
    preco_compra,
    qtd_estoque
) VALUES (
    2,
    'teclado gamer',
    250,
    180,
    1000
);

INSERT INTO produto (
    id_produto,
    nome,
    preco_venda,
    preco_compra,
    qtd_estoque
) VALUES (
    3,
    'mouse gamer',
    180,
    100,
    1000
);

INSERT INTO produto (
    id_produto,
    nome,
    preco_venda,
    preco_compra,
    qtd_estoque
) VALUES (
    4,
    'headset gamer',
    300,
    200,
    1000
);

INSERT INTO produto (
    id_produto,
    nome,
    preco_venda,
    preco_compra,
    qtd_estoque
) VALUES (
    5,
    'monitor gamer',
    3000,
    2200,
    350
);

-- INSERINDO FORNECEDORES
INSERT INTO fornecedor (
    cnpj,
    nome,
    email,
    rua,
    numero,
    bairro,
    cidade
) VALUES (
    76978335000140,
    'Xuxa Informatica',
    'xuxa@informatica.com',
    'limoeiro',
    12,
    'tejipio',
    'recife'
);

INSERT INTO fornecedor (
    cnpj,
    nome,
    email,
    rua,
    numero,
    bairro,
    cidade
) VALUES (
    68938683000130,
    'Gamers Informatica',
    'gamers@informatica.com',
    '100',
    14,
    'boa vista',
    'recife'
);

INSERT INTO fornecedor (
    cnpj,
    nome,
    email,
    rua,
    numero,
    bairro,
    cidade
) VALUES (
    65397869500018,
    'Shippuden Info',
    'shippuden@informatica.com',
    'Rua Kakashi',
    7,
    'Konohagakure',
    'Konohagakure'
);

-- INSERINDO TELEFONES DE FORNECEDORES
INSERT INTO telefone_fornecedor (
    cnpj_fornecedor,
    telefone
) VALUES (
    76978335000140,
    31345066
);

INSERT INTO telefone_fornecedor (
    cnpj_fornecedor,
    telefone
) VALUES (
    68938683000130,
    33456806
);

INSERT INTO telefone_fornecedor (
    cnpj_fornecedor,
    telefone
) VALUES (
    65397869500018,
    32446786
);

-- INSERINDO COMPRA_ENTRADAS
INSERT INTO compra_entrada (
    id_entrada,
    cnpj_fornecedor,
    data_compra,
    valor_total
) VALUES (
    1,
    76978335000140,
    DATE '2019-10-10',
    200000
);

INSERT INTO compra_entrada (
    id_entrada,
    cnpj_fornecedor,
    data_compra,
    valor_total
) VALUES (
    2,
    76978335000140,
    DATE '2019-10-10',
    180000
);

INSERT INTO compra_entrada (
    id_entrada,
    cnpj_fornecedor,
    data_compra,
    valor_total
) VALUES (
    3,
    68938683000130,
    DATE '2019-09-12',
    100000
);

INSERT INTO compra_entrada (
    id_entrada,
    cnpj_fornecedor,
    data_compra,
    valor_total
) VALUES (
    4,
    65397869500018,
    DATE '2019-05-09',
    200000
);

INSERT INTO compra_entrada (
    id_entrada,
    cnpj_fornecedor,
    data_compra,
    valor_total
) VALUES (
    5,
    65397869500018,
    DATE '2019-10-08',
    770000
);

-- INSERINDO COMPRA_PRODUTO
INSERT INTO compra_produto (
    id_produto_produto,
    id_entrada_compra,
    quantidade
) VALUES (
    1,
    1,
    100
);

INSERT INTO compra_produto (
    id_produto_produto,
    id_entrada_compra,
    quantidade
) VALUES (
    2,
    2,
    1000
);

INSERT INTO compra_produto (
    id_produto_produto,
    id_entrada_compra,
    quantidade
) VALUES (
    3,
    3,
    100
);

INSERT INTO compra_produto (
    id_produto_produto,
    id_entrada_compra,
    quantidade
) VALUES (
    4,
    4,
    1000
);

INSERT INTO compra_produto (
    id_produto_produto,
    id_entrada_compra,
    quantidade
) VALUES (
    5,
    5,
    350
);

-- INSERINDO FUNCIONARIOS
INSERT INTO funcionario (
    cpf,
    nome,
    email,
    senha,
    flagGerente
) VALUES (
    70060134020,
    'Guilherme',
    'guilherme@funcionario.com',
    '4321guilherme',
    'false'
);

INSERT INTO funcionario (
    cpf,
    nome,
    email,
    senha,
    flagGerente
) VALUES (
    09601450321,
    'Fernando',
    'fernando@funcionario.com',
    '4321fernando',
    'false'
);

INSERT INTO funcionario (
    cpf,
    nome,
    email,
    senha,
    flagGerente
) VALUES (
    12304136792,
    'Gustavo',
    'gustavo@funcionario.com',
    '4321gustavo',
    'false'
);

INSERT INTO funcionario (
    cpf,
    nome,
    email,
    senha,
    flagGerente
) VALUES (
    49709849050,
    'Regis',
    'regis@funcionario.com',
    '4321regis',
    'true'
);

-- INSERINDO GERENTES
INSERT INTO gerente ( cpf ) VALUES ( 49709849050 );

-- INSERINDO VENDEDORES
INSERT INTO vendedor (
    cpf,
    cpf_gerente,
    meta
) VALUES (
    70060134020,
    49709849050,
    30000
);

INSERT INTO vendedor (
    cpf,
    cpf_gerente,
    meta
) VALUES (
    09601450321,
    49709849050,
    30000
);

INSERT INTO vendedor (
    cpf,
    cpf_gerente,
    meta
) VALUES (
    12304136792,
    49709849050,
    30000
);

-- INSERINDO SUPERVISIONAMENTO
INSERT INTO supervisiona (
    cpf_gerente,
    cpf_vendedor
) VALUES (
    49709849050,
    70060134020
);

INSERT INTO supervisiona (
    cpf_gerente,
    cpf_vendedor
) VALUES (
    49709849050,
    09601450321
);

INSERT INTO supervisiona (
    cpf_gerente,
    cpf_vendedor
) VALUES (
    49709849050,
    12304136792
);

-- INSERINDO VENDAS
INSERT INTO venda (
    id_saida,
    cpf_funcionario_venda,
    cpf_cliente_venda,
    data_venda,
    valor_total
) VALUES (
    1,
    70060134020,
    14322795634,
    DATE '2019-05-23',
    5000
);

INSERT INTO venda (
    id_saida,
    cpf_funcionario_venda,
    cpf_cliente_venda,
    data_venda,
    valor_total
) VALUES (
    2,
    09601450321,
    14355634783,
    DATE '2019-06-15',
    750
);

INSERT INTO venda (
    id_saida,
    cpf_funcionario_venda,
    cpf_cliente_venda,
    data_venda,
    valor_total
) VALUES (
    3,
    12304136792,
    04655834793,
    DATE '2019-07-20',
    180
);

INSERT INTO venda (
    id_saida,
    cpf_funcionario_venda,
    cpf_cliente_venda,
    data_venda,
    valor_total
) VALUES (
    4,
    12304136792,
    94355634798,
    DATE '2019-07-20',
    300
);

INSERT INTO venda (
    id_saida,
    cpf_funcionario_venda,
    cpf_cliente_venda,
    data_venda,
    valor_total
) VALUES (
    5,
    09601450321,
    17355634485,
    DATE '2019-07-20',
    3000
);

-- INSERINDO VENDA_PRODUTO
INSERT INTO venda_produto (
    id_produto_produto,
    id_saida_venda,
    quantidade
) VALUES (
    1,
    1,
    2
);

INSERT INTO venda_produto (
    id_produto_produto,
    id_saida_venda,
    quantidade
) VALUES (
    2,
    2,
    3
);

INSERT INTO venda_produto (
    id_produto_produto,
    id_saida_venda,
    quantidade
) VALUES (
    3,
    3,
    1
);

INSERT INTO venda_produto (
    id_produto_produto,
    id_saida_venda,
    quantidade
) VALUES (
    4,
    4,
    1
);

INSERT INTO venda_produto (
    id_produto_produto,
    id_saida_venda,
    quantidade
) VALUES (
    5,
    5,
    1
);
