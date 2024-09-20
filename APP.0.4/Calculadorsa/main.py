import flet as ft

def calc_suma(txtNum1, txtNum2, lblResultado):
    try:
        num1 = float(txtNum1.value.strip())
        num2 = float(txtNum2.value.strip())
        resultado = num1 + num2
        lblResultado.value = f"Resultado: {resultado}"  # Fixed string formatting
    except ValueError:
        lblResultado.value = "Error: ingresa valores correctos"

def calc_resta(txtNum1, txtNum2, lblResultado):
    try:
        num1 = float(txtNum1.value.strip())
        num2 = float(txtNum2.value.strip())
        resultado = num1 - num2
        lblResultado.value = f"Resultado: {resultado}"  # Fixed string formatting
    except ValueError:
        lblResultado.value = "Error: ingresa valores correctos"

def calc_multiplicacion(txtNum1, txtNum2, lblResultado):
    try:
        num1 = float(txtNum1.value.strip())
        num2 = float(txtNum2.value.strip())
        resultado = num1 * num2
        lblResultado.value = f"Resultado: {resultado}"  # Fixed string formatting
    except ValueError:
        lblResultado.value = "Error: ingresa valores correctos"

def calc_division(txtNum1, txtNum2, lblResultado):
    try:
        num1 = float(txtNum1.value.strip())
        num2 = float(txtNum2.value.strip())
        resultado = num1 / num2
        lblResultado.value = f"Resultado: {resultado}"  # Fixed string formatting
    except ValueError:
        lblResultado.value = "Error: ingresa valores correctos"
    except ZeroDivisionError:
        lblResultado.value = "Error: división por cero"

def limpiar(txtNum1, txtNum2, lblResultado, page):
    txtNum1.value = ""  # Clear input
    txtNum2.value = ""  # Clear input
    lblResultado.value = f"Resultado: {lblResultado}"  # Reset label
    page.update()  # Update the page to reflect changes

def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor = "green"

    txtNum1 = ft.TextField(label="Ingresa el primer número", color="yellow")
    txtNum2 = ft.TextField(label="Ingresa el segundo número", color="yellow")
    lblResultado = ft.Text("Resultado: ", color="yellow")

    btnSuma = ft.ElevatedButton(text="+", on_click=lambda e: calc_suma(txtNum1, txtNum2, lblResultado))
    btnResta = ft.ElevatedButton(text="-", on_click=lambda e: calc_resta(txtNum1, txtNum2, lblResultado))
    btnMultiplicacion = ft.ElevatedButton(text="*", on_click=lambda e: calc_multiplicacion(txtNum1, txtNum2, lblResultado))
    btnDivision = ft.ElevatedButton(text="/", on_click=lambda e: calc_division(txtNum1, txtNum2, lblResultado))
    btnLimpiar = ft.ElevatedButton(text="Limpiar", on_click=lambda e: limpiar(txtNum1, txtNum2, lblResultado, page))

    page.add(
        ft.Column(controls=[
            ft.Row(controls=[txtNum1, txtNum2], alignment="center"),
            ft.Row(controls=[lblResultado], alignment="center"),
            ft.Row(controls=[btnSuma, btnResta, btnMultiplicacion, btnDivision, btnLimpiar], alignment="center")
        ])
    )

ft.app(main) 
