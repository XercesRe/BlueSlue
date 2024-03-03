import os
import time
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def print_logo():
    print("""
 _____  _            _____  _           
| __  || | _ _  ___ |   __|| | _ _  ___ 
| __ -|| || | || -_||__   || || | || -_|
|_____||_||___||___||_____||_||___||___|
                                            
    """)

def cmd_dir():
    content = os.listdir()
    print("Files in the current directory:")
    for item in content:
        print(item)

def cmd_cd():
    new_dir = input("Enter the directory to change to: ")
    os.chdir(new_dir)
    print(f"Changed directory to: {new_dir}")

def cmd_ping():
    host = input("Enter the host to ping: ")
    response = os.system("ping " + host)
    if response == 0:
        print(f"{host} is up!")
    else:
        print(f"{host} is down.")

def cmd_tracert():
    host = input("Enter the host to trace route to: ")
    response = os.system("tracert " + host)

def cmd_ipconfig():
    response = os.system("ipconfig")
    if response == 0:
        print("Network configuration displayed.")
    else:
        print("Error fetching network configuration.")

def cmd_find():
    file_name = input("Enter the file name to search for: ")
    result = os.system(f"dir /s /b {file_name}")
    if result == 0:
        print(f"File '{file_name}' found.")
    else:
        print(f"File '{file_name}' not found.")

def cmd_tree():
    result = os.system("tree")
    if result == 0:
        print("Directory tree displayed.")
    else:
        print("Error displaying directory tree.")

def cmd_cls():
    os.system("cls")
    print("Screen cleared.")

def cmd_color():
    color = input("Enter the color for the console (e.g., red, green, blue): ")
    os.system(f"color {color}")
    print(f"Console color changed to: {color}")

def cmd_systeminfo():
    os.system("systeminfo")

def cmd_date():
    os.system("date")

def cmd_time():
    os.system("time")

def cmd_whoami():
    os.system("whoami")

def cmd_tasklist():
    os.system("tasklist")

def cmd_notepad():
    os.system("notepad")

def cmd_calc():
    os.system("calc")

def cmd_python():
    os.system("python")

def cmd_create_file():
    file_name = input("Enter the file name to create: ")
    with open(file_name, "w") as file:
        file.write("")
    print(f"File '{file_name}' created.")

def cmd_delete_file():
    file_name = input("Enter the file name to delete: ")
    os.remove(file_name)
    print(f"File '{file_name}' deleted.")

def cmd_read_file():
    file_name = input("Enter the file name to read: ")
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print(f"Contents of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")

def cmd_write_file():
    file_name = input("Enter the file name to write to: ")
    content = input("Enter the content to write: ")
    with open(file_name, "w") as file:
        file.write(content)
    print(f"Content written to '{file_name}'.")

def cmd_network_status():
    response = os.system("ping google.com")
    if response == 0:
        print("Network status: Connected")
    else:
        print("Network status: Disconnected")

def cmd_network_interfaces():
    response = os.system("ipconfig /all")
    if response == 0:
        print("Network interfaces displayed.")
    else:
        print("Error fetching network interfaces.")

def cmd_create_user():
    username = input("Enter the username to create: ")
    os.system(f"net user {username} /add")
    print(f"User '{username}' created.")

def cmd_hardware_info():
    os.system("systeminfo | findstr /C:'OS Name' /C:'System Type' /C:'Total Physical Memory'")

def cmd_welcome_message():
    print("Welcome to BINXX - Your command line assistant!")

def cmd_open_url():
    url = input("Enter the URL to open: ")
    webbrowser.open(url)
    print(f"Opening {url} in the default web browser.")

def cmd_github_repo():
    print("Repository owner: YourGitHubUsername")

def cmd_search_web():
    query = input("Enter the search query: ")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    print(f"Searching the web for '{query}'...")

def cmd_play_music():
    print("Now playing your favorite music!")

def cmd_weather():
    print("Weather information: Sunny with a chance of rain")

def cmd_news():
    print("Latest news headlines: Breaking news around the world")

def cmd_calendar():
    os.system("start outlookcal:")

def cmd_convert_currency():
    amount = float(input("Enter the amount in USD: "))
    converted_amount = amount * 0.84  # Assuming conversion rate
    print(f"Converted amount: {converted_amount} EUR")

def cmd_calculator():
    expression = input("Enter the expression to calculate: ")
    result = eval(expression)
    print(f"Result: {result}")

def cmd_reminder():
    reminder = input("Set a reminder: ")
    print(f"Reminder set: {reminder}")

def cmd_send_email():
    recipient = input("Enter the recipient's email address: ")
    subject = input("Enter the email subject: ")
    body = input("Enter the email body: ")

    # Code to send email
    print(f"Email sent to {recipient} with subject: {subject}")

def cmd_secret():
    print("Upcoming Updates:")
    print(" - February 13th")
    print(" - February 18th")
    print(" - February 27th")
    print(" - March 3rd")
    # Add more upcoming updates")

def cmd_release_date():
    print("Current Release Date: February 10th, 2024")

def cmd_help():
    print("\nAvailable commands:")
    print("  dir - List files in the current directory")
    print("  cd - Change directory")
    print("  ping - Ping a host")
    print("  tracert - Trace route to a host")
    print("  ipconfig - Display network configuration")
    print("  find - Search for a file")
    print("  tree - Display directory tree")
    print("  cls - Clear the screen")
    print("  color - Change console color")
    print("  systeminfo - Display system information")
    print("  date - Display current date")
    print("  time - Display current time")
    print("  whoami - Display current user")
    print("  tasklist - List running processes")
    print("  notepad - Open Notepad")
    print("  calc - Open Calculator")
    print("  python - Open Python interpreter")
    print("  create_file - Create a new file")
    print("  delete_file - Delete a file")
    print("  read_file - Read the contents of a file")
    print("  write_file - Write content to a file")
    print("  network_status - Display network status")
    print("  network_interfaces - Display network interfaces")
    print("  create_user - Create a new user")
    print("  hardware_info - Display hardware information")
    print("  welcome_message - Display a welcome message")
    print("  open_url - Open a URL in the default web browser")
    print("  github_repo - Display the repository owner on GitHub")
    print("  search_web - Search the web using Google")
    print("  play_music - Play your favorite music")
    print("  weather - Display current weather information")
    print("  news - Display latest news headlines")
    print("  calendar - Open the calendar")
    print("  convert_currency - Convert currency")
    print("  calculator - Perform calculations")
    print("  reminder - Set a reminder")
    print("  send_email - Send an email")
    print("  secret - Display upcoming updates")
    print("  release_date - Display current release date")
    print("  exit - Exit BINXX")

def main():
    print_logo()

    while True:
        command = input("\nBINXX> ")

        if command == "dir":
            cmd_dir()

        elif command == "cd":
            cmd_cd()

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

        elif command == "cls":
            cmd_cls()

        elif command == "color":
            cmd_color()

        elif command == "systeminfo":
            cmd_systeminfo()

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

        elif command == "open_url":
            cmd_open_url()

        elif command == "github_repo":
            cmd_github_repo()

        elif command == "search_web":
            cmd_search_web()

        elif command == "play_music":
            cmd_play_music()

        elif command == "weather":
            cmd_weather()

        elif command == "news":
            cmd_news()

        elif command == "calendar":
            cmd_calendar()

        elif command == "convert_currency":
            cmd_convert_currency()

        elif command == "calculator":
            cmd_calculator()

        elif command == "reminder":
            cmd_reminder()

        elif command == "send_email":
            cmd_send_email()

        elif command == "secret":
            cmd_secret()

        elif command == "release_date":
            cmd_release_date()

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
