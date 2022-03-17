# -*- coding: UTF-8 -*-
from abc import ABCMeta,abstractmethod
from operator import truediv
from pickle import FALSE, TRUE

class Template_de_imposto_condicional(object):
    __metaclass__ = ABCMeta
    
    def calcula(self,orcamento):
        if self.deve_usar_maxima_taxacao(orcamento):
            return self.maxima_taxacao(orcamento)
        else:
            return self.minima_taxacao(orcamento)
    
    @abstractmethod
    def deve_usar_maxima_taxacao(orcamento):
        pass
    
    @abstractmethod
    def maxima_taxacao(orcamento):
        pass
    
    @abstractmethod
    def minima_taxacao(orcamento):
        pass

class ISS(object):
    def calcula(orcamento):
        return orcamento.valor * 0.1

class ICMS(object):
    def calcula(orcamento):
        return orcamento.valor * 0.06

class ICPP(Template_de_imposto_condicional):
    def calcula(self,orcamento):
        if orcamento.valor > 500:
            return orcamento.valor * 0.07
        else:
            return orcamento.valor * 0.05

class IKCV(Template_de_imposto_condicional):
    def calcula(self,orcamento):
        if orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento):
            return orcamento.valor * 0.1
        else:
            return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self,orcamento):
        for item in orcamento.obter_itens():
            if(item.valor > 100):
                return TRUE
        return FALSE
