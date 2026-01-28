import flet

def c_home():
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Home", style=flet.TextThemeStyle.DISPLAY_MEDIUM, italic=True)
            ], height=80),
            flet.Divider(),
            flet.Row([flet.Text("Database :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Host :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Port :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Staff :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
        ]
    )

def c_status():
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("System Dashboard", style=flet.TextThemeStyle.DISPLAY_MEDIUM, italic=True)
            ], height=80),
            flet.Divider(),
            flet.Row([flet.Text("Database :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Host :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Port :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Staff :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
        ]
    )

def c_statistic():
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Business Analytics", style=flet.TextThemeStyle.DISPLAY_MEDIUM, italic=True)
            ], height=80),
            flet.Divider(),
            flet.Row([flet.Text("Database :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Host :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Port :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Staff :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
        ]
    )

def c_manager():
    return flet.Column(
        controls=[
            flet.Row([
                flet.Text("Admin Management", style=flet.TextThemeStyle.DISPLAY_MEDIUM, italic=True)
            ], height=80),
            flet.Divider(),
            flet.Row([flet.Text("Database :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Host :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Port :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
            flet.Row([flet.Text("Staff :", style=flet.TextThemeStyle.BODY_LARGE), ], height=30),
        ]
    )