import tkinter as tk
from parsing import *
import webbrowser

root = tk.Tk()
root.title("Atmosphere App")



def App():
    
    def get_data():
      dollar = get_currency(DOLLAR_TENGE)
      euro = get_currency(EURO_TENGE)
      ruble = get_currency(RUBLE_TENGE)
      tiktok = atmosphere_tiktok(ATMO_TIKTOK)
      github = count_project(GITHUB)
      weather = get_weather(ALMATY_WEATHER)
      ALL_DATA = [dollar, euro, ruble, tiktok, github, weather]
      return ALL_DATA
    
    def add_values(ALL_DATA):
      global dollar_value, euro_value, ruble_value, tiktok_value, github_value, weather_value1, weather_value2, weather_value3, weather_value4

      dollar_value = tk.Label(root, text=f"{ALL_DATA[0][0]} тг.", font=("Arial", 15))
      dollar_value.grid(row=1, column=1, padx=10, pady=10)
      euro_value = tk.Label(root, text=f"{ALL_DATA[1][0]} тг.", font=("Arial", 15))
      euro_value.grid(row=2, column=1, padx=10, pady=10)
      ruble_value = tk.Label(root, text=f"{ALL_DATA[2][0]} тг.", font=("Arial", 15))
      ruble_value.grid(row=3, column=1, padx=10, pady=10)
      tiktok_value = tk.Label(root, text=f"{ALL_DATA[3][0]} подписчиков", font=("Arial", 15))
      tiktok_value.grid(row=4, column=1, padx=10, pady=10)
      github_value = tk.Label(root, text=f"{ALL_DATA[4][0]} проектов", font=("Arial", 15))
      github_value.grid(row=5, column=1, padx=10, pady=10)

      weather_value1 = tk.Label(root, text=f"{ALL_DATA[5][0]}°C", font=("Arial", 15))
      weather_value1.grid(row=7, column=1, padx=10, pady=5)
      weather_value2 = tk.Label(root, text=f"{ALL_DATA[5][1]}", font=("Arial", 15))
      weather_value2.grid(row=8, column=1, padx=10, pady=5)
      weather_value3 = tk.Label(root, text=f"{ALL_DATA[5][2]}", font=("Arial", 15))
      weather_value3.grid(row=9, column=1, padx=10, pady=5)
      weather_value4 = tk.Label(root, text=f"{ALL_DATA[5][3]}", font=("Arial", 15))
      weather_value4.grid(row=10, column=1, padx=10, pady=5)

    
    def destroy_labels():
      dollar_value.destroy()
      euro_value.destroy()
      ruble_value.destroy()
      tiktok_value.destroy()
      github_value.destroy()
      weather_value1.destroy()
      weather_value2.destroy()
      weather_value3.destroy()
      weather_value4.destroy()
    
    # Методы
    def refresh():
        ALL_DATA = get_data()
        destroy_labels()
        add_values(ALL_DATA=ALL_DATA)
        


    # Заголовок
    label = tk.Label(root, text="Atmosphere App", font=("Arial", 20), background="black", foreground="white", border=5)
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    # Доллар
    dollar_label = tk.Label(root, text="Курс доллара: ", font=("Arial", 15))
    dollar_label.grid(row=1, column=0, padx=10, pady=10)

    # Евро
    euro_label = tk.Label(root, text="Курс евро: ", font=("Arial", 15))
    euro_label.grid(row=2, column=0, padx=10, pady=10)

    # Рубль
    ruble_label = tk.Label(root, text="Курс рубля: ", font=("Arial", 15))
    ruble_label.grid(row=3, column=0, padx=10, pady=10)

    # TikTok
    tiktok_label = tk.Label(root, text="TikTok: ", font=("Arial", 15))
    tiktok_label.grid(row=4, column=0, padx=10, pady=10)

    # GitHub
    github_label = tk.Label(root, text="GitHub: ", font=("Arial", 15))
    github_label.grid(row=5, column=0, padx=10, pady=10)

    # Разделитель
    separator = tk.Label(root, text="----------------------------------------", font=("Arial", 15))
    separator.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    # Погода
    weather_label1 = tk.Label(root, text="Температура: ", font=("Arial", 15))
    weather_label1.grid(row=7, column=0, padx=10, pady=5)
    weather_label2 = tk.Label(root, text="Скорость ветра: ", font=("Arial", 15))
    weather_label2.grid(row=8, column=0, padx=10, pady=5)
    weather_label3 = tk.Label(root, text="Влажность: ", font=("Arial", 15))
    weather_label3.grid(row=9, column=0, padx=10, pady=5)
    weather_label4 = tk.Label(root, text="Вероятность осадков: ", font=("Arial", 15))
    weather_label4.grid(row=10, column=0, padx=10, pady=5)

    # Значения
    ALL_DATA = get_data()
    add_values(ALL_DATA=ALL_DATA)

    # Обновить
    update_button = tk.Button(root, text="Обновить", font=("Arial", 20), bg="white", fg="black",  command=refresh)
    update_button.grid(row=11, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

    # GitHub кнопка
    github_button = tk.Button(root, width=15, text="Github", command=lambda: webbrowser.open("https://github.com/krivalex"), bg="gray", fg="white")
    github_button.grid(row=12, column=0, columnspan=1, sticky="")

    # Instagram кнопка
    instagram_button = tk.Button(root, width=15, text="Instagram", command=lambda: webbrowser.open("https://www.instagram.com/_krivalex_/"), bg="purple", fg="white")
    instagram_button.grid(row=12, column=1, columnspan=1)

    # YouTube кнопка
    youtube_button = tk.Button(root, width=15, text="YouTube", command=lambda: webbrowser.open("https://www.youtube.com/channel/UCledP-8WCQCAy_1zrj4vukA"), bg="red", fg="white")
    youtube_button.grid(row=13, column=0, columnspan=1)

    # TikTok кнопка
    tiktok_button = tk.Button(root, width=15, text="TikTok", command=lambda: webbrowser.open("https://www.tiktok.com/@atmosphere.it"), bg="black", fg="white")
    tiktok_button.grid(row=13, column=1, columnspan=1)

    # Telegram кнопка
    telegram_button = tk.Button(root, width=15, text="Telegram", command=lambda: webbrowser.open("https://t.me/Krivalex"), bg="blue", fg="white")
    telegram_button.grid(row=14, column=0)

    # Spotify кнопка
    spotify_button = tk.Button(root, text="Spotify", width=15, command=lambda: webbrowser.open("https://open.spotify.com/user/oshhl48dq6dslgqey3vsgxn3p"), bg="green", fg="white")
    spotify_button.grid(row=14, column=1)



    





if __name__ == "__main__":
    App()
    root.mainloop()
