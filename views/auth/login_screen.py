import flet as ft


class LoginScreen:
    def __init__(self, controller):
        self.controller = controller
        self.login_layout = self.build()

    def clear_fields(self):
        self.username_field.value = ""
        self.password_field.value = ""

    def on_login_click(self, guest=False):
        self.controller.login(
            self.username_field.value,
            self.password_field.value,
            guest=guest,
        )
        self.clear_fields()

    def on_register_click(self, _):
        self.clear_fields()
        self.controller.navigation_route("/register")

    def build(self):
        # self.lottie = ft.Lottie(
        #     src="/lotties/pdf_animation.json",
        #     reverse=True,
        #     height=250,
        # )

        # self.spacebox = ft.Column(
        #     controls=[ft.Text(" ")],
        #     alignment=ft.MainAxisAlignment.CENTER,
        #     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        # )

        self.username_field = ft.TextField(
            label="E-mail", width=300, border_color="#B7BBC2"
        )
        self.password_field = ft.TextField(
            label="Senha",
            password=True,
            can_reveal_password=True,
            width=300,
            border_color="#B7BBC2",
        )

        self.login_button = ft.FilledButton(
            text="Entrar",
            on_click=lambda _: self.on_login_click(guest=False),
            width=300,
            style=ft.ButtonStyle(
                bgcolor="#B7BBC2",
                color="#252728",
                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
                side=ft.BorderSide(color="#B7BBC2", width=1),
                padding=ft.padding.all(20),
            ),
        )

        self.register_button = ft.FilledButton(
            text="Registre-se",
            on_click=self.on_register_click,
            width=300,
            style=ft.ButtonStyle(
                bgcolor="#252728",
                color="#B7BBC2",
                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
                side=ft.BorderSide(color="#B7BBC2", width=1),
                padding=ft.padding.all(20),
            ),
        )

        self.text_aux = ft.Text("ou", size=15, weight=ft.FontWeight.W_100)

        self.button_guest = ft.FilledButton(
            text="Continuar como convidado",
            on_click=lambda _: self.on_login_click(guest=True),
            width=300,
            style=ft.ButtonStyle(
                bgcolor="#252728",
                color="#B7BBC2",
                shape=ft.RoundedRectangleBorder(radius=ft.border_radius.all(10)),
                side=ft.BorderSide(color="#B7BBC2", width=1),
                padding=ft.padding.all(20),
            ),
        )

        self.content_column = ft.Column(
            controls=[
                ft.Text("FLET PDF", size=30, weight=ft.FontWeight.W_100),
                # self.lottie,
                self.username_field,
                self.password_field,
                self.login_button,
                self.register_button,
                self.text_aux,
                self.button_guest,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.AUTO,
            spacing=20,
        )

        self.login_layout = ft.Container(
            content=self.content_column,
            alignment=ft.alignment.center,
            border_radius=10,
            bgcolor="#252728",
            padding=ft.padding.symmetric(horizontal=80, vertical=0),
            margin=ft.margin.all(30),
        )

        self.row = ft.Row(
            controls=[self.login_layout],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        self.main_container = ft.Container(
            content=self.row,
            alignment=ft.alignment.center,
            expand=True,
        )

        return [self.main_container]
