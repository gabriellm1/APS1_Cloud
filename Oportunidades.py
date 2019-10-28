import json

class Oportunidade:

    def __init__(self,duracao,empresa,area,salario,ativo):

        self.dict = {
                        "duração" : duracao,
                        "empresa" : empresa,
                        "area" : area,
                        "salario" : salario,
                        "ativo" : ativo
                    }   
                    

