salario = 3450.45
despesas = 2456.2

#descubra o percentual que as despesas representam comparadas ao salario

print(f"O percentual que despesas representa é {(despesas/salario)*100:.2f}%")

is_raining = True
print('Today my clothes are ' + ('dry', 'wet')[is_raining])
print('Today my clothes are ' + ('wet' if is_raining else 'dry'))


#Operador de Membro 

lista = [1, 2, 3, 'Ana', 'Carla']
print('Carla' in lista)
print('Ana' not in lista)

#operador de identidade

x = 3 
y = x 
z = 3 
print(x is z)


# Builtins

__builtins__.type('Fala Galera!')
__builtins__.print(10/3)
# help(dir)
# print(dir(__builtins__))
nome = 'Joao da Silva'
print(len(nome))


#conversão de Tipos

print(1 + 3)
# print( 1 + '3')
a = 1
b = '3'
print(type(a))
print(type(b))
print(a + int(b))
print(str(a)+ b)
print('test')


#Coerção Automática
print('----- Coerção ------')
print(10/2)
print(type(10/3))
print(type(10//3.3))
# test = input('test: ')


#Números 
print('---- Tipos Numericos -----')
a = 5
b = 2.5
print(a/b)
print(type(a))
print(b.is_integer())
print(a.is_integer())
print((-2).__abs__())
print(abs(-4))

# numeros Decimais / import

print('---- Decimal / Import -----')
print(1.1 + 2.2)

from decimal import Decimal, getcontext
print(Decimal(1)/Decimal(7))

getcontext().prec = 4
print(Decimal(1)/Decimal(7))

#diz qual dos parametros é o maior
print(Decimal.max(Decimal(1), Decimal(7)))
# print(dir(Decimal))

print(1.1 + 2.2)
print(Decimal(1.1)+Decimal(2.2))

print('---- Strings -----')

nome = 'Saulo Pedro'
print(nome[1])
#strings ar immutable

"Marca d'água"
'Marca d\'água'

print("""Texto com multiplas
      linhas em todo canto """)

nome = 'Ana Paula'
print(nome[0])
print(nome[6])
print(nome[4:])
print(nome[:3])
print(nome[2:5])

numeros = '123456789'

print(numeros[::])
print(numeros[::2])
print(numeros[1::2])

phrase = 'Python is an excelent language'

print('py' in phrase)
print('ing' in phrase)
print(len(phrase))
print('py' in phrase.lower())
print(phrase.upper())
print(phrase.split())

print('---- Lists -----')
list = []
print(type(list))
print(len(list))
list.append(2)
print(list)
new_list = [1, 5, 'Ana', 'Bia']
new_list.remove(5)
print(new_list)
new_list.reverse()
print(new_list)
print('\n')
print('----- Dictionaries -----')

person = {'nome': 'Tales Augusto', 
          'idade': 34,
          'curso': ['inglês', 'português']}

print(person)
print(len(person))
print(person['nome'])
print(person['idade'])
print(person['curso'])
print(person.keys())
print(person.values())
print(person.items())
print(person.get('idade'))
print(person.get('tags'))
print(person.get('tags', ['Nothing']))

print('\n')

person = {'nome': 'Prof. Alberto', 'idade': 43, 'cursos': ['React', 'Python']}
person['nome'] = 'Tales test'
person['idade'] = 44
person['cursos'].append('Angular')
print(person)
print('\n')
person.pop('idade')
print(person)
person.update({'idade': 40, 'Sexo': 'M'})
print(person)
print('\n')

del person['cursos']
print(person)
person.clear()
print(person)


print('------ Conjuntos -----')
# Nao indexado, nao aceita atribuicao e nao eh ordenado

a = {1, 2, 3}
print(type(a))
# print(a)
a = set('cod3r')
print(a)
print('3' in a, 4 not in a)
print({1, 2, 3} == {3, 2, 1, 3})

#operacoes
c1 = {1, 2}
c2 = {2, 3}
c3 = c1.union(c2)
# print(c3)
print(c1.union(c2))
print(c1.intersection(c2))
# c1.update(c2)
print(c1)
print(c2 <= c1)
print({1, 2, 3} - {2})
# print({1, 2, 3} + {5})


print('-----  Interpolacao ------')

from string import Template

nome, idade = 'Ana', 30.9123
print('Nome: %s Idade: %.2f %r %r' % (nome, idade, True, False )) #versao antiga
print('nome: {0} Idade: {1}' .format(nome, idade)) # python < 3.6
print(f'Nome: {nome} Idade: {idade}') #python > 3.6

s = Template('Nome: $nomeTemplate Idade: $idadeTemplate')
print(s.substitute(nomeTemplate=nome, idadeTemplate=idade))