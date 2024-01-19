from random import randint
import sty as s

class EfeitoEspecial:
    personagem_beneficiado = object
    personagem_alvo = object
    def __init__ (self,personagem_beneficiado,personagem_alvo):
        self.personagem_beneficiado = personagem_beneficiado
        self.personagem_alvo = personagem_alvo

    def getEfeitoEspecial(self):
        if self.personagem_beneficiado.getClasse().getNome() == 'Arqueiro':
            num = randint(1,6)

            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Arco Elfico':
                if num >= 5:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(0).setForca(self.personagem_beneficiado.getClasse().getArmas(0).getForca()+1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Arco Elfico':
                if num >= 5:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(1).setForca(self.personagem_beneficiado.getClasse().getArmas(0).getForca()+1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Arco Magmático':
                arma_aleatoria = randint(0,1)
                if num >= 5:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setForca(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getForca()-1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Arco Magmático':
                arma_aleatoria = randint(0,1)
                if num >= 5:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setForca(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getForca()-1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Arco de Gelo Verdadeiro':
                arma_aleatoria = randint(0,1)
                if num >= 5:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.2)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Arco de Gelo Verdadeiro':
                arma_aleatoria = randint(0,1)
                if num >= 5:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.2)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
        if self.personagem_beneficiado.getClasse().getNome() == 'Bardo':
            num = randint(1,20)
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Flauta Anã':
                arma_aleatoria = randint(0,1)
                if num >= 14:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.15)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Flauta Anã':
                arma_aleatoria = randint(0,1)
                if num >= 14:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.15)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Flauta Barroca':
                arma_aleatoria = randint(0,1)
                if num >= 17:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.3)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Flauta Barroca':
                arma_aleatoria = randint(0,1)
                if num >= 17:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.3)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Flauta Charmosa':
                arma_aleatoria = randint(0,1)
                if num >= 19:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.5)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Flauta Charmosa':
                arma_aleatoria = randint(0,1)
                if num >= 19:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.5)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
        if self.personagem_beneficiado.getClasse().getNome() == 'Bruxo':
            num = randint(1,6)
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Varinha Ióniania':
                arma_aleatoria = randint(0,1)
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setForca(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getForca()-2)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Varinha Ióniania':
                arma_aleatoria = randint(0,1)
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setForca(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getForca()-2)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Varinha Dracônica':
                arma_aleatoria = randint(0,1)
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Varinha Dracônica':
                arma_aleatoria = randint(0,1)
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Varinha Potteriana':
                arma_aleatoria = randint(0,1)
                if num == 6:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setForca(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getForca()-5)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Varinha Potteriana':
                arma_aleatoria = randint(0,1)
                if num == 6:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setForca(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getForca()-5)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
        if self.personagem_beneficiado.getClasse().getNome() == 'Clerigo':
            num = randint(1,6)
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Livro Sacro':
                arma_aleatoria = randint(0,1)
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setForca(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getForca()-3)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Livro Sacro':
                arma_aleatoria = randint(0,1)
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setForca(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getForca()-3)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Livro Incursivo':
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(0).setForca(self.personagem_beneficiado.getClasse().getArmas(0).getForca()+2)
                    self.personagem_beneficiado.getClasse().getArmas(0).setPrecisao(self.personagem_beneficiado.getClasse().getArmas(0).getPrecisao()+0.1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Livro Incursivo':   
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(1).setForca(self.personagem_beneficiado.getClasse().getArmas(1).getForca()+2)
                    self.personagem_beneficiado.getClasse().getArmas(1).setPrecisao(self.personagem_beneficiado.getClasse().getArmas(1).getPrecisao()+0.1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
            
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Livro Apocaliptico':
                
                if num == 6:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(0).setPrecisao(self.personagem_beneficiado.getClasse().getArmas(0).getPrecisao()+0.1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Livro Apocaliptico':
                
                if num == 6:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(1).setPrecisao(self.personagem_beneficiado.getClasse().getArmas(1).getPrecisao()+0.1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
        
        if self.personagem_beneficiado.getClasse().getNome() == 'Escudeiro':
            num = randint(1,6)
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Escudo Noxiano':
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(0).setPrecisao(self.personagem_beneficiado.getClasse().getArmas(0).getPrecisao()+0.35)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Escudo Noxiano':
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(1).setPrecisao(self.personagem_beneficiado.getClasse().getArmas(1).getPrecisao()+0.35)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Escudo Amazônico':
                
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(0).setForca(self.personagem_beneficiado.getClasse().getArmas(0).getForca()+3)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Escudo Amazônico':
                
                if num >= 4:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(1).setForca(self.personagem_beneficiado.getClasse().getArmas(1).getForca()+3)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
            
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Escudo Nordico':
                
                if num == 6:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(0).setPrecisao(self.personagem_beneficiado.getClasse().getArmas(0).getPrecisao()+0.23)
                    self.personagem_beneficiado.getClasse().getArmas(0).setForca(self.personagem_beneficiado.getClasse().getArmas(0).getForca()+4)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Escudo Nordico':
                
                if num == 6:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(1).setPrecisao(self.personagem_beneficiado.getClasse().getArmas(1).getPrecisao()+0.23)
                    self.personagem_beneficiado.getClasse().getArmas(1).setForca(self.personagem_beneficiado.getClasse().getArmas(1).getForca()+4)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
        
        if self.personagem_beneficiado.getClasse().getNome() == 'Guerreiro':
            num = randint(1,10)
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Espada Gélida':
                arma_aleatoria = randint(0,1)
                if num >= 8:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.24)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setForca(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getForca()-1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Espada Gélida':
                if num >= 8:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setPrecisao(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getPrecisao()-0.24)
                    self.personagem_alvo.getClasse().getArmas(arma_aleatoria).setForca(self.personagem_alvo.getClasse().getArmas(arma_aleatoria).getForca()-1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Espada Krugeriana':
                
                if num >= 5:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(0).setForca(self.personagem_beneficiado.getClasse().getArmas(0).getForca()+1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Espada Krugeriana':
                
                if num >= 5:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(1).setForca(self.personagem_beneficiado.getClasse().getArmas(1).getForca()+1)
                    return self.personagem_beneficiado,self.personagem_alvo
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            if self.personagem_beneficiado.getClasse().getArmas(0).getNome() == 'Espada Nilista':
                
                if num >= 9:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(0).setPrecisao(self.personagem_beneficiado.getClasse().getArmas(0).getPrecisao()+1)
                    return self.personagem_beneficiado,self.personagem_alvo    
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                
            elif self.personagem_beneficiado.getClasse().getArmas(1).getNome() == 'Espada Nilista':
                
                if num >= 9:
                    print(s.fg.green+'Efeito Especial ativado com Sucesso!'+s.fg.rs + s.fg.li_green + ' ' + self.personagem_beneficiado.getClasse().getArmas(0).getEfeitoEspecial()+s.fg.rs)
                    self.personagem_beneficiado.getClasse().getArmas(1).setPrecisao(self.personagem_beneficiado.getClasse().getArmas(1).getPrecisao()+1)
                    return self.personagem_beneficiado,self.personagem_alvo    
                else:
                    print(s.fg.red+'Não foi possivel Ativar o Efeito Especial!'+s.fg.rs)
                    return self.personagem_beneficiado,self.personagem_alvo
                