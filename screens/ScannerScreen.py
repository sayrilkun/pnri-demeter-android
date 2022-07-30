from kivy.uix.screenmanager import Screen
from yutils.imports import *
from yutils.pyre import db, storage
from kivy_garden.zbarcam import ZBarCam

class ScannerScreen(Screen):
    count = 0
  
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    def on_enter(self):
        print(self.count)
        Clock.schedule_once(self._after_init)
        # self.ids.zbarcam_id.ids.xcamera.play=True

    def _after_init(self,dt):
        
        """
        Binds `ZBarCam.on_symbols()` event.
        """
        self.zbarcam = ZBarCam()
        self.add_widget(self.zbarcam)
        
        self.zbarcam.bind(symbols=self.on_symbols)
        
    def switch(self,zbarcam):
        self.manager.current = 'menu'
        # zbarcam.clear_widgets()
        # zbarcam.ids.xcamera.play=False
        Clock.unschedule(self._after_init,1)
        zbarcam.stop()
        # zbarcam.ids.xcamera._camera._device = None
        zbarcam.ids.xcamera._camera._device.release() 
        zbarcam.clear_widgets()
        Builder.unload_file('/data/user/0/org.demeter.demeter/files/app/_python_bundle/site-packages/kivy_garden/xcamera/xcamera.kv')
        Builder.unload_file('/data/data/org.demeter.demeter/files/app/_python_bundle/site-packages/kivy_garden/zbarcam/zbarcam.kv')


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
        # hey = db.child("Hoya").order_by_child("scan_id").equal_to(data).get()
        sub = 'ac&@%!'
        if sub in data:
            hey = db.child("Hoya").order_by_child("scan_id").equal_to(data).get()
            for user in hey.each():
                self.ids.forem.text = user.key()  
        else:
            self.ids.forem.text = "No Document Found"

        print(data)

    def on_leave(self):
        Clock.unschedule(self._after_init,1)
        self.zbarcam.stop()
        self.zbarcam.ids.xcamera._camera= None
        # self.zbarcam.ids.xcamera._camera._device.release() 
        self.zbarcam.clear_widgets()
        Builder.unload_file('/data/user/0/org.demeter.demeter/files/app/_python_bundle/site-packages/kivy_garden/xcamera/xcamera.kv')
        Builder.unload_file('/data/data/org.demeter.demeter/files/app/_python_bundle/site-packages/kivy_garden/zbarcam/zbarcam.kv')
