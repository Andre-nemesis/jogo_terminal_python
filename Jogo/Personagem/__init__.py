import sty 
from Personagem.Classes import Arqueiro,Bardo,Bruxo,Clerigo,Escudeiro,Guerreiro

class Person:
    #váriáveis da classe
    nome = ''
    classe = None
    raca = None

    #metodo construtor
    def __init__(self,nome:str=None,classe:Arqueiro.Arqueiro or Bardo.Bardo or Clerigo.Clerigo or Bruxo.Bruxo or Escudeiro.Escudeiro or Guerreiro.Guerreiro=None,raca:str=None):
        self.nome = nome if nome is not None else None
        self.classe = classe if nome is not None else None
        self.raca = raca if nome is not None else None
    
    #seters
    def setNome(self,nome):
        self.nome = nome
    
    def setClasse(self,classe):
        self.classe = classe

    def setRaca(self,raca):
        self.raca =raca

    #geters
    def getNome(self) -> str:
        return self.nome
    
    def getClasse(self) -> Arqueiro.Arqueiro or Bardo.Bardo or Clerigo.Clerigo or Bruxo.Bruxo or Escudeiro.Escudeiro or Guerreiro.Guerreiro:
        return self.classe
    
    def getRaca(self) -> str:
        return self.raca
    
    def showPersonagem(self):
        print("*="*5,end='')
        print(sty.fg.li_yellow+" Personagem "+sty.fg.rs,end='')
        print("*="*5)
        print(sty.fg.li_cyan+f'Nome: {self.nome}'+sty.fg.rs)
        print(sty.fg.red+f'Raça: {self.raca}'+sty.fg.rs)
        self.classe.classInfo()

