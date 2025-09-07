from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class TextInputApp(App):
    def build(self):
        #Main layout
        layout=BoxLayout(orientation='vertical',padding=20,spacing=10)
        # Text input field
        self.input_field=TextInput(hint_text="Type something here",multiline=False)
        layout.add_widget(self.input_field)
        # Button to display text
        btn=Button(text="Display Text")
        btn.bind(on_press=self.display_text)
        layout.add_widget(btn)
        #Label to show result
        self.label=Label(text="",font_size=20)
        layout.add_widget(self.label)
        return layout
    def display_text(self,instance):
        entered_text=self.input_field.text
        self.label.text=f"You typed: {entered_text}"

if __name__== "__main__":
  TextInputApp().run()