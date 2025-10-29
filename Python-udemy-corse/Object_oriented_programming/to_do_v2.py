from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def add(self, descricao):
        self.tarefas.append(Tarefa(descricao))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        
        return [tarefa for tarefa in self.tarefas if tarefa.descricao == descricao][0]
    
    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())}) tarefa(s) pendente(s)) '
    


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    
    def concluir(self):
        self.feito = True


    def __str__(self):
        return self.descricao + (' (Concluída)' if self.feito == True else '')


def main():
    casa = Projeto('Tarefas de casa')
    casa.add('Lavar prato')
    casa.add('Passar roupa')
    casa.add('Varrer a casa')

    casa.procurar('Varrer a casa').concluir()

    print(casa)
    for tarefas in casa.tarefas:
        print(f'- {tarefas}')

    mercado = Projeto('Compras no mercado')
    mercado.add('Carne')
    mercado.add('Ovos')
    mercado.add('Frutas secas')
    
    print('')
    print(mercado)
    for tarefa in mercado.tarefas:
        print(f'- {tarefa}')
main()
