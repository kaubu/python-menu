# python-menu
A module to create static menus in python.
You do not need the menu_example*.py files, as those are just examples on how to use the code.

## Example
This code is from menu_example.py, which shows how you can import the menu module and use it.

```python
import menu
import menu_example_config as config

main_menu = menu.Menu(config.example_main_menu_obj)
main_menu.start()
```
## TODO
* Change text input to keyboard input
