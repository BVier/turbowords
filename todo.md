# TODO b4:

### Startseite ordentlich formattieren
- [x] Buttons
- [x] Liste auswählen
- [x] Bearbeiten - Menü

### Listenübersicht
- [x] Zurück Button
- [x] Teilnehmername
- [x] ms-Einstellung

### Bearbeiten
- [x] Liste bearbeiten
- [x] Liste löschen
- [x] Liste hinzufügen

### Wort-Seite:
- [x] Buttons in Reihenfolge
- [x] Wiederholungs-Button

### Auswertung
- [x] schön und 
- [x] Button auf Startseite

### Patienten
- [ ] Patienten-Seite nach Login
- [ ] Patienten erstellen
- [ ] Patienten wählen
- [ ] index: Patienten ändern

### User Authentication
- [x] Login
- [ ] Logout
- [ ] User erstellen
- [ ] Gruppen
- [ ] Berechtigungen


### Befehle:

- Migration & Start:
```py manage.py makemigrations wordlists; py manage.py migrate; py manage.py runserver```
- Style update & Start: 
```cd .\static_src\; npm run compile:css; cd .. ; python manage.py collectstatic; python manage.py runserver```