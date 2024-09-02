import pyrebase
from database.config import config_keys as keys


class FirebaseAuth:
    def __init__(self):
        # Inicialização do Firebase
        firebase = pyrebase.initialize_app(keys)
        self.auth = firebase.auth()

    def login(self, email, password):
        """Realiza o login de um usuário no Firebase."""
        if not email or not password:
            return "Error: Email and password are required"

        try:
            user = self.auth.sign_in_with_email_and_password(email, password)
            return user
        except Exception as e:
            return f"Error: {str(e)}"

    def sign_up(self, email, password, confirm_password):
        """Cadastra um novo usuário no Firebase."""
        if not email or not password:
            return "Error: Email and password are required"

        if password != confirm_password:
            return "Error: Passwords do not match"

        try:
            user = self.auth.create_user_with_email_and_password(email, password)
            return user
        except Exception as e:
            return f"Error: {str(e)}"

    def revoke_token(self):
        """Revoga o token atual, efetivamente desconectando o usuário."""
        self.auth.current_user = None
        return "Success: Token revoked"
