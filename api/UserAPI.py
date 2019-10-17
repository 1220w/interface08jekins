import json

import app


class UserLogin:
    def login(self, session, mobile, password):
        return session.post(app.BASE_URL + "login", json={"mobile": mobile, "password": password})
