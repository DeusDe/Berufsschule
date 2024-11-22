#!/usr/bin/python3
# Autor: v.erkuerzer@omega.it
# Version: 0.3
# Projekt: Tarifauskunft duidbyte (Basis: Lastenheft-Auszug)

# Text-Dictionary
from Text import Text

# Preise für halben Tag
preis_erwachsene_halb = 5.0
preis_jugendliche_halb = 3.5
preis_kinder_halb = 2.5
preis_premium_halb = 3.0
preis_basis_halb = 4.0

# Preise für ganzen Tag
preis_erwachsene_ganz = 10.0
preis_jugendliche_ganz = 6.0
preis_kinder_ganz = 5.0
preis_premium_ganz = 6.0
preis_basis_ganz = 8.0

global_gesamt_preis = 0.0  # Globale Gesamtsumme aller Ticketpreise

# Sprachauswahl
print(Text['lang_select'])
print(Text['lang_input'])

lang = input().lower()

if lang == 'e':
    lang = 'EN'
else:
    lang = 'DE'

# Funktion zur Auswahl der richtigen Sprache
def get_text(key):
    return Text[key][lang]

# Haupt-Loop für Ticketabfragen
ticket = True
while ticket:
    gesamt_preis = 0.0  # Gesamtpreis bei jedem neuen Ticket zurücksetzen
    print(get_text('start_text'))
    print(get_text('age_input'))

    # Alterseingabe mit Fehlerprüfung
    while True:
        alter_gast = input()
        try:
            alter_gast = int(alter_gast)
            break
        except ValueError:
            print(get_text('false_age'))

    # Tagesauswahl
    print(get_text('ticket_half_full'))

    while True:
        tageswahl = input().lower()
        if tageswahl in ['halb', 'ganz', 'half', 'full']:
            break
        else:
            print(get_text('invalid_input'))

    # Preisberechnung nach Altersgruppe
    if alter_gast < 14:
        if tageswahl in ['halb', 'half']:
            gesamt_preis += preis_kinder_halb
            print(get_text('child_half'))
        else:
            gesamt_preis += preis_kinder_ganz
            print(get_text('child_full'))
    elif 14 <= alter_gast <= 18:
        if tageswahl in ['halb', 'half']:
            gesamt_preis += preis_jugendliche_halb
            print(get_text('youth_half'))
        else:
            gesamt_preis += preis_jugendliche_ganz
            print(get_text('youth_full'))
    else:
        # Abfrage der Mitgliedschaft
        print(get_text('membership_query'))
        print(get_text('membership_premium'))
        print(get_text('membership_basic'))
        print(get_text('membership_none'))
        antwort_rabatt = input().lower()

        if antwort_rabatt == "p":
            if tageswahl in ['halb', 'half']:
                gesamt_preis += preis_premium_halb
                print(get_text('premium_half'))
            else:
                gesamt_preis += preis_premium_ganz
                print(get_text('premium_full'))
            print(get_text('price_prompt'), gesamt_preis, "Euro")

            # Zusatzoption für Premium-Mitglieder
            print(get_text('champagne_offer'))
            sekt = input().lower()
            if sekt in ["j", "y"]:
                gesamt_preis += 0.75
                print(get_text('price_prompt'), gesamt_preis, "Euro")
        elif antwort_rabatt == "b":
            if tageswahl in ['halb', 'half']:
                gesamt_preis += preis_basis_halb
                print(get_text('basic_half'))
            else:
                gesamt_preis += preis_basis_ganz
                print(get_text('basic_full'))
        elif antwort_rabatt == "n":
            if tageswahl in ['halb', 'half']:
                gesamt_preis += preis_erwachsene_halb
                print(get_text('adult_half'))
            else:
                gesamt_preis += preis_erwachsene_ganz
                print(get_text('adult_full'))

    # Preis anzeigen
    print(get_text('price_prompt'), gesamt_preis, " Euro")

    # Ticketpreis zur Gesamtsumme hinzufügen
    print(get_text('add_to_total'))
    add_to_total = input().lower()
    if add_to_total in ["j", "y"]:
        global_gesamt_preis += gesamt_preis
        print(get_text('added_to_total'), global_gesamt_preis, "Euro")
    else:
        print(get_text('not_added_to_total'))

    # Weitere Abfrage
    print(get_text('another_inquiry'))
    abfrage_ticket = input().lower()
    if abfrage_ticket == "n":
        print(get_text('thank_you'), global_gesamt_preis, get_text('enjoy'))
        break
    print("\n")
