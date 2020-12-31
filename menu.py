from os import system

def qmenu(menu_obj): Menu(menu_obj).start() # Quick Menu. Initializes a menu in one line.

class Menu:
	def __init__(self, menu_obj):
		self.menu_obj = menu_obj
		self.parent_obj = menu_obj # Change if you want to do multiple menus

	def start(self):
		system("cls")

		for k, v in self.menu_obj.items(): print(k)

		selection = str(input(">> "))

		for i in self.menu_obj.items():
			for k, v in i[1].items():
				if callable(v): continue

				if selection in v:
					for k, v in self.menu_obj.items():
						if selection == v["key"]:
							if v["action"] == qmenu: # Use menu.qmenu if importing
								qmenu(self.parent_obj)
							else:
								v["action"]()

						elif selection == "":
							qmenu(self.menu_obj)
