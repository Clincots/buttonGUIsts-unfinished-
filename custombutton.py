from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
whar = False
whar2 = False

class FloatLayout(FloatLayout):
    def update(self):
        global volume
        global speed
        volume = self.ids.volume_label.text
        speed = self.ids.speed_label.text
        #print("volume:" + self.ids.volume_label.text)
        #print("speed:" + self.ids.speed_label.text)
        print("volume:" + volume)
        print("speed:" + speed)

        #set volume and speed to volume and speed of actual tts


    def copy(self):
        print("you pressed copy wow amazing ")
        # darren u add code here


    def L_plus_radio(self): #right
        global ineedthis
        global ineedthis2
        global whar
        global whar2
        ineedthis = False
        if whar:
            ineedthis = False
            ineedthis2 = False
            whar = False
            print("Voice 1 and 2 are not on!")
            return

        if not ineedthis:
            ineedthis = True
            ineedthis2 = False
            whar = True
            whar2 = False
            print("Voice 2 is off, and voice 1 is on!")



    def L_plus_radio2(self): #left
        global ineedthis
        global ineedthis2
        global whar2
        global whar
        ineedthis2 = False

        if whar2:
            ineedthis = False
            ineedthis2 = False
            whar2 = False
            print("Voice 1 and 2 are not on!")
            return

        if not ineedthis2:
            ineedthis2 = True
            ineedthis = False
            whar2 = True
            whar = False
            print("Voice 1 is off, and voice 2 is on!")


class CustomButtonApp(App):
    def build(self):
        return FloatLayout()


if __name__ == '__main__':
    CustomButtonApp().run()
