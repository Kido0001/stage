import os
import openai
from colorama import Fore, Style
from dotenv import load_dotenv

load_dotenv()
sujet = "Minecraft Bedrock"
# menu (work with main)
def menu_menu():
  """
  Affiche le menu et dirige l'utilisateur vers les options choisies.
  Displays the menu and directs the user to the chosen options.
  """
  menu_items = ["Craft", "Quest", "Build", "Help"]

  print("Où voulez-vous aller ?")
  for index, item in enumerate(menu_items, 1):
    print(f"{index}. {item}")

  choice = int(input("Veuillez entrer un numéro :"))

  if 1 <= choice <= len(menu_items):
    print(f"Vous avez choisi : {menu_items[choice - 1]}")
  else:
    print("choix invalide")

  if choice == 1:
    menu_craft()

  elif choice == 2:
    menu_quest()

  elif choice == 3:
    menu_build()

  elif choice == 4:
    menu_help()
# craft
def menu_craft():
  """
  Demande a l'utilisateur un craft. Les entrées sont envoyer a OpenAI.
  Asks the user for a craft. Input is sent to OpenAI.
  """
  exit_condition = False

  while not exit_condition:
    item = input(Style.BRIGHT + Fore.BLUE + "Quel est l'item dont vous voulez connaitre le craft ?")
    #retour menu
    if item == "exit":
      """
       Si l'entré est = a exit, l'utilisateur retourne au menu_menu().
       If the input is = a exit, the user returns to the menu() menu.
      """
      exit_condition = True
    #AI
    else:
      prompt = f"Affiche uniquement en Grille le craft de {item} dans {sujet}"
      completion = openai.ChatCompletion.create(
        model="gpt-4o",
        temperature=0,
        messages=[{"role": "user", "content": prompt}]
      )
      print(Fore.WHITE + completion['choices'][0]['message']['content'])
#quest
def menu_quest():
  """
  Demande le niveau de difficulté du défi.
  Ask for the difficulty level of the challenge.
  """

  exit_condition = False
  difficulty = ["Extrême", "Normal", "symple"]

  #Choice of difficulty
  while not exit_condition:
    print("Choisissez la difficulty")
    for index, item in enumerate(difficulty, 1):
      print(f"{index}. {item}")

    choice =input("Veuillez entrer un numéro :")
    #return to the menu
    if str(choice) == "exit":
      exit_condition = True
    #AI
    else:
      prompt = f"Donne moi un défi dans {sujet} original est avec comme difficulter : {difficulty[int(choice) - 1]}"
      completion = openai.ChatCompletion.create(
        model="gpt-4o",
        temperature=1,
        messages=[{"role": "user", "content": prompt}]
      )
      print(Fore.WHITE + completion['choices'][0]['message']['content'])
#build
def menu_build():
  """
  Demmande la taille de la maison ainsi que le style.
  Ask for the size of the house as well as the style.
  """
  exit_condition = False
  # IA
  while not exit_condition:
    confirmation = input(Style.BRIGHT + Fore.BLUE + "Êtes-vous sûr de vouloir faire une maison ?")
    #return to the menu
    if confirmation == "exit":
      exit_condition = True
    else:
      size = input(Style.BRIGHT + Fore.BLUE + "Quelle est la taille de la maison ? (x, z, y)")
      style = input(Style.BRIGHT + Fore.BLUE + "Quel est le style ?")
      prompt = f"Explique consiment comment faire une maison de {size} dans le style {style} dans {sujet}"

      completion = openai.ChatCompletion.create(
        model="gpt-4o",
        temperature=1,
        messages=[{"role": "user", "content": prompt}]
      )
      print(Fore.WHITE + completion['choices'][0]['message']['content'])
#help
def menu_help():
  """
  Readme : https://github.com/Kido0001/stage/blob/master/README.md
  """
  functions = [menu_craft, menu_quest, menu_build, main, menu_help]
  for functions in functions:
    print(f"{functions.__name__} : {functions.__doc__}")
# main (creates a loop, basic function)
def main():
  """
  Fonction principale du programme qui lance le menu principal.
  Main function of the program that launches the main menu.
  """
  openai.api_key = os.getenv("OPENAI_KEY")
  while True:
    menu_menu()
if __name__ == "__main__":
  main()