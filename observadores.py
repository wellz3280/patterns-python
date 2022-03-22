# -*- coding: UTF-8 -*-
class Observer(object):
        
    def imprime(self,nota_fiscal):
        print('Imprimindo nota fiscal %s'%(nota_fiscal.cnpj))
        
    def envia_por_email(self,nota_fiscal):
        print('enviando nota fiscal por email %s'%(nota_fiscal.cnpj))
            
    def salva_no_banco(self,nota_fiscal):
        print('Salvando nota fiscal %s'%(nota_fiscal.cnpj))