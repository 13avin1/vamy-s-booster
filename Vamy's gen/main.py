import discord
import time
import threading
import random
import httpx
import tkinter as tk

class variables:
    joins = 0
    boosts_done = 0
    success_tokens = []
    failed_tokens = []

def get_all_tokens(filename):
    return [j.split(":")[2] if ":" in j else j for j in open(filename, "r").read().splitlines()]

def remove(token, filename):
    tokens = get_all_tokens(filename)
    tokens.remove(token)
    with open(filename, "w") as f:
        f.write("\n".join(tokens))

def getproxy():
    try:
        proxy = random.choice(open("input/proxies.txt", "r").read().splitlines())
        return {'http': f'http://{proxy}'}
    except Exception as e:
        pass

def boost_server(invite, months, token, thread, nick):
    # Your function logic here...
    pass

def thread_boost(invite, amount, months, nick):
    variables.boosts_done = 0
    variables.success_tokens = []
    variables.failed_tokens = []
    filename = "input/1m_tokens.txt" if months == 1 else "input/3m_tokens.txt"
    
    # Add your logic for boosting servers...
    pass

def start_boost():
    invite = invite_entry.get()
    months = int(months_entry.get())
    amount = int(amount_entry.get())
    nick = nick_entry.get()
    thread_boost(invite, amount, months, nick)

# Create the GUI window
root = tk.Tk()
root.title("Vamy Radiator")
root.geometry("400x300")
root.configure(bg="#4B0082")  # Dark Purple

# Add labels and input fields
label = tk.Label(root, text="Welcome to Vamy Radiator", bg="#4B0082", fg="white", font=("Arial", 16))
label.pack(pady=20)

invite_label = tk.Label(root, text="Invite:", bg="#4B0082", fg="white")
invite_label.pack()
invite_entry = tk.Entry(root)
invite_entry.pack()

months_label = tk.Label(root, text="Months:", bg="#4B0082", fg="white")
months_label.pack()
months_entry = tk.Entry(root)
months_entry.pack()

amount_label = tk.Label(root, text="Amount:", bg="#4B0082", fg="white")
amount_label.pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

nick_label = tk.Label(root, text="Nickname:", bg="#4B0082", fg="white")
nick_label.pack()
nick_entry = tk.Entry(root)
nick_entry.pack()

start_button = tk.Button(root, text="Start Boost", command=start_boost, bg="#9400D3")  # Dark Purple
start_button.pack()

# Start the GUI main loop
root.mainloop()
