class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def inserir_inicio(self, valor):
        novo_no = No(valor)
        if self.primeiro is None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            novo_no.proximo = self.primeiro
            self.primeiro.anterior = novo_no
            self.primeiro = novo_no

    def inserir_fim(self, valor):
        novo_no = No(valor)
        if self.primeiro is None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            novo_no.anterior = self.ultimo
            self.ultimo.proximo = novo_no
            self.ultimo = novo_no

    def remover_inicio(self):
        if self.primeiro is None:
            return None
        valor_removido = self.primeiro.valor
        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            self.primeiro = self.primeiro.proximo
            self.primeiro.anterior = None
        return valor_removido

    def remover_fim(self):
        if self.ultimo is None:
            return None
        valor_removido = self.ultimo.valor
        if self.primeiro == self.ultimo:
            self.primeiro = None
            self.ultimo = None
        else:
            self.ultimo = self.ultimo.anterior
            self.ultimo.proximo = None
        return valor_removido

    def obter_valor(self, posicao):
        if self.primeiro is None:
            return None
        no_atual = self.primeiro
        pos_atual = 0
        while no_atual is not None and pos_atual != posicao:
            no_atual = no_atual.proximo
            pos_atual += 1
        if no_atual is None:
            return None
        return no_atual.valor

    def imprimir(self):
        lista = []
        no_atual = self.primeiro
        while no_atual is not None:
            lista.append(no_atual.valor)
            no_atual = no_atual.proximo
        print(lista)

    def imprimir_inverso(self):
        lista = []
        no_atual = self.ultimo
        while no_atual is not None:
            lista.append(no_atual.valor)
            no_atual = no_atual.anterior
        print(lista[::-1])

# programa principal
lista = ListaDuplamenteEncadeada()
lista.inserir_inicio(5)
lista.inserir_inicio(8)
lista.inserir_inicio(3)
lista.inserir_inicio(2)
lista.inserir_fim(7)
lista.remover_inicio()
valor = lista.obter_valor(2)
lista.remover_fim()
lista.imprimir()
lista.imprimir_inverso()
