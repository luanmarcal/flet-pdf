import flet as ft


class RegisterScreen:

    def __init__(self, controller):
        self.controller = controller
        self.register_layout = self.build()

    def clear_fields(self):
        self.username_field.value = ""
        self.password_field.value = ""
        self.confirm_password_field.value = ""

    def on_register_click(self, _):
        self.controller.register(
            self.username_field.value,
            self.password_field.value,
            self.confirm_password_field.value,
        )
        self.clear_fields()

    def on_login_click(self, _):
        self.clear_fields()
        self.controller.navigation_route("/login")

    def build(self):
        self.username_field = ft.TextField(
            label="Usuário",
            width=300,
        )
        self.password_field = ft.TextField(
            label="Senha",
            password=True,
            can_reveal_password=True,
            width=300,
        )
        self.confirm_password_field = ft.TextField(
            label="Confirmar senha",
            password=True,
            can_reveal_password=True,
            width=300,
        )

        self.register_button = ft.ElevatedButton(
            text="Registrar",
            on_click=self.on_register_click,
            width=300,
        )

        self.login_button = ft.TextButton(
            text="Login",
            on_click=self.on_login_click,
            width=300,
        )

        self.content_column = ft.Column(
            controls=[
                ft.Text("Registrar", size=30, weight=ft.FontWeight.BOLD),
                self.username_field,
                self.password_field,
                self.confirm_password_field,
                self.register_button,
                self.login_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )

        self.register_layout = ft.Container(
            content=self.content_column,
            alignment=ft.alignment.center,
            expand=True,
            padding=20,
        )

        return [self.register_layout]
