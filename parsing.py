import requests
from bs4 import BeautifulSoup

DOLLAR_TENGE = 'https://www.google.com/search?q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%82&aqs=chrome.0.0i131i433i512j69i57j0i457i512j0i402j0i131i433i512j0i512l5.5420j0j7&sourceid=chrome&ie=UTF-8'
RUBLE_TENGE = 'https://www.google.com/search?q=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&sxsrf=AJOqlzXhw_VXNUGJS7RMg0HOPt4hKpZG1w%3A1678784678841&ei=pjgQZKz0Ms-QkwXgrYuoCA&ved=0ahUKEwis376jiNv9AhVPyKQKHeDWAoUQ4dUDCA8&uact=5&oq=%D1%80%D1%83%D0%B1%D0%BB%D1%8C+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeMgYIABAHEB4yBggAEAcQHjIGCAAQBxAeOgoIABBHENYEELADOg0IABBHENYEEMkDELADOggIABCSAxCwAzoHCAAQDRCABDoNCAAQgAQQDRCxAxCDAToHCAAQgAQQDUoECEEYAFDqB1iRFmDNF2gCcAF4AIABrAGIAb8GkgEDMC41mAEAoAEByAEKwAEB&sclient=gws-wiz-serp'
EURO_TENGE = 'https://www.google.com/search?q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&sxsrf=AJOqlzWJ-LT3kK-s15fdJ8wJ19o-GfioFg%3A1678784718588&ei=zjgQZM_DI4W6sAfry4cI&ved=0ahUKEwjP4ri2iNv9AhUFHewKHevlAQEQ4dUDCA8&uact=5&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%82%D0%B5%D0%BD%D0%B3%D0%B5&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQsQMQgwEQQzIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDIHCAAQDRCABDoKCAAQRxDWBBCwAzoNCAAQRxDWBBDJAxCwAzoICAAQkgMQsAM6BwgAELADEEM6BggAEAcQHjoLCAAQBxAeEPEEEAo6CAgAEAcQHhAKOg0IABAFEAcQHhDxBBAKSgQIQRgAUPQEWMMWYIUaaANwAXgAgAHGAYgB6wqSAQMwLjiYAQCgAQHIAQrAAQE&sclient=gws-wiz-serp'

ALMATY_WEATHER = 'https://www.google.com/search?q=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%B0%D0%BB%D0%BC%D0%B0%D1%82%D0%B5&sxsrf=AJOqlzXQ5M7r-0TZ3qsG4UfPbp-VR0iN8Q%3A1678785769776&ei=6TwQZP70LvyC9u8P-52gmAw&ved=0ahUKEwi-jdirjNv9AhV8gf0HHfsOCMMQ4dUDCA8&uact=5&oq=%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0+%D0%B2+%D0%B0%D0%BB%D0%BC%D0%B0%D1%82%D0%B5&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzISCAAQgAQQsQMQgwEQChBGEIACMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKMgcIABCABBAKOgcIIxDqAhAnOgwIABDqAhC0AhBDGAE6BAgjECc6CwgAEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoICAAQsQMQgwE6CwgAEIAEEAoQARAqOgkIABCABBAKEAE6BQgAEIAEOgoIABCxAxCDARBDOgQIABBDOg8IABCxAxCDARBDEEYQgAI6DQgAELEDEIMBEMkDEEM6DQgAEIAEELEDEIMBEAo6EAgAEIAEELEDEIMBEEYQgAJKBAhBGABQAFi6KWDCKmgIcAF4AIAB0gGIAdEckgEGMC4yMC4xmAEAoAEBsAEUwAEB2gEGCAEQARgB&sclient=gws-wiz-serp'

GITHUB = 'https://github.com/krivalex'

ATMO_TIKTOK = 'https://www.tiktok.com/@atmosphere.it'
ATMO_INSTAGRAM = 'https://www.instagram.com/atmosphere_it/'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

def get_currency(url):
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"class": "DFlfde", "data-precision": "2"})
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('Нет данных')
    return result

def get_weather(url):
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert_temperature = soup.findAll("span", {"class": "wob_t q8U8x"})
    convert_wind = soup.findAll("span", {"id": "wob_ws"})
    convert_humidity = soup.findAll("span", {"id": "wob_hm"})
    convert_pressure = soup.findAll("span", {"id": "wob_pp"})
    convert = convert_temperature + convert_wind + convert_humidity + convert_pressure
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('Нет данных')
    return result


def atmosphere_tiktok(url):
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("strong", {"data-e2e": "followers-count"})
    result = []
    for c in convert:
        result.append(c.text)
    if len(result) == 0:
        result.append('Нет данных')
    return result

def count_project(url):
    full_page = requests.get(url, headers=headers)
    soup = BeautifulSoup(full_page.content, 'html.parser')
    convert = soup.findAll("span", {"data-view-component": "true", "class": "Counter"})
    result = []
    for c in convert:
        result.append(int(c.text))
    if len(result) == 0:
        result.append('Нет данных')
    return [max(result)]




# def main():
#     print(f'Курс доллара: {get_currency(DOLLAR_TENGE)}')
#     print(f'Курс евро: {get_currency(EURO_TENGE)}')
#     print(f'Курс рубля: {get_currency(RUBLE_TENGE)}')
#     print(f'Погода в Алматы: {get_weather(ALMATY_WEATHER)}')
#     print(f'Подписчики на TikTok: {atmosphere_tiktok(ATMO_TIKTOK)}')
#     print(f'Число открытых проектов на GitHub: {count_project(GITHUB)}')

# main()


