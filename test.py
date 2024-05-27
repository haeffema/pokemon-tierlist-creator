import json
import pyautogui
import time
import requests

# https://github.com/smogon/pokemon-showdown/blob/master/data/mods/gen8/formats-data.ts
# console.log(JSON.stringify(x))


counter: int = 1


def get_id(name: str) -> str:
    try:
        res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").json()
        id: str = res['id']
        return f'=IMAGE("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png")'
    except:
        return ""


def print_list(list) -> None:
    for x in list:
        time.sleep(2)
        img: str = get_id(x)
        for _ in range(counter - 1):
            pyautogui.press("tab")
        pyautogui.write(img)
        pyautogui.press("tab")
        if x in names.keys():
            pyautogui.write(names[x]["name"])
            pyautogui.press("enter")
        else:
            pyautogui.write(x)
            pyautogui.press("enter")


json_data = {}
names = {}

ou: list = []
uu: list = []
ru: list = []
nu: list = []
trash: list = []

with open("data.json", "r", encoding="utf-8") as file:
    json_data = json.loads(file.read())

with open("names.json", "r", encoding="utf-8") as file:
    names = json.loads(file.read())

for x in json_data.keys():
    if "tier" in json_data[x].keys():
        if json_data[x]["tier"] in ["OU", "UUBL"]:
            ou.append(x)
        if json_data[x]["tier"] in ["UU", "RUBL"]:
            uu.append(x)
        if json_data[x]["tier"] in ["RU", "NUBL"]:
            ru.append(x)
        if json_data[x]["tier"] in ["NU", "PUBL"]:
            nu.append(x)
        if json_data[x]["tier"] in ["PU", "ZUBL", "ZU", "NFE", "LC"]:
            trash.append(x)

ou.sort()
uu.sort()
ru.sort()
nu.sort()
trash.sort()

time.sleep(5)

for x in [{"name": "OU - 2", "list": ou}, {"name": "UU - 3", "list": uu}, {"name": "RU - 3", "list": ru}, {"name": "NU - 3", "list": nu}, {"name": "TRASH", "list": trash}]:

    for _ in range(counter):
        pyautogui.press("tab")

    pyautogui.write(x["name"])
    pyautogui.press("enter")

    print_list(x["list"])

    pyautogui.keyDown('ctrl')
    pyautogui.press('home')
    pyautogui.keyUp('ctrl')

    counter += 2
