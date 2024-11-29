#!/usr/bin/python3
# Autor: v.erkuerzer@omega.it
# Version: 0.3
# Projekt: Tarifauskunft duidbyte (Basis: Lastenheft-Auszug)

# Text-Dictionary
from Text import Text
from Prices import prices

price_sum_global = 0.0  # Globale Gesamtsumme aller Ticketpreise

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
    if key in Text:
        if lang in Text[key]:
            return Text[key][lang]
        else:
            return f'Sprache {lang} nicht in key{key}'
    else:
        return f'Key nicht im Text{key}'

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
            gesamt_preis += prices['kid_half']
            print(get_text('child_half'))
        else:
            gesamt_preis += prices['kid']
            print(get_text('child_full'))
    elif 14 <= alter_gast <= 18:
        if tageswahl in ['halb', 'half']:
            gesamt_preis += prices['kid_teen_half']
            print(get_text('youth_half'))
        else:
            gesamt_preis += prices['kid_half']
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
                gesamt_preis += prices['premium_half']
                print(get_text('premium_half'))
            else:
                gesamt_preis += prices['premium']
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
                gesamt_preis += prices['basic_half']
                print(get_text('basic_half'))
            else:
                gesamt_preis += prices['basic']
                print(get_text('basic_full'))
        elif antwort_rabatt == "n":
            if tageswahl in ['halb', 'half']:
                gesamt_preis += prices['adult']
                print(get_text('adult_half'))
            else:
                gesamt_preis += prices['adult_full']
                print(get_text('adult_full'))

    # Preis anzeigen
    print(get_text('price_prompt'), gesamt_preis, " Euro")

    # Ticketpreis zur Gesamtsumme hinzufügen
    print(get_text('add_to_total'))
    add_to_total = input().lower()
    if add_to_total in ["j", "y"]:
        price_sum_global += gesamt_preis
        print(get_text('added_to_total'), price_sum_global, "Euro")
    else:
        print(get_text('not_added_to_total'))

    # Weitere Abfrage
    print(get_text('another_inquiry'))
    abfrage_ticket = input().lower()
    if abfrage_ticket == "n":
        print(get_text('thank_you'), price_sum_global, get_text('enjoy'))
        break
    print("\n")
