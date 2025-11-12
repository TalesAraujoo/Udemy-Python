INSERT INTO empresas
    (nome, cnpj)
VALUES 
    ('Bradesco', 954324185421),
    ('Vale', 123162412431),
    ('Cielo', 1231512312)


ALTER TABLE empresas MODIFY cnpj VARCHAR(20);

select * from empresas;
select * from cidades;

desc empresas

INSERT INTO empresas_unidades  
    (empresa_id, cidade_id, sede)
VALUES
    (1, 1, 1),
    (1, 2, 0),
    (2, 1, 0)

select * from empresas_unidades