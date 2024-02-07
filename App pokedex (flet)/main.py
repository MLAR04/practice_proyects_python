import asyncio
import aiohttp
import flet as ft

#GLOBAL
block_width = 600 
block_height = 900
first_pokemon = 1
number_pokemon = 0
limit = 151

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
    #UP-DOWN POKEMON
    async def get_pokemon(e : ft.ContainerTapEvent):
        global number_pokemon
        global first_pokemon
        global limit

        if e.control == up_arrow:
            number_pokemon = number_pokemon + 1
        else:
            number_pokemon= number_pokemon - 1
        
        if number_pokemon > limit:
            number_pokemon = first_pokemon
        number = (number_pokemon%limit)
        if number < first_pokemon:
            number = number_pokemon = limit
 
        result = await request_API(f"https://pokeapi.co/api/v2/pokemon/{number}")
        habilitys = ""
        types = ""
        for hability in result['abilities']:
            habilitys += f"     - {hability['ability']['name']}\n" 
        for poke_type in result['types']:
            types += f"- {poke_type['type']['name']} "
        poke_heigth = float((result['height']*10)/100)
        entry_response = await request_API(f"https://pokeapi.co/api/v2/pokemon-species/{number}/")
        description = entry_response["flavor_text_entries"][0]["flavor_text"].replace("\f","\n").replace("\n"," ")
        pokemon_data.value = f"Number: {number} ~ Name: {result['name']}\n~ Types : {types}- ~ Height: {poke_heigth} mts.\n~ Habilities: \n{habilitys}~ Description: \n{description}"
        sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{number}.png"
        center_image.src = sprite_url
        await page.update_async()
    
    async def get_generation(e: ft.ContainerTapEvent):
        global number_pokemon
        global first_pokemon
        global limit

        if e.control == kanto:
            first_pokemon = 1
            number_pokemon = 1
            limit = 151
        elif e.control == johto:
            first_pokemon = 152
            number_pokemon = 152
            limit =  251
        else:
            first_pokemon = 252
            number_pokemon = 252
            limit = 386
        
    #TOP POKEDEX 4 Circles(Blue, red, yellow and green)
    blue_button= ft.Stack([
        ft.Container(width=50, height=50, bgcolor=ft.colors.WHITE ,border_radius=50),
        ft.Container(width=40, height=40, left =5 , top=5, bgcolor=ft.colors.BLUE, border_radius=50)
    ])
    kanto = ft.Container(width=20, height=20, bgcolor=ft.colors.RED_200 , border_radius=50, on_click=get_generation)
    johto = ft.Container(width=20, height=20, bgcolor=ft.colors.YELLOW , border_radius=50, on_click=get_generation)
    hoenn = ft.Container(width=20, height=20,bgcolor=ft.colors.GREEN , border_radius=50, on_click=get_generation)
    items_header = [
        ft.Container(blue_button, width=50, height=50),
        kanto,johto,hoenn,
    ]
    header= ft.Container(content=ft.Row(items_header),width=600,height=50, margin=ft.margin.only(left =10 , top=10))
    #MIDLE POKEDEX A Window to show the pokemon image  
    sprite_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/0.png"
    center_image = ft.Image(
                src=sprite_url,
                scale=15, # Redimensionamos a tamano muy grande
                width=18, #Con esto se reescalara a un tamano inferior automaticamente
                height=18,
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
    up_arrow = ft.Container(arrow_shape, width=80, height=50, on_click=get_pokemon)
    arrows = ft.Column(
        [
            up_arrow,
            #rad 180 grads = 3.14159
            ft.Container(arrow_shape, width=80, height=50, rotate=ft.Rotate(angle=3.14159),on_click=get_pokemon),
        ]
    )
    pokemon_data = ft.Text(
        value="Welcome!!!, I'm Your asistent in your road to be the best Pokemón Master",
        color=ft.colors.BLACK,
        size=16 
        )
    items_bottom =[
        ft.Container(width=20), #Margen izquierdos
        ft.Container(pokemon_data, padding=10, width=430, height=330, bgcolor=ft.colors.GREEN, border_radius=20),
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
    
    #RUN
    await page.add_async(contenedor)
    #get_generation()

ft.app(target=main)
