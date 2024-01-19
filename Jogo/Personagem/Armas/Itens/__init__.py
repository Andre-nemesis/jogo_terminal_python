import Personagem.Armas as Arma
from Personagem.Classes import Arqueiro,Bardo,Bruxo,Clerigo,Escudeiro,Guerreiro

import sty as s

class Itens:
    armas = []

    #gerando os itens das classes
    def __init__(self):
        #Arcos
        self.armas.append(Arma.Arma('Arco Elfico',15,0.5,'Você chamou reforços Elficos -> + 1 Dano permanente'))
        self.armas.append(Arma.Arma('Arco Magmático',20,0.7,'Inimigo sofreu uma pequena queimadura -> - 1 de Força inimigo'))
        self.armas.append(Arma.Arma("Arco de Gelo Verdadeiro", 23, 0.8, "Inimigo ficou teve uma parte do corpo congelada -> - 0.2 de precisao inimiga"))
        # Escudos
        self.armas.append(Arma.Arma("Escudo Noxiano", 21, 0.35, "Desestabilizou o inimigo -> - 0.35 de precisão"))
        self.armas.append(Arma.Arma("Escudo Amazônico", 15, 0.9, "Reflorestou o ambiente -> + 3 de Força"))
        self.armas.append(Arma.Arma("Escudo Nordico", 19, 0.58, "A história vinking foi restaurada -> + 4 de Força e + 0.23 de Precisão"))
        # Livros
        self.armas.append(Arma.Arma("Livro Sacro", 15, 0.78, "Conversão do inimigo iniciada! -> - 3 de Força inimiga e - 0.1 de precisão"))
        self.armas.append(Arma.Arma("Livro Incursivo", 18, 0.5, "Uma cruazada foi iniciada -> + 2 de Dano e + 0.1 de precisão"))
        self.armas.append(Arma.Arma("Livro Apocaliptico", 25, 0.001, "Bem-vindo ao apocalipse! -> + 0.1 de precisão"))
        # Varinhas
        self.armas.append(Arma.Arma("Varinha Ióniania", 15, 0.89, "O inimigo está mais pácifico! -> - 2 de Força inimiga"))
        self.armas.append(Arma.Arma("Varinha Dracônica", 18, 0.73, "O inimigo tomou um pequeno choque! -> - 0.1 de precisao inimiga"))
        self.armas.append(Arma.Arma("Varinha Potteriana", 22, 0.3, "O inimigo foi evenenado! -> - 5 de Força inimiga"))
        # Espadas
        self.armas.append(Arma.Arma("Espada Gélida", 15, 0.74, "Parte do alvo foi cristalizada! -> - 0.24 de precisao inimiga e - 1 de Força"))
        self.armas.append(Arma.Arma("Espada Krugeriana", 19, 0.53, "Um kruger te ajudou na rodada! -> + 1 de Força"))
        self.armas.append(Arma.Arma("Espada Nilista", 24, 0.29, "Nietzsche negou a existência do sentido! -> + 1 de precisão"))
        # Flautas
        self.armas.append(Arma.Arma("Flauta Anã", 23, 0.57, "Alvo começa a dançar -> - 0.15 de precisão inimiga"))
        self.armas.append(Arma.Arma("Flauta Barroca", 17, 0.85, "Inimigo encantado com uma obra de Aleijadinho -> - -0.3 de precisão inimiga"))
        self.armas.append(Arma.Arma("Flauta Charmosa", 15, 1, "Parece que o alvo gosta de você -> - 0.5 de precisão inimiga"))

    def getItens(self) -> list[Arma.Arma]:
        return self.armas

    def showItens(self,classe:Arqueiro.Arqueiro or Bardo.Bardo or Bruxo.Bruxo or Clerigo.Clerigo or Escudeiro.Escudeiro or Guerreiro.Guerreiro):
        print('*='*5,end='')
        print(s.fg(166)+'Armas'+s.fg.rs,end='')
        print('*='*5)
        count = 0
        indices = []
        for i,v in enumerate(self.armas):
            
            if classe.getNome() == 'Guerreiro':
                if 'Espada' in v.getNome():
                    print(f'{count} '+s.fg.da_green+v.getNome()+s.fg.rs)
                    count += 1
                    indices.append(i)
            
            elif classe.getNome() == 'Arqueiro':
                if 'Arco' in v.getNome():
                    print(f'{count} '+s.fg.da_green+v.getNome()+s.fg.rs)
                    count += 1
                    indices.append(i)
            
            elif classe.getNome() == 'Bardo':
                if 'Flauta' in v.getNome():
                    print(f'{count} '+s.fg.da_green+v.getNome()+s.fg.rs)
                    count += 1
                    indices.append(i)
            
            elif classe.getNome() == 'Bruxo':
                if 'Varinha' in v.getNome():
                    print(f'{count} '+s.fg.da_green+v.getNome()+s.fg.rs)
                    count += 1
                    indices.append(i)
            
            elif classe.getNome() == 'Escudeiro':
                if 'Escudo' in v.getNome():
                    print(f'{count} '+s.fg.da_green+v.getNome()+s.fg.rs)
                    count += 1
                    indices.append(i)
            
            elif classe.getNome() == 'Clerigo':
                if 'Livro' in v.getNome():
                    print(f'{count} '+s.fg.da_green+v.getNome()+s.fg.rs)
                    count += 1
                    indices.append(i)
        
        arr_armas = []
        
        for i in indices:
            arr_armas.append(self.armas[i])
        
        return arr_armas
    
    def reset(self):
        self.armas.clear()
        self.__init__()