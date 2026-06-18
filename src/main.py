import flet as ft
import client
from threading import Thread, Event
import time
import os
import ast
import pickle
import asyncio
import defineContent as contentDefiner


#RECIPE VARS
recipeContent={}
recipeList=[]
recipebox=ft.Container()
recipeBoxExp=False
recipeExpandedName=""
recipeExpanded=False
recipeExpRow=ft.Row()
recipeContainers={}
########################

#RAW MATERIAL VARS
inventoryList=[]
itemContainers={}
inventoryBox=ft.Container()
itemExpandedName=""
inventoryBoxExp=False
inventoryExpRow=ft.Row()
itemExpanded=False
###########################

#MONEY BOX VARS
money=0
moneybox=ft.Container()
########################

#DEFAULT VARS
DISCONNECT_MSG="!disconnect"
logged=False
userName=""
boxShadow=ft.BoxShadow(blur_radius=15, spread_radius=2.5, color=ft.Colors.DEEP_PURPLE_ACCENT, offset=ft.Offset(0,0))
grad=ft.LinearGradient(
            begin=ft.Alignment.TOP_CENTER,
            end=ft.Alignment.BOTTOM_CENTER,
            colors=[ft.Colors.BLACK, ft.Colors.BLACK, ft.Colors.PURPLE_ACCENT_700])
####################################################################################################################

def main(page: ft.Page):
    bar_width, handle_size = 300, 60
    max_x = bar_width - handle_size
    global t1
    page.window.width=1280
    page.window.height=720
    page.window.frameless=True
    page.window.gradient=grad
    page.border_radius=ft.BorderRadius.all(20)
    page.window.spacing=0
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing=0
    page.window.opacity=1
    page.theme=ft.Theme(scrollbar_theme=ft.ScrollbarTheme(thickness=0, thumb_visibility=False))
    page.window.animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_OUT)
    page.padding=0
    page.window.draggable=True
    page.window.resizable=False
    page.window.maximizable=False
    page.theme = ft.Theme(
        text_theme=ft.TextTheme(
            body_medium=ft.TextStyle(color=ft.Colors.WHITE)
        )
    )
    page.dark_theme = ft.Theme(
        text_theme=ft.TextTheme(
            body_medium=ft.TextStyle(color=ft.Colors.WHITE)
        )
    )
    page.update()
    widthscr=page.window.width
    test=ft.TextField(hint_text="Username", width=500, color=ft.Colors.WHITE)
    Pass=ft.TextField(hint_text="Password", width=500, password=True, can_reveal_password=True, color=ft.Colors.WHITE)
    t=ft.Text(value=f"Hello, {userName}", size=15)
    rw=ft.Row(spacing=10)
    invenBox={}
    reciBox={}
    def printText(f):
        t.value=str(test.value)
        page.update()
    def changeWidth(e):
        page.window.width=int(e)
        page.update()
    def login(user, passwd):
        global userName
        global logged
        global inventoryBox
        global moneybox
        global recipebox
        if os.path.exists("token.pkl") and user=="":
            with open("token.pkl", "rb") as f:
                tok=pickle.load(f)
            r=client.main(f"login", tok)
            if r["user"]!="Token not found!":
                userName=r["user"]
                user=userName
                logged=True
                page.add(topNav)
                page.add(Bg)
                t.value=f"Hello, {userName}"
                inventoryBox=ft.Container(height=300, width=300, shadow=boxShadow, border_radius=ft.BorderRadius.all(25), bgcolor=ft.Colors.GREY_900, animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT), alignment=ft.Alignment(-0.9,-0.8))
                moneybox=ft.Container(height=300, width=300, margin=ft.Margin.all(10), padding=ft.Padding.all(25), border_radius=ft.BorderRadius.all(25), bgcolor=ft.Colors.GREY_900, animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT), shadow=boxShadow, alignment=ft.Alignment(-0.9,-0.8))
                recipebox=ft.Container(height=300, width=300, margin=ft.Margin.all(10), padding=ft.Padding.all(25), border_radius=ft.BorderRadius.all(25), bgcolor=ft.Colors.GREY_900, animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT), shadow=boxShadow, alignment=ft.Alignment(-0.9,-0.8))
                everything.content=ft.Row([inventoryBox, moneybox, recipebox])
                everything.alignment=ft.Alignment.TOP_LEFT
                everything.update()
                for i in invenBox.keys():
                    try:
                        j=invenBox[i].keys()
                    except:
                        inventoryList.append(ft.Text(value=f"{i}: {invenBox[i]}"))
                    else:
                        for x in j:
                            inventoryList.append(ft.Text(value=f"{x}: {invenBox[i][x]}"))
                inventoryBox.controls=inventoryList
                moneybox.content=ft.Text(value=f"Money: {money}")
                recipebox.content=ft.Text(value=f"{recipeContent}")
                inventoryBox.update()
                everything.update()
                page.update()
                t1.start()
            elif r["user"]=="Token not found!":
                def closeTryDialog(x=None):
                    dia.open=False
                    page.update()
                t.value=f"Hello!"
                dia=ft.AlertDialog(title="Logged out!", content=ft.Text("Your account was logged out! Login again!", color=ft.Colors.BLACK))
                everything.content=ft.ResponsiveRow([
                            ft.Container(content=ft.Column([
                                test,
                                Pass,
                                ft.FloatingActionButton(content="Login", on_click=lambda x:login(test.value, Pass.value)),
                            ],
                            spacing=10,
                            alignment=ft.Alignment.CENTER,
                            expand=False,
                        ),
                        padding=10,
                        gradient=grad,
                    )],
                )
                page.add(topNav)
                page.add(Bg)
                page.show_dialog(dia)
        else:
            r=client.main(f"login",username=f"{user}",passwd=f"{passwd}")
            if r["result"]=="correct!":
                userName=user
                user=userName
                with open("token.pkl", "wb") as f:
                    pickle.dump(r["token"], f)
                logged=True
                t.value=f"Hello, {userName}"
                inventoryBox=ft.Container(height=300, width=300, shadow=boxShadow)
                moneybox=ft.Container(height=300, width=300, margin=ft.Margin.all(10), padding=ft.Padding.all(25), border_radius=ft.BorderRadius.all(25), bgcolor=ft.Colors.GREY_900, animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT), shadow=boxShadow, alignment=ft.Alignment(-0.9,-0.8))
                recipebox=ft.Container(height=300, width=300, margin=ft.Margin.all(10), padding=ft.Padding.all(25), border_radius=ft.BorderRadius.all(25), bgcolor=ft.Colors.GREY_900, animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT), shadow=boxShadow, alignment=ft.Alignment(-0.9,-0.8))
                everything.content=ft.Row([inventoryBox, moneybox, recipebox])
                everything.alignment=ft.Alignment.TOP_LEFT
                everything.update()
                for i in invenBox.keys():
                    try:
                        j=invenBox[i].keys()
                    except:
                        inventoryList.append(ft.Text(value=f"{i}: {invenBox[i]}"))
                    else:
                        for x in j:
                            inventoryList.append(ft.Text(value=f"{x}: {invenBox[i][x]}"))
                inventoryBox.controls=inventoryList
                moneybox.content=ft.Text(value=f"Money: {money}")
                inventoryBox.update()
                everything.update()
                page.update()
                t1.start()
    def defineClosedOrOpen(l):
        if t1.is_alive():
            closeConn(l)
        else:
            delete(l)
    def closeConn(l):
        logged=False
        stop_event.set()
        t1.join()
        print("stopped")
        delete(l)
    def openInventory():
        global inventoryBoxExp
        if not inventoryBoxExp:
            inventoryBoxExp=True
            getInven()
            inventoryBox.width=widthscr-20
            inventoryBox.height=600
            inventoryBox.padding=ft.Padding.all(0)
            inventoryBox.alignment=ft.Alignment.TOP_CENTER
            inventoryBox.scroll=ft.ScrollMode.HIDDEN
            moneybox.opacity=0
            recipebox.opacity=0
            getInven()
        else:
            inventoryBoxExp=False
            getInven()
            moneybox.opacity=1
            recipebox.opacity=1
            inventoryBox.width=300
            inventoryBox.height=300
            inventoryBox.alignment=ft.Alignment.TOP_LEFT
            inventoryBox.scroll=ft.ScrollMode.HIDDEN
    def openRecipes():
        global recipeBoxExp
        if not recipeBoxExp:
            recipeBoxExp=True
            getInven()
            recipebox.margin=ft.Margin.only(left=0)
            recipebox.padding=ft.Padding.all(0)
            recipebox.width=widthscr-40
            recipebox.height=600
            recipebox.padding=ft.Padding.all(0)
            recipebox.alignment=ft.Alignment.TOP_CENTER
            recipebox.scroll=ft.ScrollMode.HIDDEN
            inventoryBox.margin=ft.Margin.only(left=0)
            inventoryBox.padding=ft.Padding.all(0)
            moneybox.margin=ft.Margin.only(left=0)
            moneybox.padding=ft.Padding.all(0)
            inventoryBox.opacity=0
            inventoryBox.width=0
            moneybox.opacity=0
            moneybox.width=0
            getInven()
        else:
            recipeBoxExp=False
            getInven()
            inventoryBox.opacity=1
            inventoryBox.width=300
            recipebox.margin=ft.Margin.only(left=10)
            inventoryBox.margin=ft.Margin.only(left=10)
            inventoryBox.padding=ft.Padding.all(7.5)
            moneybox.margin=ft.Margin.only(left=10)
            moneybox.padding=ft.Padding.all(7.5)
            moneybox.opacity=1
            recipebox.padding=ft.Padding.all(7.5)
            moneybox.width=300
            recipebox.width=300
            recipebox.height=300
            recipebox.alignment=ft.Alignment.TOP_LEFT
            recipebox.scroll=ft.ScrollMode.HIDDEN
            getInven()
    async def handle_scroll(e):
        inventoryExpRow.scroll_to(delta=e.control.max_scroll_extent.y/2, duration=100)
        print("scrolled")
        inventoryBox.update()
        inventoryExpRow.update()
        everything.update()
        page.update()
    def hoverEventContainer(e):
        e.control.bgcolor=ft.Colors.GREY_700 if e.data else ft.Colors.GREY_800
        e.control.update()
        page.update()
    def itemExpand(e):
        global itemExpanded
        global itemExpandedName
        if not itemExpanded:
            itemExpanded=True
            e.control.adaptive=True
            e.control.on_hover=None
            e.control.bgcolor=ft.Colors.GREY_800
            inventoryBox.on_click=None
            itemExpandedName=e.control
            itemExpandedName.text_align=ft.Alignment.CENTER
            itemExpandedName.alignment=ft.Alignment.TOP_CENTER
            itemExpandedName.width=widthscr-50
            itemExpandedName.height=550
            itemExpandedName.update()
            everything.update()
            e.control.update()
            getInven(itemCont=e.control)
            print(f"Item Clicked: {e.control}")
            page.update()
        else:
            inventoryBox.on_click=lambda s: openInventory()
            e.control.width=300
            e.control.height=300
            itemExpanded=False
            e.control.update()
            getInven()
            page.update()

    def recipeExpand(e):
        global recipeExpanded
        global recipeExpandedName
        if not recipeExpanded:
            recipeExpanded=True
            e.control.adaptive=True
            e.control.on_hover=None
            e.control.bgcolor=ft.Colors.GREY_800
            recipebox.on_click=None
            recipeExpandedName=e.control
            recipeExpandedName.text_align=ft.Alignment.CENTER
            recipeExpandedName.alignment=ft.Alignment.TOP_CENTER
            recipeExpandedName.width=widthscr-50
            recipeExpandedName.height=550
            recipeExpandedName.update()
            everything.update()
            e.control.update()
            getInven(recipeCont=e.control)
            print(f"Item Clicked: {e.control}")
            page.update()
        else:
            recipebox.on_click=lambda s: openRecipes()
            e.control.width=300
            e.control.height=300
            recipeExpanded=False
            e.control.update()
            getInven()
            page.update()

    def getInven(itemCont=None, recipeCont=None):
        #SELL FUNCTIONS
        def sell(itemName, amount, password, itemsub=""):
            loadingAnim=ft.ProgressRing(visible=True, height=10, width=10, stroke_width=1.5)
            selldia.content=ft.Container(content=ft.Row(controls=[ft.Text("Selling..."), loadingAnim], height=50))
            q=client.main(msg="sell", passwd=password, amount=amount, materialName=itemName, materialSubtype=itemsub)
            page.update()
            if q["result"]=="Success":
                selldia.content=ft.Text("Sold Successfully!\nPress anywhere to dismiss", color=ft.Colors.BLACK)
            elif q["result"]=="Not Sufficient Quantity":
                selldia.content=ft.Text("Insufficient Quantity!\nPress anywhere to dismiss",color=ft.Colors.BLACK)
            elif q["result"]=="Incorrect Password":
                selldia.content=ft.Text("Password Incorrect!\nPress anywhere to dismiss", color=ft.Colors.BLACK)
            page.update()
        def sellfunc(itemName, itemsub=""):
            global selldia
            if itemsub=="":
                amountField = ft.TextField(
                    label="Amount",
                    value=0,
                    keyboard_type=ft.KeyboardType.NUMBER,  # Opens number pad on mobile
                    input_filter=ft.InputFilter(
                        allow=True, 
                        regex_string=r"^[0-9]*$",            # Allows only digits
                        replacement_string=""
                    )
                )
                moneyCounter=ft.Text(f"Current Balance: {moneyBal}", color=ft.Colors.BLACK)
                password=ft.TextField(label="Password", width=500, password=True, can_reveal_password=True)
                sellButton=ft.FloatingActionButton(content="Sell", on_click=lambda x:sell(itemName, amountField.value, password.value), bgcolor=ft.Colors.GREEN, height=50, width=100)
                selldia=ft.AlertDialog(
                    title=ft.Text(f"Selling {itemName.capitalize()}"),
                    content=ft.Column(
                        controls=[
                            moneyCounter,
                            amountField,
                            password,
                            sellButton
                        ],
                        height=200
                    ),
                    bgcolor=ft.Colors.GREEN_100,
                    on_dismiss=lambda e:getInven(itemExpandedName)
                )
                page.show_dialog(selldia)
                page.update()
            else:
                amountField = ft.TextField(
                    label="Amount",
                    value=0,
                    keyboard_type=ft.KeyboardType.NUMBER,  # Opens number pad on mobile
                    input_filter=ft.InputFilter(
                        allow=True, 
                        regex_string=r"^[0-9]*$",            # Allows only digits
                        replacement_string=""
                    )
                )
                moneyCounter=ft.Text(f"Current Balance: {moneyBal}", color=ft.Colors.BLACK)
                password=ft.TextField(label="Password", width=500, password=True, can_reveal_password=True)
                sellButton=ft.FloatingActionButton(content="Sell", on_click=lambda x:sell(itemName, amountField.value, password.value, itemsub=itemsub), bgcolor=ft.Colors.GREEN, height=50, width=100)
                selldia=ft.AlertDialog(
                    title=ft.Text(f"Selling {itemName.capitalize()}: {itemsub.capitalize()}"),
                    content=ft.Column(
                        controls=[
                            moneyCounter,
                            amountField,
                            password,
                            sellButton
                        ],
                        height=200
                    ),
                    on_dismiss=lambda e:getInven(itemExpandedName)
                )
                page.show_dialog(selldia)
                page.update()
        
        def sellrecipe(itemName, amount, password, itemsub=""):
            loadingAnim=ft.ProgressRing(visible=True, height=10, width=10, stroke_width=1.5)
            sellrecdia.content=ft.Container(content=ft.Row(controls=[ft.Text("Selling..."), loadingAnim], height=50))
            q=client.main(msg="sellrec", passwd=password, amount=amount, materialName=itemName, materialSubtype=itemsub)
            print(q)
            page.update()
            if q["result"]=="Success":
                sellrecdia.content=ft.Text("Sold Successfully!\nPress anywhere to dismiss", color=ft.Colors.BLACK)
            elif q["result"]=="Not Sufficient Quantity":
                sellrecdia.content=ft.Text("Insufficient Quantity!\nPress anywhere to dismiss",color=ft.Colors.BLACK)
            elif q["result"]=="Incorrect Password":
                sellrecdia.content=ft.Text("Password Incorrect!\nPress anywhere to dismiss", color=ft.Colors.BLACK)
            page.update()
        
        def sellrecipefunc(itemName, itemsub=""):
            global sellrecdia
            if itemsub=="":
                amountField = ft.TextField(
                    label="Amount",
                    value=0,
                    keyboard_type=ft.KeyboardType.NUMBER,  # Opens number pad on mobile
                    input_filter=ft.InputFilter(
                        allow=True, 
                        regex_string=r"^[0-9]*$",            # Allows only digits
                        replacement_string=""
                    )
                )
                moneyCounter=ft.Text(f"Current Balance: {moneyBal}", color=ft.Colors.BLACK)
                password=ft.TextField(label="Password", width=500, password=True, can_reveal_password=True)
                sellButton=ft.FloatingActionButton(content="Sell", on_click=lambda x:sellrecipe(itemName, amountField.value, password.value), bgcolor=ft.Colors.GREEN, height=50, width=100)
                sellrecdia=ft.AlertDialog(
                    title=ft.Text(f"Selling {itemName.capitalize()}"),
                    content=ft.Column(
                        controls=[
                            moneyCounter,
                            amountField,
                            password,
                            sellButton
                        ],
                        height=200
                    ),
                    on_dismiss=lambda e:getInven(itemExpandedName)
                )
                page.show_dialog(sellrecdia)
                page.update()
            else:
                amountField = ft.TextField(
                    label="Amount",
                    value=0,
                    keyboard_type=ft.KeyboardType.NUMBER,  # Opens number pad on mobile
                    input_filter=ft.InputFilter(
                        allow=True, 
                        regex_string=r"^[0-9]*$",            # Allows only digits
                        replacement_string=""
                    )
                )
                moneyCounter=ft.Text(f"Current Balance: {moneyBal}", color=ft.Colors.BLACK)
                password=ft.TextField(label="Password", width=500, password=True, can_reveal_password=True)
                sellButton=ft.FloatingActionButton(content="Sell", on_click=lambda x:sell(itemName, amountField.value, password.value, itemsub=itemsub), bgcolor=ft.Colors.GREEN, height=50, width=100)
                sellrecdia=ft.AlertDialog(
                    title=ft.Text(f"Selling {itemName.capitalize()}: {itemsub.capitalize()}"),
                    content=ft.Column(
                        controls=[
                            moneyCounter,
                            amountField,
                            password,
                            sellButton
                        ],
                        height=200
                    ),
                    on_dismiss=lambda e:getInven(itemExpandedName)
                )
                page.show_dialog(sellrecdia)
                page.update()
        
        def craft(itemName, amount, password, itemsub=""):
            loadingAnim=ft.ProgressRing(visible=True, height=10, width=10, stroke_width=1.5)
            craftdia.content=ft.Container(content=ft.Row(controls=[ft.Text("Crafting..."), loadingAnim], height=50))
            q=client.main(msg="craft", passwd=password, amount=amount, materialName=itemName, materialSubtype=itemsub)
            page.update()
            if q["result"]=="Success":
                craftdia.content=ft.Text("Crafting Successful!\nPress anywhere to dismiss", color=ft.Colors.BLACK)
            elif q["result"]=="Not Sufficient Funds":
                craftdia.content=ft.Text("Insufficient Balance!\nPress anywhere to dismiss",color=ft.Colors.BLACK)
            elif q["result"]=="Incorrect Password":
                craftdia.content=ft.Text("Password Incorrect!\nPress anywhere to dismiss", color=ft.Colors.BLACK)
            elif q["result"]=="Not Sufficient Materials":
                craftdia.content(ft.Text("You have insufficient amount of raw materials\nPress anywhere to dismiss", color=ft.Colors.BLACK))
            page.update()
        def craftrecipefunc(itemName, itemsub=""):
            global craftdia
            if itemsub=="":
                amountField = ft.TextField(
                    label="Amount",
                    value=0,
                    keyboard_type=ft.KeyboardType.NUMBER,  # Opens number pad on mobile
                    input_filter=ft.InputFilter(
                        allow=True, 
                        regex_string=r"^[0-9]*$",            # Allows only digits
                        replacement_string=""
                    )
                )
                moneyCounter=ft.Text(f"Current Balance: {moneyBal}", color=ft.Colors.BLACK)
                password=ft.TextField(label="Password", width=500, password=True, can_reveal_password=True)
                craftButton=ft.FloatingActionButton(content="Craft", on_click=lambda x:craft(itemName, amountField.value, password.value), bgcolor=ft.Colors.RED, height=50, width=100)
                craftdia=ft.AlertDialog(
                    title=ft.Text(f"Crafting {itemName.capitalize()}"),
                    content=ft.Column(
                     
                     controls=[
                            moneyCounter,
                            amountField,
                            password,
                            craftButton
                        ],
                        height=200
                    ),
                    on_dismiss=lambda e:getInven(recipeCont=recipeExpandedName)
                )
                page.show_dialog(craftdia)
            else:
                amountField = ft.TextField(
                    label="Amount",
                    value=0,
                    keyboard_type=ft.KeyboardType.NUMBER,  # Opens number pad on mobile
                    input_filter=ft.InputFilter(
                        allow=True, 
                        regex_string=r"^[0-9]*$",            # Allows only digits
                        replacement_string=""
                    )
                )
                moneyCounter=ft.Text(f"Current Balance: {moneyBal}", color=ft.Colors.BLACK)
                password=ft.TextField(label="Password", width=500, password=True, can_reveal_password=True)
                craftButton=ft.FloatingActionButton(content="Craft", on_click=lambda x:craft(itemName, amountField.value, password.value, itemsub=itemsub), bgcolor=ft.Colors.RED, height=50, width=100)
                craftdia=ft.AlertDialog(
                    title=ft.Text(f"Crafting {itemName.capitalize()}: {itemsub.capitalize()}"),
                    content=ft.Column(
                        controls=[
                            moneyCounter,
                            amountField,
                            password,
                            craftButton
                        ],
                        height=200
                    ),
                    on_dismiss=lambda e:getInven(recipeCont=recipeExpandedName)
                )
                page.show_dialog(craftdia)
                
        #BUY FUNCTIONS
        def buy(itemName, amount, password, itemsub=""):
            loadingAnim=ft.ProgressRing(visible=True, height=10, width=10, stroke_width=1.5)
            buydia.content=ft.Container(content=ft.Row(controls=[ft.Text("Purchasing..."), loadingAnim], height=50))
            q=client.main(msg="buy", passwd=password, amount=amount, materialName=itemName, materialSubtype=itemsub)
            page.update()
            if q["result"]=="Success":
                buydia.content=ft.Text("Purchase Successful!\nPress anywhere to dismiss", color=ft.Colors.BLACK)
            elif q["result"]=="Not Sufficient Funds":
                buydia.content=ft.Text("Insufficient Balance!\nPress anywhere to dismiss",color=ft.Colors.BLACK)
            elif q["result"]=="Incorrect Password":
                buydia.content=ft.Text("Password Incorrect!\nPress anywhere to dismiss", color=ft.Colors.BLACK)
            page.update()
        def buyfunc(itemName, itemsub=""):
            global buydia
            if itemsub=="":
                amountField = ft.TextField(
                    label="Amount",
                    value=0,
                    keyboard_type=ft.KeyboardType.NUMBER,  # Opens number pad on mobile
                    input_filter=ft.InputFilter(
                        allow=True, 
                        regex_string=r"^[0-9]*$",            # Allows only digits
                        replacement_string=""
                    )
                )
                moneyCounter=ft.Text(f"Current Balance: {moneyBal}", color=ft.Colors.BLACK)
                password=ft.TextField(label="Password", width=500, password=True, can_reveal_password=True)
                buyButton=ft.FloatingActionButton(content="Buy", on_click=lambda x:buy(itemName, amountField.value, password.value), bgcolor=ft.Colors.RED, height=50, width=100)
                buydia=ft.AlertDialog(
                    title=ft.Text(f"Buying {itemName.capitalize()}"),
                    content=ft.Column(
                     
                     controls=[
                            moneyCounter,
                            amountField,
                            password,
                            buyButton
                        ],
                        height=200
                    ),
                    on_dismiss=lambda e:getInven(itemExpandedName)
                )
                page.show_dialog(buydia)
            else:
                amountField = ft.TextField(
                    label="Amount",
                    value=0,
                    keyboard_type=ft.KeyboardType.NUMBER,  # Opens number pad on mobile
                    input_filter=ft.InputFilter(
                        allow=True, 
                        regex_string=r"^[0-9]*$",            # Allows only digits
                        replacement_string=""
                    )
                )
                moneyCounter=ft.Text(f"Current Balance: {moneyBal}", color=ft.Colors.BLACK)
                password=ft.TextField(label="Password", width=500, password=True, can_reveal_password=True)
                buyButton=ft.FloatingActionButton(content="Buy", on_click=lambda x:buy(itemName, amountField.value, password.value, itemsub=itemsub), bgcolor=ft.Colors.RED, height=50, width=100)
                buydia=ft.AlertDialog(
                    title=ft.Text(f"Buying {itemName.capitalize()}: {itemsub.capitalize()}"),
                    content=ft.Column(
                        controls=[
                            moneyCounter,
                            amountField,
                            password,
                            buyButton
                        ],
                        height=200
                    ),
                    on_dismiss=lambda e:getInven(itemExpandedName)
                )
                page.show_dialog(buydia)
        
        #MAIN START
        if logged==False:
            return
        else:
            print("updated")
            if not inventoryBoxExp and not recipeBoxExp:
                log=client.main(f"info")
                money=log["info"].pop("money")
                recipeContent=log["info"].pop("recipes")
                group=log['info'].pop("group")
                invenBox=log["info"]
                inventoryList.clear()
                recipeList.clear()
                for i in invenBox.keys():
                    try:
                        j=invenBox[i].keys()
                    except:
                        inventoryList.append(ft.Text(value=f"{i.capitalize()}: {invenBox[i]}"))
                    else:
                        inventoryList.append(ft.Text(value=f"{i.capitalize()}:"))
                        for x in j:
                            inventoryList.append(ft.Text(value=f"   {x.capitalize()}: {invenBox[i][x]}"))
                for b in recipeContent.keys():
                    try:
                        recipeKeys=recipeContent[b].keys()
                    except:
                        recipeList.append(ft.Text(value=f"{b.capitalize()}: {recipeContent[b]}"))
                    else:
                        recipeList.append(ft.Text(f"{b.capitalize()}"))
                        for individualRecipeKey in recipeKeys:
                            recipeList.append(ft.Text(f"    {individualRecipeKey.capitalize()}: {recipeContent[b][individualRecipeKey]}"))
                #INVENTORY BOX SETTINGS
                inventoryBox.content=(ft.Column([ft.Container(content=ft.Text(value=f"Raw Materials:", size=25), padding=ft.Padding.all(10), bgcolor="#4A009E", border_radius=ft.BorderRadius.all(15)), ft.Column(controls=inventoryList, scroll=ft.ScrollMode.HIDDEN)],scroll=ft.ScrollMode.HIDDEN))
                inventoryBox.border_radius=ft.BorderRadius.all(13)
                inventoryBox.on_click=lambda s: openInventory()
                inventoryBox.margin=ft.Margin.only(left=10)
                inventoryBox.padding=ft.Padding.all(7.5)
                inventoryBox.bgcolor=ft.Colors.GREY_900
                inventoryBox.scroll=ft.ScrollMode.HIDDEN
                inventoryBox.animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
                inventoryBox.adaptive=True
                
                #MONEY BOX SETTINGs
                moneybox.margin=ft.Margin.only(left=10)
                moneybox.border_radius=ft.BorderRadius.all(13)
                moneybox.padding=ft.Padding.all(7.5)
                moneybox.alignment=ft.Alignment.TOP_CENTER
                moneybox.content=ft.Container(content=ft.Column([ft.Text(value=f"Money: {money}", size=20), ft.Text(value=f"Group: {group}", size=20)], width=600, expand=False, horizontal_alignment=ft.CrossAxisAlignment.CENTER), padding=ft.Padding.all(10), bgcolor="#4A009E", border_radius=ft.BorderRadius.all(15), height=100)
                moneybox.animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
                
                #RECIPE BOX SETTINGS
                recipebox.content=ft.Column([ft.Container(content=ft.Text(value=f"Recipes:", size=25), padding=ft.Padding.all(10), bgcolor="#4A009E", border_radius=ft.BorderRadius.all(15)), ft.Column(controls=recipeList, scroll=ft.ScrollMode.HIDDEN)])
                recipebox.border_radius=ft.BorderRadius.all(13)
                recipebox.on_click=lambda s: openRecipes()
                recipebox.margin=ft.Margin.only(left=10)
                recipebox.padding=ft.Padding.all(7.5)
                recipebox.bgcolor=ft.Colors.GREY_900
                recipebox.scroll=ft.ScrollMode.HIDDEN
                recipebox.animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
                recipebox.adaptive=True
                
                everything.alignment=ft.Alignment(-0.9,-0.9)
                page.update()
            elif recipeBoxExp and not recipeExpanded and not inventoryBoxExp:
                global recipeExpRow
                log=client.main(f"info")
                money=log["info"].pop("money")
                group=log['info'].pop("group")
                recipeContent=log["info"].pop("recipes")
                craftPrices=client.main("craftPrices")
                print(craftPrices)
                sellRecipePrices=client.main("sellRecipePrices")
                invenBox=log["info"]
                inventoryList.clear()
                recipeList.clear()
                for i in recipeContent.keys():
                    try:
                        j=recipeContent[i].keys()
                    except:
                        recipeContainers[i]=ft.Container(content=ft.Column(controls=[
                            ft.Container(content=ft.Image(src="icon.png", width=65, height=65), border_radius=ft.BorderRadius.all(15)),
                            ft.Text(value=f"{i.capitalize()}: {recipeContent[i]}\n", text_align=ft.Alignment.CENTER, size=13),
                            ft.Text(value=f"Crafting Price: {craftPrices[i]}", text_align=ft.Alignment.CENTER, color=ft.Colors.RED, size=13),
                            ft.Text(value=f"Sell Price: {sellRecipePrices[i]}", text_align=ft.Alignment.CENTER, color=ft.Colors.GREEN, size=13)
                            ], spacing=5),
                            bgcolor=ft.Colors.GREY_800,
                            border_radius=ft.BorderRadius.all(15), 
                            height=200, width=200, 
                            alignment=ft.Alignment.CENTER,
                            padding=ft.Padding.all(10), 
                            on_hover=hoverEventContainer, 
                            on_click=recipeExpand,
                            animate=ft.Animation(600, ft.AnimationCurve.BOUNCE_OUT)
                            )
                        recipeList.append(recipeContainers[i])
                    else:
                        recipeContainers[i]={}
                        totalcount=0
                        for x in j:
                            totalcount+=recipeContent[i][x]
                        for x in j:
                            recipeContainers[i][x]=ft.Container(content=ft.Column(controls=[
                                ft.Container(content=ft.Image(src="icon.png", width=65, height=65), border_radius=ft.BorderRadius.all(15)),
                                ft.Text(value=f"{i.capitalize()}: {totalcount}\n{x.capitalize()}: {recipeContent[i][x]}", text_align=ft.Alignment.CENTER, size=13),
                                ft.Text(value=f"Crafting Price: {craftPrices[i][x]}", text_align=ft.Alignment.CENTER, color=ft.Colors.RED, size=13),
                                ft.Text(value=f"Sell Price: {sellRecipePrices[i][x]}", text_align=ft.Alignment.CENTER, color=ft.Colors.GREEN, size=13)], spacing=5),
                                bgcolor=ft.Colors.GREY_800,
                                border_radius=ft.BorderRadius.all(15), 
                                height=200, 
                                width=200, 
                                alignment=ft.Alignment.CENTER, 
                                padding=ft.Padding.all(10), 
                                on_hover=hoverEventContainer,
                                on_click=recipeExpand,
                                animate=ft.Animation(600, ft.AnimationCurve.BOUNCE_OUT)
                                )
                            recipeList.append(recipeContainers[i][x])
                recipeExpRow=ft.Row(controls=recipeList, scroll=ft.ScrollMode.ALWAYS)
                recipebox.content=ft.Container(content=recipeExpRow)
                recipebox.border_radius=ft.BorderRadius.all(5)
                moneybox.border_radius=ft.BorderRadius.all(5)
                recipebox.on_click=lambda s: openRecipes()
                recipebox.padding=ft.Padding.all(7.5)
                recipebox.bgcolor=ft.Colors.GREY_900
                recipebox.alignment=ft.Alignment.CENTER
                recipebox.scroll=ft.ScrollMode.HIDDEN
                recipebox.animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
                recipebox.adaptive=True
                moneybox.content=ft.Column([ft.Text(value=f"Money: {money}"), ft.Text(value=f"Group: {group}")])
                moneybox.animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
                everything.alignment=ft.Alignment.TOP_LEFT
                everything.update()
                moneybox.update()
                page.update()
            elif inventoryBoxExp and not itemExpanded and not recipeExpanded:
                print("Item Not Expanded")
                global inventoryExpRow
                log=client.main(f"info")
                money=log["info"].pop("money")
                group=log['info'].pop("group")
                recipeContent=log["info"].pop("recipes")
                buyPrices=client.main("buyPrices")
                sellPrices=client.main("sellPrices")
                invenBox=log["info"]
                inventoryList.clear()
                for i in invenBox.keys():
                    try:
                        j=invenBox[i].keys()
                    except:
                        itemContainers[i]=ft.Container(content=ft.Column(controls=[
                            ft.Container(content=ft.Image(src="icon.png", width=65, height=65), border_radius=ft.BorderRadius.all(15)),
                            ft.Text(value=f"{i.capitalize()}: {invenBox[i]}\n", text_align=ft.Alignment.CENTER, size=13),
                            ft.Text(value=f"Buy Price: {buyPrices[i]}", text_align=ft.Alignment.CENTER, color=ft.Colors.RED, size=13),
                            ft.Text(value=f"Sell Price: {sellPrices[i]}", text_align=ft.Alignment.CENTER, color=ft.Colors.GREEN, size=13)
                            ], spacing=5),
                            bgcolor=ft.Colors.GREY_800,
                            border_radius=ft.BorderRadius.all(15), 
                            height=200, width=200, 
                            alignment=ft.Alignment.CENTER, 
                            padding=ft.Padding.all(10), 
                            on_hover=hoverEventContainer, 
                            on_click=itemExpand,
                            animate=ft.Animation(600, ft.AnimationCurve.BOUNCE_OUT)
                            )
                        inventoryList.append(itemContainers[i])
                    else:
                        itemContainers[i]={}
                        totalcount=0
                        for x in j:
                            totalcount+=invenBox[i][x]
                        for x in j:
                            itemContainers[i][x]=ft.Container(content=ft.Column(controls=[
                                ft.Container(content=ft.Image(src="icon.png", width=65, height=65), border_radius=ft.BorderRadius.all(15)),
                                ft.Text(value=f"{i.capitalize()}: {totalcount}\n{x.capitalize()}: {invenBox[i][x]}", text_align=ft.Alignment.CENTER, size=13),
                                ft.Text(value=f"Buy Price: {buyPrices[i][x]}", text_align=ft.Alignment.CENTER, color=ft.Colors.RED, size=13),
                                ft.Text(value=f"Sell Price: {sellPrices[i][x]}", text_align=ft.Alignment.CENTER, color=ft.Colors.GREEN, size=13)], spacing=5),
                                bgcolor=ft.Colors.GREY_800,
                                border_radius=ft.BorderRadius.all(15), 
                                height=200, 
                                width=200, 
                                alignment=ft.Alignment.CENTER, 
                                padding=ft.Padding.all(10), 
                                on_hover=hoverEventContainer,
                                on_click=itemExpand,
                                animate=ft.Animation(600, ft.AnimationCurve.BOUNCE_OUT)
                                )
                            inventoryList.append(itemContainers[i][x])
                inventoryExpRow=ft.Row(controls=inventoryList, scroll=ft.ScrollMode.ALWAYS)
                inventoryBox.content=ft.Container(content=inventoryExpRow)
                inventoryBox.border_radius=ft.BorderRadius.all(5)
                moneybox.border_radius=ft.BorderRadius.all(5)
                inventoryBox.on_click=lambda s: openInventory()
                inventoryBox.margin=ft.Margin.only(left=10)
                inventoryBox.padding=ft.Padding.all(7.5)
                inventoryBox.bgcolor=ft.Colors.GREY_900
                inventoryBox.alignment=ft.Alignment.CENTER
                moneybox.margin=ft.Margin.only(left=10)
                moneybox.padding=ft.Padding.all(7.5)
                inventoryBox.scroll=ft.ScrollMode.HIDDEN
                inventoryBox.animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
                inventoryBox.adaptive=True
                moneybox.content=ft.Column([ft.Text(value=f"Money: {money}"), ft.Text(value=f"Group: {group}")])
                moneybox.animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
                everything.alignment=ft.Alignment.TOP_LEFT
                everything.update()
                moneybox.update()
                page.update()
            elif recipeBoxExp and recipeExpanded:
                global moneyBal
                print("Recipe Expanded")
                log=client.main(f"info")
                moneyBal=log["info"].pop("money")
                group=log['info'].pop("group")
                recipeContent=log["info"].pop("recipes")
                craftPrices=client.main("craftPrices")
                sellRecipePrices=client.main("sellRecipePrices")
                invenBox=log["info"]
                recipebox.content=ft.Container(content=recipeCont)
                print(f"To Find: {itemCont}")
                for d in recipeContainers.keys():
                    try:
                        h=recipeContainers[d].keys()
                    except:
                        if recipeContainers[d]==recipeCont:
                            recName=d
                            print(f"ItemExpandedName: {recName}, ID: {recipeContainers[d]}")
                            recipeCont.content=ft.Container(ft.Row(controls=[ft.Column(controls=[
                                ft.Container(content=ft.Image(src="wood.png", width=250, height=250), border_radius=ft.BorderRadius.all(15)),
                                ft.Container(content=ft.Column(controls=[ft.Text(value=f"{d.capitalize()}:\n{recipeContent[d]}", size=13, text_align=ft.TextAlign.CENTER)]), bgcolor=ft.Colors.DEEP_PURPLE, padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(10), width=100, alignment=ft.Alignment.CENTER),
                                ft.Container(),
                                ft.Row(controls=[ft.Container(content=ft.Text(value=f"Craft Price: {craftPrices[d]}", text_align=ft.Alignment.CENTER), padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(15), bgcolor=ft.Colors.RED_700),
                                ft.Container(content=ft.Text(value=f"Sell Price: {sellRecipePrices[d]}", text_align=ft.Alignment.CENTER), padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(15), bgcolor=ft.Colors.GREEN_700)]),
                                ft.Row(controls=[ft.FloatingActionButton(content="Craft", on_click=lambda x:craftrecipefunc(recName), bgcolor=ft.Colors.RED, height=50, width=100), ft.FloatingActionButton(content="Sell", on_click=lambda x:sellrecipefunc(recName), bgcolor=ft.Colors.GREEN, height=50, width=100)])], horizontal_alignment=ft.CrossAxisAlignment.CENTER)], 
                                alignment=ft.MainAxisAlignment.CENTER), width=250, height=500)
                            recipeCont.alignment=ft.Alignment.CENTER
                            recipeContainers[d]=recipeCont
                            recipeCont.update()
                            page.update()
                        else:
                            print(f"Not Found, Continuing Item Name, current: {d}, container ID: {recipeContainers[d]}")
                            continue
                    else:
                        for u in h:
                            if recipeContainers[d][u]==recipeCont:
                                recName=d
                                recSub=u
                                print(f"ItemExpandedName: {recName}:{recSub}, ID: {recipeContainers[d][u]}")
                                recipeCont.content=ft.Container(ft.Row(controls=[ft.Column(controls=[
                                ft.Container(content=ft.Image(src="icon.png", width=250, height=250), border_radius=ft.BorderRadius.all(15)),
                                ft.Container(content=ft.Column(controls=[ft.Text(value=f"{d.capitalize()}:\n{u.capitalize()}:\n{recipeContent[d][u]}", size=13, text_align=ft.TextAlign.CENTER)]), bgcolor=ft.Colors.DEEP_PURPLE, padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(10), width=100, alignment=ft.Alignment.CENTER),
                                ft.Row(controls=[ft.Container(content=ft.Text(value=f"Buy Price: {craftPrices[d][u]}", text_align=ft.Alignment.CENTER), padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(15), bgcolor=ft.Colors.RED_700),
                                ft.Container(content=ft.Text(value=f"Sell Price: {sellRecipePrices[d][u]}", text_align=ft.Alignment.CENTER), padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(15), bgcolor=ft.Colors.GREEN_700)]),
                                ft.Row(controls=[ft.FloatingActionButton(content="Craft", on_click=lambda x:craftrecipefunc(recName,recSub), bgcolor=ft.Colors.RED, height=50, width=100), ft.FloatingActionButton(content="Sell", on_click=lambda x:sellrecipefunc(recName,recSub), bgcolor=ft.Colors.GREEN, height=50, width=100)])], horizontal_alignment=ft.CrossAxisAlignment.CENTER)], alignment=ft.Alignment.CENTER),width=250, height=500)  
                                recipeCont.alignment=ft.Alignment(0,0)
                                recipeContainers[d][u]=itemCont
                                recipeCont.update()
                                page.update()
                            else:
                                print(f"Not Found, Continuing Item SUB, current: {d}: {u}, container ID: {recipeContainers[d][u]}")
                                continue
                print(f"Item Received: {recipeCont}")
                inventoryBox.update()
                everything.update()
                moneybox.update()
                page.update()
            elif inventoryBoxExp and itemExpanded:
                print("Item Expanded")
                log=client.main(f"info")
                moneyBal=log["info"].pop("money")
                group=log['info'].pop("group")
                recipeContent=log["info"].pop("recipes")
                buyPrices=client.main("buyPrices")
                sellPrices=client.main("sellPrices")
                invenBox=log["info"]
                inventoryBox.content=ft.Container(content=itemCont)
                print(f"To Find: {itemCont}")
                for d in itemContainers.keys():
                    try:
                        h=itemContainers[d].keys()
                    except:
                        if itemContainers[d]==itemCont:
                            itName=d
                            print(f"ItemExpandedName: {itName}, ID: {itemContainers[d]}")
                            itemCont.content=ft.Container(ft.Row(controls=[ft.Column(controls=[
                                ft.Container(content=ft.Image(src="wood.png", width=250, height=250), border_radius=ft.BorderRadius.all(15)),
                                ft.Container(content=ft.Column(controls=[ft.Text(value=f"{d.capitalize()}:\n{invenBox[d]}", size=13, text_align=ft.TextAlign.CENTER)]), bgcolor=ft.Colors.DEEP_PURPLE, padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(10), width=100, alignment=ft.Alignment.CENTER),
                                ft.Container(),
                                ft.Row(controls=[ft.Container(content=ft.Text(value=f"Buy Price: {buyPrices[d]}", text_align=ft.Alignment.CENTER), padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(15), bgcolor=ft.Colors.RED_700),
                                ft.Container(content=ft.Text(value=f"Sell Price: {sellPrices[d]}", text_align=ft.Alignment.CENTER), padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(15), bgcolor=ft.Colors.GREEN_700)]),
                                ft.Row(controls=[ft.FloatingActionButton(content="Buy", on_click=lambda x:buyfunc(itName), bgcolor=ft.Colors.RED, height=50, width=100), ft.FloatingActionButton(content="Sell", on_click=lambda x:sellfunc(itName), bgcolor=ft.Colors.GREEN, height=50, width=100)])], horizontal_alignment=ft.CrossAxisAlignment.CENTER)], 
                                alignment=ft.MainAxisAlignment.CENTER), width=250, height=500)
                            itemCont.alignment=ft.Alignment.CENTER
                            itemContainers[d]=itemCont
                            itemCont.update()
                            page.update()
                        else:
                            print(f"Not Found, Continuing Item Name, current: {d}, container ID: {itemContainers[d]}")
                            continue
                    else:
                        for u in h:
                            if itemContainers[d][u]==itemCont:
                                itName=d
                                itSub=u
                                print(f"ItemExpandedName: {itName}:{itSub}, ID: {itemContainers[d][u]}")
                                itemCont.content=ft.Container(ft.Row(controls=[ft.Column(controls=[
                                ft.Container(content=ft.Image(src="icon.png", width=250, height=250), border_radius=ft.BorderRadius.all(15)),
                                ft.Container(content=ft.Column(controls=[ft.Text(value=f"{d.capitalize()}:\n{u.capitalize()}:\n{invenBox[d][u]}", size=13, text_align=ft.TextAlign.CENTER)]), bgcolor=ft.Colors.DEEP_PURPLE, padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(10), width=100, alignment=ft.Alignment.CENTER),
                                ft.Row(controls=[ft.Container(content=ft.Text(value=f"Buy Price: {buyPrices[d][u]}", text_align=ft.Alignment.CENTER), padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(15), bgcolor=ft.Colors.RED_700),
                                ft.Container(content=ft.Text(value=f"Sell Price: {sellPrices[d][u]}", text_align=ft.Alignment.CENTER), padding=ft.Padding.all(15), border_radius=ft.BorderRadius.all(15), bgcolor=ft.Colors.GREEN_700)]),
                                ft.Row(controls=[ft.FloatingActionButton(content="Buy", on_click=lambda x:buyfunc(itName,itSub), bgcolor=ft.Colors.RED, height=50, width=100), ft.FloatingActionButton(content="Sell", on_click=lambda x:sellfunc(itName,itSub), bgcolor=ft.Colors.GREEN, height=50, width=100)])], horizontal_alignment=ft.CrossAxisAlignment.CENTER)], alignment=ft.Alignment.CENTER),width=250, height=500)  
                                itemCont.alignment=ft.Alignment(0,0)
                                itemContainers[d][u]=itemCont
                                itemCont.update()
                                page.update()
                            else:
                                print(f"Not Found, Continuing Item SUB, current: {d}: {u}, container ID: {itemContainers[d][u]}")
                                continue
                print(f"Item Received: {itemCont}")
                itemCont.update()
                inventoryBox.update()
                everything.update()
                moneybox.update()
                page.update()

    async def updateInven(stop_Flag):
        while not stop_Flag.is_set():
            if page.window.visible==False:
                t1.join()
                stop_Flag.set()
                break
            else:
                if itemExpanded:
                    getInven(itemExpandedName)
                elif recipeExpanded:
                    getInven(recipeCont=recipeExpandedName)
                elif not itemExpanded:
                    getInven()
                await asyncio.sleep(5)
    thumb = ft.Container(
        width=handle_size, height=handle_size,
        bgcolor=ft.Colors.PURPLE_ACCENT_700, border_radius=handle_size/2,
        content=ft.Icon(ft.Icons.CHEVRON_RIGHT, color="white"),
    )

    # We use a GestureDetector and update its 'left' property
    slider = ft.GestureDetector(
        content=thumb,
        left=0,
        animate_position=ft.Animation(100, ft.AnimationCurve.EASE),
        on_pan_update=lambda e: handle_move(e),
        on_pan_end=lambda e: handle_release(e),
    )

    def handle_move(e: ft.DragUpdateEvent):
        # VERSION-PROOF DELTA CHECK
        delta = 0
        try:
            if e.delta_x is not None: delta = e.delta_x
        except AttributeError:
            try:
                if e.local_delta.x is not None: delta = e.local_delta.x
            except AttributeError:
                if e.primary_delta is not None: delta = e.primary_delta

        # Apply movement
        new_left = slider.left + delta
        # Lock strictly inside [0, max_x]
        slider.left = max(0, min(new_left, max_x))
        slider.update()

    def handle_release(e: ft.DragEndEvent):
        # Snap or Confirm
        slider.animate_position = ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT)
        
        if slider.left > max_x * 0.95 and test.value!="":# 95% through the bar
            st.alignment=ft.Alignment.CENTER 
            slider.left = max_x
            thumb.bgcolor = ft.Colors.GREEN_700
            thumb.content = ft.Icon(ft.Icons.CHECK, color="white")
            txt.value=""
            track.width=handle_size
            slider.padding=ft.Padding.all(0)
            slider.left=bar_width/2.6
            page.update()
            time.sleep(2)
            login(test.value, Pass.value)
        else:
            slider.left = 0 # Smoothly slides back
            
        slider.update()
        thumb.update()
    def delete(l):
        inventoryBox.controls=[ft.Text(value="Closing...")]
        page.update()
        page.controls.clear()
        page.update()
        page.window.opacity=0
        page.update()
        page.window.visible=False
        page.window.destroy()
        page.update()
        quit(1)
    def minimize(l):
        page.window.minimized=True
        page.update()
    def testAnim(l):
        everything.opacity=0
        everything.update()
        everything.content=ft.FloatingActionButton(text="Login", on_click=lambda x:login(test.value, Pass.value))
        everything.opacity=1
        everything.gradient=grad
        everything.update()
        page.update()
    topNav=ft.ResponsiveRow([
        ft.WindowDragArea(
            ft.Container(
                width=widthscr,
                gradient=ft.LinearGradient(
                    begin=ft.Alignment.TOP_CENTER,
                    end=ft.Alignment.BOTTOM_CENTER,
                    colors=[ft.Colors.BLACK, ft.Colors.BLACK],
                ),
                padding=15,
                content=ft.Column([ft.Row([
                    ft.Image(src="/icon.png", width=75, height=45),
                    ft.Column([t], alignment=ft.Alignment.TOP_LEFT, width=500),
                    ft.Row(width=575),
                    ft.Row([
                    ft.Row(width=10),
                    ft.TextButton(icon=ft.Icons.REMOVE, width=35, height=25, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)), on_click=lambda x: minimize(x)),
                    ft.TextButton(icon=ft.Icons.CLOSE, width=35,height=25, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), overlay_color=ft.Colors.DEEP_ORANGE),on_click=lambda x: defineClosedOrOpen(x)),], 
                    width=200, spacing=0,
                    alignment=ft.Alignment.TOP_CENTER),
                ],
                expand=True)
            ],
            spacing=5)
            )
        ),
    ])
    everything=ft.Container(
        content=ft.ResponsiveRow([
            ft.Container(content=ft.Column([
                test,
                Pass,
                ft.FloatingActionButton(content="Login", on_click=lambda x:login(test.value, Pass.value), bgcolor=ft.Colors.DEEP_PURPLE_ACCENT, width=150, height=50),
            ],
            spacing=10,
            alignment=ft.Alignment.CENTER,
            expand=False,
        ),
        padding=10,
        gradient=grad,
    )],
    ),
    width=widthscr,
    height=page.window.height,
    alignment=ft.Alignment.TOP_CENTER,
    animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
    )
    Bg=ft.Container(content=everything,
    gradient=grad,
    )
    stop_event = Event()
    t1=Thread(target=asyncio.run, args=(updateInven(stop_event),))
    if os.path.exists("token.pkl"):
        login(user="", passwd="")
    else:
        page.add(topNav)
        page.add(Bg)
        page.update()

ft.run(main=main, assets_dir="assets")