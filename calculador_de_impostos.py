# design patterns strategy
# em python é possivel passar uma função por parâmetro

from inpostos import ISS,ICMS,ICPP,IKCV
from orcamento import Item

class Calculador_de_impostos(object):
    def realiza_calculo(self,orcamento,imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print(imposto_calculado)


if __name__ =='__main__':
    from orcamento import Orcamento

    calculador = Calculador_de_impostos()
    orcamento = Orcamento()
    
    orcamento.adiciona_item(Item('Item A',100.0))
    orcamento.adiciona_item(Item('Item B',50.0))
    orcamento.adiciona_item(Item('Item C',400.0))
    
    print('ISS e ICMS')
    calculador.realiza_calculo(orcamento,ISS())
    calculador.realiza_calculo(orcamento,ICMS())
    
    print('ICMS COM ISS')
    calculador.realiza_calculo(orcamento,ICMS(ISS()))
    
    print('ICPP e IKVC')
    calculador.realiza_calculo(orcamento,ICPP())
    calculador.realiza_calculo(orcamento,IKCV())
    
    print('IKVC COM ICPP')
    calculador.realiza_calculo(orcamento,IKCV(ICPP()))

