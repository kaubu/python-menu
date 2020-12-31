from os import system

def back(menu_obj): Menu(menu_obj).start()

class Menu:
	def __init__(self, menu_obj):
		self.menu_obj = menu_obj
		self.parent_obj = None # Change if you want to do multiple menus

	def start(self):
		system("cls")

		for k, v in self.menu_obj.items(): print(k)

		selection = str(input(">> "))

		for k, v in self.menu_obj.items():
			if selection == v["key"]:
				if v["action"] == back: # Use menu.back if importing
					back(self.parent_obj)
				else:
					v["action"]()