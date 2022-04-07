# import cv2
# import numpy as np
import random
import os
import webbrowser
import pyrebase
import qrcode
import string
import requests
import threading



from kivy.clock import mainthread
from kivymd.toast import toast
from pyzbar.pyzbar import decode

from kivy_garden.zbarcam import ZBarCam
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDIconButton, MDFloatingActionButton
from kivy.properties import StringProperty
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.core.window import Window
from kivymd.uix.list import IRightBodyTouch, OneLineListItem, OneLineIconListItem, OneLineAvatarIconListItem
from kivymd.uix.list import IconLeftWidget
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.utils import asynckivy
from kivymd.uix.button import MDFlatButton, MDRaisedButton, MDRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import AsyncImage
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.uix.camera import Camera

from android.storage import app_storage_path, primary_external_storage_path, secondary_external_storage_path
from android.permissions import request_permissions, Permission

# Window.size=(400,700)
request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE, Permission.CAMERA])
primary_ext_storage = primary_external_storage_path()

config = {
    "apiKey": "AIzaSyBH3WOpmUdPj0vGIpneswkW2CS8fFidlXw",
    "authDomain": "pnri-demeter.firebaseapp.com",
    "databaseURL": "https://pnri-demeter-default-rtdb.firebaseio.com",
    "projectId": "pnri-demeter",
    "storageBucket": "pnri-demeter.appspot.com",
    "messagingSenderId": "456214792415",
    "appId": "1:456214792415:web:773d7ea18f8ba214df816a",
    "measurementId": "G-00QH790MRG",
}

# cred = credentials.Certificate("serviceAccountKey.json")
# firebase_admin.initialize_app(cred)
firebase = pyrebase.initialize_app(config)
storage= firebase.storage()
db= firebase.database()

class ContentSpin(BoxLayout):
    pass


class Content(BoxLayout):
    pass

class KivyCamera(Image):
    pass

class ImageButton(ButtonBehavior):
    pass

class IconLeftSampleWidget(IRightBodyTouch, MDIconButton):
    pass

class OneLine(OneLineListItem):
    divider = None

class OneLineIcon(OneLineAvatarIconListItem):
    pass

# class AndroidCamera(Camera):
#     camera_resolution = (480, 480)
#     cam_ratio = camera_resolution[0] / camera_resolution[1]
    
    # camera_resolution = (100, 100)
    # counter = 0

    # def _camera_loaded(self, *largs):
    #     self.texture = Texture.create(size=np.flip(self.camera_resolution), colorfmt='rgb')
    #     self.texture_size = list(self.texture.size)

    # def on_tex(self, *l):
    #     if self._camera._buffer is None:
    #         return None
    #     frame = self.frame_from_buf()

    #     self.frame_to_screen(frame)
    #     super(AndroidCamera, self).on_tex(*l)

    # def frame_from_buf(self):
    #     w, h = self.resolution
    #     frame = np.frombuffer(self._camera._buffer.tostring(), 'uint8').reshape((h + h // 2, w))
    #     frame_bgr = cv2.cvtColor(frame, 93)
    #     return np.rot90(frame_bgr, 3)

    # def frame_to_screen(self, frame):
    #     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #     cv2.putText(frame_rgb, str(self.counter), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
    #     self.counter += 1
    #     flipped = np.flip(frame_rgb, 0)
    #     buf = flipped.tostring()
    #     self.texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

class LoginScreen(Screen):
    pass

class CollectionsScreen(Screen):
    pass
class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

class GeneratorScreen(Screen):
    pass

class HelpScreen(Screen):
    pass
class SingleDocScreen(Screen):
    pass

class UploadDocScreen(Screen):
    def eraser(self):
        for i in range(1,13):
            self.manager.get_screen('uploaddoc').ids[f'input_{i}'].text = ""

class FileManagerScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            # preview=True,
        )

    def file_manager_open(self):
        self.file_manager.show(primary_ext_storage)  # output manager to the screen
        self.manager_open = True
        print(typee)

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        
        self.exit_manager()
        self.manager.current = 'uploaddoc'
        self.manager.transition.direction = 'right'
        if typee == 0:
            self.manager.get_screen('uploaddoc').ids.input_11.text = path
        else:
            self.manager.get_screen('uploaddoc').ids.input_12.text = path

        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


class Tab(MDFloatLayout, MDTabsBase):
    pass

class ScannerScreen(Screen):
    # def on_start(self):
    #     Clock.schedule_once(self.get_frame, 5)

  
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self._after_init)
        # self.ids.zbarcam_id.ids.xcamera.play=True

    def _after_init(self, dt):
        """
        Binds `ZBarCam.on_symbols()` event.
        """
        zbarcam = self.ids.zbarcam_id
        zbarcam.bind(symbols=self.on_symbols)

    def on_symbols(self, zbarcam, symbols):
        """
        Loads the first symbol data to the `QRFoundScreen.data_property`.
        """
        # going from symbols found to no symbols found state would also
        # trigger `on_symbols`
        if not symbols:
            return

        # qrfound_screen = self.manager.current_screen
        symbol = symbols[0]
        data = symbol.data.decode('utf8')
        hey = db.child("Hoya").order_by_child("scan_id").equal_to(data).get()
        for user in hey.each():
            if user.key() is None or user.key() == " ":
                self.manager.get_screen('qr').ids.data.text = data
            else:
                self.manager.get_screen('qr').ids.data.text = user.key()     
        print(data)
        # self.manager.get_screen('qr').ids.data.text= data
        self.manager.transition.direction = 'left'
        self.manager.current = 'qr'
    # def get_frame(self, dt):  
    #     cam = self.ids.a_cam
    #     image_object = cam.export_as_image(scale=round((400 / int(cam.height)), 2))
    #     w, h = image_object._texture.size
    #     frame = np.frombuffer(image_object._texture.pixels, 'uint8').reshape(h, w, 4)
    #     gray = cv2.cvtColor(frame, cv2.COLOR_RGBA2GRAY)
    #     ret, frame = cam.capture.read()
    #     if ret:
    #         for barcode in decode(frame):
    #             myData = barcode.data.decode('utf-8')
    #             print(myData)
    #             self.manager.get_screen('qr').ids.forem.text = myData

    #             # hey = db.child("Hoya").order_by_child("scan_id").equal_to("APDF5JYG").get()
    #             # for user in hey.each():
    #             #     self.manager.get_screen('qr').ids.forem.text = user.key()        
    #             self.manager.current = 'qr'

    #     # self.ids.frame_counter.text = f'frame: {self.counter}'
    #     # self.counter += 1
    #     Clock.schedule_once(self.get_frame, 0.25)

    # def on_leave(self):
    #     event.cancel()
class QRScreen(Screen):
    # self.help.transition.direction = 'left'
    def on_pre_enter(self):
        myDate = self.ids.data.text
        self.ids.link.add_widget(
            MDRaisedButton( text = "Open link",
            on_press = lambda x: webbrowser.open(myDate))
        )

class DemoApp(MDApp):


    def change_type(self, status):
        global typee
        typee = status
        

###################################################################
# COLOR SCHEMES
###################################################################
    purple = 56/255,40/255,81/255,1
    dark_green = 43/255, 172/255, 127/255, 1
    light_green =  197/255, 230/255, 127/255, 1
    light_green2 = 27/255, 229/255, 127/255, 1
    light_green3 = 135/255, 230/255, 127/255, 1
    light_green4 = 193/255, 225/255, 193/255, 1
    dark_green2 = 37/255, 160/255, 127/255, 1
    dark1 = 143/255, 188/255, 143/255,1
    light1 = 60/255, 179/255, 113/255, 1
    dark2 = 46/255, 139/255, 87/255, 1

###################################################################
# DIALOGS
###################################################################
    dialog2= None
    dialog3= None
    dialog4= None
    dialog6= None


    def show_no_doc_dialog(self):
        if not self.dialog2:
            self.dialog2 = MDDialog(
                text= "File does not exist!",
                buttons=[
                    MDRaisedButton(text="OK", 
                    on_press = lambda x :self.dialog2.dismiss(force=True)
                    )
                ],
            )
        self.dialog2.open()

    def show_simple_dialog(self):
        if not self.dialog3:
            self.dialog3 = MDDialog(
                type="custom",
                content_cls=Content(),
            )
        self.dialog3.open()

    def delete_dialog(self):
        if not self.dialog4:
            self.dialog4 = MDDialog(
                text= "Are you sure you want to delete?",
                buttons=[
                    MDFlatButton(
                        text = 'Cancel',
                        on_press = lambda x: self.dialog4.dismiss(force=True)),
                    MDRaisedButton(
                        text="OK", 
                        on_press = lambda x : self.delete_doc(),
                        on_release = lambda x: self.dialog4.dismiss(force=True)

                    )
                ],
            )
        self.dialog4.open()

    def spin_dialog(self):
        if not self.dialog6:
            self.dialog6 = MDDialog(
                type="custom",
                content_cls=ContentSpin(),
            )
        self.dialog6.open()

###################################################################
# OPEN FILE MANAGER
###################################################################


###################################################################
# SWITCH SCREEN
###################################################################

    def swtchScrn(self,*args):
        self.search_callback()
        self.help.current = 'collections'
        self.help.transition.direction = 'right'


    def swtchScreen(self,screen,*args):
        # self.refresh_callback()
        self.help.current = screen
        self.help.transition.direction = 'right'

###################################################################
# DELETE DOCUMENT
###################################################################
    def delete_doc(self):
        doc= self.help.get_screen('singledoc').ids.species.title
        db.child("Hoya").child(doc).remove()
        self.swtchScrn()

###################################################################
# OPEN SCANNED DOCUMENT TO APP
###################################################################
    def open_scanned_document(self):
        myDate = self.help.get_screen('qr').ids.data.text
        try:
            self.passValue(myDate)
        except Exception as e:
            toast("No Such Document!")

###################################################################
# OPEN SCANNED LINK TO WEBSITE
###################################################################
    def my_qr(self):
        myDate = self.ids.forem.text
        self.ids.link.add_widget(
            MDRaisedButton( text = "Open link",
            on_press = lambda x: webbrowser.open(myDate))
        )  

###################################################################
# GENERATE ENCRYPTED SCAN ID
###################################################################
    def generate(self):
        S = 8  # number of characters in the string.  
        # call random.choices() string module to find the string in Uppercase + numeric data.  
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
        x= str(ran)
        return x

###################################################################
# GENERATE QR CODE
###################################################################
    def add_qr(self, name, scan_id):
        input_data = scan_id
        #Creating an instance of qrcode
        qr = qrcode.QRCode(
                version=1,
                box_size=10,
                border=5)
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        # fname = os.path.join( primary_external_storage_path(),'testfile')
        filename = f'/storage/emulated/0/Download/{name}_qr.png'
        img.save(filename)
        # toast(f"{name}_qr.png saved to /storage/emulated/0/Download/")
        storage.child(f"{name}/{name}_qr").put(filename)
        qr_url = storage.child(f"{name}/{name}_qr").get_url(None)
        # print(qr_url)
        return qr_url

###################################################################
# LOG IN USER
###################################################################

    def sign_in(self):
        username = self.help.get_screen('login').ids.username.text
        password = self.help.get_screen('login').ids.password.text

        if username == 'admin' and password == '12345':
            self.help.current = 'menu'
            self.help.transition.direction = 'right'
        
        else:
            self.help.get_screen('login').ids.status.text = 'Invalid credentials. Please try again.'

###################################################################
# UPLOAD DOCUMENT
###################################################################
    def upload(self):
        
        # self.show_donot_dialog()

        input_fields = ['name','dateAcq','accOrg','project','prjLdr','otherDtls',
                        'pollinium','retinaculum','translator', 'caudicle', 'image', 'file']
            
        name = self.help.get_screen('uploaddoc').ids.input_1.text
        dateAcq = self.help.get_screen('uploaddoc').ids.input_2.text
        accOrg = self.help.get_screen('uploaddoc').ids.input_3.text
        project = self.help.get_screen('uploaddoc').ids.input_4.text
        prjLdr = self.help.get_screen('uploaddoc').ids.input_5.text
        otherDtls = self.help.get_screen('uploaddoc').ids.input_6.text
        pollinium = self.help.get_screen('uploaddoc').ids.input_7.text
        retinaculum = self.help.get_screen('uploaddoc').ids.input_8.text
        translator = self.help.get_screen('uploaddoc').ids.input_9.text
        caudicle = self.help.get_screen('uploaddoc').ids.input_10.text
        image = self.help.get_screen('uploaddoc').ids.input_11.text
        file = self.help.get_screen('uploaddoc').ids.input_12.text

        if image == "":
            img_url = ""
        else:
            storage.child(f"{name}/{name}_image").put(image)
            img_url = storage.child(f"{name}/{name}_image").get_url(None)
        
        if file == "":
            file_url = ""
        else:
            storage.child(f"{name}/{name}_file").put(file)
            file_url = storage.child(f"{name}/{name}_file").get_url(None)

        scan_id = self.generate()

        qr_url = self.add_qr(name, scan_id)

        data = { 
            'Name': f'{name}',
            'Date Acquired':f'{dateAcq}',
            'Accession Origin': f'{accOrg}',
            'Project': f'{project}',
            'Project Leader': f'{prjLdr}',
            'Other Details': f'{otherDtls}',
            'Pollinium': f'{pollinium}',
            'Retinaculum': f'{retinaculum}',
            'Translator': f'{translator}',
            'Caudicle Bulb Diameter': f'{caudicle}',
            'img_url' : f'{img_url}',
            'file_url' : f'{file_url}',
            'qr_url': f'{qr_url}',
            'scan_id' : f'{scan_id}'
            }

        db.child('Hoya').child(f'{name}').set(data)

        self.dialog6.dismiss(force=True)
        toast("Document Saved Successfully")
        self.swtchScrn()

    def upload_thread(self):
        threading.Thread(target=(self.upload)).start()
###################################################################
# GET DOCUMENT LISTS FROM DATABASE
###################################################################
    def catch_error(self):
        try:
            self.help.current = 'collections'
            self.help.transition.direction = "left"

        except requests.exceptions.ConnectionError:
            toast("NO INTERNET CONNECTION")

    def search_list(self):
        async def search_list():

            search=self.help.get_screen('collections').ids.search.text
            all_docs = db.child("Hoya").get()
            for i in all_docs.each():
                name = i.key()
                # print(name)
            # for doc in docs:
                if search in name:
                    await asynckivy.sleep(0)
                    self.help.get_screen('collections').ids.box.add_widget(
                        OneLineIcon(text= f'{name}',
                        on_press= lambda x, value_for_pass=name: self.passValue(value_for_pass),
                        ))
        asynckivy.start(search_list())

    def search_callback(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.help.get_screen('collections').ids.box.clear_widgets()
            self.search_list()
            self.help.get_screen('collections').ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)

###################################################################
# GET DATA FOR EACH DOCUMENT
###################################################################
    def passValue(self, *args):
        self.help.current = 'singledoc'    
        self.help.transition.direction = 'left'
        
        args_str = ','.join(map(str,args))
        print(args_str)
        # single_doc = db.child("Hoya").child(args_str)

        icon = 'https://firebasestorage.googleapis.com/v0/b/pnri-demeter.appspot.com/o/flower.png?alt=media&token=3553abca-251f-42a3-b939-5d8eefc10a9a'
        passportData = ['Name','Date of Acquisition', 'Accession Origin', 'Project', 'Project Leader', 'Other Detals']
        morphology = ['Pollinium', 'Retinaculum', 'Caudicle Bulb Diameter', 'Translator']

        img_url = db.child("Hoya").child(args_str).child("img_url").get().val()
        print(f"img:{img_url}")
        qr_url= db.child("Hoya").child(args_str).child("qr_url").get().val()
        print(f"qr:{qr_url}")
        file_url= db.child("Hoya").child(args_str).child("file_url").get().val()
        print(f"img:{file_url}")
        screen2 = self.help.get_screen('singledoc')
        screen2.ids.datas.clear_widgets()

        def open(url):
            if url is None or url == '':
                self.show_no_doc_dialog()

            else:
                webbrowser.open(url)

        screen2.ids.imag.add_widget(
            MDRoundFlatButton(
                text = "View IMG",
                on_press = lambda x : open(img_url)
            )
        )
        screen2.ids.file.add_widget(
            MDRoundFlatButton(
                text = "View PDF",
                on_press = lambda x : open(file_url)
            )
        )
        screen2.ids.qr.add_widget(
            MDRaisedButton(
                text = "Save QR Code",
                on_press = lambda x : open(qr_url)
            )
        )

        if img_url is None or img_url == '':
            screen2.ids.img_url.source = icon

        else:
            screen2.ids.img_url.source = img_url
            # screen2.ids.image_url.text = img_url

        if qr_url is None or qr_url == '':
            screen2.ids.qr_url.source = icon

        else:
            screen2.ids.qr_url.source = qr_url


        screen2.ids['species'].title = args_str
        # screen2.ids['datos'].text = datos
        screen2.ids['header'].text = f"Morphometric Analysis of {args_str}"



        # for complete documents / to separeate passport data and morphology
        for i in range(3):
            screen2.ids.dataso.add_widget(
                OneLine(
                    text=f'hehe{[i]}'
                    # halign="center"
                )
            )
        passport_data = db.child("Hoya").child(args_str).get()
        for datas in passport_data.each():
            screen2.ids.datas.add_widget(
                OneLine(
                    text=f"{datas.key()} : {datas.val()}"
                    # halign="center"
                )
            )
        # print(format_2[i])


    def on_start(self):
        try:
            self.search_list()

        except requests.exceptions.ConnectionError:
            pass

    def storage_try(self):

        storage.child("Try/try_file").put("images/food.png")
        print("ok")

    def update(self, dt):
        cam = self.help.get_screen('scanner').ids.cam
        ret, frame = cam.capture.read()
        # duts = []
        if ret:
            # cv2.putText(frame, 'dfgd', (50, 50),
            #                 cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
            
            for barcode in decode(frame):
                
                myData = barcode.data.decode('utf-8')
                self.help.get_screen('qr').ids.forem.text = myData
                qr_ref = db.child('Hoya')
                docs = qr_ref.where('scan_id', '==', f'{myData}').get()
                for doc in docs:
                    self.help.get_screen('qr').ids.forem.text = doc.id
                self.help.current = 'qr'
                # webbrowser.open(myData)
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
                pts2 = barcode.rect
                cv2.putText(frame, myData,(pts2[0],pts2[1]),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
                            
            buf1 = cv2.flip(frame, -1)
            buf = buf1.tobytes()
            image_texture =Texture.create(
                size = (frame.shape[1], frame.shape[0]), colorfmt='bgr'
            )
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            cam.texture = image_texture

    def show_cam(self):
        cam = self.help.get_screen('scanner').ids.cam
        self.clock_event = Clock.schedule_interval(self.update, 1.0 /30)
        cam.capture = cv2.VideoCapture(-1)



    def build(self):        
        self.title='Demeter'
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"   

        self.help = Builder.load_file('main.kv')
        # screen.add_widget(self.help)
        return self.help

DemoApp().run()