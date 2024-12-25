import os
import customtkinter as ctk
from tkinter import filedialog, messagebox

def load_alphabet():
    return {
        'a': "Kraken", 'b': "Spyglass", 'c': "Rudder", 'd': "Plunder", 'e': "Wench",
        'f': "Grog", 'g': "Treasure", 'h': "Scallywag", 'i': "Buccaneer", 'j': "Cutlass",
        'k': "Corsair", 'l': "Maroon", 'm': "Privateer", 'n': "Bilge", 'o': "Doubloon",
        'p': "Helm", 'q': "Swash", 'r': "Anchor", 's': "CrowNest", 't': "Hull",
        'u': "Barnacle", 'v': "Keel", 'w': "Cannon", 'x': "Pistol", 'y': "Rigging",
        'z': "Parrot",
        'A': "Wave", 'B': "Deck", 'C': "Mast", 'D': "Voyage", 'E': "Flag",
        'F': "Jolly", 'G': "Booty", 'H': "Land", 'I': "Skull", 'J': "Iron",
        'K': "Starboard", 'L': "Crow", 'M': "Map", 'N': "Compass", 'O': "Sea",
        'P': "Shanty", 'Q': "Quarters", 'R': "Loot", 'S': "Sword", 'T': "Harpoon",
        'U': "Port", 'V': "Galleon", 'W': "Wind", 'X': "Spy", 'Y': "Cove",
        'Z': "Reef",
        'à': "Tide", 'è': "Octopus", 'é': "Harbor", 'ì': "PegLeg", 'ò': "Mermaid", 'ù': "Trex",
        'À': "Plank", 'È': "Nautical", 'É': "Admiral", 'Ì': "Broadside", 'Ò': "Corsair", 'Ù': "Prow",
        ' ': "_", '\n': "NL",
        '0': "Cannonball", '1': "Anchorline", '2': "Buoy", '3': "CrowNest", '4': "Dinghy",
        '5': "EspyGlass", '6': "Fathom", '7': "Gunwale", '8': "Hammock", '9': "Island",
        '!': "Exclaim", '?': "Mystery", '.': "End", ',': "Pause", ':': "Point",
        ';': "Break", '"': "Quote", "'": "Mark"
    }

def translate_to_piratesco(text, alphabet):
    result = []
    for char in text:
        result.append(alphabet.get(char, char))  # Use dictionaty to translate character
    return ''.join(result)

def translate_to_plain(text, reverse_alphabet):
    result = []
    buffer = ""
    for char in text:
        buffer += char
        if buffer in reverse_alphabet:
            result.append(reverse_alphabet[buffer])
            buffer = ""  # Reset buffer
    if buffer:  # Manage the unprocessed buffer
        result.append(buffer)
    return ''.join(result).replace("NL", "\n")

def process_file(input_file):
    pirate_alphabet = load_alphabet()
    reverse_alphabet = {v: k for k, v in pirate_alphabet.items()}

    base, ext = os.path.splitext(input_file)
    if ext == '.txt':
        output_file = base + '.arrr'
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        translated = translate_to_piratesco(content, pirate_alphabet)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated)
        return f"Translate in piratesco completed: {output_file}"

    elif ext == '.arrr':
        output_file = base + '.txt'
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        translated = translate_to_plain(content, reverse_alphabet)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated)
        return f"Translate in plain text completed: {output_file}"

    else:
        return "File format not supported. Please select a .txt or .arrr file."

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("Pirate files", "*.arrr")])
    if file_path:
        try:
            result = process_file(file_path)
            messagebox.showinfo("Success", result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the main window
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Piratesco Translator")
app.geometry("500x300")

label = ctk.CTkLabel(app, text="Select the file to translate:", font=("Arial", 16))
label.pack(pady=20)

select_button = ctk.CTkButton(app, text="Select file", command=select_file)
select_button.pack(pady=10)

exit_button = ctk.CTkButton(app, text="Exit", command=app.quit)
exit_button.pack(pady=10)

app.mainloop()
