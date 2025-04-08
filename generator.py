import random
import string
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow

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

# Interface graphique
fenetre = tk.Tk()
fenetre.title("Générateur de mot de passe")
fenetre.geometry("400x450")  # Augmenté la taille de la fenêtre pour accueillir un plus grand ours

# Charger l'image de l'ours et l'ajuster (augmentation de la taille de l'image)
image_ours = Image.open("ours.png")  # Assurez-vous que l'image est dans le bon répertoire
image_ours = image_ours.resize((250, 250), Image.Resampling.LANCZOS)  # Image plus grande
photo_ours = ImageTk.PhotoImage(image_ours)

# Créer un Canvas pour afficher l'image
canvas = tk.Canvas(fenetre, width=250, height=350)  # Hauteur augmentée pour l'image plus grande et plus d'espace pour le texte
canvas.pack(pady=10)

# Ajouter l'image sur le Canvas
canvas.create_image(125, 125, image=photo_ours)  # Positionner l'image au centre du canvas

# Ajouter le texte sous l'image avec plus d'espace
canvas.create_text(125, 270, text="Dimitri Orthwein", font=("Helvetica", 16), fill="black")  # Texte déplacé plus bas

# Interface utilisateur
tk.Label(fenetre, text="Longueur du mot de passe :").pack()
entree_longueur = tk.Entry(fenetre)
entree_longueur.pack(pady=5)

tk.Button(fenetre, text="Générer", command=generer_mot_de_passe).pack(pady=10)

resultat = tk.StringVar()
tk.Entry(fenetre, textvariable=resultat, font=("Courier", 12), width=30).pack(pady=5)

fenetre.mainloop()
