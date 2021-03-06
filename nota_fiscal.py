# -*- coding: UTF-8 -*-
from datetime import date
class Item(object):
    def __init__(self,descricao,valor):
        self.__descricao = descricao
        self.__valor = valor
    
    @property
    def descricao(self):
        return self.__descricao
    
    @property
    def valor(self):
        return self.__valor
    
class Nota_Fiscal(object):
    # parametros opcionais devem os ultimos parametros do construtor
    def __init__(self,razao_social,cnpj,itens,data_de_emissao=date.today(),detalhes='',observadores=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        
        if(len(detalhes) >20):
            raise Exception('Detalhes da nota não podeter mais deo que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens
        
        for observador in observadores:
            observador(self)
        
    @property
    def razao_social(self):
        return self.__razao_social
    
    @property
    def cnpj(self):
        return self.__cnpj
    
    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes
    

if __name__ == '__main__':
    from criador_de_nota_filcal import Criador_de_nota_fiscal
    from observadores import Observer
    
    itens = [
        Item('ITEM A ',100),
        Item('ITEM B',200)
    ]
    
    obj_observer = Observer()
    
    # parametros nomeados
    nota_fiscal = Nota_Fiscal(
        cnpj='01234567891234',
        razao_social='FHSA ltda',
        itens = itens,
        data_de_emissao =date.today(),
        detalhes='',
        observadores=[obj_observer.imprime,obj_observer.envia_por_email,obj_observer.salva_no_banco]
    )
    
    # nf_builder = (Criador_de_nota_fiscal()
    #             .com_razao_social('well Obj ltda')
    #             .com_cnpj('365299728033')
    #             .com_itens(itens)
    #             .constroi())
    