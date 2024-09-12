import flet as ft

def calcular_suma(txt_num1, txt_num2, txt_resultado):
    try:
        num1 = float(txt_num1.value.strip())
        num2 = float(txt_num2.value.strip())
        resultado = num1 + num2
        txt_resultado.value = f"resultado :{resultado}"
    except value



def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = "#4d4c44"
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.vertical_alignment=ft.MainAxisAlignment.CENTER

    lbl1=ft.Text("CALCULADORA",
                style=ft.TextStyle(size=40,weight="blod"))
    img1=ft.Image(src="",width=200,height=200)

    btnprimer_valor=ft.ElevatedButton("primer_valor",
                            
                            color="pink",
                            width=100,
                            height=50
                            )
    btnsegundo_valor=ft.ElevatedButton("segundo_valor",
                            color="red",
                            width=100,
                            height=50
                            )
ft.app(main)
