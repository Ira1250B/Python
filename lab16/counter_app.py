from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CounterApp(App):
    def build(self):
        # Main layout
        self.count = 0
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Label to show counter value
        self.label = Label(text=f"Counter: {self.count}", font_size=32)
        layout.add_widget(self.label)

        # Button to increment counter
        btn = Button(text="Increment", font_size=24)
        btn.bind(on_press=self.increment_counter)
        layout.add_widget(btn)

        return layout

    def increment_counter(self, instance):
        self.count += 1
        self.label.text = f"Counter: {self.count}"

if __name__ == "__main__":
    CounterApp().run()
