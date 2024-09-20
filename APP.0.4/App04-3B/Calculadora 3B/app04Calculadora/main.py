from pydoc import pager
import flet as ft

def calc_suma(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1+num2
        lblResultado.value="Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
def calc_resta(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1-num2
        lblResultado.value="Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
def calc_multiplicacion(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1*num2
        lblResultado.value="Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
        
def calc_division(txtNum1,txtNum2,lblResultado):
    try:
        num1=float(txtNum1.value.strip())
        num2=float(txtNum2.value.strip())
        resultado=num1/num2
        lblResultado.value="Resultado: {resultado}"
    except ValueError:
        lblResultado.value="Error ingresa valores correctos"
    except ZeroDivisionError:
        lblResultado.value="Error división por cero" 


def main(page: ft.Page):
    page.title = "Calculadora"
    page.bgcolor="green"
    
    txtNum1=ft.TextField(label="Ingresa el primer número",color="yellow")
    txtNum2=ft.TextField(label="Ingresa el segundo número",color="yellow")
    lblResultado=ft.Text("Resultado: ",color="yellow")
    
    btnSuma=ft.ElevatedButton(text="+",on_click=calc_suma)
    btnResta=ft.ElevatedButton(text="-",on_click=calc_resta)
    btnMultiplicacion=ft.ElevatedButton(text="*",on_click=calc_multiplicacion)
    btnDivision=ft.ElevatedButton(text="/",on_click=calc_division)
    
    
    
def on_calc_suma(e):
    calc_suma(txtNum1, txtNum2, lblResultado) # type: ignore
    pager.update()
        
def on_calc_resta(e):
    calc_resta(txtNum1, txtNum2, lblResultado) # type: ignore
    pager.update()
        
def on_calc_multiplicacion(e):
    calc_multiplicacion(txtNum1, txtNum2, lblResultado) # type: ignore
    pager.update()
        
def on_calc_division(e):
    calc_division(txtNum1, txtNum2, lblResultado) # type: ignore
    pager.update()
        
def limpiar(e):
    txtNum1.value # type: ignore
    txtNum2.value"" # type: ignore
    lblResultado.value"Resultado: " # type: ignore
    pager.update()
    
    
    
    pager.add(
        ft.Column(controls=[
            ft.Row(controls=[
                txtNum1, # type: ignore # type: ignore # type: ignore # type: ignore # type: ignore
                txtNum2
            ],alignment="center"),
        ]),
        ft.Row(controls=[lblResultado],alignment="center"), # type: ignore
        ft.Row(controls=[
            btnSuma, # type: ignore
            btnResta, # type: ignore
            btnMultiplicacion, # type: ignore # type: ignore # type: ignore # type: ignore
            btnDivision
        ],alignment="center")
    )
    


ft.app(main)
