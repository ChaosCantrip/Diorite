import os

print("Starting Diorite Launcher Script")

while True:
    os.system("sudo git pull")

    if os.path.exists("reboot"):
        # Reboot the bot
        os.remove("reboot")
        os.system("sudo reboot")
    elif os.path.exists("restart"):
        # Restart the bot
        os.remove("restart")
        os.system("sudo -E python main.py")
    else:
        # Enter maintenance mode
        os.system("sudo -E python maintenance.py")
