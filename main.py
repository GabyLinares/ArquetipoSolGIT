import Menu
import cache as Cache

import json
if __name__ == "__main__":
    in_app = True
    while in_app:
        c = Cache.GestorCache()
        in_app = Menu.menu(c)