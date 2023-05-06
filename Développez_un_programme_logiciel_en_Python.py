from view import View
import logging

logging.basicConfig(level=logging.INFO)
if __name__ == "__main__":
    
    logging.debug("Loging configure")
    view = View()
    while True:
        view.menu(True)

