import sty as s
from Personagem import Person
from Personagem.Racas import Racas
from Personagem.Classes import Classes
from Personagem.Armas import Itens
from Personagem.Armas import Arma
import time
from random import randint
from os import system

class Game:
    nome_do_jogo = ''
    personagens = []
    rac = Racas()
    cla = Classes()
    itn = Itens.Itens()

    def __init__(self,nome_do_jogo:str=None):
        self.nome_do_jogo = nome_do_jogo
        
        if self.nome_do_jogo is None:
            print(s.fg(82)+'Bem-Vindo a'+s.fg.rs+s.fg.li_red+' JUMANJI'+s.fg.rs)
            time.sleep(0.5)
            print('Iniciando Jogo...')
            time.sleep(3)
        
        else:
            print(s.fg(82)+'Bem-Vindo a'+s.fg.rs+s.fg.li_red+f' {self.nome_do_jogo}'+s.fg.rs)
            time.sleep(0.5)
            print('Iniciando Jogo...')
            time.sleep(3)
        self.Menu()
        
    def Menu(self):
        system('cls')
        print(s.fg.li_cyan+'-------- Menu Inicial --------'+s.fg.rs)

        print(s.fg.li_magenta+'0 - Sair do Jogo')
        print('1 - Criar Personagem')
        print('2 - Ver Personagem')
        print('3 - Batalhar!'+s.fg.rs)

        opcao = int(input(s.fg.li_yellow+'Digite uma opção: '+s.fg.rs))

        match opcao:
            case 0:
                print(s.fg(177)+'Até Breve!'+s.fg.rs)
                exit()
            case 1:
                if len(self.personagens)==2:
                    print(s.fg.blue+'2 Personagens já criados!'+s.fg.rs)
                    time.sleep(1)
                else:
                    self.personagens.append(self.criarPersonagem())
                self.Menu()
            case 2:
                if len(self.personagens)==0:
                    print(s.bg.red+'Não há personagens criados ainda!'+s.bg.rs)
                    time.sleep(2)
                else:
                    for i in self.personagens:
                        i.showPersonagem()
                    time.sleep(3)
                self.Menu()
            case 3:
                if len(self.personagens) == 0 or len(self.personagens) == 1:
                    print(s.bg.li_red+'O modo Batalhar não está disponivel para essa quantidade de jogadores!'+s.bg.rs)
                    time.sleep(2)
                    self.Menu()
                else:
                    self.Batalhar()
            case _:
                print(s.bg.red+'Opção Inválida!'+s.bg.rs)
                self.Menu()

    def criarPersonagem(self) -> Person | object:
        system('cls')
        self.rac.showRacas()
        racas = self.rac.getRacas()
        while True:
            opcao = int(input('Escolha a sua ' +s.fg.red+'Raça: '+s.fg.rs))
            if 0<= opcao <=5:
                break
            else:
                print(s.bg.red+'Opção Inválida!'+s.bg.rs)
        
        raca_escolhida = racas[opcao]

        system('cls')
        self.cla.showClasses()
        while True:
            opcao = int(input('Escolha a sua ' +s.fg.li_blue+'Classe: '+s.fg.rs))
            if 0<= opcao <=5:
                break
            else:
                print(s.bg.red+'Opção Inválida!'+s.bg.rs)
        
        classes = self.cla.getClasses()
        classe_escolhida = classes[opcao]
        self.cla.removeClass(classe_escolhida)

        system('cls')
        armas_escolhidas = []
        armas = self.itn.showItens(classe_escolhida)
        
        while True:
            opcao = int(input('Escolha a sua ' +s.fg.li_grey+' 1° Arma: '+s.fg.rs))
            if 0<= opcao <=2:
                break
            else:
                print(s.bg.red+'Opção Inválida!'+s.bg.rs)
        armas_escolhidas.append(armas[opcao])
        
        while True:
            opcao = int(input('Escolha a sua ' +s.fg.li_grey+' 2° Arma: '+s.fg.rs))
            if 0<= opcao <=2:
                break
            else:
                print(s.bg.red+'Opção Inválida!'+s.bg.rs)
        
        armas_escolhidas.append(armas[opcao])

        system('cls')
        nome_person = str(input(s.fg(208)+'Digite o nome do seu Personagem: '+s.fg.rs))

        #construindo Personagem
        classe_escolhida.setArma(armas_escolhidas[0])
        classe_escolhida.setArma(armas_escolhidas[1])
        personagem = Person(nome_person,classe_escolhida,raca_escolhida)

        system('cls')
        print(s.bg.li_green+'Personagem criado com sucesso!'+s.bg.rs)
        time.sleep(1.5)

        return personagem
    
    def Batalhar(self):
        system('cls')
        print(s.bg.da_cyan+'Para a Batalha será lançado um Dado D6 para cada jogador.'+s.bg.rs)
        time.sleep(5)
        print(s.fg.li_yellow+'Jogando Dado para o jogador 1.'+s.fg.rs)
        time.sleep(1)
        num_jogador_1 = randint(1,6)
        print('Número do Dado: ' + s.fg.li_magenta+f'{num_jogador_1}'+s.fg.rs)
        
        print(s.fg.li_yellow+'Jogando Dado para o jogador 2.'+s.fg.rs)
        time.sleep(1)
        num_jogador_2 = randint(1,6)
        print('Número do Dado: ' + s.fg.li_magenta+f'{num_jogador_2}'+s.fg.rs)

        if num_jogador_1 > num_jogador_2:
            print(s.fg.green+'O jogador 1 inicia Atacando!'+s.fg.rs)
            time.sleep(2)
            self.menuBatalha(self.personagens[0],self.personagens[1],self.personagens[0].getClasse().getVida(),self.personagens[1].getClasse().getVida())
        else:
            print(s.fg.green+'O jogador 2 inicia Atacando!'+s.fg.rs)
            time.sleep(2)
            self.menuBatalha(self.personagens[1],self.personagens[0],self.personagens[1].getClasse().getVida(),self.personagens[0].getClasse().getVida())
    
    def menuBatalha(self,personagem1:Person,personagem2:Person,vida1:int,vida2:int):
        system('cls')
        print(s.bg.da_magenta+'Fase inicial de Batalha!'+s.bg.rs)
        print(s.fg.li_yellow+'\nFase de escolha de Arma do primeiro Jogador!'+s.fg.rs)
        
        armas_p1 = personagem1.getClasse().getArmas()

        for i,v in enumerate(armas_p1):
            print(f'{i} - '+s.fg(223)+f'{v.getNome()}'+s.fg.rs)
        
        while True:
            opcao = int(input('Escolha a sua arma: '))
            if 0 <= opcao <=1:
                break
            else:
                print(s.bg.li_red+'Opção inválida!'+s.bg.rs)
        arma_p1 = armas_p1[opcao]
        
        time.sleep(1)

        print(s.fg.li_yellow+'\nFase de escolha de Arma do segundo Jogador!'+s.fg.rs)

        armas_p2 = personagem2.getClasse().getArmas()
        for i,v in enumerate(armas_p2):
            print(f'{i} - '+s.fg(223)+f'{v.getNome()}'+s.fg.rs)
        
        while True:
            opcao = int(input('Escolha a sua arma: '))
            if 0 <= opcao <=1:
                break
            else:
                print(s.bg.li_red+'Opção inválida!'+s.bg.rs)
        arma_p2 = armas_p2[opcao]    
        
        time.sleep(1)

        self.determinarVencedor(arma_p1,arma_p2,vida1,vida2)

        while personagem1.getClasse().getVida() > 0 or personagem2.getClasse().getVida() > 0:
            if personagem1.getNome() == self.personagens[0].getNome():
                self.menuBatalha(personagem2,personagem1,vida1,vida2)
            else:
                self.menuBatalha(personagem2,personagem1,vida1,vida2)

    def menuEfeitoEspecial(self) -> int:
        print(s.fg.da_cyan+'Deseja Tentar ativar o efeito especial da Arma?'+s.fg.rs)
        print('\n1 - Sim\n2 - Não\n')
        
        while True:
            op = int(input(s.fg.yellow+'Digite sua opção: '+s.fg.rs))
            if op == 1:
                return 1
            elif op == 2:
                return 0
            else:
                print(s.fg.li_red+'Opção inválida!'+s.fg.rs)

    def determinarVencedor(self,arma_1:Arma,arma_2:Arma,vida1:int,vida2:int):
        chance_de_acerto_atacante = (arma_1.getPrecisao()*0.6) + (arma_1.getForca()*0.4)
        chance_de_acerto_oponente = (arma_2.getPrecisao()*0.6) + (arma_2.getForca()*0.4)

        if chance_de_acerto_atacante > chance_de_acerto_oponente:
            if self.personagens[0].getClasse().getArmas(0).getNome() == arma_1.getNome() or self.personagens[0].getClasse().getArmas(1).getNome() == arma_1.getNome():
                print('\nO ataque com a arma '+ s.fg.li_green+arma_1.getNome()+s.fg.rs+' é bem sucedido!')
                resultado_da_escolha = self.menuEfeitoEspecial()
                if resultado_da_escolha == 1:
                    self.personagens[0],self.personagens[1] = arma_1.ativarEfeitoEspecial(self.personagens[0],self.personagens[1])
                print('\n'+s.bg.da_green+ self.personagens[0].getNome()+s.bg.rs+' ganhou a rodada!')
                self.personagens[1].getClasse().setVida(self.personagens[1].getClasse().getVida()-arma_1.getForca())

                print(s.fg.li_yellow+'\nVida Restante dos Personagens: '+s.fg.rs)
                print(s.fg.li_cyan+self.personagens[0].getNome()+s.fg.rs+s.fg.li_red+f': {self.personagens[0].getClasse().getVida()}'+s.fg.rs)
                print(s.fg.li_cyan+self.personagens[1].getNome()+s.fg.rs+s.fg.li_red+f': {self.personagens[1].getClasse().getVida()}'+s.fg.rs)

                time.sleep(7)

                if self.personagens[1].getClasse().getVida() <= 0:
                    print(s.bg.li_green+ self.personagens[0].getNome()+s.bg.rs+' ganhou o jogo!')
                    time.sleep(3)

                    self.menuFinal(vida1,vida2)
            
            else:
                print('\nO ataque com a arma '+ s.fg.li_green+arma_1.getNome()+s.fg.rs+' é bem sucedido!')
                resultado_da_escolha = self.menuEfeitoEspecial()
                if resultado_da_escolha == 1:
                    self.personagens[1],self.personagens[0] = arma_1.ativarEfeitoEspecial(self.personagens[1],self.personagens[0])
                print('\n'+s.bg.da_green+ self.personagens[1].getNome()+s.bg.rs+' ganhou a rodada!')
                
                self.personagens[0].getClasse().setVida(self.personagens[0].getClasse().getVida()-arma_1.getForca())

                print(s.fg.li_yellow+'\nVida Restante dos Personagens: '+s.fg.rs)
                print(s.fg.li_cyan+self.personagens[0].getNome()+s.fg.rs+s.fg.li_red+f': {self.personagens[0].getClasse().getVida()}'+s.fg.rs)
                print(s.fg.li_cyan+self.personagens[1].getNome()+s.fg.rs+s.fg.li_red+f': {self.personagens[1].getClasse().getVida()}'+s.fg.rs)

                time.sleep(7)

                if self.personagens[0].getClasse().getVida() <= 0:
                    print(s.bg.li_green+ self.personagens[1].getNome()+s.bg.rs+' ganhou o jogo!')
                    time.sleep(3)

                    self.menuFinal(vida1,vida2)

        elif chance_de_acerto_atacante < chance_de_acerto_oponente:
            if self.personagens[0].getClasse().getArmas(0).getNome() == arma_2.getNome() or self.personagens[0].getClasse().getArmas(1).getNome() == arma_2.getNome():
                print('\nO ataque com a arma '+ s.fg.li_green+arma_2.getNome()+s.fg.rs+' é bem sucedido!')
                resultado_da_escolha = self.menuEfeitoEspecial()
                if resultado_da_escolha == 1:
                    self.personagens[0],self.personagens[1] = arma_2.ativarEfeitoEspecial(self.personagens[0],self.personagens[1])
                print('\n'+s.bg.da_green+ self.personagens[0].getNome()+s.bg.rs+' ganhou a rodada!')
                
                self.personagens[1].getClasse().setVida(self.personagens[1].getClasse().getVida()-arma_2.getForca())

                print(s.fg.li_yellow+'\nVida Restante dos Personagens: '+s.fg.rs)
                print(s.fg.li_cyan+self.personagens[0].getNome()+s.fg.rs+s.fg.li_red+f': {self.personagens[0].getClasse().getVida()}'+s.fg.rs)
                print(s.fg.li_cyan+self.personagens[1].getNome()+s.fg.rs+s.fg.li_red+f': {self.personagens[1].getClasse().getVida()}'+s.fg.rs)

                time.sleep(7)

                if self.personagens[1].getClasse().getVida() <= 0:
                    print(s.bg.li_green+ self.personagens[0].getNome()+s.bg.rs+' ganhou o jogo!')
                    time.sleep(3)

                    self.menuFinal(vida1,vida2)
            
            else:
                print('\nO ataque com a arma '+ s.fg.li_green+arma_2.getNome()+s.fg.rs+' é bem sucedido!')
                resultado_da_escolha = self.menuEfeitoEspecial()
                if resultado_da_escolha == 1:
                    self.personagens[1],self.personagens[0] = arma_2.ativarEfeitoEspecial(self.personagens[1],self.personagens[0])
                print('\n'+s.bg.da_green+ self.personagens[1].getNome()+s.bg.rs+' ganhou a rodada!')
                
                self.personagens[0].getClasse().setVida(self.personagens[0].getClasse().getVida()-arma_2.getForca())

                print(s.fg.li_yellow+'\nVida Restante dos Personagens: '+s.fg.rs)
                print(s.fg.li_cyan+self.personagens[0].getNome()+s.fg.rs+s.fg.li_red+f': {self.personagens[0].getClasse().getVida()}'+s.fg.rs)
                print(s.fg.li_cyan+self.personagens[1].getNome()+s.fg.rs+s.fg.li_red+f': {self.personagens[1].getClasse().getVida()}'+s.fg.rs)

                time.sleep(7)

                if self.personagens[0].getClasse().getVida() <= 0:
                    print(s.bg.li_green+ self.personagens[1].getNome()+s.bg.rs+' ganhou o jogo!')
                    time.sleep(3)

                    self.menuFinal(vida1,vida2)

        else:
            print(s.fg.blue+'Ambos os ataques falharam!'+s.fg.rs)    
    
    def menuFinal(self,vida_1:int,vida_2:int):
        system('cls')
        print(s.fg.da_red+'Deseja uma revanche?')
        opcao = int(input(s.fg.li_yellow+'\n1 - Sim\n2 - Voltar para o menu principal\n3 - Sair do jogo\n'+s.fg.rs))
        match opcao:
            case 1:
                self.personagens[0].getClasse().setVida(vida_1)
                self.personagens[1].getClasse().setVida(vida_2)
                self.Batalhar()
            case 2:
                self.personagens.clear()
                self.cla.reset()
                self.itn.reset()
                self.Menu()
            case 3:
                print(s.fg.li_blue+'Até Breve!'+s.fg.rs)
                exit()
            case _:
                print(s.bg.red+'Opção inválida!'+s.bg.rs)

    def iniciar(self):
        self.Menu()

if __name__ == "__main__":
    gm = Game()
    gm.iniciar()