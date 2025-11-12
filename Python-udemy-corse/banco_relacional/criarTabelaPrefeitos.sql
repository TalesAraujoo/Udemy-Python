CREATE TABLE IF NOT EXISTS prefeitos (
    id INT unsigned NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    cidade_id int unsigned,
    PRIMARY KEY (id),
    UNIQUE KEY (cidade_id),
    FOREIGN KEY (cidade_id) REFERENCES cidades (id)
)

select * from cidades