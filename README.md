# python-menu
A module to create static menus in python.
You do not need the menu_example*.py files, as those are just examples on how to use the code.

## Example
This code is from an example file, which shows how you can import the menu module and use it.  
There is another example in menu_example.py, which is split between itself and menu_example_config.py which has all of the menus and functions.

```python
import menu

def hello_world(): print("Hello World!")

def nested_menu_func(): 
	nested_menu = menu.Menu(nested_menu_obj)
	nested_menu.parent_obj = menu_obj
	nested_menu.start()

def add_num(): print (int(input("Number 1: ")) + int(input("Number 2: ")))

def echo(): print(input("Text to echo: "))

def sub_num(): print (int(input("Number 1: ")) - int(input("Number 2: ")))

menu_obj = {
	"[1] print Hello World": {
		"action": hello_world,
		"key": "1"
	},
	"[2] Nested Menu": {
		"action": nested_menu_func,
		"key": "2"
	},
	"[3] Add two numbers": {
		"action": add_num,
		"key": "3"
	}
}

nested_menu_obj = {
	"[1] Echo text": {
		"action": echo,
		"key": "1"
	},
	"[2] Subtract two numbers": {
		"action": sub_num,
		"key": "2"
	},
	"[3] Back": {
		"action": menu.qmenu,
		"key": "3"
	}
}

main_menu = menu.Menu(menu_obj)
main_menu.start()
```
## TODO
* Change text input to keyboard input
