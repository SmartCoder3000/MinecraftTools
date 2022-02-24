import os

options = os.listdir('src')
print("""  __  __          _____                  _     
 |  \/  |        |  __ \                | |    
 | \  / |   ___  | |  | |   __ _   ___  | |__  
 | |\/| |  / __| | |  | |  / _` | / __| | '_ \ 
 | |  | | | (__  | |__| | | (_| | \__ \ | | | |
 |_|  |_|  \___| |_____/   \__,_| |___/ |_| |_|
                                               
                                               """)
print("The Mincraft account hacking tool")
print("Made by SmartCoder3000\n\n")

i = 1
for file in os.listdir("src"):
  if not ".py" in file:
    desc = open( f"src/{file}").read()
    desc = f"[{i}]{desc}"
    print(desc)
    i+=1

print("\nWhat would you like to do?\n")


option = input(">> ")

if not int(option) <= len(options):
  print(f"Invalid Option, ({option}), exiting...")
elif option == "1":
  exec(open(f"src/{options[int(option)-1]}").read())
elif option == "2":
  print("")