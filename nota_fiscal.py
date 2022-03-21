
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
    def __init__(self,razao_social,cnpj,itens,data_de_emisao,detalhes):
        self.__razao_social = razao_social
        self.__cnpf = cnpj
        self.__data_de_emisao = data_de_emisao
        
        if(len(detalhes) >20):
            raise Exception('Detalhes da nota não podeter mais deo que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens
    
    @property
    def razao_social(self):
        return self.__razao_social
    
    @property
    def cnpj(self):
        return self.__cnpf
    
    @property
    def data_de_emisao(self):
        return self.__data_de_emisao

    @property
    def detalhes(self):
        return self.__detalhes