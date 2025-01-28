import os.path
import os
import sys
import time
import openai
from colorama import Fore, Style
from dotenv import load_dotenv

animation = "|/-\\"
start_time = time.time()
while True:
  for i in range(25) :
    time.sleep(0.2)
    sys.stdout.write("\r" + "initialisation" + animation[i % len(animation)])
    sys.stdout.flush()
  if time.time() - start_time > 1:
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
        menu_craft()

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