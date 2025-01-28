import os.path
import os
import sys
import time
import openai
from colorama import Fore, Style
from dotenv import load_dotenv



sujet = "Minecraft Bedrock"

openai.api_key = os.getenv("OPENAI_KEY")
load_dotenv()

# menu
def menu_menu():

  menu_items = ["Craft", "Quest", "Build"]

  print("Où voulez vous aller ?")
  for index, item in enumerate(menu_items, 1):
    print(f"{index}. {item}")

  choice = int(input("Veuillez entrer un numéro :"))

  if 1 <= choice <= len(menu_items):
    print(f"Vous avez choisi : {menu_items[choice - 1]}")
  else:
    print("choix invalide")

  if choice == 1:
    menu_craft()

  if choice == 2:
    menu_quest()

  if choice == 3:
    menu_craft()
# craft
def menu_craft():

  openai.api_key = os.getenv("OPENAI_KEY")
  condition = False
  item = input(Style.BRIGHT + Fore.BLUE + "Quelle est l'iteam d'on vous vouler connaitre le craft ?")

  while item == "menu":
    menu_menu()
  # IA
  if not condition:
    # sujet = "Minecraft"
    prompt = f"Affiche uniquemment en Grille le craft de {item}"
    # prompt = f"Explique tres brievement comment crafter {item} dans {sujet} et ce en expliquant uniquement les materiaux n'hessecaire et leurs empacement"

    completion = openai.ChatCompletion.create(
      model="gpt-4o",
      temperature=1,
      #  max_tokens=,
      messages=[{"role": "user", "content": prompt}]
    )
    print(Fore.WHITE + completion['choices'][0]['message']['content'])
#quest
def menu_quest():

  openai.api_key = os.getenv("OPENAI_KEY")
  condition = False

  while item == "menu":
    menu_menu()
  # IA
  if not condition:

    difficulter = ["Hard", "Normal", "Easy"]

    print("Choisisser la difficulter")
    for index, item in enumerate(difficulter, 1):
      print(f"{index}. {item}")
      choice = int(input("Veuillez entrer un numéro :"))

    prompt = f"Donne moi un défi dans {sujet} original est avec comme difficulter: {difficulter}"

    completion = openai.ChatCompletion.create(
      model="gpt-4o",
      temperature=1,
      #  max_tokens=,
      messages=[{"role": "user", "content": prompt}]
    )
    print(Fore.WHITE + completion['choices'][0]['message']['content'])