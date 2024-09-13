import flet as ft

def main(page: ft.Page):
    page.title = "SUMA DE DOS CIFRAS"
    page.bgcolor = "#e17cb8"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    lbl1=ft.Text("",
                style=ft.TextStyle(size=40,weight="blod"))

def calcular_suma(txt_num1, txt_num2, txt_resultado):
    try:
        num1 = float(txt_num1.value.strip())
        num2 = float(txt_num2.value.strip())
        resultado = num1 + num2
        txt_resultado.value = f"Resultado: {resultado}"
    except ValueError:
        txt_resultado.value = "Error: Ingresa valores correctos"
    
    page.add(
        ft.Column(
            [
                lbl1,
                ft.Row(
                    btntxt_num1
                    alignment=ft.MainAxisAlignment.CENTER
                ),  
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )
    
ft.app(main)