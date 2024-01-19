import sty
from Personagem.Armas import Arma

class Guerreiro:
    nome = 'Guerreiro'
    vida = 200
    armas = []

    def __init__(self,armas:list[Arma] = [] ):
        self.armas = armas if armas is not None else None

    def setArma(self,arma:Arma):
        if len(self.armas) == 2:
            print(sty.fg.li_red+'Número máximo de Armas para esse personagem!'+sty.fg.rs)
        else:
            self.armas.append(arma)
    
    def getNome(self) -> str:
        return self.nome
    
    def getArmas(self,indice:int=None) -> Arma or list[Arma]:
        if indice is None:
            return self.armas
        else:
            return self.armas[indice]
    
    def getVida(self) -> int:
        return self.vida
    
    def setVida(self, nova_vida:int):
        self.vida = nova_vida
    
    def classInfo(self):
        print("*="*5,end='')
        print(sty.fg.da_red+f' {self.nome} '+sty.fg.rs,end='')
        print("*="*5)
        print(sty.fg(160)+f'Vida: {self.vida}'+sty.fg.rs)
        print(sty.fg(40)+f'Armas: {self.armas[0].getNome(),self.armas[1].getNome()}'+sty.fg.rs)