from kivy.app import App
from kivy.lang import Builder

from app.presentation.pages.ad.ad_page import AdPage
from app.presentation.pages.col.col_page import ColPage
from app.presentation.pages.main.main_page import MainPage
from app.presentation.routers.main_router import MainRouter

Builder.load_file('app/presentation/routers/main_router.kv')
Builder.load_file('app/presentation/pages/main/main_page.kv')
Builder.load_file('app/presentation/pages/ad/ad_page.kv')
Builder.load_file('app/presentation/pages/col/col_page.kv')


class QaApp(App):
    def build(self):
        sm = MainRouter()
        sm.add_widget(MainPage())
        sm.add_widget(ColPage())
        sm.add_widget(AdPage())
        sm.add_widget(MainPage())
        return sm


if __name__ == '__main__':
    QaApp().run()

