select * from estados
-- select * from estados where id = 40

INSERT INTO cidades(nome, area, estado_id)
VALUES('Campinas', 795, 46)

insert into cidades (nome, area, estado_id)
values('Niterói', 133.9, 40)

select * from cidades

INSERT INTO cidades (nome, area, estado_id)
VALUES (
    'Caruaru',
    920.6,
    (select id from estados where sigla = 'PE')
)

iNSERT INTO cidades 
    (nome, area, estado_id)
VALUES 
    ('Juazeiro do Norte', 248.2, (select id from estados where sigla = 'CE'))

INSERT INTO cidades
    (nome, estado_id)
VALUES
    ('Jaguariaíva', (select id from estados where sigla = 'PR'))


UPDATE cidades
set area = 1.524
where nome = 'Jaguariaíva'


select * from cidades