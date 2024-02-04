import os
import time

def print_logo():
    print("""
 _____  _            _____  _           
| __  || | _ _  ___ |   __|| | _ _  ___ 
| __ -|| || | || -_||__   || || | || -_|
|_____||_||___||___||_____||_||___||___|
                                            
    """)

def cmd_help():
    print("\nAvailable commands:")
    print("  dir")
    print("  cd")
    print("  ping")
    print("  tracert")
    print("  ipconfig")
    print("  find")
    print("  tree")
    print("  cls")
    print("  color")
    print("  systeminfo")
    print("  date")
    print("  time")
    print("  whoami")
    print("  tasklist")
    print("  notepad")
    print("  calc")
    print("  python")
    print("  exit")
    print("  create_file")
    print("  delete_file")
    print("  read_file")
    print("  write_file")
    print("  network_status")
    print("  network_interfaces")
    print("  create_user")
    print("  hardware_info")
    print("  welcome_message")

def cmd_dir():
    os.system("dir")

def cmd_ping():
    hostname = input("Enter the hostname or IP address to ping: ")
    os.system("ping " + hostname)

def cmd_tracert():
    hostname = input("Enter the hostname or IP address to trace route: ")
    os.system("tracert " + hostname)

def cmd_ipconfig():
    os.system("ipconfig")

def cmd_find():
    filename = input("Enter the filename to search for: ")
    os.system("dir /s /b " + filename)

def cmd_tree():
    os.system("tree")

def cmd_color():
    os.system("color")

def cmd_date():
    os.system("date")

def cmd_time():
    os.system("time")

def cmd_whoami():
    os.system("whoami")

def cmd_tasklist():
    os.system("tasklist")

def cmd_notepad():
    filename = input("Enter the filename to open with notepad: ")
    os.system("notepad " + filename)

def cmd_calc():
    os.system("calc")

def cmd_python():
    os.system("python")

def cmd_create_file():
    filename = input("Enter the filename to create: ")
    os.system("echo. > " + filename)

def cmd_delete_file():
    filename = input("Enter the filename to delete: ")
    os.system("del " + filename)

def cmd_read_file():
    filename = input("Enter the filename to read: ")
    os.system("type " + filename)

def cmd_write_file():
    filename = input("Enter the filename to write to: ")
    content = input("Enter the content to write: ")
    with open(filename, "w") as file:
        file.write(content)

def cmd_network_status():
    os.system("netstat -a")

def cmd_network_interfaces():
    os.system("ipconfig /all")

def cmd_create_user():
    username = input("Enter the username to create: ")
    os.system("net user " + username + " /add")

def cmd_hardware_info():
    os.system("wmic cpu get name /format:list")
    os.system("wmic memorychip list /format:list")
    os.system("wmic diskdrive get name /format:list")
    os.system('systeminfo | findstr "OS Name" "OS Version"')

def cmd_welcome_message():
    username = os.getenv('username')
    print(f"Welcome {username} to BINXX!")

def main():
    print_logo()

    while True:
        command = input("\nBINXX> ")

        if command == "dir":
            cmd_dir()

        elif command == "ping":
            cmd_ping()

        elif command == "tracert":
            cmd_tracert()

        elif command == "ipconfig":
            cmd_ipconfig()

        elif command == "find":
            cmd_find()

        elif command == "tree":
            cmd_tree()

        elif command == "color":
            cmd_color()

        elif command == "date":
            cmd_date()

        elif command == "time":
            cmd_time()

        elif command == "whoami":
            cmd_whoami()

        elif command == "tasklist":
            cmd_tasklist()

        elif command == "notepad":
            cmd_notepad()

        elif command == "calc":
            cmd_calc()

        elif command == "python":
            cmd_python()

        elif command == "create_file":
            cmd_create_file()

        elif command == "delete_file":
            cmd_delete_file()

        elif command == "read_file":
            cmd_read_file()

        elif command == "write_file":
            cmd_write_file()

        elif command == "network_status":
            cmd_network_status()

        elif command == "network_interfaces":
            cmd_network_interfaces()

        elif command == "create_user":
            cmd_create_user()

        elif command == "hardware_info":
            cmd_hardware_info()

        elif command == "welcome_message":
            cmd_welcome_message()

        elif command == "exit":
            print("Exiting BINXX...")
            time.sleep(2)
            break

        elif command == "help":
            cmd_help()

        else:
            print("Invalid command. Type 'help' to see available commands.")

if __name__ == "__main__":
    main()