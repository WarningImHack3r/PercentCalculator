from tkinter import *
from tkinter.messagebox import *
import sys

#Variables
LARGEUR=400
HAUTEUR=300
COULEUR_BG="#C0C0C0"
resu=""

#Initialisation
fenetre_tk=Tk()
fenetre_tk.title("PercentCalculator")
fenetre_tk.configure(width=LARGEUR, height=HAUTEUR, bg=COULEUR_BG)
fenetre_tk.resizable(0, 0)
fenrw = fenetre_tk.winfo_reqwidth()
fenrh = fenetre_tk.winfo_reqheight()
sw = fenetre_tk.winfo_screenwidth()
sh = fenetre_tk.winfo_screenheight()
fenetre_tk.geometry("%dx%d+%d+%d" % (fenrw, fenrh, (sw-fenrw)/2, (sh-fenrh)/2))
fenetre_tk.update()

#Définition des widgets
textPoint=Label(fenetre_tk)
labelNb=Label(fenetre_tk)
labelPrct=Label(fenetre_tk)
scale_plusmoins=Scale(fenetre_tk)
calculerBtn=Button(fenetre_tk)

#Barre de menu
menubar=Menu(fenetre_tk, tearoff=0)
mainmenu=Menu(menubar, tearoff=0)
langVar=IntVar()
langmenu=Menu(menubar, tearoff=0)
helpmenu=Menu(menubar, tearoff=0)

#Fonctions
resuLabel=Label(fenetre_tk, text="", fg="black", bg=COULEUR_BG, font="calibri 16 bold")
def calculate():
    """Permet de calculer avec les entrées fournies et affiche le résultat sous le bouton"""
    global PLUSMOINS, resu
    PLUSMOINS=scale_plusmoins.get()
    nombre=entryNb.get()
    nombre=float(nombre.replace(",", "."))
    prctage=entryPrct.get()
    prctage=float(prctage.replace(",", "."))
    if nombre=="":
        if choixLang=="fr":
            showerror("Erreur", "Vous devez entrer un nombre valide")
        if choixLang=="en":
            showerror("Error", "You have to input a correct number")
    if prctage=="":
        if choixLang=="fr":
            showerror("Erreur", "Vous devez entrer un pourcentage valide")
        if choixLang=="en":
            showerror("Error", "You have to input a correct percentage")
    if nombre=="" and prctage=="":
        if choixLang=="fr":
            showerror("Erreur", "Vous devez entrer des nombres")
        if choixLang=="en":
            showerror("Error", "You have to input a numbers")        
    resuLabel.config(text="")
    if PLUSMOINS==0:
        resu=round(float(nombre)+float(nombre)*((float(prctage)/100)), 2)
        resuLabel.config(text=str(nombre)+" + "+str(prctage)+"% = "+str(resu))
    if PLUSMOINS==1:
        resu=round(float(nombre)-float(nombre)*((float(prctage)/100)), 2)
        resuLabel.config(text=str(nombre)+" - "+str(prctage)+"% = "+str(resu))
    resuLabel.place(x=LARGEUR/2, y=260, anchor="center")
    resuLabel.bind("<Button-3>", clicDroit)

#Fonctions de langues
def fr():
    global choixLang, ABOUT
    choixLang="fr"
    ABOUT="A propos"
    f=open("lang.txt", "r+")
    f.seek(0)
    f.truncate()
    f.write("fr")
    f.close()
    mainmenu.entryconfig(0, label="Copier le résultat")
    mainmenu.entryconfig(1, label="Tout effacer")
    mainmenu.entryconfig(3, label="Quitter")
    menubar.entryconfig(0, label="Programme")
    menubar.entryconfig(1, label="Langues")
    helpmenu.entryconfig(0, label="A propos")
    menubar.entryconfig(2, label="Aide")
    labelNb.config(text="Entrez le nombre de base :")
    labelPrct.config(text="Entrez le pourcentage :")
    scale_plusmoins.config(label="Augmentation ou réduction ?")
    calculerBtn.config(text=" Calculer ! ")
    fenetre_tk.update()

def en():
    global choixLang, ABOUT
    choixLang="en"
    ABOUT="About"
    f=open("lang.txt", "r+")
    f.seek(0)
    f.truncate()
    f.write("en")
    f.close()
    mainmenu.entryconfig(0, label="Copy the result")
    mainmenu.entryconfig(1, label="Erase all")
    mainmenu.entryconfig(3, label="Exit")
    menubar.entryconfig(0, label="Program")
    menubar.entryconfig(1, label="Languages")
    helpmenu.entryconfig(0, label="About")
    menubar.entryconfig(2, label="Help")
    labelNb.config(text="Enter your number :")
    labelPrct.config(text="Enter your percentage :")
    scale_plusmoins.config(label="  Increasing or decreasing ?")
    calculerBtn.config(text=" Calculate ! ")
    fenetre_tk.update()

#Fichier lang.txt
if "fr" in open("lang.txt", "r+").read():
    langVar.set(0)
    fr()
    fenetre_tk.update()
if "en" in open("lang.txt", "r+").read():
    langVar.set(1)
    en()
    fenetre_tk.update()

def scalepm(n):
    PLUSMOINS=n

def copycb():
    global resu, choixLang
    fenetre_tk.clipboard_clear()
    if resu=="":
        if choixLang=="en":
            showerror("Error", "The result is actually empty")
        elif choixLang=="fr":
            showerror("Erreur", "Le résultat est actuellement vide")
    else:
        fenetre_tk.clipboard_append(resu)
        if choixLang=="en":
            showinfo("Information", "The result has been successfully copied. It will stay available while PercentCalculator stays open")
        elif choixLang=="fr":
            showinfo("Information", "Le résultat a bien été copié dans le presse-papier. Il sera disponible tant que le programme restera ouvert")
    fenetre_tk.update()

def clicDroit(event):
    global resu, choixLang
    fenetre_tk.clipboard_clear()
    if resu=="":
        if choixLang=="en":
            showerror("Error", "The result is actually empty")
        elif choixLang=="fr":
            showerror("Erreur", "Le résultat est actuellement vide")
    else:
        fenetre_tk.clipboard_append(resu)
        if choixLang=="en":
            showinfo("Information", "The result has been successfully copied. It will stay available while PercentCalculator stays open")
        elif choixLang=="fr":
            showinfo("Information", "Le résultat a bien été copié dans le presse-papier. Il sera disponible tant que le programme restera ouvert")
    fenetre_tk.update()

def clear():
    global resu
    entryNb.delete(0, END)
    entryPrct.delete(0, END)
    resu=""
    resuLabel.config(text="")
    scale_plusmoins.set(0)

def about():
    global ABOUT
    showinfo(ABOUT, "                      PercentCalculator                          \n                          Version 1.1.0                          \n                    by WarningImHack3r                         ")
    

"""Menu"""
mainmenu.add_command(label="Copier le résultat", command=copycb)
mainmenu.add_command(label="Tout effacer", command=clear)
mainmenu.add_separator()
mainmenu.add_command(label="Quitter", command=fenetre_tk.quit)
menubar.add_cascade(label="Programme", menu=mainmenu)

"""Langue"""
langmenu.add_radiobutton(label="Français", command=fr, variable=langVar, value=0)
langmenu.add_radiobutton(label="English", command=en, variable=langVar, value=1)
menubar.add_cascade(label="Langues", menu=langmenu)


"""A propos"""
helpmenu.add_command(label="A propos", command=about)
menubar.add_cascade(label="Aide", menu=helpmenu)

fenetre_tk.config(menu=menubar)

#Titre
text_wlcme=Label(fenetre_tk, text="PercentCalculator", fg="black", bg=COULEUR_BG, font="calibri 18 bold")
text_wlcme.place(x=LARGEUR/2, y=40, anchor="center")

#Entrées
labelNb.config(text="Entrez le nombre de base :", bg=COULEUR_BG)
labelNb.place(x=195, y=88, anchor="e")
entryNb=Entry(fenetre_tk)
entryNb.place(x=200, y=80)

labelPrct.config(text="Entrez le pourcentage :", bg=COULEUR_BG)
labelPrct.place(x=195, y=120, anchor="e")
entryPrct=Entry(fenetre_tk)
entryPrct.place(x=200, y=110)

#Choix signes
scale_plusmoins.config(orient="horizontal", from_=0, to=1, resolution=1, tickinterval=1, length=170, showvalue=0, sliderlength=20, fg="black", bg=COULEUR_BG, highlightthickness=0, font="calibri 10", cursor="sb_h_double_arrow", label="Augmentation ou réduction ?", command=scalepm)
scale_plusmoins.place(x=(LARGEUR/2)-85, y=140)
scale_plusmoins.set(0)
text_plusmoins_plus=Label(fenetre_tk, text="+", bg=COULEUR_BG, font="calibri 11")
text_plusmoins_plus.place(x=122, y=180)
text_plusmoins_moins=Label(fenetre_tk, text="-", bg=COULEUR_BG, font="calibri 11")
text_plusmoins_moins.place(x=273, y=180)

#Bouton
calculerBtn.config(text=" Calculer ! ", bg=COULEUR_BG, command=calculate)
calculerBtn.place(x=LARGEUR/2, y=210, anchor="center")



fenetre_tk.mainloop()