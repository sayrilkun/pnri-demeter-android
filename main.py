from yutils.imports import *
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine, MDExpansionPanelOneLine
from yutils.pyre import db, storage
import os
import os.path
from kivy.uix.screenmanager import Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
# from yutils.dialog import dialog


request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE, Permission.CAMERA])
primary_ext_storage = primary_external_storage_path()

arr = os.listdir("kv/")
for i in arr:
    Builder.load_file(f'kv/{i}')
class KivyCamera(Image):
    pass
# Window.size = (375, 625)
# class ScannerScreen(Screen):
#     # def on_start(self):
#     #     Clock.schedule_once(self.get_frame, 5)

  
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         Clock.schedule_once(self._after_init)
#         # self.ids.zbarcam_id.ids.xcamera.play=True

#     def _after_init(self, dt):
#         """
#         Binds `ZBarCam.on_symbols()` event.
#         """
#         zbarcam = self.ids.zbarcam_id
#         zbarcam.bind(symbols=self.on_symbols)

#     def on_symbols(self, zbarcam, symbols):
#         """
#         Loads the first symbol data to the `QRFoundScreen.data_property`.
#         """
#         # going from symbols found to no symbols found state would also
#         # trigger `on_symbols`
#         if not symbols:
#             return

#         # qrfound_screen = self.manager.current_screen
#         symbol = symbols[0]
#         data = symbol.data.decode('utf8')
#         # hey = db.child("Hoya").order_by_child("scan_id").equal_to(data).get()
#         sub = 'ac&@%!'
#         if sub in data:
#             hey = db.child("Hoya").order_by_child("scan_id").equal_to(data).get()
#             for user in hey.each():
#                 self.manager.get_screen('qr').ids.forem.text = user.key()  
#         else:
#             self.manager.get_screen('qr').ids.forem.text = "NO DOCUMENT AVAILABLE"
#         # for user in hey.each():
#         #     if user.key() is None or user.key() == " ":
#         #         self.manager.get_screen('qr').ids.data.text = data
#         #     else:
#         #         self.manager.get_screen('qr').ids.data.text = user.key()     
#         print(data)
#         # self.manager.get_screen('qr').ids.data.text= data
#         self.manager.transition.direction = 'left'
#         self.manager.current = 'qr'

class FileManagerScreen(Screen):
    def on_enter(self):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            # preview=True,
        )

    def file_manager_open(self):
        # if platform == 'android':
        self.file_manager.show(primary_ext_storage)  # output manager to the screen
        # else:
        #     self.file_manager.show('C:\\')  # output manager to the screen
        self.manager_open = True
        # print(typee)

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''
        
        self.exit_manager()
        self.manager.current = 'uploaddoc'
        self.manager.transition.direction = 'right'
        # if typee == 0:
        self.manager.get_screen('uploaddoc').ids.input_11.text = path
        # else:
        #     self.manager.get_screen('uploaddoc').ids.input_12.text = path

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



class HelpContent(MDBoxLayout):
    '''Custom content.'''

class HelpContent2(MDBoxLayout):
    '''Custom content.'''

class HelpContent3(MDBoxLayout):
    '''Custom content.'''
class HelpContent4(MDBoxLayout):
    '''Custom content.'''

class HelpContent5(MDBoxLayout):
    '''Custom content.'''
class KivyCamera(Image):
    pass


class ImageButton(ButtonBehavior):
    pass


class IconLeftSampleWidget(IRightBodyTouch, MDIconButton):
    pass


class OneLineIcon(OneLineAvatarIconListItem):
    text = StringProperty()


class ThreeLineIcon(ThreeLineAvatarIconListItem):
    pass


class OneLine(OneLineListItem):
    divider = None


class Tab(MDFloatLayout, MDTabsBase):
    pass


class SwipeToDeleteItem(MDCardSwipe):
    text = StringProperty()


class DemoApp(MDApp):

    ###################################################################
    # COLOR SCHEMES
    ###################################################################
    purple = 56/255, 40/255, 81/255, 1
    dark_green = 43/255, 172/255, 127/255, 1
    light_green = 197/255, 230/255, 127/255, 1
    light_green2 = 27/255, 229/255, 127/255, 1
    light_green3 = 135/255, 230/255, 127/255, 1
    light_green4 = 193/255, 225/255, 193/255, 1
    dark_green2 = 37/255, 160/255, 127/255, 1
    dark1 = 143/255, 188/255, 143/255, 1
    light1 = 60/255, 179/255, 113/255, 1
    dark2 = 1, 1, 1, 1

    access = 'admin'
    all_docs = {}
    arr = []
    paginated = ()
    page_length = 0
    page_number = 0

    morph = {
        "Morphology": {
        }
    }

    current_year = date.today().year
    current_species = []
###################################################################
# DIALOGS
###################################################################

    dialog = None

    def form_dialog(self):
        dialog.form_dialog(self)

    dialog2 = None

    def show_no_doc_dialog(self):
        dialog.show_no_doc_dialog(self)

    dialog3 = None

    def show_simple_dialog(self):
        dialog.show_simple_dialog(self)

    dialog4 = None

    def delete_dialog(self):
        dialog.delete_dialog(self)

    dialog6 = None

    @mainthread
    def spin_dialog(self):
        dialog.spin_dialog(self)

    dialog7 = None

    def show_morph(self, morph, *args):
        dialog.show_morph(self, morph, *args)

    dialog8 = None

    def show_dialog(self):
        dialog.show_dialog(self)

    # dialog9 = None

    # def ttest_dialog(self, uk, passed_species, d, *args):
    #     dialog.ttest_dialog(self, uk, passed_species, d, *args)

    def not_avail(self):
        toast("This feature is not available on mobile version")

    def change_type(self, status):
        global typee
        typee = status
###################################################################
# LOG IN USER
###################################################################
    def admin_state(self, state):
        self.access = state
        print(self.access)

    def admin_toast(self):
        toast('Administrator access is needed')

    def sign_in(self):
        # auth = {}
        auth = db.child("Auth").get().val()

        username = self.help.get_screen('login').ids.username.text
        password = self.help.get_screen('login').ids.password.text

        if username == auth[self.access]['username'] and password == auth[self.access]['password']:
            self.help.current = 'menu'
            self.help.transition.direction = 'right'

        else:
            toast('Invalid credentials. Please try again.')
###################################################################
# SWITCH SCREEN
###################################################################

    def swtchScrn(self, *args):
        self.page_number = 0
        self.refresh_callback()
        self.eraser()
        self.help.current = 'collections'
        self.help.transition.direction = 'right'

    def swtchScreen(self, screen, *args):
        # self.refresh_callback()
        self.eraser()
        self.clear_morph()
        self.help.current = screen
        self.help.transition.direction = 'right'

###################################################################
# DELETE DOCUMENT
###################################################################
    def delete_doc(self):
        if self.access == 'admin':
            doc = self.help.get_screen('singledoc').ids.species.title
            db.child("Hoya").child(doc).remove()
            self.swtchScrn()
        else:
            self.admin_toast()

    def openGdrive(self):
        doc = self.help.get_screen('singledoc').ids.species.title
        try:
            url = self.all_docs[doc]['urls']['drive']
            if url is None or url == '':
                toast('File does not exist')
            else:
                webbrowser.open(url)
        except Exception as e:
            toast('File does not exist')

###################################################################
# GET DOCUMENT LISTS FROM DATABASE
###################################################################

    def next_button(self):
        self.page_number += 1
        print(self.page_number)
        if self.page_number < self.page_length:
            self.list_callback()
            self.help.get_screen(
                'collections').ids.page_number.text = f"Page {self.page_number+1} of {self.page_length}"
            self.help.get_screen(
                'collections').ids.page_numberad.text = f"{(self.page_number+1)*10} out of {len(self.arr)}"

        else:
            self.page_number -= 1

    def prev_button(self):
        self.page_number -= 1
        print(self.page_number)
        if self.page_number >= 0:
            self.list_callback()
            self.help.get_screen(
                'collections').ids.page_number.text = f"Page {self.page_number+1} of {self.page_length}"
            self.help.get_screen(
                'collections').ids.page_numberad.text = f"{(self.page_number+1)*10} of {len(self.arr)}"

        else:
            self.page_number += 1

    def pop_array(self):
        self.all_docs = db.child("Hoya").get().val()
        # print(self.all_docs)
        for key, value in self.all_docs.items():
            self.arr.append(key)

        def chunk(it, size):
            it = iter(it)
            return iter(lambda: tuple(islice(it, size)), ())
        self.paginated = list(chunk(self.arr, 10))
        self.page_length = len(self.paginated)
        self.help.get_screen(
            'collections').ids.page_number.text = f"Page {self.page_number+1} of {self.page_length}"
        self.help.get_screen(
            'collections').ids.page_numberad.text = f"{(self.page_number+1)*10} of {len(self.arr)}"

    def list_array(self):
        async def search_list():
            search = self.help.get_screen('collections').ids.search.text
            for i in self.paginated[self.page_number]:
                if search in i:
                    await asynckivy.sleep(0)
                    # sample_num = db.child("Hoya").child(i).child("sample_num").get()
                    # status = db.child("Hoya").child(i).child("status").get()
                    sample_num = self.all_docs[i]['sample_num']
                    status = self.all_docs[i]['status']
                    self.help.get_screen('collections').ids.box.add_widget(
                        ThreeLineIcon(text=f'{i}',
                                      secondary_text=f'Status: {status}',
                                      tertiary_text=f'{sample_num} sample/s',
                                      # on_touch_down = lambda x: print("adfads")
                                      # on_release = lambda y: self.spin_dialog(),
                                      # on_press= lambda x, value_for_pass=i: self.passValue(value_for_pass),

                                      ))
        asynckivy.start(search_list())

    def search_array(self):
        async def search_list():
            search = self.help.get_screen('collections').ids.search.text
            if search == '':
                self.list_callback()
            else:
                for i in self.arr:
                    if search in i:
                        await asynckivy.sleep(0)
                        # sample_num = db.child("Hoya").child(i).child("sample_num").get()
                        # status = db.child("Hoya").child(i).child("status").get()
                        sample_num = self.all_docs[i]['sample_num']
                        status = self.all_docs[i]['status']
                        self.help.get_screen('collections').ids.box.add_widget(
                            ThreeLineIcon(text=f'{i}',
                                          secondary_text=f'Status: {status}',
                                          tertiary_text=f'{sample_num} sample/s',
                                          # on_touch_down = lambda x: print("adfads")
                                          # on_release = lambda y: self.spin_dialog(),
                                          # on_press= lambda x, value_for_pass=i: self.passValue(value_for_pass),

                                          ))

        asynckivy.start(search_list())

    def list_callback(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.help.get_screen('collections').ids.box.clear_widgets()
            self.list_array()
            # self.help.get_screen(
            #     'collections').ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)

    def search_callback(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.help.get_screen('collections').ids.box.clear_widgets()
            self.search_array()
            # self.help.get_screen(
            #     'collections').ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)

    def refresh_callback(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.help.get_screen('collections').ids.box.clear_widgets()
            self.all_docs = {}
            self.arr = []
            self.pop_array()
            self.list_array()
            # self.help.get_screen(
            #     'collections').ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)
###################################################################
# GET DATA FOR EACH DOCUMENT
###################################################################

    def open_thread(self, *args):
        threading.Thread(target=self.open, args=args).start()

    def open(self, args_str, type):
        # print(arstr[-1])
        # print(self.current_species)
        # url = self.help.get_screen('singledoc').ids.qr_url.source
        toast("Downloading... Do not press any key")
        storage.child(f"{args_str}/{args_str}_{type}.png").download(f"{args_str}_{type}.png",f"/storage/emulated/0/Download/{args_str}_{type}.png")
        toast("Saved to Downloads")
        # webbrowser.open(url)

    def passValue(self, args_str):
        # args_str = ','.join(map(str,args))
        # self.current_species.append(args_str)

        icon = 'https://firebasestorage.googleapis.com/v0/b/pnri-demeter.appspot.com/o/hoya%20(1).png?alt=media&token=491584b8-4d48-487a-9f41-c5a3faa1401c'
        passportData = ['Name', 'Date of Acquisition',
                        'Accession Origin', 'Project', 'Project Leader', 'Other Detals']
        morphology = ['Pollinium', 'Retinaculum',
                      'Caudicle Bulb Diameter', 'Translator']

        # img_url = db.child("Hoya").child(args_str).child("urls").child("img_url").get().val()
        # qr_url= db.child("Hoya").child(args_str).child("urls").child("qr_url").get().val()
        # file_url= db.child("Hoya").child(args_str).child("urls").child("file_url").get().val()

        img_url = self.all_docs[args_str]['urls']["img_url"]
        qr_url = self.all_docs[args_str]['urls']["qr_url"]
        # watermark =  self.all_docs[args_str]['urls']["watermark"]

        screen2 = self.help.get_screen('singledoc')
        # screen2.ids.img_url.cr_widgets()
        screen2.ids.datas.clear_widgets()
        screen2.ids.dataso.clear_widgets()
        # screen2.ids['species'].clear_widgets()
        # screen2.ids.imag.add_widget(
        #     MDRoundFlatButton(
        #         text = "View IMG",
        #         on_press = lambda x : open(img_url)
        #     )
        # )
        # screen2.ids.file.add_widget(
        #     MDRoundFlatButton(
        #         text = "View PDF",
        #         on_press = lambda x : open(file_url)
        #     )
        # )
        # screen2.ids.qr.add_widget(
        #     MDRaisedButton(
        #         text="Save QR Code",
        #         on_press=lambda x: self.open(args_str, "qr")
        #         # on_press = lambda x :

        #     )
        # )

        if img_url is None or img_url == '':
            screen2.ids.img_url.source = icon

        else:
            screen2.ids.img_url.source = img_url

        if qr_url is None or qr_url == '':
            screen2.ids.qr_url.source = icon

        else:
            screen2.ids.qr_url.source = qr_url

        screen2.ids['species'].title = args_str
        # screen2.ids['datos'].text = datos
        # screen2.ids['header'].text = f"Morphometric Analysis of {args_str}"

        # for complete documents / to separeate passport data and morphology
        # morphology = db.child("Hoya").child(args_str).child("Morphology").get()

        morphology = self.all_docs[args_str]['Morphology']
        morphi = {
            "Morphology": {
            }
        }
        morphi['Morphology'].update(morphology)
        for key, value in morphology.items():
            screen2.ids.dataso.add_widget(
                OneLine(
                    text=f"{key}",
                    on_press=lambda x, value_for_pass=key: self.show_morph(
                        morphi, value_for_pass)
                    # halign="center"
                )
            )

        # passport_data = db.child("Hoya").child(args_str).child("Passport Data").get()
        passport_data = self.all_docs[args_str]["Passport Data"]
        for key, value in passport_data.items():
            screen2.ids.datas.add_widget(
                OneLine(
                    text=f"{key} : {value}",
                    # on_long_touch = print('fads')
                    # halign="center"
                )
            )
        self.help.current = 'singledoc'
        self.help.transition.direction = 'left'
        # args_str = ''

        # self.dialog6.dismiss(force=True)

###################################################################
# UPLOAD/EDIT STATE
###################################################################
    def change_state(self, num):
        global states
        states = num
        print(states)
        # return state

    def check_state(self):

        if states == 0:
            self.switchScreen('uploaddoc')
        elif states == 1:
            # self.switchScreen('edit')
            pass
        else:
            toast('Invalid')

    def upload_state(self):
        self.change_state(0)
        self.check_state()

    def edit_state(self):
        self.change_state(1)
        self.check_state()
###################################################################
# EDIT DOCUMENT
###################################################################

    def editDoc(self):
        self.eraser()
        self.change_state(0)
        self.swtchScreen('uploaddoc')
        doc = self.help.get_screen('singledoc').ids.species.title
        self.help.get_screen(
            'uploaddoc').ids.input_1.text = self.all_docs[doc]["Passport Data"]['Name']
        self.help.get_screen(
            'uploaddoc').ids.input_2.text = self.all_docs[doc]["Passport Data"]['Date Acquired']
        self.help.get_screen(
            'uploaddoc').ids.input_3.text = self.all_docs[doc]["Passport Data"]['Accession Origin']
        self.help.get_screen(
            'uploaddoc').ids.input_4.text = self.all_docs[doc]["Passport Data"]['Project']
        self.help.get_screen(
            'uploaddoc').ids.input_5.text = self.all_docs[doc]["Passport Data"]['Project Leader']
        self.help.get_screen(
            'uploaddoc').ids.input_6.text = self.all_docs[doc]["Passport Data"]['Other Details']
        self.help.get_screen(
            'uploaddoc').ids.input_7.text = self.all_docs[doc]["Passport Data"]['Status']

        self.help.get_screen(
            'uploaddoc').ids.input_11.text = self.all_docs[doc]['urls']["img_url"]
        self.help.get_screen(
            'uploaddoc').ids.input_12.text = self.all_docs[doc]['urls']["watermark"]
        self.help.get_screen(
            'uploaddoc').ids.input_13.text = self.all_docs[doc]['urls']["drive"]

        morphology = self.all_docs[doc]['Morphology']
        morphi = {
            "Morphology": {
            }
        }
        morphi['Morphology'].update(morphology)
        self.morph['Morphology'].update(morphology)
        for key, value in morphology.items():
            self.help.get_screen('uploaddoc').ids.box.add_widget(
                OneLineIcon(
                    text=f"{key}",
                    on_press=lambda x, value_for_pass=key: self.show_morph(
                        morphi, value_for_pass)
                    # halign="center"
                )
            )

    # def edit_doc(self):
    #     passportData = ['Name', 'Date of Acquisition',
    #                     'Accession Origin', 'Project', 'Project Leader', 'Other Detals']
    #     # morphology = ['Pollinium', 'Retinaculum', 'Caudicle Bulb Diameter', 'Translator']

    #     self.swtchScreen('edit')
    #     doc = self.help.get_screen('singledoc').ids.species.title

    #     passport_data = db.child("Hoya").child(
    #         doc).child("Passport Data").get()
    #     for datas in passport_data.each():
    #         self.help.get_screen('edit').ids.passpo.add_widget(
    #             MDTextField(
    #                 # id= "Adf",
    #                 hint_text=datas.key(),
    #                 text=datas.val(),
    #                 size_hint=(.75, 0.08),
    #                 mode="rectangle",
    #                 color_mode='accent',
    #                 pos_hint={"center_x": 0.5}
    #             )
    #         )

    # def update_doc(self):
    #     pass

    # dict = {}

    # def add_textfields(self):
    #     self.dialog.dismiss(force=True)
    #     # self.dialog.content_cls.ids.title.text, self.dialog.content_cls.ids.desc.text = "",""

    #     title = self.dialog.content_cls.ids.title.text
    #     desc = self.dialog.content_cls.ids.desc.text
    #     self.dict[f'{title}'] = f'{desc}'
    #     print(self.dict)
    #     self.help.get_screen('edit').ids.morph.add_widget(
    #         MDTextField(hint_text=title,
    #                     text=desc,
    #                     size_hint=(.75, 0.08),
    #                     mode="rectangle",
    #                     color_mode='accent',
    #                     pos_hint={"center_x": 0.5}
    #                     ))

###################################################################
# UPLOAD DOCUMENT
###################################################################
    def remove_item(self, instance, wet):
        # self.help.get_screen('iden').ids.box.remove_widget(instance)
        self.help.get_screen('uploaddoc').ids.box.remove_widget(instance)
        del self.morph['Morphology'][wet]
        print(self.morph)

    # def popMorph(self):
    #     self.help.get_screen('iden').ids.box.remove_widget()

    def puppy(self):

        sn = self.dialog8.content_cls.ids.input_19.text
        cb = self.dialog8.content_cls.ids.input_7.text
        el = self.dialog8.content_cls.ids.input_8.text
        hl = self.dialog8.content_cls.ids.input_9.text
        pl = self.dialog8.content_cls.ids.input_10.text
        pw = self.dialog8.content_cls.ids.input_13.text
        rl = self.dialog8.content_cls.ids.input_14.text
        shl = self.dialog8.content_cls.ids.input_15.text
        tal = self.dialog8.content_cls.ids.input_16.text
        td = self.dialog8.content_cls.ids.input_17.text
        wl = self.dialog8.content_cls.ids.input_18.text

        sopu = {
            f'{sn}': {
                'Caudicle Bulb': f'{cb}',
                "Extension": f'{el}',
                "Hips": f'{hl}',
                'Pollinium Length': f'{pl}',
                "Pollinium Widest": f'{pw}',
                "Retinaculum Length": f'{rl}',
                "Shoulder": f'{shl}',
                "Translator Arm Length": f'{tal}',
                "Translator Depth": f'{td}',
                "Waist": f'{wl}',
            }
        }
        if sn == '' or cb == '' or el == '' or hl == '' or pl == '' or pw == '' or rl == '' or shl == '' or tal == '' or td == '' or wl == '':
            toast("Data must be complete")
        else:
            self.morph['Morphology'].update(sopu)
            print(self.morph)

            self.help.get_screen('uploaddoc').ids.box.add_widget(
                OneLineIcon(text=sn,
                            # on_touch_down = lambda x: print("adfads")
                            # on_release = lambda y: self.show_morph(),
                            on_press=lambda x, value_for_pass=sn: self.show_morph(
                                self.morph, value_for_pass),

                            ))

            # self.help.get_screen('iden').ids.box.add_widget(
            #     OneLineIcon(text=sn,
            #                 # on_touch_down = lambda x: print("adfads")
            #                 # on_release = lambda y: self.show_morph(),
            #                 on_press=lambda x, value_for_pass=sn: self.show_morph(
            #                     self.morph, value_for_pass),

            #                 ))

            for i in range(7, 11):
                self.dialog8.content_cls.ids[f'input_{i}'].text = ""

            for i in range(13, 20):
                self.dialog8.content_cls.ids[f'input_{i}'].text = ""

    def eraser(self):
        for i in range(1,8):
            self.help.get_screen('uploaddoc').ids[f'input_{i}'].text = ""
        for i in range(11,15):
            self.help.get_screen('uploaddoc').ids[f'input_{i}'].text = ""

    def clear_morph(self):
        self.morph = {
            "Morphology": {
            }
        }
        self.help.get_screen('uploaddoc').ids.box.clear_widgets()
        # self.help.get_screen('iden').ids.box.clear_widgets()


    def upload(self):

        input_fields = ['name', 'dateAcq', 'accOrg', 'project', 'prjLdr', 'otherDtls',
                        'pollinium', 'retinaculum', 'translator', 'caudicle', 'image', 'file']

        

        name = self.help.get_screen('uploaddoc').ids.input_1.text
        dateAcq = self.help.get_screen('uploaddoc').ids.input_2.text
        accOrg = self.help.get_screen('uploaddoc').ids.input_3.text
        project = self.help.get_screen('uploaddoc').ids.input_4.text
        prjLdr = self.help.get_screen('uploaddoc').ids.input_5.text
        otherDtls = self.help.get_screen('uploaddoc').ids.input_6.text
        status = self.help.get_screen('uploaddoc').ids.input_7.text

        sample_num = len(self.morph['Morphology'].keys())

        image = self.help.get_screen('uploaddoc').ids.input_11.text
        photograp = self.help.get_screen('uploaddoc').ids.input_12.text
        drive = self.help.get_screen('uploaddoc').ids.input_13.text
        watermark = self.help.get_screen('uploaddoc').ids.input_14.text
        
        

        if image == "":
            img_url = ""
        elif 'https' in image:
            img_url = image
        else:
            toast("Uploading... Do not press any key")
            
            im = PIL.Image.open(image)
            width, height = im.size

            drawer = ImageDraw.Draw(im)
            if watermark == "":
                texty = f" © {photograp}, {self.current_year} | Philippine Nuclear Research Institute"
            else:
                texty = watermark
            # font = ImageFont.truetype('/storage/emulated/0/Download/arial.ttf', 20)
            file_exists = os.path.exists('/storage/emulated/0/Download/arial.ttf')
            if file_exists:
                font = ImageFont.truetype('/storage/emulated/0/Download/arial.ttf', 20)
                textwidth, textheight = drawer.textsize(texty, font)

            else:
                font = ImageFont.load_default()
                textwidth, textheight = drawer.textsize(texty, font)
            # calculate the x,y coordinates of the text
            margin = 10
            x = width - textwidth - margin
            y = height - textheight - margin

            # draw watermark in the bottom right corner
            drawer.text((x, y), texty, font=font)
            # im.show()
            im.save(f'/storage/emulated/0/Download/{name}_image.png')

            toast("Creating Watermark... Do not press any key")

            storage.child(
                f"{name}/{name}_image.png").put(f'/storage/emulated/0/Download/{name}_image.png')
            img_url = storage.child(f"{name}/{name}_image.png").get_url(None)


        # if file == "":
        #     file_url = ""
        # elif 'https' in file:
        #     file_url = file
        # else:
        #     storage.child(f"{name}/{name}_file").put(file)
        #     file_url = storage.child(f"{name}/{name}_file").get_url(None)

        if states == 1:
            toast("Generating QR Code... Do not press any key")
            scan_id = self.generate()

            qr_url = self.add_qr(name, scan_id)

            data = {
                "Passport Data": {
                    'Name': f'{name}',
                    'Date Acquired': f'{dateAcq}',
                    'Accession Origin': f'{accOrg}',
                    'Project': f'{project}',
                    'Project Leader': f'{prjLdr}',
                    'Other Details': f'{otherDtls}',
                    'Status': f'{status}',
                },

                "urls": {
                    'img_url': f'{img_url}',
                    'photograp': f'{photograp}',
                    'watermark': f'{watermark}',
                    'qr_url': f'{qr_url}',
                    'drive': f'{drive}',
                },

                'scan_id': f'{scan_id}',
                'status': f'{status}',
                'sample_num': sample_num,
            }
            data.update(self.morph)

        else:

            data = {
                "Passport Data": {
                    'Name': f'{name}',
                    'Date Acquired': f'{dateAcq}',
                    'Accession Origin': f'{accOrg}',
                    'Project': f'{project}',
                    'Project Leader': f'{prjLdr}',
                    'Other Details': f'{otherDtls}',
                    'Status': f'{status}',
                },
                'status': f'{status}',
                'sample_num': sample_num,
            }
            data.update(self.morph)

            url_data = {
                'img_url': f'{img_url}',
                'watermark': f'{watermark}',
                'drive': f'{drive}',
            }

        if name == '' or '.' in name:
            toast("Name cannot be empty or contains symbols")
            # self.dialog6.dismiss(force=True)

        elif bool(data['Morphology']) == False:
            toast("At least one sample is required")
            # self.dialog6.dismiss(force=True)

        else:
            if states == 1:
                if name in self.arr:
                    toast("Unable to upload! Name exists in database!")
                    # self.dialog6.dismiss(force=True)
                else:
                    toast('Finishing data upload...')
                    db.child('Hoya').child(f'{name}').set(data)
            else:
                toast('Finishing data update...')
                db.child('Hoya').child(f'{name}').update(data)
                db.child('Hoya').child(f'{name}').child(
                    'urls').update(url_data)

            self.clear_morph()
            # self.dialog6.dismiss(force=True)
            toast("Document Saved Successfully")
            self.swtchScrn()
            
    def upload_thread(self):
        self.spin_dialog()
        threading.Thread(target=(self.upload)).start()

    def downloadFont(self):
        toast("Downloading... Do not click any key")
        storage.child(f"font/arial.ttf").download(f"arial.ttf",f"/storage/emulated/0/Download/arial.ttf")
        toast("Saved to Downloads")

    # def add_img(self):
    #     root = tk.Tk()
    #     root.withdraw()
    #     image = filedialog.askopenfilename(title='select', filetypes=[
    #         ("image", ".jpeg"),
    #         ("image", ".png"),
    #         ("image", ".jpg"), ]
    #     )
    #     print(image)
    #     self.help.get_screen('uploaddoc').ids.input_11.text = image

    # def add_file(self):
    #     root = tk.Tk()
    #     root.withdraw()
    #     file = filedialog.askopenfilename()
    #     print(file)
    #     # print(file)
    #     self.help.get_screen('uploaddoc').ids.input_12.text = file

###################################################################
# GENERATE ENCRYPTED SCAN ID
###################################################################
    def generate(self):
        S = 8  # number of characters in the string.
        # call random.choices() string module to find the string in Uppercase + numeric data.
        ran = 'ac&@%!' + \
            ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
        x = str(ran)
        return x

###################################################################
# GENERATE QR CODE
###################################################################
    def add_qr(self, name, scan_id):
        input_data = scan_id
        # Creating an instance of qrcode
        qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
        qr.add_data(input_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        filename = f'/storage/emulated/0/Download/{name}_qr.png'
        img.save(filename)
        storage.child(f"{name}/{name}_qr.png").put(filename)
        qr_url = storage.child(f"{name}/{name}_qr.png").get_url(None)
        # print(qr_url)
        return qr_url
###################################################################
# OPEN SCANNED DOCUMENT TO APP
###################################################################

    def oks_qr(self):
        myDate = self.help.get_screen('scanner').ids.forem.text
        try:
            self.passValue(myDate)
        except Exception as e:
            toast("No Such Document!")

    def oks_thread(self):
        self.spin_dialog()
        threading.Thread(target=(self.oks_qr)).start()
###################################################################
# QR CODE SCANNER
###################################################################
    # def show_camscanner(self):
    #     cam = self.help.get_screen('scanner').ids.cam
    #     self.clock_event = Clock.schedule_interval(self.update, 1.0 / 30)
    #     cam.capture = cv2.VideoCapture(1)
    #     # cam.capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    # def update(self, dt):
    #     cam = self.help.get_screen('scanner').ids.cam
    #     ret, frame = cam.capture.read()
    #     # duts = []
    #     if ret:
    #         # cv2.putText(frame, 'dfgd', (50, 50),
    #         #                 cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    #         for barcode in decode(frame):

    #             myData = barcode.data.decode('utf-8')
    #             sub = 'ac&@%!'
    #             if sub in myData:
    #                 hey = db.child("Hoya").order_by_child(
    #                     "scan_id").equal_to(myData).get()
    #                 for user in hey.each():
    #                     self.help.get_screen('qr').ids.forem.text = user.key()
    #             else:
    #                 self.help.get_screen(
    #                     'qr').ids.forem.text = "NO DOCUMENT AVAILABLE"
    #             # qr_ref = db.collection('Hoya')
    #             # docs = qr_ref.where('scan_id', '==', f'{myData}').get()
    #             # for doc in docs:
    #             #     self.help.get_screen('qr').ids.forem.text = doc.id
    #             self.help.current = 'qr'
    #             # webbrowser.open(myData)
    #             pts = np.array([barcode.polygon], np.int32)
    #             pts = pts.reshape((-1, 1, 2))
    #             cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
    #             pts2 = barcode.rect
    #             cv2.putText(frame, myData, (pts2[0], pts2[1]),
    #                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

    #         buf1 = cv2.flip(frame, -1)
    #         buf = buf1.tobytes()
    #         image_texture = Texture.create(
    #             size=(frame.shape[1], frame.shape[0]), colorfmt='bgr'
    #         )
    #         image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
    #         cam.texture = image_texture




###################################################################
# OPEN SCANNED LINK TO WEBSITE
###################################################################
    # def my_qr(self):
    #     myDate = self.ids.forem.text
    #     self.ids.link.add_widget(
    #         MDRaisedButton(text="Open link",
    #                        on_press=lambda x: webbrowser.open(myDate))
    #     )

###################################################################
# CREATE TABLES
###################################################################
# def iden_thread(self, *args):
#     self.spin_dialog()
#     threading.Thread(target=(self.identify), args=self.morph).start()

    # def iden_thread(self, *args):
    #     threading.Thread(target=iden.identify, args=(self, self.morph)).start()

    # def createTable(self):
    #     self.spin_dialog()
    #     self.iden_thread(self.morph)
        # self.swtchScreen('result')

        # if len(self.morph['Morphology']) < 3:
        #     toast("need at last 3 samples")
        # # morph = {'Morphology': {'sample 1': {'Caudicle Bulb': '0.08', 'Extension': '0.13', 'Hips': '0.34', 'Pollinium Length': '0.73', 'Pollinium Widest': '0.38', 'Retinaculum Length': '0.20', 'Shoulder': '0.08', 'Translator Arm Length': '0.16', 'Translator Depth': '0.06', 'Waist': '0.13'}, 'sample 2': {'Caudicle Bulb': '0.06', 'Extension': '0.11', 'Hips': '0.06', 'Pollinium Length': '0.81', 'Pollinium Widest': '0.19', 'Retinaculum Length': '0.61', 'Shoulder': '0.17', 'Translator Arm Length': '0.23', 'Translator Depth': '0.05', 'Waist': '0.12'}, 'sample 3': {'Caudicle Bulb': '0.12', 'Extension': '0.17', 'Hips': '0.02', 'Pollinium Length': '0.62', 'Pollinium Widest': '0.24', 'Retinaculum Length': '0.35', 'Shoulder': '0.26', 'Translator Arm Length': '0.03', 'Translator Depth': '0.02', 'Waist': '0.08'}}}
        # else:
        #     # iden.identify(self, self.morph)
        #     self.spin_dialog()
        #     self.iden_thread(self.morph)

        # score_table,passed_species,t_test_df = iden.identify(self.morph)
        # print(score_table,passed_species,t_test_df)
        # self.swtchScreen('result')
        # morphi['Morphology'].update(morphology.val())
        # for passed in passed_species:
        #     self.help.get_screen('result').ids.passed.add_widget(
        #         OneLineListItem(
        #             text= passed,
        #         )
        #     )
        # unknown_data = [
        #         [0.08,	0.13,	0.34,	0.73,	0.38,	0.2,	0.08,	0.16,	0.06,	0.13],
        #         [0.06,	0.11,	0.06,	0.81,	0.19,	0.61,	0.17,	0.23,	0.05,	0.12],
        #         [0.12,	0.17,	0.02,	0.62,	0.24,	0.35,	0.26,	0.03,	0.02,	0.08]
        # ]

        # unknown = pd.DataFrame(unknown_data)
        # score_row = list(score_table.itertuples(index=False, name=None))
        # print(score_row)
        # # layout = AnchorLayout()
        # data_tables = MDDataTable(
        #     size_hint=(0.9, 0.9),
        #     use_pagination=True,
        #     rows_num=10,
        #     column_data=[
        #         ("Hoya Species", dp(35)),
        #         ("Mean Difference Score", dp(50)),
        #     ],
        #     row_data= score_row
        # )
        # self.help.get_screen('result').ids.diff.add_widget(data_tables)

        # t_test_row = list(t_test_df.itertuples(index=False, name=None))
        # print(t_test_row)
        # # layout = AnchorLayout()
        # data_tables = MDDataTable(
        #     size_hint=(0.9, 0.9),
        #     use_pagination=True,
        #     rows_num=10,
        #     column_data=[
        #         ("Landmarks", dp(35)),
        #         ("pvalue", dp(15)),
        #         ("interpretation", dp(50)),
        #     ],
        #     row_data= t_test_row
        # )
        # self.help.get_screen('result').ids.ttest.add_widget(data_tables)
        # layout.add_widget(data_tables)
        # return layout


###################################################################
# CAMERA
###################################################################

    # def capture(self):
    #     self.help.get_screen(
    #         'image').ids.cap_img.source = 'assets/captured_img/image.png'
    #     self.swtchScreen('image')

    # def save_img(self):
    #     self.help.get_screen(
    #         'uploaddoc').ids.input_11.text = 'assets/captured_img/image.png'
    #     self.swtchScreen('uploaddoc')

    # def show_camie(self):
    #     # disabled cam, naglalag kasi
    #     cam = self.help.get_screen('camera').ids.camie
    #     self.clock_event = Clock.schedule_interval(
    #         self.object_detection, 1.0 / 60)
    #     cam.capture = cv2.VideoCapture(1)
    #     # cam.capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    #     self.help.current = 'camera'
    #     self.help.transition.direction = "left"

    # def object_detection(self, dt):

    #     cam = self.help.get_screen('camera').ids.camie
    #     ret, frame = cam.capture.read()
    #     if ret:

    #         buf1 = cv2.flip(frame, 0)
    #         buf = buf1.tobytes()
    #         image_texture = Texture.create(
    #             size=(frame.shape[1], frame.shape[0]), colorfmt='bgr'
    #         )
    #         image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
    #         cam.texture = image_texture
    #         self.help.get_screen('camera').ids.capture.add_widget(
    #             MDFloatingActionButton(
    #                 text="Capture",
    #                 icon='camera-iris',
    #                 md_bg_color="#f8d7e3",
    #                 text_color="#211c29",
    #                 on_press=lambda x: cv2.imwrite(
    #                     f'assets/captured_img/image.png', frame),
    #                 on_release=lambda x: self.capture())
    #         )

    # def cam_start(self):
    #     camruler.start()

    # def camruler_thread(self):
    #     threading.Thread(target=(self.cam_start)).start()
    #     # self.dialog6.dismiss(force=True)

    def on_start(self):
        self.pop_array()
        self.list_array()

        # contentArray = ['dadgad','fadfad','fdsf', 'fadf']
        help_array = ['Camera', 'Collections', 'QR Code Scanner', 'Settings', 'Other']
        help_content =[HelpContent(), HelpContent2(), HelpContent3(), HelpContent4(),HelpContent5()]
        for i in range(5):
            self.help.get_screen('help').ids.box.add_widget(
                MDExpansionPanel(
                    # icon=f"{images_path}kivymd.png",
                    content=help_content[i],
                    panel_cls=MDExpansionPanelOneLine(
                        text=help_array[i],
                        # secondary_text="Secondary text",
                        # tertiary_text="Tertiary text",
                    )
                )
            )
        # for j in contentArray:
        #     self.help.get_screen('help').ids.boxerino.add_widget(
        #                     OneLineListItem(text= j))
        # GeneratorScreen.panget(self)
        # CollectionsScreen.pop_array(self)
        # CollectionsScreen.list_array(self)

    def build(self):
        self.title = 'Demeter'
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.material_style = "M3"
        self.help = Builder.load_file('main.kv')
        # screen.add_widget(self.help)
        return self.help


DemoApp().run()
