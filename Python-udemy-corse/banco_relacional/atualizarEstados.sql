update estados
set nome = 'Maranhão'
where sigla = 'MA'


select nome from estados
where sigla = 'MA'

select estados.nome from estados where sigla = ' PR'

update estados
set nome = 'Paraná', populacao = 11.32
WHERE sigla = 'PR'

select * from estados where sigla = 'PR'