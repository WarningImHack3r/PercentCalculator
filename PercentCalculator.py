from tkinter import *
import sys

LARGEUR=400
HAUTEUR=300
COULEUR_BG="#C0C0C0"

   
fenetre_tk=Tk()
fenetre_tk.title("PercentCalculator")
fenetre_tk.configure(width=LARGEUR, height=HAUTEUR, bg=COULEUR_BG)
fenetre_tk.update()
fenrw = fenetre_tk.winfo_reqwidth()
fenrh = fenetre_tk.winfo_reqheight()
sw = fenetre_tk.winfo_screenwidth()
sh = fenetre_tk.winfo_screenheight()
fenetre_tk.geometry("%dx%d+%d+%d" % (fenrw, fenrh, (sw-fenrw)/2, (sh-fenrh)/2))

text_wlcme=Label(fenetre_tk, text="PercentCalculator", fg="black", bg=COULEUR_BG, font="calibri 14 bold")
text_wlcme.place(x=LARGEUR/2, y=30, anchor="center")

textPoint=Label(fenetre_tk, text="(Utilisez des points pour les virgules)", fg="black", bg=COULEUR_BG, font="calibri 8")
textPoint.place(x=LARGEUR/2, y=50, anchor="center")

resuLabel=Label(fenetre_tk, text="", fg="black", bg=COULEUR_BG, font="calibri 16 bold")
def calculate():
    global PLUSMOINS
    PLUSMOINS=scale_plusmoins.get()
    nombre=entryNb.get()
    prctage=entryPrct.get()
    resuLabel.config(text="")
    if PLUSMOINS==0:
        resu=round(float(nombre)+float(nombre)*((float(prctage)/100)), 2)
        resuLabel.config(text=str(nombre)+" + "+str(prctage)+"% = "+str(resu))
    if PLUSMOINS==1:
        resu=round(float(nombre)-float(nombre)*((float(prctage)/100)), 2)
        resuLabel.config(text=str(nombre)+" - "+str(prctage)+"% = "+str(resu))
    resuLabel.place(x=LARGEUR/2, y=260, anchor="center")

def scalepm(n):
    PLUSMOINS=n

labelNb=Label(fenetre_tk, text="Entrez le nombre de base :", bg=COULEUR_BG)
labelNb.place(x=50, y=80)
entryNb=Entry(fenetre_tk)
entryNb.place(x=200, y=80)

labelPrct=Label(fenetre_tk, text="Entrez le pourcentage :", bg=COULEUR_BG)
labelPrct.place(x=68, y=110)
entryPrct=Entry(fenetre_tk)
entryPrct.place(x=200, y=110)

scale_plusmoins=Scale(fenetre_tk, orient="horizontal", from_=0, to=1, resolution=1, tickinterval=1, length=170, showvalue=0, sliderlength=20, fg="black", bg=COULEUR_BG, highlightthickness=0, font="calibri 10", cursor="sb_h_double_arrow", label="Augmentation ou réduction ?", command=scalepm)
scale_plusmoins.place(x=(LARGEUR/2)-85, y=140)
scale_plusmoins.set(0)
text_plusmoins_plus=Label(fenetre_tk, text="+", bg=COULEUR_BG, font="calibri 11")
text_plusmoins_plus.place(x=122, y=180)
text_plusmoins_moins=Label(fenetre_tk, text="-", bg=COULEUR_BG, font="calibri 11")
text_plusmoins_moins.place(x=273, y=180)

calculerBtn=Button(fenetre_tk, text="Calculer !", bg=COULEUR_BG, command=calculate)
calculerBtn.place(x=LARGEUR/2, y=210, anchor="center")

vNb=Label(fenetre_tk, text="v1.0.4", bg=COULEUR_BG, font="calibri 8")
vNb.place(x=LARGEUR-10, y=HAUTEUR-15, anchor="e")



fenetre_tk.mainloop()