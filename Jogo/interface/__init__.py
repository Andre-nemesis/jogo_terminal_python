import flet as ft
from time import sleep as sl

def main(page: ft.Page):
    texto = ft.Text('Bem vindo a JUMANJI',color='RED',size=30)
    texto2 = ft.Text('Jogo Iniciado!',color='GREEN',size=30)
    greetings = ft.Column()

    def btn_click(e):
        greetings.controls.append(ft.Text(f"Iniciando...",color='YELLOW'))
        page.update()
        sl(3)
        page.add(texto2)    

    page.add(
        texto,
        ft.ElevatedButton("Iniciar Jogo!", on_click=btn_click),
        greetings,
    )

ft.app(target=main)
