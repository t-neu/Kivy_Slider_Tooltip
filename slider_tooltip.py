from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.label import Label

class MyPBtext(Label):
    pass

class MypbSlider(Slider):
    pass
 
root = Builder.load_string('''

BoxLayout:
    orientation: 'vertical'
    BoxLayout:
        orientation: 'vertical'
        FloatLayout:
            id: float_mypb
            MyPBtext:
                size_hint: None, None
                size: 60, 60
                pos: (mypb_slider.value_pos[0] - 30, mypb_slider.value_pos[1] + 60)
                text: str(int(mypb_slider.value))
                id: mypb_text
                color: 1.0, 1.0, 0.0, 0.0
                font_size: 24
        MypbSlider:
            min: 10
            max: 240
            value: 40
            step: 5
            id: mypb_slider
            on_touch_up: mypb_text.color = (0.3833, 1.0, 0.0, 0.0)
            on_touch_down: mypb_text.color = (1.0, 0.7, 0.0, 1.0)
 ''')
 
 
class MyApp(App):
 
    def build(self):
        return root
 
MyApp().run()