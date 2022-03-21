# -*- coding: UTF-8 -*-
# orcamento.py
from abc import ABCMeta,abstractmethod
from operator import le
class Estado_de_um_orcamento(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def aplica_desconto_extra(self,orcamento):
        pass
    
    @abstractmethod
    def aprova(self,orcamento):
        pass
    
    @abstractmethod
    def reprova(self,orcamento):
        pass
    
    @abstractmethod
    def finaliza(self,orcamento):
        pass
    
    
    
# patters state
class Em_aprovacao(Estado_de_um_orcamento):
    def aplica_desconto_extra(self,orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
    
    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()

    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()
    
    def finaliza(self, orcamento):
        raise Exception('Orçamento em aprovação não pode ir para finalizados')
class Aprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self,orcamento):
        orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
    
    def aprova(self, orcamento):
        raise Exception('Orçamento ja esta aprovado')
        
    def reprova(self, orcamento):
        raise Exception('Orçamentos aprovados não podem ser reprovados')
        
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

    
class Reprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self,orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra.')
    
    def aprova(self, orcamento):
        raise Exception('Orçamento Esta Reprovado e não pode ser aprovado')
        
    def reprova(self, orcamento):
        raise Exception('Orçamentos reprovado não pode ser reprovado novamente')
        
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()
        
class Finalizado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self,orcamento):
        raise Exception('Orçamentos Finalizados não recebem desconto extra.')
    
    def aprova(self, orcamento):
        raise Exception('Orçamento ja esta Finalizado')
        
    def reprova(self, orcamento):
        raise Exception('Orçamentos finalizados não podem ser reprovados')
        
    def finaliza(self, orcamento):
        raise Exception('Orçamentos finalizados não podem ser finalizados novamento')

# Estudos designer patterns
class Orcamento(object):

    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0
    
    def aprova(self):
        self.estado_atual.aprova(orcamento)
    
    def reprova(self):
        self.estado_atual.reprova(orcamento)
    
    def finaliza(self):
        self.estado_atual.finaliza(orcamento)
        
    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)
        
    def adiciona_desconto_extra(self,desconto):
        self.__desconto_extra = desconto
        
    # quando a propriedade for acessada, ela soma cada item retornando o valor do orçamento
    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total+= item.valor
        return total - self.__desconto_extra

    # retornamos uma tupla, já que não faz sentido alterar os itens de um orçamento
    def obter_itens(self):

        return tuple(self.__itens)

    # perguntamos para o orçamento o total de itens
    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

# um item criado não pode ser alterado, suas propriedades são somente leitura
class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome


    
if __name__ == '__main__':
    
    orcamento = Orcamento()
    
    orcamento.adiciona_item(Item('Item A',100.0))
    orcamento.adiciona_item(Item('Item B',50.0))
    orcamento.adiciona_item(Item('Item C',400.0))
    
    print(orcamento.valor)
    orcamento.aprova()
    orcamento.finaliza()
    
    # orcamento.aplica_desconto_extra()
    # print(orcamento.valor)