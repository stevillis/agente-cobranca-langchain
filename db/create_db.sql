CREATE TABLE negociadores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_admissao DATE NOT NULL,
    status BOOLEAN NOT NULL DEFAULT FALSE
);
CREATE TABLE devedores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf_cnpj VARCHAR(20) NOT NULL
);
CREATE TABLE dividas (
    id SERIAL PRIMARY KEY,
    devedor_id INT NOT NULL,
    valor DECIMAL(12, 2) NOT NULL,
    data_venc DATE NOT NULL,
    descricao TEXT,
    FOREIGN KEY (devedor_id) REFERENCES devedores(id)
);
CREATE TABLE acordos (
    id SERIAL PRIMARY KEY,
    divida_id INT NOT NULL,
    negociador_id INT NOT NULL,
    valor_acordo DECIMAL(12, 2) NOT NULL,
    qtd_parcelas INT NOT NULL,
    data_acordo DATE NOT NULL,
    cancelado BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (divida_id) REFERENCES dividas(id),
    FOREIGN KEY (negociador_id) REFERENCES negociadores(id)
);
