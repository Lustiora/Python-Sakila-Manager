# -- Import --
import flet
from menubar.menubar import menu_bar
# -- Module --
def main_window(page: flet.Page):
    # -- Frame --
    page.title = "Sakila"
    page.window.width = 1024
    page.window.height = 768
    page.window.resizable = True
    page.window.min_width = page.window.width
    page.window.min_height = page.window.height
    page.vertical_alignment = flet.MainAxisAlignment.START
    page.window.center()
    # -- Exit --
    page.window.prevent_close = True # X 이벤트 옵션 추가
    def close_pop(e):
        e.page.close(main_quit)  # 팝업창 종료 명령어
    def close_main(e):
        e.page.window.close()
        e.page.window.destroy()
    main_quit = flet.AlertDialog(
        title=flet.Text("Quit"),
        content=flet.Text("Exit?"),
        actions=[flet.TextButton("OK", on_click=close_main),
                 flet.TextButton("Cancel", on_click=close_pop)
                 ], actions_alignment=flet.MainAxisAlignment.END)
    def window_event(e):
        if e.data == "close":
            e.page.open(main_quit)
    page.window.on_event = window_event
    # -- Menubar --
    page.add(menu_bar())
    # -- Statusbar --

    # -- Update --
    page.update()
# -- Run Test --
# flet.app(target=main_window)