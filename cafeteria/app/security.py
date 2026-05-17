from flask_appbuilder.security.sqla.manager import SecurityManager as SQLASecurityManager
from werkzeug.security import generate_password_hash
import logging

log = logging.getLogger(__name__)

class CustomSecurityManager(SQLASecurityManager):
    def add_user(self, username, first_name, last_name, email, role, password="", hashed_password=""):
        if password:
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        return super().add_user(username, first_name, last_name, email, role, hashed_password=hashed_password)
