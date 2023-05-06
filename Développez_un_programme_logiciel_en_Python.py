from view import View
import logging

<<<<<<< HEAD
logging.basicConfig(level=logging.INFO)
=======
>>>>>>> 74c0f9e7c5c326ae1b397e153ed0caba29f7d80a
if __name__ == "__main__":
    
    logging.debug("Loging configure")
    view = View()
    while True:
        view.menu(True)
