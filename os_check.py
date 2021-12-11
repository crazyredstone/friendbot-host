import os

def checkmaster():
    print(os.getcwd())
    print("CheckMaster сейчас проверит корневую папку бота, на наличие папки logs.")
    if os.path.exists("logs"):
        createpath = "Папка имеется, создание отменяется..."
    else:
        createpath = "Папка для логов не найдена, создание новой...", os.mkdir("logs")
    return createpath


logpath = checkmaster()
print(logpath)
