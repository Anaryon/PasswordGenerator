import random
import string
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os

def generer_mot_de_passe():
    try:
        longueur = int(entree_longueur.get())
        if longueur < 4:
            raise ValueError
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une longueur valide (≥ 4).")
        return

    lettres = string.ascii_letters
    chiffres = string.digits
    speciaux = string.punctuation
    tous = lettres + chiffres + speciaux

    mot_de_passe = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(chiffres),
        random.choice(speciaux),
    ] + random.choices(tous, k=longueur - 4)

    random.shuffle(mot_de_passe)
    resultat.set(''.join(mot_de_passe))

fenetre = tk.Tk()
fenetre.title("Générateur de mot de passe")
fenetre.geometry("500x550+200+200")

# Vérification de la bonne position de l'image
if getattr(sys, 'frozen', False):
    # Si l'application est un .exe
    image_path = os.path.join(sys._MEIPASS, "ours.png")
else:
    # Si tu exécutes en mode script Python
    image_path = "ours.png"

try:
    image_ours = Image.open(image_path)
except FileNotFoundError:
    messagebox.showerror("Erreur", "L'image 'ours.png' est introuvable.")
    fenetre.quit()
    exit()

image_ours = image_ours.resize((300, 300), Image.Resampling.LANCZOS)
photo_ours = ImageTk.PhotoImage(image_ours)

canvas = tk.Canvas(fenetre, width=300, height=400)
canvas.pack(pady=10)

canvas.create_image(150, 150, image=photo_ours)
canvas.create_text(150, 330, text="Dimitri Orthwein", font=("Helvetica", 16), fill="black")

tk.Label(fenetre, text="Longueur du mot de passe :").pack()
entree_longueur = tk.Entry(fenetre)
entree_longueur.pack(pady=5)

tk.Button(fenetre, text="Générer", command=generer_mot_de_passe).pack(pady=10)

resultat = tk.StringVar()
tk.Entry(fenetre, textvariable=resultat, font=("Courier", 12), width=30).pack(pady=5)

fenetre.mainloop()

