import flet as ft
import client
from threading import Thread, Event
import time
import os
import ast
import pickle
import asyncio
import defineContent as contentDefiner

DISCONNECT_MSG="!disconnect"
logged=False
userName=""
inventoryList=[]
inventoryBox=ft.Container()
inventoryBoxExp=False
inventoryRow=ft.Row()
grad=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.Colors.BLACK, ft.Colors.BLACK, ft.Colors.PURPLE_ACCENT_700])
def main(page: ft.Page):
    page.window.width=1280
    page.window.height=720
    page.window.center()
    page.window.frameless=True
    page.window.gradient=grad
    page.border_radius=ft.border_radius.all(20)
    page.window.spacing=0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.spacing=0
    page.window.opacity=1
    page.window.animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_OUT)
    page.padding=0
    page.window.draggable=True
    page.window.resizable=False
    page.window.maximizable=False
    page.update()
    widthscr=page.window.width
    test=ft.TextField(hint_text="Username", width=500)
    Pass=ft.TextField(hint_text="Password", width=500)
    t=ft.Text(value=f"Hello, {userName}", size=15)
    rw=ft.Row(spacing=10)
    invenBox={}
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
        global inventoryRow
        if os.path.exists("token.pkl") and user=="":
            with open("token.pkl", "rb") as f:
                tok=pickle.load(f)
            log=client.main("!connect")
            r=client.main(f"LOGINTOKEN-{tok}-token")
            r=r.split("!")
            if r[0]=="Successfully logged in":
                userName=r[1]
                user=userName
                logged=True
                t.value=f"Hello, {userName}"
                inventoryBox=ft.Container(height=200, width=200)
                inventoryRow=ft.Row(controls=[inventoryBox],alignment=ft.alignment.top_center, width=200)
                inventoryRow.animate_size=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
                everything.content=inventoryRow
                everything.alignment=ft.alignment.top_center
                everything.update()
                for i in invenBox.keys():
                    try:
                        j=invenBox[i].keys()
                    except:
                        inventoryList.append(ft.Container(content=ft.Text(value=f"{i}: {invenBox[i]}"),
                        margin=ft.margin.symmetric(vertical=0.25),
                        width=inventoryBox.width,
                        bgcolor=ft.Colors.PURPLE,
                        padding=ft.padding.symmetric(vertical=15, horizontal=15)))
                    else:
                        for x in j:
                            inventoryList.append(ft.Container(content=ft.Text(value=f"{x}: {invenBox[i][x]}"),
                            margin=ft.margin.symmetric(vertical=0.25),
                            width=inventoryBox.width,
                            bgcolor=ft.Colors.PURPLE,
                            padding=ft.padding.symmetric(vertical=15, horizontal=15)))
                inventoryBox.controls=inventoryList
                inventoryBox.update()
                everything.update()
                page.update()
                t1.start()
        else:
            log=client.main("!connect")
            r=client.main(f"login-{user}-{passwd}")
            r=r.split("!")
            if r[0]=="Successfully logged in":
                logged=True
                os.environ["loggedWW"] = "TRUE"
                os.environ["loggedWWT"] = r[1]
                userName=user
                t.value=f"Hello, {userName}"
                with open("token.pkl", "wb") as f:
                    pickle.dump(r[1], f)
                inventoryBox=ft.Column()
                for i in invenBox.keys():
                    try:
                        j=invenBox[i].keys()
                    except:
                        inventoryList.append(ft.Text(value=f"{i}: {invenBox[i]}", overflow=ft.TextOverflow.ELLIPSIS))
                    else:
                        for x in j:
                            inventoryList.append(ft.Text(value=f"{x}: {invenBox[i][x]}", overflow=ft.TextOverflow.ELLIPSIS))
                inventoryBox.controls=inventoryList
                inventoryBox.update()
                everything.update()
                page.update()
                t1.start()
    async def defineClosedOrOpen(l):
        if t1.is_alive():
            await closeConn(l)
        else:
            await delete(l)
    async def closeConn(l):
        logged=False
        stop_event.set()
        t1.join()
        print("stopped")
        await delete(l)
    async def openInventory():
        global inventoryBoxExp
        if not inventoryBoxExp:
            inventoryRow.width=widthscr
            inventoryRow.alignment=ft.alignment.top_right
            await asyncio.sleep(2)
            inventoryBox.width=widthscr
            inventoryBox.height=600
            inventoryBox.margin=ft.margin.only(left=0)
            inventoryBox.padding=ft.padding.only(left=0)
            inventoryBox.alignment=ft.alignment.top_center
            inventoryBoxExp=True
        else:
            inventoryRow.alignment=ft.alignment.top_center
            inventoryBox.width=200
            inventoryBox.height=200
            inventoryBoxExp=False

    def getInven():
        if logged==False:
            return
        else:
            client.main("!connect")
            print(userName)
            log=client.main(f"user-{userName}")
            s=client.main("show-inven")
            invenBox=ast.literal_eval(s)
            x=client.main(DISCONNECT_MSG)
            inventoryList.clear()
            for i in invenBox.keys():
                try:
                    j=invenBox[i].keys()
                except:
                    inventoryList.append(ft.Container(content=ft.Text(value=f"{i.capitalize()}: {invenBox[i]}"),
                    margin=ft.margin.symmetric(vertical=0.25),
                    width=inventoryBox.width,
                    bgcolor=ft.Colors.PURPLE,
                    padding=ft.padding.symmetric(vertical=15, horizontal=15)))
                else:
                    inventoryList.append(ft.Container(content=ft.Text(value=f"{i.capitalize()}:"),
                    margin=ft.margin.symmetric(vertical=0.25),
                    width=inventoryBox.width,
                    bgcolor=ft.Colors.PURPLE,
                    padding=ft.padding.symmetric(vertical=15, horizontal=15)))
                    for x in j:
                        inventoryList.append(ft.Container(content=ft.Text(value=f"   {x.capitalize()}: {invenBox[i][x]}"),
                        margin=ft.margin.symmetric(vertical=0.25),
                        width=inventoryBox.width,
                        bgcolor=ft.Colors.PURPLE,
                        padding=ft.padding.symmetric(vertical=15, horizontal=15)))
            inventoryBox.content=(ft.Column(controls=inventoryList, scroll=ft.ScrollMode.ALWAYS))
            inventoryBox.border_radius=5
            inventoryBox.spacing=0
            inventoryBox.on_click=lambda s: asyncio.run(openInventory())
            inventoryBox.margin=ft.margin.only(left=10)
            inventoryBox.padding=ft.padding.all(7.5)
            inventoryBox.bgcolor=ft.Colors.GREY_900
            inventoryBox.scroll=ft.ScrollMode.AUTO
            inventoryBox.animate_size=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
            inventoryBox.animate_offset=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
            inventoryBox.adaptive=True
            everything.alignment=ft.alignment.top_left
            everything.update()
            page.update()
    async def updateInven(stop_Flag):
        while not stop_Flag.is_set():
            if page.window.visible==False:
                t1.join()
                stop_Flag.set()
                break
            else:
                getInven()
                await asyncio.sleep(5)
    async def delete(l):
        inventoryBox.controls=[ft.Text(value="Closing...")]
        page.update()
        await asyncio.sleep(1)
        page.controls.clear()
        page.update()
        await asyncio.sleep(1)
        page.window.opacity=0
        page.update()
        page.window.visible=False
        await asyncio.sleep(2)
        page.window.destroy()
        page.update()
        await asyncio.sleep(20)
        exit(1)
    def minimize(l):
        page.window.minimized=True
        page.update()
    async def testAnim(l):
        everything.opacity=0
        everything.update()
        await asyncio.sleep(1)
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
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[ft.Colors.BLACK, ft.Colors.BLACK],
                ),
                padding=15,
                content=ft.Column([ft.Row([
                    ft.Column([t], alignment=ft.alignment.top_left, width=500),
                    ft.Row(width=565),
                    ft.Row([ft.TextButton(text="INVENTORY", on_click=lambda x:getInven()),
                    ft.Row(width=10),
                    ft.TextButton(icon=ft.Icons.REMOVE, width=35, height=25, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)), on_click=lambda x: minimize(x)),
                    ft.TextButton(icon=ft.Icons.CLOSE, width=35,height=25, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), overlay_color=ft.Colors.DEEP_ORANGE),on_click=lambda x: asyncio.run(defineClosedOrOpen(x))),], 
                    width=200, spacing=0,
                    alignment=ft.alignment.top_center),
                ],
                expand=True)
            ],
            spacing=5)
            )
        ),
    ])
    page.add(topNav)
    everything=ft.Container(
        content=ft.ResponsiveRow([
            ft.Container(content=ft.Column([
                test,
                Pass,
                ft.FloatingActionButton(text="500", on_click=lambda x: changeWidth(500)),
                ft.FloatingActionButton(text="Login", on_click=lambda x:login(test.value, Pass.value)),
                ft.FloatingActionButton(text="testAnim", on_click=testAnim),
                ft.OutlinedButton(text="Check", on_click=lambda x: contentDefiner.checkLog()),
            ],
            spacing=10,
            alignment=ft.alignment.center,
            expand=False,
        ),
        padding=10,
        gradient=grad,
    )],
    ),
    width=widthscr,
    height=page.window.height,
    alignment=ft.alignment.top_center,
    animate_opacity=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
    )
    Bg=ft.Container(content=everything,
    gradient=grad,
    )
    page.add(Bg)
    stop_event = Event()
    t1=Thread(target=asyncio.run, args=(updateInven(stop_event),))

ft.app(main)