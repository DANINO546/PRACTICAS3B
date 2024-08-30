import flet as ft


def main(page: ft.Page):
    page.title=("mostrar nombre")
    page.bgcolor="f0a3da"
    text_field=ft.textfield(label=ingresa tu nombre)
    button=ft.elevated_button(
        text="di mi nombre", 
        onclick=lambda e: mostrar_nombre(text_fiel,page)
    )


ft.app(main)
