from importlib.metadata import distribution
from tkinter import messagebox
ttkthemes_version = distribution("ttkthemes")
pytube_version = distribution("pytube")
outdated_packages = []


def list_outdated_packages():
    return "\n".join(outdated_packages)


def check_ttkthemes():
    # Separando a versão
    ttkthemes_sp = ttkthemes_version.version.split(".")
    peste2 = []
    # For para transformar cada item da lista em um inteiro.
    for item in ttkthemes_sp:
        item1 = int(item)
        peste2.append(item1)
    if peste2[0] >= 3:
        if peste2[1] >= 2:
            if peste2[2] >= 2:
                print(peste2)
                return True
            return False
        return False
    return False


def check_pytube():
    # Separando a versão
    pytube_sp = pytube_version.version.split(".")
    peste = []
    # For para transformar cada item da lista em um inteiro.
    for item in pytube_sp:
        item1 = int(item)
        peste.append(item1)
    if peste[0] >= 11:
        if peste[2] >= 2:
            print(peste)
            return True
        return False
    return False


def check_version():
    if check_ttkthemes():
        pass
    else:
        ttkthemes_np = "ttkthemes " + ttkthemes_version.version
        outdated_packages.append(ttkthemes_np)
    if check_pytube():
        pass
    else:
        pytube_np = "pytube " + pytube_version.version
        outdated_packages.append(pytube_np)
        text = f"You're using a outdated version of the following packages:\n\n{list_outdated_packages()}\n\nIf you continue, the program may not working properly.\nDo you want to continue anyway?"
        res = messagebox.askquestion('Do you want to continue?', text)
        if res == "yes":
            pass
        elif res == "no":
            exit()


if "__name__" == "__main__":
    pass
