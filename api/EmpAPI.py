import app


class EmpADUG:
    def emp_add(self, session, username, mobile, workNumber):
        myADDEmp = {"username": username,
                    "mobile": mobile,
                    "workNumber": workNumber
                    }
        return session.post(app.BASE_URL + "user", json=myADDEmp,
                            headers={"Authorization": "Bearer " + app.TOKEN})

    def emp_update(self, session,  userId,username=None):
        return session.put(app.BASE_URL + "user/" + userId, json={"username": username},
                           headers={"Authorization": "Bearer " + app.TOKEN})

    def emp_get(self, session, userId):
        return session.get(app.BASE_URL + "user/" + userId,
                           headers={"Authorization": "Bearer " + app.TOKEN})

    def emp_delete(self, session, userId):
        return session.delete(app.BASE_URL + "user/" + userId,
                              headers={"Authorization": "Bearer " + app.TOKEN})
