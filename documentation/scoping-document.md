In diesem Dokument wird der tatsächlich umgesetzten Projektumfang und die aus den begrenzten Ressourcen resultierenden Grenzen des Projekts erläutert. Zudem erfolgt ein Vergleich der geplanten und tatsächlichen eingehaltenen Meilenstein und Liefergegenstände der einzelnen Sprints, eine Risikoanalyse, sowie eine Auswertung des Risiko- und Projektmanagements auf Grundlage der vorangegangenen Erkenntnisse.

# 1. Projektumfang und Grenzen 


 Eine detailliertere Beschreibung der funktionalen und nicht-funktionalen Anforderungsanalyse befindet sich im [Requirement Dokument](https://gitlab.rz.htw-berlin.de/iiw-vertiefung-softwareengineering/202324-wise/mindmachine/mindmachine/-/blob/main/documentation/requirements-document.md).

---

## 1.1 Funktionalen Anforderungen


### Im Projektumfang enthalten
  

Bei der nachfolgenden Auflistung handelt es sich um erfolgreich implementierten Funktionalitäten in priorisierter Reihenfolge:

  

- **Benutzerzugriff und Authentifizierung:**

  - Öffnen der Website für HTW-Anwender und Administratoren.

  - Sicheres Anmelden für HTW-Anwender mit personalisierten Startseiten.

  - Manuelle Abmeldung und automatisches Ausloggen bei Inaktivität für erhöhte Privatsphäre und Sicherheit.

  

- **Dateiverwaltung:**

  - Privates Dateiverzeichnis für HTW-Anwender mit Ansicht.

  - Hochladen von Dateien mit Prüfung auf Gültigkeit (OCR-PDF).

  - Öffnen, Löschen und Umbenennen von Dokumenten im privaten Verzeichnis.

  

- **Intelligente Suchfunktion:**

  - Text- und Sprachabfrage für ML-Integration.

  - Anpassung und Bearbeitung von gestellten Fragen.

  - Anzeige von Suchhistorie und erneutes Auslösen vergangener Suchanfragen.

  

- **Administrationsfunktionen:**

  - Anmeldung für HTW-Administratoren mit speziellen Privilegien.

  - Globale Änderung der Speicherkapazität für alle Benutzer.

  - Anzeige von Statistiken zu Fragen, Nutzerzahlen und Speicherkapazität.

  - Einstellung des automatischen Log-Outs für Benutzer.

  - Logging-Protokollverwaltung für umfassende Überwachung und Fehleranalyse.

  
Hinsichtlich der funktionalen Anforderungen kann festgehalten werden, dass alle User Storys zum Ende des letzten Sprints geschlossen werden konnten. Jedoch gibt es geringfügige Abweichungen bei der Erfüllung einzelner Akzeptanzkriterien der funktionalen Anforderungen. Folgende Funktionalität konnten nicht in dieser Projektphase implementiert werden und sind somit den folgenden Weiterentwicklungsprojektphase zu ergänzen:

  

### Nicht im Projektumfang enthaltene Funktionen

  
#### User Story 1.1: Website öffnen als Anwender


- **Nicht enthaltene Akzeptanzkriterien:**

    - Punkt 1: Öffentlicher Zugang ist vorbereitet, die Freigabe in der Firewall durch die IT der HTW Berlin steht noch aus.


#### User Story 4.1: Ergebnisse anzeigen lassen

  

- **Nicht enthaltene Akzeptanzkriterien:**

    - Punkt 6: Oberhalb der Ergebnisse wird eine zusammenfassende Antwort auf die gestellte Frage präsentiert.

    - Punkt 7 (teilweise): Link zum PDF nicht in der gleichen Seite geöffnet.

  

#### User Story 4.2: Relevante Passagen kopieren

  

- - **Nicht enthaltene Akzeptanzkriterien:**

    - Punkt 3: Keine Quellenangaben zu den Dokumenten.

  

#### User Story 3.2: Frage abändern

  

- **Nicht enthaltene Akzeptanzkriterien:**

    - Technische Implementierung vorhanden, jedoch Verbesserungsbedarf in der Benutzerfreundlichkeit.

  

#### User Story 6.3: Speicherkapazität anzeigen lassen

  

- **Enthaltene Akzeptanzkriterien, jedoch mit optimierbarer Benutzerfreundlichkeit:**

    - Punkt 2: Die angezeigte globale Speicherkapazität entspricht der tatsächlichen Kapazität des Servers.

    - Punkt 3: Die Anzeige umfasst Informationen über den aktuellen Speicherstand und verfügbaren Speicherplatz.

    - Punkt 4: Die globale Speicherkapazität wird in einem leicht verständlichen Format präsentiert.

- **Nicht enthaltene Akzeptanzkriterien:**

    - Punkt 6: Der Administrator kann auf der Admin-Verwaltungsseite den Verlauf der globalen Speicherkapazität überprüfen

  

#### User Story 6.4: Statistiken anzeigen lassen

  

- **Nicht enthaltene Akzeptanzkriterien:**

    - Punkt 2: Keine Statistiken zu den Fragestellungen im UI.

    - Punkt 7: Keine Anzeige der userspezifischen Speicherkapazität.

    - Punkt 10: Zeitraumauswahl für Statistiken nicht implementiert.

  

#### User Story 6.6: Logging-Protokollverwaltung

  

- **Nicht implementierbar:**

    - Punkt 4: Die Nutzerstatistiken umfassen Informationen wie Gesamtzahl der aktiven Benutzer. Nicht umsetzbar.

  

---

## 1.2 Umsetzung der nicht-funktionale Anforderungen


### Leistung

- **Reaktionsgeschwindigkeit**:

    - Antwortzeiten im Millisekundenbereich, sehr gut bewertet.

    - Uploadgeschwindigkeit abhängig von Internetverbindung und Dateigröße.

    - Begrenzung für gleichzeitigen Dateiupload: 20 MB.

- **Skalierbarkeit**:

    - Gute Skalierbarkeit, anpassbar auf Kundenwunsch.

    - Verbesserung durch bessere Hardware und effizientere Verteilung von Nutzerzugriffen auf verschiedene Docker möglich.
 

### Sicherheit

- **Benutzerdatenschutz**:

    - Bisher keine strikte Befolgung der Datenschutzrichtlinien, unrealistisch bei gegebenen Projektressourcen.

- **Authentifizierung und Autorisierung**:

    - JW-Tokens wurden für die Authentifizierung und Autorisierung implementiert.

- **Schutz vor Angriffen**:

    - Kein Schutz gegen SQL-Injektionen und XSS implementiert. Nachträglich Implementierung möglich.

- **Datensicherheit**:

    - Keine Datensicherheit abseits von vorbereitetem HTTPS-Zertifikat vorhanden. Demnach auch keine Daten-Backups vorhanden.
  

### Benutzerfreundlichkeit

- **Barrierefreiheit**:

    - Keine mobile Ansicht vorhanden und nicht geplant.

- **Dokumentation**:

    - Nachzulesen im [Testing Documentation](https://gitlab.rz.htw-berlin.de/iiw-vertiefung-softwareengineering/202324-wise/mindmachine/mindmachine/-/blob/main/documentation/UI-documentation.md) und [UI-Documentation](https://gitlab.rz.htw-berlin.de/iiw-vertiefung-softwareengineering/202324-wise/mindmachine/mindmachine/-/blob/main/documentation/UI-documentation.md)

  
### Zuverlässigkeit

- **Testing**:

    - Hier befindet sich eine Dokumentation der [Testing Strategie](https://gitlab.rz.htw-berlin.de/iiw-vertiefung-softwareengineering/202324-wise/mindmachine/mindmachine/-/blob/main/documentation/testing-strategy.md). 

    - Während der Entwicklungsphase wurden ausschließlich manuelle Funktionstest auf der Website durchgeführt. 
   
    -  Derzeit erfolgt ein automatisches Neubauen des Projekts auf dem   Produktionsserver bei Merges im Git, ergänzt durch eine Vorbereitung zur Test- Implementierung.

  
### Wartbarkeit

- **Kommentierungsrichtlinien**:

    - Einheitlicher Stil für JavaScript (JSDoc) und Python (PEP 257).

    - Detaillierte Richtlinien für Code-Kommentare, inklusive Header-, Funktions-/Methoden- und Inline-Kommentare.


### Testing-Infrastruktur und Evaluierung der Suchalgorithmen

Im Rahmen der Weiterentwicklung der **MindMachine**-Anwendung wurde eine umfangreiche Testing-Pipeline etabliert, die es ermöglicht, die Effektivität unterschiedlicher Suchmethoden zu evaluieren. Folgende Hyperparameter können für jeden Test konfiguriert werden:

1. **Encoder**: Definition des spezifischen Encoders.
2. **Distance**: Auswahl der Distanzfunktion, entweder COS oder DOT, die die Ähnlichkeitsmessung bestimmt.
3. **Chunk Size**: Festlegung, ob und wie Dokumente in kleinere Segmente aufgeteilt werden, um die maximale Sequenzlänge des Encoders nicht zu überschreiten.
4. **Remove Stop-Words**: Entscheidung über das Entfernen von Füllwörtern aus dem Text zur Optimierung der Suchergebnisse.
5. **Overlap**: Bestimmung des Überlappungsgrades zwischen aufeinanderfolgenden Textsegmenten, falls eine Aufteilung stattfindet.

Diese Pipeline analysiert die eingereichten Fragen aus einem definierten Datensatz, encodet die zugehörigen Dokumente und integriert diese in Qdrant, wobei jeder Testlauf einem spezifischen Collectionnamen zugewiesen wird. Anschließend erfolgt eine systematische Abfrage dieser Kollektion, um die Präzision der Suchergebnisse zu bestimmen. 

![Testergebnisse KI-Suche](https://lh7-us.googleusercontent.com/Oluzaa4uyx8aGQtn-9J5o5c2GjD9t49FkhKtnZWYq3wkXo5q4kA9XlHh99crsd1PPYAZNdi7k7kLB4Ir2RrtitnaOYmKktXbAfrXAOn-ZXz4aO4lfYULYijKjyNoPmic_4UDErERW9qeQeWzWCssG1Q)
*Abb 1.: Testergebnisse für Englisch und Deutsch im Vergleich mit den selben vier Testkategorien* 

Die Genauigkeit wird pro Sprache und Kategorie dargestellt und in einem Genauigkeitsplot visualisiert, der die durchschnittliche Präzision über alle Kategorien hinweg zeigt.

Die höchste Präzision wurde mit dem Modell 'multi-qa-mpnet-base-dot-v1' erreicht, bei Verwendung der DOT-Distanzfunktion, einem Überlappungswert von 30 und ohne Entfernung von Stop-Words. Diese Konfiguration erzielte eine Genauigkeit von 100 % bei englischen und 58 % bei deutschen Dokumenten. Basierend auf den Anforderungen, die Suche primär in Englisch durchzuführen, wurde diese Methode für die Implementierung ausgewählt.

Die Suchanfragen in Qdrant geben eine Passage von maximal 512 Wörtern zurück, was der maximalen Sequenzlänge des 'mpnet'-Modells entspricht. Zur Extraktion der spezifischen Antworten aus diesen Passagen wird ein Extractive Question-Answering BERT-Modell ('distilbert-base-cased-distilled-squad') verwendet, das nach einem Satzende sucht, um eine vollständige Antwort zu liefern. Schließlich wird dem Frontend ein Dictionary bereitgestellt, das Dokumentennamen, Passagen und den extrahierten Satz enthält.

---

# 2. Meilensteine und Liefergegenstände

  

Die Hauptziele des Projekts waren die Entwicklung einer benutzerfreundlichen Webanwendung mit den Kernfunktionen: Benutzerzugriff, Dateiverwaltung und intelligente Suche. Die Liefergegenstände umfassten eine fertige Plattform, die an den Arbeitsalltag der HTW-Nutzer angepasst ist.

  

Nachfolgend befindet sich ein visuelle Aufarbeitung der geplanten Meilensteine und entsprechenden Liefergegenstände und eine visuelle Aufarbeitung des tatsächliche Projektverlaufs.


![Geplante Milestones](./assets/milestones_planned.jpg)
*Abb. 2: geplante Sprintverläufe*


![Tatsächliche Milestones](./assets/milestones_reality.jpg)
*Abb 3.: tatsächlicher Sprintverläufe*

  

Vergleicht man die die geplanten und die tatsächlichen Sprintverläufe wird offensichtlich, dass trotz starker Abweichungen vom ursprünglichen Plan alle User Storys bis Projektende implementiert werden konnten. Dies ist unteranderem auf die steile Lernkurve des Teams als auch auf die agile Arbeitsweise im Projekt zurückzuführen.

---

# 3. Risikoanalyse und -management

  

Risiken im Projekt beinhalteten neben technische Herausforderungen, wie die Integration verschiedener Docker-Container und die Implementierung einer vektorbasierten Datenbank zusätzlich strukturelle in der universitären Projektarbeitsweise verankerte Risiken. Durch das frühzeitige Erkennen der Risiken konnten im gesamten Projektverlauf effektive Risikomanagement-Strategien umgesetzt werden, um diese Herausforderungen zu bewältigen. Nachfolgend befindet sich eine detaillierte Auflistung der erkannten und somit gemanagten Risiken:

  

#### Technische Risiken

  

- **Technologische Herausforderungen**: Risiken durch unbekannte Technologien oder Plattformen, die Entwicklungsdelay verursachen können.

- **Datenverlust**: Risiko des Datenverlusts aufgrund technischer Probleme oder Fehler in der Datenverwaltung. Keine Backups vorhanden, Risiko durch direktes Überschreiben von Produktionsdaten bei Merges.

  

#### Zeitliche Risiken

  

- **Projektzeitplan Verzögerungen**: Risiko von Verzögerungen durch unvorhergesehene Ereignisse oder Anforderungsänderungen.

  

#### Ressourcenrisiken

  

- **Mangelnde Ressourcen**: Risiko der Beeinträchtigung der Projektumsetzung aufgrund unzureichender personeller Ressourcen oder Budgetbeschränkungen.

  

#### Kommunikationsrisiken

  

- **Mangelnde Kommunikation**: Risiken durch fehlende oder ineffektive Kommunikation innerhalb des Teams und mit Stakeholdern, inklusive Sprachbarrieren und Erreichbarkeitsproblemen.

  

#### Anforderungsrisiken

  

- **Unklare Anforderungen**: Risiken durch unvollständige oder unklare Anforderungen, die zu Fehlinterpretationen und Änderungen im Projektumfang führen können.

  

#### Qualitätsrisiken

  

- **Niedrige Codequalität**: Risiko durch unzureichend getesteten oder nicht wartbaren Code, der die Softwarequalität beeinträchtigen könnte.

  

#### Sicherheitsrisiken

  

- **Datenschutzverletzungen**: Risiken durch unsichere Datenverarbeitung oder unsachgemäßen Umgang mit sensiblen Informationen.

  

#### Risiken im Projektmanagement

  

- **Fehlendes Projektmanagement**: Risiko der Ineffizienz und unkoordinierten Aktivitäten aufgrund mangelnder Erfahrung.

  

#### Externe Abhängigkeiten

  

- **Abhängigkeit von Dritten**: Risiko durch Abhängigkeit von externen Dienstleistern, deren Verfügbarkeit oder Dienstleistungsqualität das Projekt beeinflussen könnte.

  

#### Rechtliche Risiken

  

- **Urheberrechtsverletzungen**: Risiko rechtlicher Konsequenzen bei Nutzung von Software oder Inhalten ohne entsprechende Lizenzen.

  

---

# 4.  Projektmanagement-Übersicht 


Das Projekt nutzte agile Methoden in einer angepassten Form von Scrum und moderne Tools für Requirements- und Konfigurations-Management. Die Teamarbeit und enge Zusammenarbeit zwischen HTW Berlin und Studierenden waren zentrale Aspekte des Managements.

Im Projektverlauf wurde eine deutliche Steigerung der Teamleistung durch die angewandten und sukzessive optimierten Projektmanagement-Methoden erzielt. Dies ist deutlich anhand der Leistungssteigerung über die drei Sprint zu erkennen und kann in den nachfolgenden "Burn _out_ "-Charts nachvollzogen werden.


![Sprint 1](./assets/Sprint1.png)
*Abb. 4.: Burndown und Burnup-Chart von Sprint 1*


![Sprint 2](./assets/Sprint2.png)
*Abb. 5.: Burndown und Burnup-Chart von Sprint 2*


![Sprint 3](./assets/Sprint3.png)
*Abb. 6.:: Burndown und Burnup-Chart von Sprint 3*


---

# 5. Vorgeschlagene Erfolgsmetriken für zukünftige Bewertung



**Zweck:** Dieser Abschnitt skizziert Metriken, die für die zukünftige Bewertung und kontinuierliche Verbesserung des **MindMachine**-Projekts vorgeschlagen werden. Diese Metriken sind darauf ausgerichtet, die Effektivität der Anwendung in Bezug auf Benutzerfreundlichkeit, Leistung und Sicherheit zu messen.

  

**1. Benutzerfreundlichkeit:**

  

- **Benutzerzufriedenheitsbewertungen:** Regelmäßige Umfragen unter den Nutzern, um ihre Zufriedenheit mit der Anwendung auf einer Skala zu bewerten.

- **Analyse der Benutzerinteraktion:** Messung der durchschnittlichen Zeit, die Benutzer benötigen, um bestimmte Aufgaben zu erledigen.

  

**2. Effizienz der Dateiverwaltung:**

  

- **Erfolgsrate des Dateiuploads:** Anteil der erfolgreichen Uploads im Vergleich zu den Gesamtversuchen.

- **Durchschnittliche Upload-Zeit:** Messung der Zeit für das Hochladen von Dateien.

  

**3. KI-gestützte Suchanfragen:**

  

- **Genauigkeit der Suchergebnisse:** Bewertung der Relevanz der Suchergebnisse basierend auf Benutzerfeedback.

- **Antwortzeit der Suchanfragen:** Durchschnittliche Zeit von der Anfrage bis zur Ergebnisanzeige.

  

**4. Sicherheit und Datenschutz:**

  

- **Anzahl der Sicherheitsvorfälle:** Dokumentation und Bewertung aller Sicherheitsvorfälle.

- **Einhaltung von Datenschutzstandards:** Überprüfung der Einhaltung relevanter Datenschutzrichtlinien.

  

**5. Suchhistorie und Interaktionshistorie:**

  

- **Nutzung der Suchhistorie-Funktion:** Prozentsatz der Benutzer, die diese Funktion nutzen.

- **Wiederverwendung von Suchanfragen:** Häufigkeit der erneuten Nutzung vergangener Suchanfragen.

  

**Umsetzung:** Aufgrund der aktuellen Projektbeschränkungen (wie Zeit, Ressourcen und Umfang) ist die Implementierung und Analyse dieser Metriken außerhalb des Umfangs des aktuellen Projekts. Jedoch werden diese Metriken als wichtige Komponenten für die zukünftige Entwicklung und Bewertung des **MindMachine**-Projekts vorgeschlagen.

  

**Bedeutung:** Die Implementierung dieser vorgeschlagenen Erfolgsmetriken in zukünftigen Projektphasen wird eine umfassende Bewertung der Anwendungsleistung ermöglichen und wichtige Einblicke in Bereiche für Verbesserungen bieten. Dies könnte dazu beitragen, dass die langfristige Vision und die Ziele des Projekts über den aktuellen Rahmen hinaus berücksichtigt werden.