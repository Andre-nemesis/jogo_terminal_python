import sty
from Personagem.Armas import Efeito_Especial

class Arma:
    nome = ''
    foca = 0
    precisao = 0.0
    efeito_especial = ''

    def __init__(self,nome:str,foca:int,precisao:float,efeito_especial:str):
        self.nome = nome
        self.foca = foca
        self.efeito_especial = efeito_especial
        self.precisao = precisao
    
    def getNome(self) -> str:
        return self.nome
    
    def getForca(self) -> int:
        return self.foca
    
    def getEfeitoEspecial(self):
        return self.efeito_especial
    
    def ativarEfeitoEspecial(self,personagem_beneficiado:object,personagem_alvo:object) ->tuple[type[object]]:
        Esp_Efect = Efeito_Especial.EfeitoEspecial(personagem_beneficiado,personagem_alvo)
        return Esp_Efect.getEfeitoEspecial()
    
    def getPrecisao(self) -> float:
        return self.precisao
    
    def setForca(self,nova_forca):
        self.foca = nova_forca
    
    def setPrecisao(self,nova_precisao):
        self.precisao = nova_precisao
    
    def armInfo(self):
        print("*="*5,end='')
        print(sty.fg(214)+f" {self.nome} "+sty.fg.rs,end='')
        print("*="*5)
        print(sty.fg(39)+f'Força: {self.foca}'+sty.fg.rs)
        print(sty.fg(226)+f'Precisão: {self.precisao}'+sty.fg.rs)
        print(sty.fg(141)+f'Efeito Especial: {self.efeito_especial}'+sty.fg.rs)