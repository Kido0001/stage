import os.path
import time
import sys
import os
import openai
import colorama
from colorama import Fore, Style
from dotenv import load_dotenv
load_dotenv()

def menu_craft():

  condition = False

  openai.api_key = os.getenv("OPENAI_KEY")

  while not condition:
    sujet = "Minecraft"
    item = input( Style.BRIGHT + Fore.BLUE +"Quelle est l'iteam d'on vous vouler connaitre le craft ?")
    prompt = f"Affiche uniquemment en Grille le craft de {item}"
    #prompt = f"Explique tres brievement comment crafter {item} dans {sujet} et ce en expliquant uniquement les materiaux n'hessecaire et leurs empacement"

    completion = openai.ChatCompletion.create(
      model="gpt-4o",
      temperature=1,
      #  max_tokens=,
      messages=[{"role": "user", "content": prompt}]
    )
    print(Fore.WHITE + ['choices'][0]['message']['content'])
  if user_input.lower() == "stop":
    condition = True