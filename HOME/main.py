from HOME.CRAFT.craft import menu_craft

menu_items = ["Craft", "Quest", "Build"]

print("Où voulez vous aller ?")
for index, item in enumerate(menu_items, 1):
  print(f"{index}. {item}")

choice = int(input("Veuillez entrer un numéro :"))

if 1 <= choice <= len(menu_items):
  print(f"Vous avez choisi : {menu_items[choice-1]}")
else:
  print("choix invalide")

if choice == 1:
  menu_craft()

if choice == 2:
  menu_craft()

if choice == 3:
  menu_craft()

