select e.nome, c.nome, regiao from estados e, cidades c
where e.id = c.estado_id;

-- the plugin probably has a bug where it doesnt show '2 names' (state and city) 
-- even if you specify e. estados and c. for cidades
select 
    e.nome as Estado,
    c.nome as Cidade,
    regiao as Região
from estados e, cidades c
where e.id = c.estado_id


select 
    c.nome as Cidade,
    e.nome as Estado,
    regiao as Região
from estados e
inner join cidades c
    on e.id = c.estado_id