import flet as ft

def main(page: ft.Page):
    page.title = "Crypto Hub"

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationDestination(icon=ft.icons.CHAT, label="Chat"),
            ft.NavigationDestination(icon=ft.icons.COMMUTE, label="Community"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Profile",
            ),
        ]
    )
    page.add(ft.Text("Body!"))

    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True, horizontal=True)

    lv.controls.append(ft.Text("Tovar 1"))
    lv.controls.append(ft.Text("Tovar 2"))
    lv.controls.append(ft.Text("Tovar 1"))


ft.app(target=main, view=ft.WEB_BROWSER, port=8000)