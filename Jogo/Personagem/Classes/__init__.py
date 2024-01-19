from Personagem.Classes import Arqueiro,Bardo,Clerigo,Bruxo,Escudeiro,Guerreiro
import sty as s

class Classes:
    classes = []
    def __init__(self):
        self.classes.append(Bardo.Bardo())
        self.classes.append(Arqueiro.Arqueiro())
        self.classes.append(Clerigo.Clerigo())
        self.classes.append(Bruxo.Bruxo())
        self.classes.append(Escudeiro.Escudeiro())
        self.classes.append(Guerreiro.Guerreiro())        
    
    def showClasses(self):
        print('*='*5,end='')
        print(s.fg(220)+'Classes'+s.fg.rs,end='')
        print('*='*5)
        for i,v in enumerate(self.classes):
            print(f'{i} - '+s.fg(223)+v.getNome()+s.fg.rs)
    
    def getClasses(self) -> list[str]:
        return self.classes
    
    def reset(self):
        self.classes.clear()
        self.__init__()

    def removeClass(self,classe:Arqueiro.Arqueiro or Bardo.Bardo or Clerigo.Clerigo or Bruxo.Bruxo or Escudeiro.Escudeiro or Guerreiro.Guerreiro):
        self.classes.remove(classe)