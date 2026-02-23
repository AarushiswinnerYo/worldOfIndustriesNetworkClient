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
money=0
boxShadow=ft.BoxShadow(blur_radius=15, spread_radius=2.5, color=ft.Colors.DEEP_PURPLE_ACCENT, offset=ft.Offset(0,0), blur_style=ft.ShadowBlurStyle.NORMAL)
moneybox=ft.Container()
inventoryBoxExp=False
grad=ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[ft.Colors.BLACK, ft.Colors.BLACK, ft.Colors.PURPLE_ACCENT_700])
def main(page: ft.Page):
    global t1
    page.window.width=1280
    page.window.height=720
    page.window.center()
    page.window.frameless=True
    page.window.gradient=grad
    page.border_radius=ft.border_radius.all(20)
    page.window.spacing=0
    page.vertical_alignment = "top"
    page.horizontal_alignment = "left"
    page.spacing=0
    page.window.opacity=1
    page.theme=ft.Theme(scrollbar_theme=ft.ScrollbarTheme(thickness=0, thumb_visibility=False))
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
        global moneybox
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
                inventoryBox=ft.Container(height=200, width=200, shadow=boxShadow)
                moneybox=ft.Container(height=200, width=200, margin=ft.margin.all(10), padding=ft.padding.all(15), bgcolor=ft.Colors.GREY_900, animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT))
                everything.content=ft.Row([inventoryBox, moneybox])
                everything.alignment=ft.alignment.top_left
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
            elif r["user"]=="Token not found!":
                def closeTryDialog(x=None):
                    dia.open=False
                    page.update()
                t.value=f"Hello!"
                dia=ft.AlertDialog(title="Logged out!", content="Your account was logged out! Login again!", actions=[ft.TextButton(text="Login", on_click=lambda x:closeTryDialog())],open=True)
                everything.content=ft.ResponsiveRow([
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
                )
                page.add(topNav)
                page.add(Bg)
        else:
            r=client.main(f"login",username=f"{user}",passwd=f"{passwd}")
            if r["result"]=="correct!":
                userName=user
                user=userName
                with open("token.pkl", "wb") as f:
                    pickle.dump(r["token"], f)
                logged=True
                t.value=f"Hello, {userName}"
                inventoryBox=ft.Container(height=200, width=200, shadow=boxShadow)
                moneybox=ft.Container(height=200, width=200, margin=ft.margin.all(10), padding=ft.padding.all(15), bgcolor=ft.Colors.GREY_900, animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT))
                everything.content=ft.Row([inventoryBox, moneybox])
                everything.alignment=ft.alignment.top_left
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
            getInven()
            moneybox.opacity=0
            inventoryBox.width=widthscr-20
            inventoryBox.height=600
            inventoryBox.margin=ft.margin.all(0)
            inventoryBox.padding=ft.padding.all(0)
            inventoryBox.shadow=None
            inventoryBox.alignment=ft.alignment.top_center
            inventoryBox.scroll=ft.ScrollMode.HIDDEN
            inventoryBoxExp=True
        else:
            getInven()
            moneybox.opacity=1
            inventoryBox.width=200
            inventoryBox.height=200
            inventoryBox.shadow=boxShadow
            inventoryBox.alignment=ft.alignment.top_left
            inventoryBox.scroll=ft.ScrollMode.HIDDEN
            inventoryBoxExp=False

    def getInven():
        if logged==False:
            return
        else:
            log=client.main(f"info",username=f"{userName}")
            money=log["info"].pop("money")
            group=log['info'].pop("group")
            invenBox=log["info"]
            inventoryList.clear()
            for i in invenBox.keys():
                try:
                    j=invenBox[i].keys()
                except:
                    inventoryList.append(ft.Text(value=f"{i.capitalize()}: {invenBox[i]}"))
                else:
                    inventoryList.append(ft.Text(value=f"{i.capitalize()}:"))
                    for x in j:
                        inventoryList.append(ft.Text(value=f"   {x.capitalize()}: {invenBox[i][x]}"))
            inventoryBox.content=(ft.Column(controls=inventoryList, scroll=ft.ScrollMode.HIDDEN))
            inventoryBox.border_radius=5
            moneybox.border_radius=5
            inventoryBox.on_click=lambda s: openInventory()
            inventoryBox.margin=ft.margin.only(left=10)
            inventoryBox.padding=ft.padding.all(7.5)
            inventoryBox.bgcolor=ft.Colors.GREY_900
            moneybox.margin=ft.margin.only(left=10)
            moneybox.padding=ft.padding.all(7.5)
            inventoryBox.scroll=ft.ScrollMode.HIDDEN
            inventoryBox.animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
            inventoryBox.adaptive=True
            moneybox.content=ft.Column([ft.Text(value=f"Money: {money}"), ft.Text(value=f"Group:{group}")])
            moneybox.animate=ft.Animation(1000, ft.AnimationCurve.EASE_IN_OUT)
            everything.alignment=ft.alignment.top_left
            moneybox.update()
            everything.update()
            page.update()
    def updateInven(stop_Flag):
        while not stop_Flag.is_set():
            if page.window.visible==False:
                t1.join()
                stop_Flag.set()
                break
            else:
                getInven()
                time.sleep(5)
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
        try:
            exit(1)
        except:
            pass
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
                    begin=ft.alignment.top_center,
                    end=ft.alignment.bottom_center,
                    colors=[ft.Colors.BLACK, ft.Colors.BLACK],
                ),
                padding=15,
                content=ft.Column([ft.Row([
                    ft.Image(src="assets/icon.png", width=75, height=45),
                    ft.Column([t], alignment=ft.alignment.top_left, width=500),
                    ft.Row(width=475),
                    ft.Row([ft.TextButton(text="INVENTORY", on_click=lambda x:getInven()),
                    ft.Row(width=10),
                    ft.TextButton(icon=ft.Icons.REMOVE, width=35, height=25, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0)), on_click=lambda x: minimize(x)),
                    ft.TextButton(icon=ft.Icons.CLOSE, width=35,height=25, style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), overlay_color=ft.Colors.DEEP_ORANGE),on_click=lambda x: defineClosedOrOpen(x)),], 
                    width=200, spacing=0,
                    alignment=ft.alignment.top_center),
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
    stop_event = Event()
    t1=Thread(target=updateInven, args=(stop_event,))
    if os.path.exists("token.pkl"):
        login(user="", passwd="")
    else:
        page.add(topNav)
        page.add(Bg)
        page.update()

ft.app(main)