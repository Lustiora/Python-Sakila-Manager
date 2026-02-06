import warnings
warnings.filterwarnings("ignore") # 경고 메시지 출력으로 인한 딜레이 방지

# -- Import --
import flet, os, sys, configparser, base64, psycopg2
from db_monitor import connect_test
from test_nav_tile import nav
# -- Variable --
# -- Module --
def check_login_process(page: flet.Page):
    store_id = 1
    store_address = "test Address"
    staff_user = "Superuser"
    # -- Load Config --
    if sys.platform == "win32":
        appdata = os.getenv("APPDATA")  # %appdata% 경로 변환
    else:
        appdata = os.path.expanduser("~/.config")
    config_dir = os.path.join(appdata, "sakila", "db")
    config_file = os.path.join(config_dir, "config.ini")
    print(f"\nConfig Load : {config_file}")
    config = configparser.ConfigParser()
    if config.read(config_file):
        # -- DB Connect --
        login_db = config['DB Connect']['db']
        login_host = config['DB Connect']['host']
        login_port = config['DB Connect']['port']
        login_id = config['DB Connect']['user']
        # -- Password Base64 Decode --
        encrypted_pw = config['DB Connect']['password']  # Encode Text Call
        pw_bytes = base64.b64decode(encrypted_pw)  # base64.b64decode Decode
        decrypted_pw = pw_bytes.decode('utf-8')  # utf-8 Decode
        # --
        conn = psycopg2.connect(dbname=login_db,
                                        host=login_host, # Default : localhost
                                        port=login_port, # Default : 5432
                                        user=login_id,
                                        password=decrypted_pw)
        # -- Frame --
        page.title = "Sakila"
        page.bgcolor = flet.Colors.BLUE_GREY_50
        page.vertical_alignment = flet.MainAxisAlignment.START
        page.update()
        # -- Statusbar --
        con_status = flet.Container(
            content=flet.Text(value="status "),
            alignment=flet.Alignment(1, 1),
            height=24,
            padding=2,
            border_radius=5,
            bgcolor=flet.Colors.OUTLINE
        )
        # -- Main Area --
        ex_tile, basic_content = nav(page, login_db, login_host, login_port, store_address, staff_user, store_id,
                                     conn)  # test
        # -- Page --
        page.add(
            flet.Row([
                flet.Column([ex_tile
                             ], scroll=flet.ScrollMode.AUTO, alignment=flet.MainAxisAlignment.START),
                flet.VerticalDivider(width=1),
                flet.Column([basic_content, con_status], expand=True),
            ], expand=True, vertical_alignment=flet.CrossAxisAlignment.START
            )
        )
        # connect_test(conn, con_status, page)
        # -- Update --
        page.update()
    else:
        return
# -- Run Test --
if __name__ == "__main__":
    flet.app(target=check_login_process, assets_dir="assets") # test