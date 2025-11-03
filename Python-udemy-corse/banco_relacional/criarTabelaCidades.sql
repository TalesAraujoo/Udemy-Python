CREATE TABLE IF NOT EXISTS cidades (
    id INT unsigned NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    estado_id INT unsigned NOT NULL,
    area DECIMAL (10,2),
    PRIMARY KEY (id),
    FOREIGN KEY (estado_id) REFERENCES estados (id)
);


CREATE TABLE IF NOT EXISTS cidades_test (
    id INT unsigned NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS cidades;
DROP TABLE IF EXISTS cidades_test;