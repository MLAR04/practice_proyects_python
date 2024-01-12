from ctypes import alignment
from turtle import bgcolor
import flet as ft

async def main(page: ft.page):
    ## Inicializar la ventana
    page.window_width = 720
    page.window_height = 1280
    page.window_resizable = False
    page.padding = 0
    page.margin = 0
    #TOP POKEDEX 4 Circles(Blue, red, yellow and green)
    blue_button= ft.Stack([
        ft.Container(width=80, height=80, bgcolor=ft.colors.WHITE ,border_radius=50),
        ft.Container(width=70, height=70, left =3 , top=4, bgcolor=ft.colors.BLUE, border_radius=50)
    ])
    items_header = [
        ft.Container(blue_button, width=80, height=80,border=ft.border.all()),
        ft.Container(width=40, height=40, bgcolor=ft.colors.RED_200 , border_radius=50),
        ft.Container(width=40, height=40, bgcolor=ft.colors.YELLOW , border_radius=50),
        ft.Container(width=40, height=40,bgcolor=ft.colors.GREEN , border_radius=50),
    ]
    header= ft.Container(content=ft.Row(items_header),width=600,height=80, margin = ft.margin.only(top=40))
    
    stack_central= ft.Stack([
        ft.Container(width=600, height=400,bgcolor=ft.colors.WHITE, border=ft.border.all()),
        ft.Container(width=550, height=350,bgcolor=ft.colors.BLACK, border=ft.border.all())
    ])
    
    center = ""#ft.Container(stack_central, width=600,height=400, margin = ft.margin.only(top=40), alignment=ft.alignment.center)
    bottom = ""#ft.Container(content=ft.Row(items_inferior), width=600,height=400, margin = ft.margin.only(top=80))
    
    colum_general = ft.Column(
        spacing=0, 
        controls=[
            header,
            center,
            bottom,
        ]
    )
    contenedor = ft.Container(
        width = 720, 
        height = 1280, 
        bgcolor=ft.colors.RED, 
        alignment=ft.alignment.top_center
    )
    await page.add_async(contenedor)

ft.app(target=main)