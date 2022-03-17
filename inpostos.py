# -*- coding: UTF-8 -*-
from abc import ABCMeta,abstractmethod
from operator import truediv
from pickle import FALSE, TRUE

# classe 
class Template_de_imposto_condicional(metaclass=ABCMeta):
    __metaclass__ = ABCMeta
    
    def calcula(self,orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)
    
    @abstractmethod
    def deve_usar_maxima_taxacao(self,orcamento):
        pass
    
    @abstractmethod
    def maxima_taxacao(self,orcamento):
        pass
    
    @abstractmethod
    def minima_taxacao(self,orcamento):
        pass

class ISS(object):
    def calcula(orcamento):
        return orcamento.valor * 0.1

class ICMS(object):
    def calcula(orcamento):
        return orcamento.valor * 0.06

# classes usando metodos abstratos
class ICPP(Template_de_imposto_condicional):
    def deve_usar_maxima_taxacao(self,orcamento):
        return orcamento.valor > 500

    def maxima_taxacao(self,orcamento):
        return orcamento.valor * 0.07
    
    def minima_taxacao(self,orcamento):
        return orcamento.valor * 0.05
class IKCV(Template_de_imposto_condicional):

    def deve_usar_maxima_taxacao(self,orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)
    
    def maxima_taxacao(self,orcamento):
        return orcamento.valor * 0.1
    
    def minima_taxacao(orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self,orcamento):
        for item in orcamento.obter_itens():
            if(item.valor > 100):
                return TRUE
        return FALSE
