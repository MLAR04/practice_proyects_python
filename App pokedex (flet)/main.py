import asyncio
import aiohttp
import flet as ft
block_width = 600 
block_height = 900

async def main(page: ft.page):
    #CONFIG WINDOW
    page.window_width = block_width
    page.window_height = block_height
    page.window_resizable = False
    page.padding = 0
    page.margin = 0
    page.fonts = {
        "zpix": "https://github.com/SolidZORO/zpix-pixel-font/releases/download/v3.1.8/zpix.ttf"
    }
    page.theme= ft.Theme(font_family="zpix")

    #FUNCTIONS
    async def request_API(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.json()
    
    async def void_event(e : ft.ContainerTapEvent):
        print("click")
    #TOP POKEDEX 4 Circles(Blue, red, yellow and green)
    blue_button= ft.Stack([
        ft.Container(width=50, height=50, bgcolor=ft.colors.WHITE ,border_radius=50),
        ft.Container(width=40, height=40, left =5 , top=5, bgcolor=ft.colors.BLUE, border_radius=50)
    ])
    items_header = [
        ft.Container(blue_button, width=50, height=50),
        ft.Container(width=20, height=20, bgcolor=ft.colors.RED_200 , border_radius=50),
        ft.Container(width=20, height=20, bgcolor=ft.colors.YELLOW , border_radius=50),
        ft.Container(width=20, height=20,bgcolor=ft.colors.GREEN , border_radius=50),
    ]
    header= ft.Container(content=ft.Row(items_header),width=600,height=50, margin=ft.margin.only(left =10 , top=10))
    #MIDLE POKEDEX A Window to show the pokemon image  
    center_image = ft.Image(
                src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/132.png",
                scale=15, # Redimensionamos a tamano muy grande
                width=30, #Con esto se reescalara a un tamano inferior automaticamente
                height=30,
                top=300/2,
                right=500/2,
    )
    stack_central= ft.Stack([
        ft.Container(width=500, height=300,bgcolor=ft.colors.WHITE),
        ft.Container(width=450, height=250, left = 25, top=25 ,bgcolor=ft.colors.BLACK),
        center_image
    ])
    center = ft.Container(stack_central, width=600,height=300, margin = ft.margin.only(top=40), alignment=ft.alignment.center)
    #BOTTOM POKEDEX A Window to show the pokemon data and an arrow to change pokemon 
    arrow_shape = ft.canvas.Canvas([
        ft.canvas.Path(
                [
                    ft.canvas.Path.MoveTo(40, 0),
                    ft.canvas.Path.LineTo(0,50),
                    ft.canvas.Path.LineTo(80,50),
                ],
                paint=ft.Paint(
                    style=ft.PaintingStyle.FILL,
                ),
            ),
        ],
        width=80,
        height=50,
    )
    up_arrow = ft.Container(arrow_shape, width=80, height=50, on_click=void_event)#_get_pokemon)
    arrows = ft.Column(
        [
            up_arrow,
             #rad 180 grads = 3.14159
            ft.Container(up_arrow, width=80, height=50, rotate=ft.Rotate(angle=3.14159),), #on_click=evento_get_pokemon),
        ]
    )
    pokemon_data = ft.Text(
        value="In This box is goin to show the text with the pokemon data",
        color=ft.colors.BLACK,
        size=16 
        )
    items_bottom =[
        ft.Container(width=25), #Margen izquierdos
        ft.Container(pokemon_data, padding=10, width=400, height=300, bgcolor=ft.colors.GREEN, border_radius=20),
        ft.Container(width=5), #Margen derecho
        ft.Container(arrows, width=80, height=120),
    ]
    bottom = ft.Container(content=ft.Row(items_bottom), width=600, height=400)
    
    #GENERAL LAYOUT
    colum_general = ft.Column(
        spacing=0, 
        controls=[
            header,
            center,
            bottom,
        ]
    )
    contenedor = ft.Container(
        colum_general,
        width = block_width, 
        height = block_height, 
        bgcolor=ft.colors.RED, 
        alignment=ft.alignment.top_center
    )
    
    #ADD
    await page.add_async(contenedor)

ft.app(target=main)