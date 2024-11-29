from Text import Text  # Import des Text-Dictionaries für mehrsprachige Textausgabe
from Prices import prices  # Import des Dictionaries mit Ticketpreisen

price_sum_global = 0.0  # Globale Variable für die Gesamtsumme aller Ticketpreise

# Sprachauswahl
print(Text['lang_select'])  # Aufforderung, die Sprache auszuwählen
print(Text['lang_input'])   # Hinweis, wie die Sprache eingegeben werden soll

# Setzt die Sprache basierend auf Benutzereingabe
if input().lower() == 'e':  # Falls 'e' eingegeben wird, wird Englisch gesetzt
    lang = 'EN'
else:  # Standardmäßig wird Deutsch als Sprache gesetzt
    lang = 'DE'

# Funktion zur Sprachwahl für Textbausteine
def get_text(key):
    """
    Holt den Text für den angegebenen Schlüssel und die aktuelle Sprache.
    Falls die Sprache oder der Schlüssel nicht gefunden wird, wird eine Fehlermeldung zurückgegeben.
    """
    if key in Text:  # Prüft, ob der Schlüssel im Text-Dictionary existiert
        if lang in Text[key]:  # Prüft, ob der Schlüssel für die gewählte Sprache vorhanden ist
            return Text[key][lang]
        else:
            return f'Sprache {lang} nicht in key {key}'  # Fehlermeldung, falls die Sprache fehlt
    else:
        return f'Key nicht im Text {key}'  # Fehlermeldung, falls der Schlüssel fehlt

# Hauptschleife zur Ticketabfrage
ticket = True
while ticket:
    ticket_price = 0.0  # Zurücksetzen des Ticketpreises bei jeder neuen Abfrage
    print(get_text('start_text'))  # Begrüßungstext
    print(get_text('age_input'))   # Aufforderung zur Eingabe des Alters

    # Altersabfrage mit Validierung
    while True:
        age = input()  # Eingabe des Alters
        try:
            age = int(age)  # Versucht, die Eingabe in eine Ganzzahl umzuwandeln
            break  # Falls erfolgreich, wird die Schleife beendet
        except ValueError:
            print(get_text('false_age'))  # Fehlermeldung bei ungültiger Eingabe

    # Abfrage, ob halbes oder ganzes Ticket gewünscht ist
    print(get_text('ticket_half_full'))

    while True:
        day = input().lower()  # Eingabe des Tickettyps (halb/ganz)
        if day in ['halb', 'ganz', 'half', 'full']:  # Validierung der Eingabe
            break
        else:
            print(get_text('invalid_input'))  # Fehlermeldung bei ungültiger Eingabe

    # Preisberechnung basierend auf Altersgruppe
    if age < 14:  # Kinderpreis
        if day in ['halb', 'half']:  # Halbes Ticket
            ticket_price += prices['kid_half']
            print(get_text('child_half'))
        else:  # Ganzes Ticket
            ticket_price += prices['kid']
            print(get_text('child_full'))
    elif 14 <= age <= 18:  # Jugendpreis
        if day in ['halb', 'half']:  # Halbes Ticket
            ticket_price += prices['teen_half']
            print(get_text('youth_half'))
        else:  # Ganzes Ticket
            ticket_price += prices['teen']
            print(get_text('youth_full'))
    else:  # Erwachsener
        # Abfrage nach Mitgliedschaft
        print(get_text('membership_query'))
        print(get_text('membership_premium'))  # Premium-Mitgliedschaft
        print(get_text('membership_basic'))    # Basis-Mitgliedschaft
        print(get_text('membership_none'))     # Keine Mitgliedschaft
        antwort_rabatt = input().lower()

        if antwort_rabatt == "p":  # Premium-Mitglied
            if day in ['halb', 'half']:
                ticket_price += prices['premium_half']
                print(get_text('premium_half'))
            else:
                ticket_price += prices['premium']
                print(get_text('premium_full'))
            print(get_text('price_prompt'), ticket_price, "Euro")

            # Zusatzangebot für Premium-Mitglieder: Sekt
            print(get_text('champagne_offer'))
            sekt = input().lower()
            if sekt in ["j", "y"]:  # Falls ja, wird der Preis für Sekt hinzugefügt
                ticket_price += 0.75
                print(get_text('price_prompt'), ticket_price, "Euro")
        elif antwort_rabatt == "b":  # Basis-Mitglied
            if day in ['halb', 'half']:
                ticket_price += prices['basic_half']
                print(get_text('basic_half'))
            else:
                ticket_price += prices['basic']
                print(get_text('basic_full'))
        elif antwort_rabatt == "n":  # Keine Mitgliedschaft
            if day in ['halb', 'half']:
                ticket_price += prices['adult']
                print(get_text('adult_half'))
            else:
                ticket_price += prices['adult_full']
                print(get_text('adult_full'))

    # Endpreis des aktuellen Tickets anzeigen
    print(get_text('price_prompt'), ticket_price, " Euro")

    # Ticketpreis zur globalen Gesamtsumme hinzufügen
    print(get_text('add_to_total'))
    add_to_total = input().lower()
    if add_to_total in ["j", "y"]:  # Falls der Benutzer zustimmt, wird der Preis addiert
        price_sum_global += ticket_price
        print(get_text('added_to_total'), price_sum_global, "Euro")
    else:
        print(get_text('not_added_to_total'))

    # Abfrage, ob weitere Tickets benötigt werden
    print(get_text('another_inquiry'))
    abfrage_ticket = input().lower()
    if abfrage_ticket == "n":  # Falls keine weiteren Tickets benötigt werden
        print(get_text('thank_you'), price_sum_global, get_text('enjoy'))  # Abschlusstext
        break  # Beendet die Schleife
    print("\n")  # Leerzeile zur Trennung der nächsten Abfrage
