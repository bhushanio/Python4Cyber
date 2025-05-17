import re
import tkinter as tk
from tkinter import messagebox, filedialog
from datetime import datetime


def leetspeak(word):
    substitutions = {'a': '@', 's': '$', 'o': '0', 'i': '1', 'e': '3', 'l': '1'}
    return ''.join(substitutions.get(c.lower(), c) for c in word)


def case_variants(word):
    return {word.lower(), word.upper(), word.capitalize()}


def generate_passwords(email, first_name, last_name, birthdate, mobile):
    passwords = set()

    email_user = email.split("@")[0]
    birth_parts = re.findall(r'\d+', birthdate)
    birth_day, birth_month, birth_year = birth_parts if len(birth_parts) == 3 else ('', '', '')

    birth_year_short = birth_year[-2:] if birth_year else ''
    mobile_last4 = mobile[-4:]
    mobile_first4 = mobile[:4]

    months = ["jan", "feb", "mar", "apr", "may", "jun",
              "jul", "aug", "sep", "oct", "nov", "dec"]
    birth_month_name = months[int(birth_month) - 1] if birth_month.isdigit() else ''

    nicknames = [first_name[:3], first_name[:4] + "i", first_name.lower() + "y", first_name.lower() + "boy"]

    base_words = list(set([
        first_name.lower(), last_name.lower(), email_user.lower(),
        first_name.capitalize(), last_name.capitalize(),
        first_name.lower() + last_name.lower(),
        first_name[0].lower() + last_name.lower(),
        *nicknames
    ]))

    common_words = [
        'password', 'admin', 'qwerty', 'letmein', 'hello', 'welcome',
        'iloveyou', 'test', 'trust', 'bestie', 'always', 'dilse', 'dost', 'forever', 'missyou'
    ]

    suffixes = [
        '', '123', '1234', '1', '!', '@', '@123', '321', '007', '786',
        birth_year, birth_year_short, birth_day + birth_month, mobile_last4, mobile_first4,
        'love', 'life', '<3', 'cool', 'king', 'queen', 'star', 'rocks'
    ]

    separators = ['_', '@', '.', '-', '~']

    for base in base_words:
        for variant in case_variants(base):
            for suf in suffixes:
                passwords.add(variant + suf)
                for sep in separators:
                    passwords.add(variant + sep + suf)

            passwords.add(variant[::-1])
            passwords.add(leetspeak(variant) + '123')
            passwords.add(variant + birth_month_name + birth_year)
            passwords.add(variant + birth_day + birth_month_name)
            passwords.add(variant + variant[-1] * 2)

    for word in common_words:
        for suf in ["123", birth_year, birth_year_short, "!"]:
            passwords.add(word + suf)

    passwords.add(first_name.lower() + mobile_last4)
    passwords.add(last_name.lower() + birth_year)
    passwords.add(first_name.lower() + last_name.lower() + '123')
    passwords.add(first_name[0].lower() + last_name.lower() + mobile_last4)
    passwords.add(first_name.lower() + birth_year_short)
    passwords.add(mobile[-2:] * 3)

    return sorted(passwords)


def run_generator():
    email = email_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    birthdate = birthdate_entry.get()
    mobile = mobile_entry.get()

    if not all([email, first_name, last_name, birthdate, mobile]):
        messagebox.showerror("Input Error", "Please fill in all fields")
        return

    passwords = generate_passwords(email, first_name, last_name, birthdate, mobile)

    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if not filepath:
        return

    with open(filepath, 'w') as f:
        for pwd in passwords:
            f.write(pwd + "\n")

    messagebox.showinfo("Success", f"Generated {len(passwords)} passwords and saved to file")


# UI Setup
app = tk.Tk()
app.title("Password Pattern Generator")
app.geometry("400x300")

labels = ["Email", "First Name", "Last Name", "Birthdate (DD-MM-YYYY)", "Mobile"]
entries = []

for i, label_text in enumerate(labels):
    label = tk.Label(app, text=label_text)
    label.grid(row=i, column=0, padx=10, pady=5, sticky='w')
    entry = tk.Entry(app, width=30)
    entry.grid(row=i, column=1)
    entries.append(entry)

email_entry, first_name_entry, last_name_entry, birthdate_entry, mobile_entry = entries

generate_button = tk.Button(app, text="Generate Passwords", command=run_generator)
generate_button.grid(row=6, column=0, columnspan=2, pady=20)

app.mainloop()