# import pandas as pd
# data=pd.read_csv("list-indian-states-and-capitals-28j.csv")
# data["State Name"].to_json("states.json")

""" import json
 state=json.load(open("json/states.json"))
 location=json.load(open("json/locations.json"))
 combine={}
 for i in range(29):
     combine[state[f"{i}"]]=location[i]
# json.dump(combine,open("json/states_with_coords.json","w")"""
import pyautogui as pg
import json
content=json.load(open("/home/anasmohammed361/vs/Python Course/Turtle/india_map_game/json/states.json")).values()
pg.sleep(5)
for i in content:
     print(i)
     pg.typewrite(i)
     pg.press("return")
     pg.sleep(2)
