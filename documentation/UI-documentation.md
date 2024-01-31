  
  

Dieses Dokument bietet einen Überblick über die Benutzeroberfläche (UI) des [Projekts MindMachine](../README.md).

Es beschreibt die wichtigsten Aspekte der Benutzeroberfläche und wie Benutzer damit interagieren können.

---

# 1. Benutzeranforderungen

  

Eines der wesentlichen Projektziele ist die Benutzerfreundlichkeit:

Die Anwendung soll eine leicht verständliche Benutzeroberfläche bieten, die eine intuitive Navigation und Interaktion ermöglicht. Sowohl HTW-Anwender als auch Administratoren sollen sich mühelos auf der Plattform zurechtfinden können.

  

Folgende Auflistung fasst die **wichtigsten Anforderungen** an die Benutzeroberfläche, die auf den Bedürfnissen und Erwartungen der Benutzer basieren, zusammen.

  

1. **Anmeldung**: Benutzer müssen sich mit ihren HTW-Anmeldeinformationen (Benutzername und Passwort) auf der Website anmelden können.

  

2. **Datei-Upload**: Benutzer müssen die Möglichkeit haben, Dokumente im pdf-Format auf die Plattform hochzuladen.

  

3. **Suchfunktion**: Die Benutzeroberfläche muss eine Suchleiste bieten, über die Benutzer nach Fragen und Inhalten suchen können.

  

4. **Ergebnisliste**: Nach einer Suche werden die Suchergebnisse in einer übersichtlichen Liste dargestellt. Dabei sollen relevante Informationen wie Titel, Beschreibung und Autor angezeigt werden.

  

5. **Dateidownload**: Benutzer müssen die heruntergeladenen Dateien in ihrem persönlichen Profil verwalten können. Dies beinhaltet das Herunterladen von Dateien und das Löschen nicht mehr benötigter Dateien.

  

6. **Benachrichtigungen**: Die UI sollte Benutzer über wichtige Ereignisse wie erfolgreiches Hochladen von Dateien oder neue Antworten auf gestellte Fragen benachrichtigen.

  

7. **Benutzerfreundlichkeit**: Die Benutzeroberfläche muss intuitiv und benutzerfreundlich gestaltet sein, damit Benutzer ohne größere Schwierigkeiten navigieren und Aufgaben erledigen können.


  

---
 

# 2. UI-Designkonzepte

  

Das UI-Designkonzept orientiert sich an den [Designvorgaben der HTW Berlin](https://corporatedesign.htw-berlin.de/).

Demnach wurden folgende Designelemente gewählt:

- **Farbschema**: Der Hintergrund ist hauptsächlich in grau gehalten, um die Intensität des Lichts zu reduzieren und die Elemente in den von der HTW vorgegebenen Farbcodes optisch besser zu Geltung kommen zu lassen. Zu den verwendeten Farbcodes gehören unter anderem:

    - Farbcode des HTW-Grün (Hex): 76B900

    - Farbcode für Tabellenköpfe (Hex): 0272F5

    - Farbcodes des Hintergrunds (Hex): FFFFF 95%

    - Farbcodes für optische Highlights (Hex): A8BBFE 75% , 774DF0 66%

- **Schriften**: Auch bei der Wahl der Schrift wurde auf die Design-Vorgaben der HTW berücksichtigt

    - Schriftart: HTWBerlin Office

    - Schriftgröße für Desktop: 48, 24, 20

    - Schriftgröße für Smartphone: 24, 20, 16 (geplant, nicht umgesetzt)

  

---

  

# 3. Wireframes und Mockups 

  

Die Navigation zwischen Seiten erfolgt hauptsätzlich beim Klicken auf Buttons und kann in Abb. 1: Wireframes nachvollzogen werden

![Prototyp](./assets/Mind-Machine-Prototyping.png)

*Abb. 1: Wireframes der Webanwendung* 

## 3.1 Interaktionsfluss

  

Der Interaktionsfluss besteht im Wesentlichen aus den folgenden Schritten:

- Beim Aufrufen der Website fungiert die Log-In-Seite als Startseite.

      Auf der Startseite befinden sich zwei Buttons:

    - Log-In-Button für HTW-Anwender ohne Admin-Status

    - Log-In-Button für Administratoren der als Admin

    Hier muss der Benutzer Anmeldeinformationen eingeben und auf einen Button zu klicken.

- Nach der Anmeldung, landet der Nutzer auf seiner userspezifischen Library-Ansicht

    Auf der userspezifischen Library-Ansicht befinden sich folgende Elemente:

    - Search-Textbox zur Eingabe der Suche

    - Search-Button um die Suche zu starten

    - Mikrofon-Button zum Starten der Speech-To-Text-Funktion

    - Add-new-file-Button um neue Datei hochzuladen

    Mittels des Navigationsbars am Seitenkopf kann der Nutzer auf folgende Seiten zugreifen:

    - Home: Redirect zur Library-Ansicht

    - Search History: Übersicht über vergangene Suchanfragen

    - Log Out: Redirect zur Anmeldeseite

    - Admin Panel: Zugriff auf die Admin-Page (vorausgesetzt Adminstatus vorhanden)

  

## 3.2 Mockups

  

Nachfolgend befinden sich Mockups der wichtigsten Seiten  der Benutzeroberfläche, um den visuellen Entwurf zu verdeutlichen.

  
![Wireframe-Login](./assets/Wireframe%20-%201Login.png)
*Abb. 2: Mockup Startseite* 

  
![Wireframe-Home](./assets/Wireframe%20-%202Home.png)
*Abb. 3: Mockup userspezifischen Bibliothek-Startseite* 

  
![Wireframe-Results](./assets/Wireframe%20-%203Result.png)
*Abb. 4: Mockup Ergebnisseite der aktuellen Suchanfrage*

  
![Wireframe-FileInformation](./assets/Wireframe%20-%205FileInformation.png)
*Abb. 5: Mockup Dokumenteninformation*

![Wireframe-SearchHistory](./assets/Wireframe%20-%204SearchHistory.png)
*Abb. 6: Mockup der Suchhistorie*

  
![Wireframe-Impressum](./assets/Wireframe%20-%206Impressum.png)
*Abb. 7: Mockup des Impressums*


![Logo](./assets/Log*o.png)
*Abb. 8: Logo*

---

  

## 4. Benutzerfreundlichkeit

  

## 4.1 Barrierefreiheit 

  

Die Barrierefreiheit ist ein wesentlicher Aspekt unseres Projekts MindMachine, da wir sicherstellen möchten, dass unsere Webanwendung für alle Benutzer zugänglich und nutzbar ist, unabhängig von ihren individuellen Fähigkeiten oder Beeinträchtigungen.

  

1. **Text-Alternative**: Bilder, Grafiken und andere nicht-textuelle Inhalte sollten alternative Textbeschreibungen haben, damit Menschen mit Sehbehinderungen den Inhalt verstehen können. Screenreader können diese Textbeschreibungen vorlese

  

2. **Kontrast und Farbgestaltung**: Die Farben und der Kontrast in der Anwendung sollten so gestaltet sein, dass sie auch für Menschen mit Sehbehinderungen gut sichtbar sind.

  

3. **Strukturierte Semantik**: Die Verwendung von HTML-Elementen sollte semantisch korrekt sein, um die Informationen in einer logischen und verständlichen Reihenfolge darzustellen. Dies hilft Screenreadern und anderen Hilfsmitteln, den Inhalt richtig zu interpretieren.

  

## 4.2 Akzeptanzkriterien

  

- Die Benutzeroberfläche muss auf den gängigsten Webbrowsern korrekt angezeigt werden.

- Die Ladezeiten für Seiten oder Funktionen dürfen 2 Sekunden nicht überschreiten.

Alle Akzeptanzkriterien hinsichtlich der Benutzeroberfläche konnten wie geplant erfüllt werden werden und sind damit losgelöst vom [Scoping Document](https://gitlab.rz.htw-berlin.de/iiw-vertiefung-softwareengineering/202324-wise/mindmachine/mindmachine/-/blob/main/documentation/scoping-document.md) dokumentiert.

  

Im Zuge einer Weiterentwicklung der **MindMachine**-Webanwendung könnte das responsive Design ggf. für Smartphones ausgeweitet werden. Dies war in dieser Projektphase jedoch nicht von sonderlich hoher Bedeutung, da ein Zugriff auf die Webadresse nur bei Verbindung mit der HTW-Netzwerk möglich ist.

  
