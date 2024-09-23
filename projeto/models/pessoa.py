from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco)  -> None:
        self.nome = nome
        self.telefone = telefone 
        self.email = email 
        self.endereco = endereco 
    
    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nTelefone: {self.telefone}"
                f"\nEmail: {self.email}"
                f"\nEndereco: {self.endereco}"
                )

                


    #def _verificar_idade(self, idade):
     #   if idade < 0:
      #      raise ValueError("Idade não pode ser negativa.")
       # if not isinstance(idade, int):
        ##    raise TypeError("Idade deve conter apenas números.")
        #return idade
