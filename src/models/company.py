class Company:
    def __init__(self, scraped_array):
        self.__cnpj = scraped_array[1]
        self.__razao_social = scraped_array[4]
        self.__nome_fantasia = scraped_array[5]
        self.__abertura = scraped_array[6]
        self.__tipo = scraped_array[10]
        self.__situacao = scraped_array[11]
        self.__email = scraped_array[13]
        self.__telefone = scraped_array[14]
        self.__logradouro = scraped_array[15]
        self.__complemento = scraped_array[16]
        self.__bairro = scraped_array[17]
        self.__cep = scraped_array[18]
    

    def __str__(self):
        return f'''
cnpj: {self.__cnpj}
abertura: {self.__abertura}
tipo: {self.__tipo}
situação: {self.__situacao}
email: {self.__email}
telefone: {self.__telefone}
logradouro: {self.__logradouro}
complemento: {self.__complemento}
bairro: {self.__bairro}
cep: {self.__cep}
'''