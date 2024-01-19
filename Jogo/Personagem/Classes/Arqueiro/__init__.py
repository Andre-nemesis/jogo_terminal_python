import sty
import Personagem.Armas as Arma

class Arqueiro:
    nome = 'Arqueiro'
    vida = 180
    armas = []

    def __init__(self,armas:list[Arma.Arma] = [] ):
        self.armas = armas if armas is not None else None

    def setArma(self,arma:Arma.Arma):
        if len(self.armas) == 2:
            print(sty.fg.li_red+'Número máximo de Armas para esse personagem!'+sty.fg.rs)
        else:
            self.armas.append(arma)
    
    def setVida(self, nova_vida:int):
        self.vida = nova_vida
    
    def getNome(self) -> str:
        return self.nome
    
    def getArmas(self,indice:int=None) -> Arma.Arma or list[Arma.Arma]:
        if indice is None:
            return self.armas
        else:
            return self.armas[indice]
    
    def getVida(self) -> int:
        return self.vida
    
    def classInfo(self):
        print("*="*5,end='')
        print(sty.fg(32)+f' {self.nome} '+sty.fg.rs,end='')
        print("*="*5)
        print(sty.fg(160)+f'Vida: {self.vida}'+sty.fg.rs)
        print(sty.fg(40)+f'Armas: {self.armas[0].getNome(),self.armas[1].getNome()}'+sty.fg.rs)