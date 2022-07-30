from kivy.uix.screenmanager import Screen
from yutils.pyre import db
from kivymd.toast import toast

class SettingsScreen(Screen):
    access ='admin'
    def admin_state(self, state):
        self.access = state
        print(self.access)
    def changeCred(self):
        auth = db.child("Auth").get().val()
        curUser = self.ids.input_7.text
        newUser = self.ids.input_8.text
        curPass = self.ids.input_9.text
        newPass = self.ids.input_10.text

        if curUser == auth[self.access]['username'] and curPass == auth[self.access]['password']:
            data = {  
                    "username": f"{newUser}",
                    "password": f"{newPass}",
                    }

            db.child("Auth").child(self.access).update(data)
            self.manager.current = 'login'
            self.manager.transition.direction = 'right'
            toast("Credentials updated successfully")
        
        else:
            toast('Invalid credentials. Please try again.')
    def on_leave(self):
        self.ids.input_7.text=''
        self.ids.input_8.text=''
        self.ids.input_9.text =''
        self.ids.input_10.text = ''