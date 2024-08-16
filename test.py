import ctypes

def show_message():
    ctypes.windll.user32.MessageBoxW(0, "ESSE é bala", "Your tidfgdfgtle", 1)