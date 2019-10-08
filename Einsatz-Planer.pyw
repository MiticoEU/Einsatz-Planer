# Setup
from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser

#config
cfg = ConfigParser()
cfg.read('config.ini')


#Variablen



# Button actionen
def fertig_action():
	einsatznummer_text = einsatznummer.get()
	meldebild_text = meldebild.get()
	einsatz = open("Einsatz/Einsatz " + str(einsatznummer_text) + " (" + str(meldebild_text) + ").txt","w")
	einsatz.write("Einsatznummer: " + str(einsatznummer_text) + "\n")
	entry_text = variable.get()
	einsatz.write("Stichwort: " + str(entry_text) + "\n")
	einsatz.write("Meldebild: " + str(meldebild_text) + "\n")
	entry_text = bemerkung.get()
	einsatz.write("Bemerkung: " + str(entry_text) + "\n")
	entry_text = ort.get()
	einsatz.write("Ort: " + str(entry_text) + "\n")
	entry_text = ortsteil.get()
	einsatz.write("Ortsteil: " + str(entry_text) + "\n")
	entry_text = strasse.get()
	entry_text2 = hausnummer.get()
	einsatz.write("Strasse: " + str(entry_text) + " " + str(entry_text2) + "\n")
	einsatz.write("Strassenabschnitt:\n")
	entry_text = objekt.get()
	einsatz.write("Objekt: " + str(entry_text) + "\n")
	einsatz.write("Unterobjekt:\n")
	einsatz.write("Bemerkung zum E-Ort:\n")
	einsatz.write("GMA:\n")
	entry_text = breitengrad.get()
	entry_text2 = längengrad.get()
	einsatz.write("Koordinaten: " + str(entry_text) + ", " + str(entry_text2) + "\n")
	einsatz.write("AAO: Default")
	einsatz.close()
	action_get_speicher_dialog()

	

def action_get_info_dialog():
	m_text = "\
************************\n\
Autor: Maikel Klee\n\
Date: 09.09.19\n\
Version: 0.0.1\n\
************************"
	messagebox.showinfo(message=m_text, title = "Infos")
	
def action_get_speicher_dialog():
	m_text = "\
Speichern erfolgreich\n\
"
	messagebox.showinfo(message=m_text, title = "Speichern")
	

# Fenster erstellen
fenster = Tk()
fenster.title(cfg.get('Einstellung', 'title'))
fenster.geometry("400x450")
fenster.iconbitmap("alert.ico")

# Menüleiste erstellen 
menuleiste = Menu(fenster)

# Menü Datei
datei_menu = Menu(menuleiste, tearoff=0)
menuleiste.add_cascade(label="Datei", menu=datei_menu)
datei_menu.add_command(label="Beenden", command=fenster.quit)

# Menü Hilfe

help_menu = Menu(menuleiste, tearoff=0)
menuleiste.add_cascade(label="Hilfe", menu=help_menu)
help_menu.add_command(label="Info", command=action_get_info_dialog)


# Label
überschrift_label = Label(fenster, text="Alamierungs E-Mail erstellen")
einsatznummer_label = Label(fenster, text="Einsatznummer:")
stichwort_label = Label(fenster, text="Einsatzstichwort:")
meldebild_label = Label(fenster, text="Meldebild:")
bemerkung_label = Label(fenster, text="Bemerkung:")
ort_label = Label(fenster, text="Ort:")
ortsteil_label = Label(fenster, text="Ortsteil:")
strasse_label = Label(fenster, text="Strasse:")
hausnummer_label =Label(fenster, text="Hausnummer:")
srassenabschnitt_label = Label(fenster, text="Strassenabschnitt:")
objekt_label = Label(fenster, text="Objekt:")
unterobjekt_label = Label(fenster, text="Unterobjekt:")
bemerkungzumeort_label = Label(fenster, text="Bemerkung zum E-Ort:")
gma_label = Label(fenster, text="GMA:")
breitengrad_label = Label(fenster, text="Breitengrad:")
längengrad_label = Label(fenster, text="Längengrad:")
aao_label = Label(fenster, text="AAO:")

# Feste Werte
srassenabschnitt = Label(fenster, text="---------------")
unterobjekt = Label(fenster, text="---------------")
bemerkungzumeort = Label(fenster, text="---------------")
gma =  Label(fenster, text="---------------")
aao =  Label(fenster, text="Default")

# Abfrage
OptionList = [
"F 1",
"F 2",
"F 2 Y",
"F 3",
"F 3 Y",
"F 4",
"F BMA",
"F BUS Y",
"F FLUG 1 Y",
"F FLUG 2 Y",
"F GAS 1",
"F GAS 2",
"F LKW",
"F ZUG",
"F ZUG Y",
"F RWM",
"F SCHIFF 1",
"F SCHIFF 2",
"F SCHIFF 2 Y",
"F SCHIFF 2 GEFAHR",
"F WALD 1",
"F WALD 2",
"H 1",
"H 1 Y",
"H 2",
"H ABST Y",
"H ELEK",
"H EINST Y",
"H FLUSS",
"H FLUSS Y",
"H WASS Y",
"H GAS 1",
"H GAS 2",
"H GEFAHR 1",
"H GEFAHR 2",
"H KLEMM 1 Y",
"H KLEMM 2 Y",
"H ÖL FLUSS",
"H ÖL WASS",
"H RADIOAKTIV",
"H SCHIFF",
"H SCHIFF Y",
"H ZUG 1 Y",
"H ZUG 2 Y"
] 
variable = StringVar(fenster)
variable.set(OptionList[0])

stichwort = OptionMenu(fenster, variable, *OptionList)
stichwort.config(width=25, font=('Helvetica', 10))



# Eingabefelder
einsatznummer = Entry(fenster, bd=5, width=40)
meldebild = Entry(fenster, bd=5, width=40)
bemerkung = Entry(fenster, bd=5, width=40)
ort = Entry(fenster, bd=5, width=40)
ortsteil = Entry(fenster, bd=5, width=40)
strasse = Entry(fenster, bd=5, width=40)
hausnummer = Entry(fenster, bd=5, width=40)
objekt = Entry(fenster, bd=5, width=40)
breitengrad = Entry(fenster, bd=5, width=40)
längengrad = Entry(fenster, bd=5, width=40)

# Buttons
fertig_button = Button(fenster, text="Speichern", command=fertig_action)
exit_button = Button(fenster, text="Beenden", command=fenster.quit)

# Fenster Aufbau
fenster.config(menu=menuleiste) 
überschrift_label.grid(row = 0, column = 0, columnspan = 2)
einsatznummer_label.grid(row = 1, column = 0)
einsatznummer.grid(row = 1, column = 1)
stichwort_label.grid(row = 2, column = 0)
stichwort.grid(row = 2, column = 1)
meldebild_label.grid(row = 3, column = 0)
meldebild.grid(row = 3, column = 1)
bemerkung_label.grid(row = 4, column = 0)
bemerkung.grid(row = 4, column = 1)
ort_label.grid(row = 5, column = 0)
ort.grid(row = 5, column = 1)
ortsteil_label.grid(row = 6, column = 0)
ortsteil.grid(row = 6, column = 1)
strasse_label.grid(row = 7, column = 0)
strasse.grid(row = 7, column = 1)
hausnummer_label.grid(row = 8, column = 0)
hausnummer.grid(row =8, column = 1)
srassenabschnitt_label.grid(row = 9, column = 0)
srassenabschnitt.grid(row = 9, column = 1)
objekt_label.grid(row = 10, column = 0)
objekt.grid(row = 10, column = 1)
unterobjekt_label.grid(row = 11, column = 0)
unterobjekt.grid(row = 11, column = 1)
bemerkungzumeort_label.grid(row = 12, column = 0)
bemerkungzumeort.grid(row = 12, column = 1)
gma_label.grid(row = 13, column = 0)
gma.grid(row = 13, column = 1)
breitengrad_label.grid(row = 13, column = 0)
breitengrad.grid(row = 13, column = 1)
längengrad_label.grid(row = 14, column = 0)
längengrad.grid(row = 14, column = 1)
aao_label.grid(row = 15, column = 0)
aao.grid(row = 15, column = 1)
fertig_button.grid(row = 16, column = 0)
exit_button.grid(row = 16, column = 1)
 

 
# Ereignisschleife
fenster.mainloop()
