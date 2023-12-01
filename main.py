from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class TrafficTicketsPDD2023(MDApp):
    def build(self):
        return MDLabel(text="Привет, мой первый пользователь", halign="center")


TrafficTicketsPDD2023().run()