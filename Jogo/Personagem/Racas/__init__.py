import sty as s

class Racas:
    racas = []

    #gerando a lista de raças para a escolha no jogo
    def __init__(self):
        self.racas.append('Humano')
        self.racas.append('Elfo')
        self.racas.append('Anão')
        self.racas.append('Vastaya')
    
    def getRacas(self) -> list[str]:
        return self.racas

    def showRacas(self) -> None:
        print('*='*5,end='')
        print(s.fg(120)+'Raças'+s.fg.rs,end='')
        print('*='*5)
        for i,v in enumerate(self.racas):
            print(f'{i} - '+s.fg(223)+v+s.fg.rs)
  