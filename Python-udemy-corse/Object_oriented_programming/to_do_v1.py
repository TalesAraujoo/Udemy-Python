from datetime import datetime


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    
    def concluir(self):
        self.feito = True


    def __str__(self):
        return 'Tarefa ' + self.descricao + (' concluída' if self.feito == True else ' incompleta')


def main():
    casa = []
    casa.append(Tarefa('Passar roupa'))
    casa.append(Tarefa('Lavar prato'))
    
    #list comprehension version
    # [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar prato']
    for task in casa:
        if task.descricao == 'Lavar prato':
            task.concluir()
        print(task)


main()
