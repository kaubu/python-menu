import menu

# Functions
def new_game(): print("Starting new game...")

def load_game():
	load_menu = menu.Menu(example_load_menu_obj)
	load_menu.parent_obj = example_main_menu_obj
	load_menu.start()

def settings():
	settings_menu = menu.Menu(example_settings_menu_obj)
	settings_menu.parent_obj = example_main_menu_obj
	settings_menu.start()

def game_quit(): quit()

def load_save_1(): print("Loading Save 1...")
def load_save_2(): print("Loading Save 2...")
def load_save_3(): print("Loading Save 3...")

def graphics(): print("Showing Graphics settings...")
def controls(): print("Showing Controls settings...")
def sound(): print("Showing Sound settings...")

# Menu Objects
example_main_menu_obj = {
	"[1] New Game": {
		"action": new_game,
		"key": "1"
	},
	"[2] Load Game": {
		"action": load_game,
		"key": "2"
	},
	"[3] Settings": {
		"action": settings,
		"key": "3"
	},
	"[4] Quit": {
		"action": game_quit,
		"key": "4"
	}
}

example_load_menu_obj = {
	"[1] Load Save 1": {
		"action": load_save_1,
		"key": "1"
	},
	"[2] Load Save 2": {
		"action": load_save_2,
		"key": "2"
	},
	"[3] Load Save 3": {
		"action": load_save_3,
		"key": "3"
	},
	"[4] Back": {
		"action": menu.back,
		"key": "4"
	}
}

example_settings_menu_obj = {
	"[1] Graphics": {
		"action": graphics,
		"key": "1"
	},
	"[2] Controls": {
		"action": controls,
		"key": "2"
	},
	"[3] Sound": {
		"action": sound,
		"key": "3"
	},
	"[4] Back": {
		"action": menu.back,
		"key": "4"
	}
}