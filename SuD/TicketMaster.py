from Text import Text # Text-Dictionary
from Prices import prices # Price-Dictionary

price_sum_global = 0.0  # Globale Gesamtsumme aller Ticketpreise

# Sprachauswahl
print(Text['lang_select'])
print(Text['lang_input'])

#Setzt die sprache von dem Input
if input().lower() == 'e':
    lang = 'EN'
else:
    lang = 'DE' #Deutsch ist der Fallback

# Funktion zur Auswahl der richtigen Sprach Strings
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
    ticket_price = 0.0  # Gesamtpreis bei jedem neuen Ticket zurücksetzen
    print(get_text('start_text'))
    print(get_text('age_input'))

    # Alterseingabe mit Fehlerprüfung
    while True:
        age = input()
        try: #Überprüfung ob das alter in einem int umgewandelt werden kann, ansonsten wird der loop neu ausgeführt
            age = int(age)
            break
        except ValueError:
            print(get_text('false_age'))

    # Tagesauswahl
    print(get_text('ticket_half_full'))

    while True:
        day = input().lower()
        if day in ['halb', 'ganz', 'half', 'full']:
            break
        else:
            print(get_text('invalid_input'))

    # Preisberechnung nach Altersgruppe
    if age < 14:
        if day in ['halb', 'half']:
            ticket_price += prices['kid_half']
            print(get_text('child_half'))
        else:
            ticket_price += prices['kid']
            print(get_text('child_full'))
    elif 14 <= age <= 18:
        if day in ['halb', 'half']:
            ticket_price += prices['teen_half']
            print(get_text('youth_half'))
        else:
            ticket_price += prices['teen']
            print(get_text('youth_full'))
    else:
        # Abfrage der Mitgliedschaft
        print(get_text('membership_query'))
        print(get_text('membership_premium'))
        print(get_text('membership_basic'))
        print(get_text('membership_none'))
        antwort_rabatt = input().lower()

        if antwort_rabatt == "p":
            if day in ['halb', 'half']:
                ticket_price += prices['premium_half']
                print(get_text('premium_half'))
            else:
                ticket_price += prices['premium']
                print(get_text('premium_full'))
            print(get_text('price_prompt'), ticket_price, "Euro")

            # Zusatzoption für Premium-Mitglieder
            print(get_text('champagne_offer'))
            sekt = input().lower()
            if sekt in ["j", "y"]:
                ticket_price += 0.75
                print(get_text('price_prompt'), ticket_price, "Euro")
        elif antwort_rabatt == "b":
            if day in ['halb', 'half']:
                ticket_price += prices['basic_half']
                print(get_text('basic_half'))
            else:
                ticket_price += prices['basic']
                print(get_text('basic_full'))
        elif antwort_rabatt == "n":
            if day in ['halb', 'half']:
                ticket_price += prices['adult']
                print(get_text('adult_half'))
            else:
                ticket_price += prices['adult_full']
                print(get_text('adult_full'))

    # Preis anzeigen
    print(get_text('price_prompt'), ticket_price, " Euro")

    # Ticketpreis zur Gesamtsumme hinzufügen
    print(get_text('add_to_total'))
    add_to_total = input().lower()
    if add_to_total in ["j", "y"]:
        price_sum_global += ticket_price
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
