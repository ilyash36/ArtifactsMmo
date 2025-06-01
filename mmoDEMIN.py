import time
import requests
from tkinter import *
from tkinter import ttk

# Класс Action созданный для методов действия персонажа
class Action:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InZucXNjaWF0QGdtYWlsLmNvbSIsInBhc3N3b3JkX2NoYW5nZWQiOiIifQ.N8OuQXJXnrv-KYgdFevNoiXQDrGbmICuj0WLgEOgyig",
        "Connection": "close"
    }
    # Передвинуть персонажа на x и y позицию
    def move(self, x, y):
        url = "https://api.artifactsmmo.com/my/fatmonti/action/move"
        # в payload используем int() чтобы преобразовать текст в целочисленное
        payload = {
        "x": int(x),
        "y": int(y)
        }
        response = requests.post(url, json=payload, headers=self.headers)
        print(response.json())

        #Обрабатываем нажатие кнопки и отображение кулдауна (Надо сделать нормальный метод епта )0)) )
        Button_Move["text"] = "Кулдаун..."
        Button_Move.state(["disabled"])
        Button_Move.after(11000, lambda: Button_Move.configure(state="normal", text="Передвинуть"))

    # Копать (добывать) ресурс или урожай
    def gathering(self, i):
        while i <= 10:
            url = "https://api.artifactsmmo.com/my/fatmonti/action/gathering"
            response = requests.post(url, headers=self.headers)
            print(response.json())
            i += 1
            print(f'Добыто руды: {i}')
            time.sleep(30)

# Класс Info дочерний от Action для вывода информации в статус бар
class Info(Action):
    def get_info_status_bar(self):
        url = "https://api.artifactsmmo.com/my/characters"
        response = requests.get(url, headers=super().headers)
        print(response.json())
        result_json = response.json()



# Объект класса Action для действий
Character = Action()

# Объект класса Info для отображения информации об персонаже
Status_bar = Info()

#######################################################################################################################

# MainWindow = Tk() # Создаем окно программы
# MainWindow.title("Artifact Helper Console") # Указываем заголовок программы
# MainWindow.geometry("500x500") # Устанавливаем размер окна
#
# # Поле для ввода Х
# x_position = ttk.Entry()
# x_position.pack(anchor=NW, padx = 6, pady = 6)
# # Поле для ввода Y
# y_position = ttk.Entry()
# y_position.pack(anchor=NW, padx = 6, pady = 6)
#
# # Кнопка, после нажатия которой вызывается метод Move и передаются значения из двух полей X и Y через метод .get()
# Button_Move = ttk.Button(text="Передвинуть", command =lambda: Character.move(x_position.get(), y_position.get()))
# Button_Move.pack()
#
# # Отрисовываем главное окно и саму программу
# MainWindow.mainloop()

#######################################################################################################################

Status_bar.get_info_status_bar()






