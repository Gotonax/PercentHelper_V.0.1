from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import MDScreenManager #MDScreen, SlideTransition
from kivymd.uix.transition.transition import MDFadeSlideTransition
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield.textfield import MDTextField
from kivymd.uix.scrollview import MDScrollView
import re

import webbrowser
from kivy.core.window import Window


#Config.set('graphics', 'resizable', True)


class MyApp(MDApp):


    def build(self):
        Window.bind(on_keyboard=self.key_input)

        self.sm=MDScreenManager(transition=MDFadeSlideTransition())

        #LogoScr= MDScreencolour(name='Logo Screen')
        MainScr= MDScreen(name='Main Screen', _md_bg_color='#CDD0C8')


        #img = Image(source='icon.png', size_hint=(1, .5), pos_hint={'center_x': .5, 'center_y': .5})
        scr1 = MDScreen(name='First MDScreen', _md_bg_color='#CDD0C8')
        scr2 = MDScreen(name='Second MDScreen', _md_bg_color='#CDD0C8')
        scr3 = MDScreen(name='Third MDScreen', _md_bg_color='#CDD0C8')
        scr4 = MDScreen(name='Fourth MDScreen', _md_bg_color='#CDD0C8')
        scr5 = MDScreen(name='Fifth MDScreen', _md_bg_color='#CDD0C8')
        scr6 = MDScreen(name='Sixth MDScreen', _md_bg_color='#CDD0C8')
        scr7 = MDScreen(name='Seventh MDScreen', _md_bg_color='#CDD0C8')
        scr8 = MDScreen(name='Eighth MDScreen', _md_bg_color='#CDD0C8')
        scr9 = MDScreen(name='Ninth MDScreen', _md_bg_color='#CDD0C8')
        scr10 = MDScreen(name='Tenth MDScreen', _md_bg_color='#CDD0C8')
        scrStory = MDScreen(name='Story', _md_bg_color='#CDD0C8')
        FeedBackScr = MDScreen(name='Feedback', _md_bg_color='#CDD0C8')


        blMS = MDBoxLayout(orientation='vertical', padding=50, spacing=10, size_hint_y=1.5)
        scrollMS=MDScrollView()
        blscr1 = MDBoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr2 = MDBoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr3 = MDBoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr4 = MDBoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr5 = MDBoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr6 = MDBoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr7 = MDBoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr8 = MDBoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr9 = MDBoxLayout(orientation='vertical', padding=50, spacing=10)
        blscr10 = MDBoxLayout(orientation='vertical', padding=50, spacing=10)
        blscrStory = MDBoxLayout(orientation='vertical', padding=50, spacing=10, size_hint_y=1.5)
        blFBS = MDBoxLayout(orientation='vertical', padding=50, spacing=10)


        mainlb=MDLabel(text='Percent helper', halign='center', size_hint=(1,.1),font_size='20dp', theme_text_color= "Custom", text_color="#354A00") # Меню основного экрана
        mainbut1=MDRectangleFlatButton(text='Найти процент от числа', size_hint= (1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbut1.bind(on_release=self.toset1)
        mainbut2 = MDRectangleFlatButton(text='Сколько процентов составляет число от числа', size_hint= (1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbut2.bind(on_release=self.toset2)
        mainbut3 = MDRectangleFlatButton(text='Увеличить число на процент', size_hint= (1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbut3.bind(on_release=self.toset3)
        mainbut4 = MDRectangleFlatButton(text='Уменьшить число на процент', size_hint= (1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbut4.bind(on_release=self.toset4)
        mainbut5 = MDRectangleFlatButton(text='Каждый третий, каждый пятый, что это?', size_hint=(1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbut5.bind(on_release=self.toset5)
        mainbut6 = MDRectangleFlatButton(text='Часть от числа, это сколько? \n(вторая часть, третья, четверть)', size_hint=(1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbut6.bind(on_release=self.toset6)
        mainbut7 = MDRectangleFlatButton(text='Дробь от числа (умножение дроби на число)', size_hint=(1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbut7.bind(on_release=self.toset7)
        mainbut8 = MDRectangleFlatButton(text='Деление числа на дробь', size_hint=(1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbut8.bind(on_release=self.toset8)
        mainbut9 = MDRectangleFlatButton(text='НДС (Ищем число зная сумму с НДС)', size_hint=(1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbut9.bind(on_release=self.toset9)
        mainbut10 = MDRectangleFlatButton(text='Возведение числа в степень', size_hint=(1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbut10.bind(on_release=self.toset10)
        mainbutStory = MDRectangleFlatButton(text='История запросов (результаты)', size_hint=(1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbutStory.bind(on_release=self.tosetStory)
        mainbutFB = MDRectangleFlatButton(text='Обратная связь', size_hint=(1, 0.1), text_color="#354A00", line_color="#354A00")
        mainbutFB.bind(on_release=self.tosetFB)

        blMS.add_widget(mainlb)
        blMS.add_widget(mainbut1)
        blMS.add_widget(mainbut2)
        blMS.add_widget(mainbut3)
        blMS.add_widget(mainbut4)
        blMS.add_widget(mainbut5)
        blMS.add_widget(mainbut6)
        blMS.add_widget(mainbut7)
        blMS.add_widget(mainbut8)
        blMS.add_widget(mainbut9)
        blMS.add_widget(mainbut10)
        blMS.add_widget(mainbutStory)
        blMS.add_widget(mainbutFB)
        scrollMS.add_widget(blMS)
        MainScr.add_widget(scrollMS)
        #LogoScr.add_widget(img)



        scr1but=MDRectangleFlatButton(text='Возврат в меню', size_hint=(1,.2), text_color="#354A00", line_color="#354A00") # Меню экрана 1 - процент от числа
        scr1but.bind(on_release=self.tomain)
        self.scr1lb=MDLabel(text="Если Вам необходимо найти процент от \nчисла, введите в первую графу число, \nот которого необходимо найти процент,\n во вторую графу процент, который \nнадо найти и нажмите кнопку рассчитать. \n(Пример: от числа 100 найти процент 30)", halign='center', size_hint= (1, 1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        self.scr1inp1 = FloatInput(size_hint= (1, None), height="30dp", hint_text="Сюда число", input_type="number")
        self.scr1inp2 = FloatInput(size_hint= (1, None), height="30dp", hint_text="Сюда процент", input_type="number")
        scr1but1 = MDRectangleFlatButton(text='Рассчитать', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")
        scr1but1.bind(on_press=self.scr1count)
        self.scr1rez =MDLabel(text="Результат: ", halign="center", theme_text_color= "Custom", text_color="#354A00")
        blscr1.add_widget(scr1but)

        blscr1.add_widget(self.scr1lb)
        blscr1.add_widget(self.scr1inp1)
        blscr1.add_widget(self.scr1inp2)
        blscr1.add_widget(self.scr1rez)
        blscr1.add_widget(scr1but1)

        scr1.add_widget(blscr1)


        scr2but =MDRectangleFlatButton(text='Возврат в меню', size_hint=(1,.2), text_color="#354A00", line_color="#354A00") # Меню экрана 2 -Сколько процентов составляет число от числа
        scr2but.bind(on_release=self.tomain)
        self.scr2lb =MDLabel(text="Если Вам необходимо найти, сколько \nпроцентов одно число составляет от \nдругого, введите в первую графу число, \nпо которому нужно найти процент, \nво вторую графу число, от которого ищется \nпроцент и нажмите кнопку рассчитать. \n(Пример: \nсколько процентов 25 составляет от 200)", halign='center', size_hint= (1, 1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        self.scr2inp1 = FloatInput(size_hint= (1, None), height="30dp", hint_text="Сюда первое число", input_type="number")
        self.scr2inp2 = FloatInput(size_hint= (1, None), height="30dp", hint_text="Сюда число от которого ищем процент", input_type="number")
        self.scr2rez =MDLabel(text="Результат: ", halign="center", theme_text_color= "Custom", text_color="#354A00")
        scr2but1 =MDRectangleFlatButton(text='Рассчитать', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")
        scr2but1.bind(on_press=self.scr2count)
        blscr2.add_widget(scr2but)
        blscr2.add_widget(self.scr2lb)
        blscr2.add_widget(self.scr2inp1)
        blscr2.add_widget(self.scr2inp2)
        blscr2.add_widget(self.scr2rez)
        blscr2.add_widget(scr2but1)
        scr2.add_widget(blscr2)


        scr3but =MDRectangleFlatButton(text='Возврат в меню', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")  # Меню экрана 3 - Увеличить число на процент
        scr3but.bind(on_release=self.tomain)
        scr3lb =MDLabel(
            text="Если Вам необходимо увеличить число на\nопределенный процент введите в первую графу\nчисло, которое надо увеличить,\n во вторую графу процент, на котороый\nувеличивается число и \nнажмите кнопку рассчитать. \n(Пример: увеличить число 120 на 30%)",
            halign='center', size_hint= (1, 1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        self.scr3inp1 = FloatInput(size_hint= (1, None), height="30dp", hint_text="Сюда число", input_type="number")
        self.scr3inp2 = FloatInput(size_hint= (1, None), height="30dp", hint_text="Сюда процент на который увеличиваем", input_type="number")
        self.scr3rez =MDLabel(text="Результат: ", halign="center", theme_text_color= "Custom", text_color="#354A00")
        scr3but1 =MDRectangleFlatButton(text='Рассчитать', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")
        scr3but1.bind(on_press=self.scr3count)
        blscr3.add_widget(scr3but)
        blscr3.add_widget(scr3lb)
        blscr3.add_widget(self.scr3inp1)
        blscr3.add_widget(self.scr3inp2)
        blscr3.add_widget(self.scr3rez)
        blscr3.add_widget(scr3but1)
        scr3.add_widget(blscr3)


        scr4but =MDRectangleFlatButton(text='Возврат в меню', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")  # Меню экрана 4 - Увеличить число на процент
        scr4but.bind(on_release=self.tomain)
        scr4lb =MDLabel(
            text="Если Вам необходимо уменьшить число \nна определенный процент, введите в первую\nграфу число, которое надо уменьшить,\n во вторую графу процент, на \nкоторый уменьшается число \nи нажмите кнопку рассчитать. \n(Пример: уменьшить число 120 на 40%)",
            halign='center', size_hint= (1, 1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        self.scr4inp1 = FloatInput(size_hint= (1, None), height="30dp", hint_text="Сюда число", input_type="number")
        self.scr4inp2 = FloatInput(size_hint= (1, None), height="30dp", hint_text="Сюда процент на который уменьшаем", input_type="number")
        self.scr4rez =MDLabel(text="Результат: ", halign="center", theme_text_color= "Custom", text_color="#354A00")
        scr4but1 =MDRectangleFlatButton(text='Рассчитать', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")
        scr4but1.bind(on_press=self.scr4count)
        blscr4.add_widget(scr4but)
        blscr4.add_widget(scr4lb)
        blscr4.add_widget(self.scr4inp1)
        blscr4.add_widget(self.scr4inp2)
        blscr4.add_widget(self.scr4rez)
        blscr4.add_widget(scr4but1)
        scr4.add_widget(blscr4)


        scr5but =MDRectangleFlatButton(text='Возврат в меню', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")  # Меню экрана 5 – Каждый 3 каждый 5
        scr5but.bind(on_release=self.tomain)
        scr5lb =MDLabel(
            text="Часто в результатах опросов слышишь: \nКаждый третий из опрошенный.... \nЧто же это значит? Это значит, что из трёх \nопрошенных людей, один выразил то \nили инное мнение. Для расчета введите в \nпервую графу число (3-ий или 5-ый)\nА во вторую графу, от какого это общего числа.\n(Пример: каждый 5 из всех 500000 жителей)",
            halign='center', size_hint= (1, 1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        self.scr5inp1 = FloatInput(size_hint= (1, None), height="30dp", hint_text="Сюда каждого)", input_type="number")
        self.scr5inp2 = FloatInput(size_hint= (1, None), height="30dp", hint_text="Сюда от какого числа", input_type="number")
        self.scr5rez =MDLabel(text="Результат: ", halign="center", theme_text_color= "Custom", text_color="#354A00")
        scr5but1 =MDRectangleFlatButton(text='Рассчитать', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")
        scr5but1.bind(on_press=self.scr5count)
        blscr5.add_widget(scr5but)
        blscr5.add_widget(scr5lb)
        blscr5.add_widget(self.scr5inp1)
        blscr5.add_widget(self.scr5inp2)
        blscr5.add_widget(self.scr5rez)
        blscr5.add_widget(scr5but1)
        scr5.add_widget(blscr5)


        scr6but =MDRectangleFlatButton(text='Возврат в меню', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")  # Меню экрана 6 – Часть от числа (пятая, треть, четверть)
        scr6but.bind(on_release=self.tomain)
        scr6lb =MDLabel(
            text="Данная операция поможет найти \nчасть от числа.В первую графу \nвведите часть (3, 4, 5 и т.д.),\nВо вторую графу число, от которого часть\n(Пример: Треть(3 часть) от числа 600",
            halign='center', size_hint= (1, 1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        self.scr6inp1 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда часть", input_type="number")
        self.scr6inp2 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда число", input_type="number")
        self.scr6rez =MDLabel(text="Результат: ", halign="center", theme_text_color= "Custom", text_color="#354A00")
        scr6but1 =MDRectangleFlatButton(text='Рассчитать', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")
        scr6but1.bind(on_press=self.scr6count)
        blscr6.add_widget(scr6but)
        blscr6.add_widget(scr6lb)
        blscr6.add_widget(self.scr6inp1)
        blscr6.add_widget(self.scr6inp2)
        blscr6.add_widget(self.scr6rez)
        blscr6.add_widget(scr6but1)
        scr6.add_widget(blscr6)


        scr7but =MDRectangleFlatButton(text='Возврат в меню', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")  # Меню экрана 7 – Дробь от числа (умножение)
        scr7but.bind(on_release=self.tomain)
        scr7lb =MDLabel(
            text="Данная операция умножает дробь на число.\n То есть, фактически находит дробь от числа.\n  В первую графу введите числитель.\n Во вторую графу введите знаменатель. \n В третью - само число.\n(Пример: 2/3 от числа 600)",
            halign='center', size_hint=(1, 1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        self.scr7inp1 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда числитель дроби", input_type="number")
        self.scr7inp2 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда знаменатель дроби", input_type="number")
        self.scr7inp3 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда число", input_type="number")
        self.scr7rez =MDLabel(text="Результат: ", halign="center", theme_text_color= "Custom", text_color="#354A00")
        scr7but1 =MDRectangleFlatButton(text='Рассчитать', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")
        scr7but1.bind(on_press=self.scr7count)
        blscr7.add_widget(scr7but)
        blscr7.add_widget(scr7lb)
        blscr7.add_widget(self.scr7inp1)
        blscr7.add_widget(self.scr7inp2)
        blscr7.add_widget(self.scr7inp3)
        blscr7.add_widget(self.scr7rez)
        blscr7.add_widget(scr7but1)
        scr7.add_widget(blscr7)


        scr8but =MDRectangleFlatButton(text='Возврат в меню', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")  # Меню экрана 8 – Дробь от числа (Деление)
        scr8but.bind(on_release=self.tomain)
        scr8lb =MDLabel(
            text="Данная операция делит число на дробь.\n В первую графу введите число.\n Во вторую графу введите числитель.\n В третью - знаменатель.\n(Пример: число 600 делить на 2/3)",
            halign='center', size_hint=(1, 1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        self.scr8inp1 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда число", input_type="number")
        self.scr8inp2 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда числитель дроби", input_type="number")
        self.scr8inp3 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда знаменатель дроби", input_type="number")
        self.scr8rez =MDLabel(text="Результат: ", halign="center", theme_text_color= "Custom", text_color="#354A00")
        scr8but1 =MDRectangleFlatButton(text='Рассчитать', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")
        scr8but1.bind(on_press=self.scr8count)
        blscr8.add_widget(scr8but)
        blscr8.add_widget(scr8lb)
        blscr8.add_widget(self.scr8inp1)
        blscr8.add_widget(self.scr8inp2)
        blscr8.add_widget(self.scr8inp3)
        blscr8.add_widget(self.scr8rez)
        blscr8.add_widget(scr8but1)
        scr8.add_widget(blscr8)


        scr9but =MDRectangleFlatButton(text='Возврат в меню', size_hint=(1,.2), text_color="#354A00", line_color="#354A00")  # Меню экрана 9 – Дробь от числа (Деление)
        scr9but.bind(on_release=self.tomain)
        scr9lb =MDLabel(
            text="Данная операция находит сумму без НДС.\n То есть, если Вам известна\n число с НДС( в том числе НДС)\n в первую графу введите число,\n во вторую графу введите процент НДС \n(18 или 20 или другое). \n(Пример: число с НДС 1200, НДС 20%)",
            halign='center', size_hint=(1, 1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        self.scr9inp1 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда число", input_type="number")
        self.scr9inp2 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда процент НДС", input_type="number")
        self.scr9rez =MDLabel(text="Результат: ", halign="center", theme_text_color= "Custom", text_color="#354A00")
        scr9but1 =MDRectangleFlatButton(text='Рассчитать', size_hint=(1, .2))
        scr9but1.bind(on_press=self.scr9count)
        blscr9.add_widget(scr9but)
        blscr9.add_widget(scr9lb)
        blscr9.add_widget(self.scr9inp1)
        blscr9.add_widget(self.scr9inp2)
        blscr9.add_widget(self.scr9rez)
        blscr9.add_widget(scr9but1)
        scr9.add_widget(blscr9)

        scr10but =MDRectangleFlatButton(text='Возврат в меню', size_hint=(1, .2), text_color="#354A00", line_color="#354A00")  # Меню экрана 10 – Степень числа
        scr10but.bind(on_release=self.tomain)
        scr10lb =MDLabel(
            text="Данная операция возводит число\n в заданную степень\n То есть квадрат числа, куб и\n другие степени. \n В первую графу введите число,\n которое возводите в степень. \nВо вторую графу - степень \n(Пример: число 11 в степени 5",
            halign='center', size_hint=(1, 1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        self.scr10inp1 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда число", input_type="number")
        self.scr10inp2 = FloatInput(size_hint=(1, None), height="30dp", hint_text="Сюда степень", input_type="number")
        self.scr10rez =MDLabel(text="Результат: ", halign="center", theme_text_color= "Custom", text_color="#354A00")
        scr10but1 =MDRectangleFlatButton(text='Рассчитать', size_hint=(1, .2), text_color="#354A00", line_color="#354A00")
        scr10but1.bind(on_press=self.scr10count)
        blscr10.add_widget(scr10but)
        blscr10.add_widget(scr10lb)
        blscr10.add_widget(self.scr10inp1)
        blscr10.add_widget(self.scr10inp2)
        blscr10.add_widget(self.scr10rez)
        blscr10.add_widget(scr10but1)
        scr10.add_widget(blscr10)

        scrStorybut =MDRectangleFlatButton(text='Возврат в меню', size_hint=(1, 0.05), text_color="#354A00", line_color="#354A00")  # Меню экрана 11 – Список результатов
        scrollStory = MDScrollView()
        scrStorybut.bind(on_release=self.tomain)
        scrStorylb =MDLabel(
            text="Список ранее проведённых Вами операций.\n (Только 1000 символов).\nЕсли хотите очистить историю,\n нажмите Очистить.",
            halign='center', size_hint=(1, 0.1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        scrStorybut1 =MDRectangleFlatButton(text='Очистить', size_hint=(1, 0.05), text_color="#354A00", line_color="#354A00")
        scrStorybut1.bind(on_press=self.scrStorycount)
        self.scrStoryrez =MDLabel(text="История:\n", halign='center',valign='top', size_hint=(1, 1))



        blscrStory.add_widget(scrStorybut)
        blscrStory.add_widget(scrStorylb)
        blscrStory.add_widget(scrStorybut1)
        blscrStory.add_widget(self.scrStoryrez)
        scrollStory.add_widget(blscrStory)
        scrStory.add_widget(scrollStory)


        FeedBackScrbut =MDRectangleFlatButton(text='Возврат в меню', size_hint=(1, .1), text_color="#354A00", line_color="#354A00") # Экран обратной связи
        FeedBackScrbut.bind(on_release=self.tomain)
        FeedBackScrlb =MDLabel(
            text="Все ваши пожелания и сообщения об \nошибках присылайте на электронный адрес:\n Percenthelper@yandex.ru\n Если есть желание поощрить работу автора приложения:\n Криптокошелёк:\n 0x47a5f8b28e4fd470367c1f8123167fbb6fcdb13d\n Номер карты: 5536 9137 6801 9172",
            halign='center', size_hint=(1, 1), underline=True, theme_text_color= "Custom", text_color="#354A00")
        PrivacyPolicybut =MDRectangleFlatButton(text='Наша политика конфиденциальности \n(Privacy Policy)', size_hint=(1, .1),  halign='center', text_color="#354A00", line_color="#354A00") # Экран обратной связи
        PrivacyPolicybut.bind(on_release=self.privacy)
        blFBS.add_widget(FeedBackScrbut)
        blFBS.add_widget(PrivacyPolicybut)
        blFBS.add_widget(FeedBackScrlb)
        FeedBackScr.add_widget(blFBS)


        #self.sm.add_widget(LogoScr)
        self.sm.add_widget(MainScr)
        self.sm.add_widget(scr1)
        self.sm.add_widget(scr2)
        self.sm.add_widget(scr3)
        self.sm.add_widget(scr4)
        self.sm.add_widget(scr5)
        self.sm.add_widget(scr6)
        self.sm.add_widget(scr7)
        self.sm.add_widget(scr8)
        self.sm.add_widget(scr9)
        self.sm.add_widget(scr10)
        self.sm.add_widget(scrStory)
        self.sm.add_widget(FeedBackScr)
        self.sm.current='Main Screen'

        return self.sm


    def toset1(self, instance):

        self.sm.current='First MDScreen'
    def toset2(self, instance):

        self.sm.current='Second MDScreen'
    def toset3(self, instance):

        self.sm.current='Third MDScreen'
    def toset4(self, instance):

        self.sm.current='Fourth MDScreen'
    def toset5(self, instance):

        self.sm.current='Fifth MDScreen'
    def toset6(self, instance):

        self.sm.current='Sixth MDScreen'
    def toset7(self, instance):

        self.sm.current='Seventh MDScreen'
    def toset8(self, instance):

        self.sm.current='Eighth MDScreen'
    def toset9(self, instance):

        self.sm.current='Ninth MDScreen'
    def toset10(self, instance):

        self.sm.current='Tenth MDScreen'
    def tosetStory(self, instance):

        self.sm.current='Story'
    def tosetFB(self, instance):

        self.sm.current='Feedback'

    def tomain(self, instance):
        if self.sm.current=='First MDScreen':
            self.scr1rez.text = str("Результат: ")
            self.scr1inp1.text = ''
            self.scr1inp2.text = ''
        elif self.sm.current=='Second MDScreen':
            self.scr2rez.text = str("Результат: ")
            self.scr2inp1.text = ''
            self.scr2inp2.text = ''
        elif self.sm.current=='Third MDScreen':
            self.scr3rez.text = str("Результат: ")
            self.scr3inp1.text = ''
            self.scr3inp2.text = ''
        elif self.sm.current=='Fourth MDScreen':
            self.scr4rez.text = str("Результат: ")
            self.scr4inp1.text = ''
            self.scr4inp2.text = ''
        elif self.sm.current=='Fifth MDScreen':
            self.scr5rez.text = str("Результат: ")
            self.scr5inp1.text = ''
            self.scr5inp2.text = ''
        elif self.sm.current=='Sixth MDScreen':
            self.scr6rez.text = str("Результат: ")
            self.scr6inp1.text = ''
            self.scr6inp2.text = ''
        elif self.sm.current=='Seventh MDScreen':
            self.scr7rez.text = str("Результат: ")
            self.scr7inp1.text = ''
            self.scr7inp2.text = ''
            self.scr7inp3.text = ''
        elif self.sm.current=='Eighth MDScreen':
            self.scr8rez.text = str("Результат: ")
            self.scr8inp1.text = ''
            self.scr8inp2.text = ''
            self.scr8inp3.text = ''
        elif self.sm.current=='Ninth MDScreen':
            self.scr9rez.text = str("Результат: ")
            self.scr9inp1.text = ''
            self.scr9inp2.text = ''
        elif self.sm.current=='Tenth MDScreen':
            self.scr10rez.text = str("Результат: ")
            self.scr10inp1.text = ''
            self.scr10inp2.text = ''
        if len(self.scrStoryrez.text)>1000:
            self.scrStoryrez.text = "История:\n"

        self.sm.current='Main Screen'
    def scr1count(self, instance):
        try:
            (float(self.scr1inp1.text) * float(self.scr1inp2.text) / 100)
            self.scr1rez.text = f"Результат: {self.scr1inp2.text}% \nот числа {self.scr1inp1.text} \n составляет {round((float(self.scr1inp1.text)*float(self.scr1inp2.text)/100),5)}\n"
            self.scr1inp1.text=''
            self.scr1inp2.text = ''
            self.scrStoryrez.text+= self.scr1rez.text
        except OverflowError:
            self.scr1rez.text = str("Вы ввели слишком большое число, \nк сожалению, не сможем посчитать(")
        except:
            self.scr1rez.text = str("Результат: Нельзя ставить ноль или пусто")
    def scr2count(self, instance):
        try:
            float(self.scr2inp1.text) / float(self.scr2inp2.text)
            self.scr2rez.text = f"Результат: Число {self.scr2inp1.text}\nсоставляет {round(((float(self.scr2inp1.text))/float(self.scr2inp2.text)*100),5)}% \nот числа {self.scr2inp2.text}\n"
            self.scr2inp1.text = ''
            self.scr2inp2.text = ''
            self.scrStoryrez.text += self.scr2rez.text
        except OverflowError:
            self.scr2rez.text = str("Вы ввели слишком большое число, \nк сожалению, не сможем посчитать(")
        except:
            self.scr2rez.text = str("Результат: Нельзя ставить ноль или пусто")


    def scr3count(self, instance):
        try:
            (float(self.scr3inp1.text) * (1 + (float(self.scr3inp2.text) / 100)))
            self.scr3rez.text = f"Результат: Число {self.scr3inp1.text}\nувеличенное на {self.scr3inp2.text}% \n составляет {round((float(self.scr3inp1.text)*(1+(float(self.scr3inp2.text)/100))),5)}\n"
            self.scr3inp1.text = ''
            self.scr3inp2.text = ''
            self.scrStoryrez.text += self.scr3rez.text
        except OverflowError:
            self.scr3rez.text = str("Вы ввели слишком большое число, \nк сожалению, не сможем посчитать(")
        except:
            self.scr3rez.text = str("Результат: Нельзя ставить ноль или пусто")


    def scr4count(self, instance):
        try:
            (float(self.scr4inp1.text) * (1 - (float(self.scr4inp2.text) / 100)))
            self.scr4rez.text =f"Результат: Число {self.scr4inp1.text} \nуменьшенное на {self.scr4inp2.text}% \n составляет {round((float(self.scr4inp1.text)*(1-(float(self.scr4inp2.text)/100))),5)}\n"
            self.scr4inp1.text = ''
            self.scr4inp2.text = ''
            self.scrStoryrez.text += self.scr4rez.text
        except OverflowError:
            self.scr4rez.text = str("Вы ввели слишком большое число, \nк сожалению, не сможем посчитать(")
        except:
            self.scr4rez.text = str("Результат: Нельзя ставить ноль или пусто")


    def scr5count(self, instance):
        try:
            float(self.scr5inp2.text) / float(self.scr5inp1.text)
            self.scr5rez.text = f"Результат: Каждый {self.scr5inp1.text}\nот числа {self.scr5inp2.text}\n составляет {round((float(self.scr5inp2.text) / float(self.scr5inp1.text)),5)}\n"
            self.scr5inp1.text = ''
            self.scr5inp2.text = ''
            self.scrStoryrez.text += self.scr5rez.text
        except OverflowError:
            self.scr5rez.text = str("Вы ввели слишком большое число, \nк сожалению, не сможем посчитать(")
        except:
            self.scr5rez.text = str("Результат: Нельзя ставить ноль или пусто")

    def scr6count(self, instance):
        try:
            float(self.scr6inp2.text) / float(self.scr6inp1.text)
            self.scr6rez.text = f"Результат: {self.scr6inp1.text} часть \nот числа {self.scr6inp2.text}\n составляет {round((float(self.scr6inp2.text) / float(self.scr6inp1.text)),5)}\n"
            self.scr6inp1.text = ''
            self.scr6inp2.text = ''
            self.scrStoryrez.text += self.scr6rez.text
        except OverflowError:
            self.scr6rez.text = str("Вы ввели слишком большое число, \nк сожалению, не сможем посчитать(")
        except:
            self.scr6rez.text = str("Результат: Нельзя ставить ноль или пусто")


    def scr7count(self, instance):
        try:
            float(self.scr7inp1.text)/float(self.scr7inp2.text) * float(self.scr7inp3.text)
            self.scr7rez.text = f"Результат: Дробь {self.scr7inp1.text}/{self.scr7inp2.text}\nот числа {self.scr7inp3.text}\n составляет {round((float(self.scr7inp1.text)/float(self.scr7inp2.text) * float(self.scr7inp3.text)),5)}\n"
            self.scr7inp1.text = ''
            self.scr7inp2.text = ''
            self.scr7inp3.text = ''
            self.scrStoryrez.text += self.scr7rez.text
        except OverflowError:
            self.scr7rez.text = str("Вы ввели слишком большое число, \nк сожалению, не сможем посчитать(")
        except:
            self.scr7rez.text = str("Результат: Нельзя ставить ноль или пусто")


    def scr8count(self, instance):
        try:
            float(self.scr8inp1.text) / (float(self.scr8inp2.text)/float(self.scr8inp3.text))
            self.scr8rez.text = f"Результат: Число {self.scr8inp1.text} \n деленное на дробь {self.scr8inp2.text}/{self.scr8inp3.text}\n составляет {round((float(self.scr8inp1.text) / (float(self.scr8inp2.text)/float(self.scr8inp3.text))),5)}\n"
            self.scr8inp1.text = ''
            self.scr8inp2.text = ''
            self.scr8inp3.text = ''
            self.scrStoryrez.text += self.scr8rez.text
        except OverflowError:
            self.scr8rez.text = str("Вы ввели слишком большое число, \nк сожалению, не сможем посчитать(")
        except:
            self.scr8rez.text = str("Результат: Нельзя ставить ноль или пусто")

    def scr9count(self, instance):
        try:
            (float(self.scr9inp1.text) / float(self.scr9inp2.text))
            self.scr9rez.text = f"Результат: Число {self.scr9inp1.text} (с НДС), составляют: \nбез НДС: {(float(self.scr9inp1.text) / (100+float(self.scr9inp2.text)))*100}.\n Сумма НДС {self.scr9inp2.text}%: {float(self.scr9inp1.text) / (float(100)+float(self.scr9inp2.text))*float(self.scr9inp2.text)}\n"
            self.scr9inp1.text = ''
            self.scr9inp2.text = ''
            self.scrStoryrez.text += self.scr9rez.text
        except OverflowError:
            self.scr9rez.text = str("Вы ввели слишком большое число, \nк сожалению, не сможем посчитать(")
        except:
            self.scr9rez.text = str("Результат: Нельзя ставить ноль или пусто")
    def scr10count(self, instance):
        try:
            (float(self.scr10inp1.text) ** float(self.scr10inp2.text))
            self.scr10rez.text = f"Результат: Число {self.scr10inp1.text}\nв степени {self.scr10inp2.text}\nсоставляет: {float(self.scr10inp1.text) ** (float(self.scr10inp2.text))}\n"
            self.scr10inp1.text = ''
            self.scr10inp2.text = ''
            self.scrStoryrez.text += self.scr10rez.text
        except OverflowError:
            self.scr10rez.text = str("Вы ввели слишком большое число, \nк сожалению, не сможем посчитать(")
        except:
            self.scr10rez.text = str("Результат: Нельзя ставить ноль или пусто")


    def scrStorycount(self, instance):
            self.scrStoryrez.text = str("История:\n")


    def key_input(self, window, key, scancode, codepoint, modifier):
        if key == 27 and self.sm.current != 'Main Screen':

            self.sm.current = 'Main Screen'
            return True
        else:
            return False




    def privacy(self, x):
        x='https://docs.yandex.ru/docs/view?url=ya-disk-public%3A%2F%2FpPlCTRuztDbO5ekyhCfvieZqIbcQawDaq0G%2FTYg2dQgEvum8WBqtO1k6Oi%2Ftk6Btq%2FJ6bpmRyOJonT3VoXnDag%3D%3D&name=%D0%9D%D0%BE%D0%B2%D1%8B%D0%B9%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82.docx'
        webbrowser.open_new_tab(x)

class FloatInput(MDTextField):
    line_color_normal =(0, 0, 0, 1)
    line_color_focus = (0, 0, 0, 1)
    hint_text_color_normal = (0, 0, 0, 1)
    hint_text_color_focus = (0, 0, 0, 1)
    text_color_focus = (0, 0, 0, 1)
    pat = re.compile('[^0-9]')
    def insert_text(self, substring, from_undo=False):
        pat = self.pat
        if '.' in self.text:
            s = re.sub(pat, '', substring) #замена не чисел на ничто (убирает)
        else:
            s = '.'.join(re.sub(pat, '', s) for s in substring.split('.', 1))



        return super().insert_text(s, from_undo=from_undo)




if __name__ == '__main__':
    MyApp().run()
