from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Initialize Tkinter root window
root = Tk()
root.title("Google Translator 2.0")
root.geometry("1080x400")
root.resizable(False, False)
root.configure(background="white")

# Initialize Google Translator
translator = Translator()

def translate_text():
    # Get selected languages
    src_lang = combo1.get().lower()
    dest_lang = combo2.get().lower()
    
    # Convert language names to language codes
    src_lang_code = {v: k for k, v in LANGUAGES.items()}.get(src_lang)
    dest_lang_code = {v: k for k, v in LANGUAGES.items()}.get(dest_lang)
    
    if src_lang_code and dest_lang_code:
        # Translate the text
        try:
            translated = translator.translate(text1.get("1.0", "end-1c"), src=src_lang_code, dest=dest_lang_code)
            text2.delete("1.0", "end")
            text2.insert("1.0", translated.text)
        except Exception as e:
            text2.delete("1.0", "end")
            text2.insert("1.0", f"Error: {str(e)}")
    else:
        text2.delete("1.0", "end")
        text2.insert("1.0", "Error: Invalid language selected")

def on_language_change(event):
    # Update labels to show selected languages
    src_lang = combo1.get().capitalize()
    dest_lang = combo2.get().capitalize()
    label1.configure(text=src_lang)
    label2.configure(text=dest_lang)

def on_translate_button_click():
    translate_text()

# Load arrow image
arrow_image = PhotoImage(file="arrow.png")
image_label = Label(root, image=arrow_image, bg="white")
image_label.place(x=460, y=150)

# Create a list of languages
languageV = list(LANGUAGES.values())

# First combobox
combo1 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo1.place(x=100, y=50)
combo1.set("English")
combo1.bind("<<ComboboxSelected>>", on_language_change)

label1 = Label(root, text="English", font="Segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=100)

# Second combobox
combo2 = ttk.Combobox(root, values=languageV, font="Roboto 14", state="readonly")
combo2.place(x=730, y=50)
combo2.set("Select Language")
combo2.bind("<<ComboboxSelected>>", on_language_change)

label2 = Label(root, text="Select Language", font="Segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=100)

# Translate Button
translate_button = Button(root, text="Translate", command=on_translate_button_click, font="Roboto 14 bold", fg="white", bg="black")
translate_button.place(x=460, y=300, width=160, height=40)

# First frame
f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=150, width=440, height=210)
text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar1 = Scrollbar(f, command=text1.yview)
scrollbar1.pack(side=RIGHT, fill='y')
text1.configure(yscrollcommand=scrollbar1.set)

# Second frame
f1 = Frame(root, bg="Black", bd=5)
f1.place(x=620, y=150, width=440, height=210)
text2 = Text(f1, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.pack(side=LEFT, fill=BOTH, expand=True)
scrollbar2 = Scrollbar(f1, command=text2.yview)
scrollbar2.pack(side=RIGHT, fill='y')
text2.configure(yscrollcommand=scrollbar2.set)

# Run the Tkinter event loop
root.mainloop()
