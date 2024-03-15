import os

print("Starting Diorite Launcher Script")

while True:
    os.system("git pull")

    if os.path.exists("reboot"):
        # Reboot the bot
        os.remove("reboot")
        os.system("reboot")
    elif os.path.exists("restart"):
        # Restart the bot
        os.remove("restart")
        os.system("python main.py")
    else:
        # Enter maintenance mode
        os.system("python maintenance.py")