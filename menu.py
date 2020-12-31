from os import system

def qmenu(menu_obj): Menu(menu_obj).start() # Quick Menu. Initializes a menu in one line.

class Menu:
	def __init__(self, menu_obj): self.menu_obj = self.parent_obj = menu_obj # Change self.parent_obj if you want to do nested menus

	def start(self):
		valid_input = False

		system("cls")

		for k, v in self.menu_obj.items(): print(k)

		selection = str(input(">> "))

		for i in self.menu_obj.items():
			for k, v in i[1].items():
				if callable(v): continue

				if selection in v:
					valid_input = True
					for k, v in self.menu_obj.items():
						if selection == v["key"]:
							if v["action"] == qmenu: # Use menu.qmenu if importing
								qmenu(self.parent_obj)
							else:
								v["action"]()

						elif selection == "":
							qmenu(self.menu_obj)

		#if not valid_input: 
		if valid_input == False: qmenu(self.menu_obj)