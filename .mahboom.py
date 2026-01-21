#!/usr/bin/env python
import os
import requests

# Clear screen
os.system("clear")

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")

# ASCII Banner colored (lolcat)
os.system('echo "    ╔╦╗ ╔═╗ ╦ ╦ ╔╗ ╔═╗╔═╗╔╦╗" | lolcat -a')
os.system('echo "    ║║║ ╠═╣ ╠═╣ ╠╩╗║ ║║ ║║║║" | lolcat -a')
os.system('echo "    ╩ ╩ ╩ ╩ ╩ ╩ ╚═╝╚═╝╚═╝╩ ╩" | lolcat -a')

# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")

# Owner / Server info colored
os.system('echo "𝙳𝚎𝚟𝚎𝚕𝚘𝚙𝚎𝚛 ➤ 𝙼𝙰𝙷𝙱𝚄𝙱𝚄𝙻 𝙰𝙻𝙰𝙼" | lolcat')
os.system('echo "𝚂𝚎𝚛𝚟𝚎𝚛 𝙾𝙽𝙻𝙸𝙽𝙴 ✓ | 𝚅𝙴𝚁𝚂𝙸𝙾𝙽 1.0" | lolcat\n')

# Password check
password = input("𝙴𝚗𝚝𝚎𝚛 𝙿𝚊𝚜𝚜𝚠𝚘𝚛𝚍 ➤ ")
if password != "mahbub":
    print("\033[91m𝙿𝚎𝚛𝚖𝚒𝚜𝚜𝚒𝚘𝚗 𝙳𝚎𝚗𝚒𝚎𝚍 ×\033[0m")
    exit()
print("\033[92m𝙰𝚌𝚌𝚎𝚜𝚜 𝙶𝚛𝚊𝚗𝚝𝚎𝚍 ✓\033[0m\n")

# Main menu loop
while True:
    print("\033[96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")
    print("\033[96m[1] Start Tool\033[0m")
    print("\033[93m[2] Update Tool\033[0m")
    print("\033[92m[3] Contact Admin\033[0m")
    print("\033[91m[0] Exit\033[0m")
    print("\033[96m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[0m")

    choice = input("𝙼𝙰𝙷𝙱𝙾𝙾𝙼 ➤ ")

    if choice == "1":
        number = input("Enter Target Number ➤ ")

        # Number validation
        if not number.isdigit():
            print("❌ Invalid Number\n")
            continue

        amount = input("Enter Amount (Max 100) ➤ ")

        # Amount validation
        if not amount.isdigit():
            print("❌ Amount must be number\n")
            continue

        amount = int(amount)
        if amount < 1 or amount > 100:
            print("❌ Amount must be between 1 and 100\n")
            continue

        print("\033[95m⏳ Starting Boom.....\033[0m")

        # ===== API CALL =====
        url = "https://premium.jubairbro.store:81/api/api"
        params = {
            "key": "app",      # fixed key
            "num": number,     # user input number
            "amount": amount   # user input amount
        }

        try:
            r = requests.get(url, params=params, timeout=15)
            print("\033[92m𝗕𝗼𝗼𝗺𝗯𝗶𝗻𝗴 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 ✓\033[0m")
            # print(r.text)
        except Exception:
            print("\033[91m❌ Network or API Error\033[0m")

        print("\n🚀 Starting BooM\n")

    elif choice == "2":
        print("\033[93m❌ 𝙽𝚘 𝙰𝚋𝚊𝚒𝚕𝚊𝚋𝚕𝚎 𝚄𝚙𝚍𝚊𝚝𝚎𝚜 \033[0m\n")

    elif choice == "3":
        print("\033[92m💬 ▶Telegram :💬 @lord_ragna 💬\033[0m\n")

    elif choice == "0":
        print("\033[91mExiting... Bye!👋\033[0m")
        break

    else:
        print("\033[91m❌ Invalid Option\033[0m\n")

