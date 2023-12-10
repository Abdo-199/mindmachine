# 1. Visionen und Ziele 

  

Die Vision für das MindMachine-Projekt ist die Schaffung einer intuitiven und leistungsstarken Browseranwendung, die es HTW-Anwendern ermöglicht, ihre Dateien effizient zu verwalten und mithilfe von KI-gestützten Suchanfragen relevante Informationen aus den Dokumenten zu extrahieren. Das Hauptziel besteht darin, eine benutzerfreundliche Plattform zu entwickeln, die nahtlos in den Arbeitsalltag der HTW-Anwender integriert werden kann.

  

Die wesentlichen Ziele des Projekts sind:

  

1. **Benutzerfreundlichkeit:** Die Anwendung soll eine leicht verständliche Benutzeroberfläche bieten, die eine intuitive Navigation und Interaktion ermöglicht. Sowohl HTW-Anwender als auch Administratoren sollen sich mühelos auf der Plattform zurechtfinden können.

  

2. **Effiziente Dateiverwaltung:** HTW-Anwender sollen in der Lage sein, ihr privates Dateiverzeichnis mithilfe der Anwendung effizient zu öffnen, Dateien hochzuladen, zu öffnen, zu löschen und umzubenennen. Die Ansicht des Dateiverzeichnisses soll dabei individuell auf den angemeldeten Benutzer zugeschnitten sein.

  

3. **KI-gestützte Suchanfragen:** Die Anwendung soll HTW-Anwendern die Möglichkeit bieten, Fragen in Form von Text- oder Sprachprompten zu stellen. Die KI verarbeitet diese Anfragen, generiert Suchanfragen und zeigt relevante Ergebnisse direkt auf der Benutzeroberfläche an.

  

4. **Sicherheit und Datenschutz:** Die Plattform muss höchsten Sicherheitsstandards genügen, insbesondere im Hinblick auf die Authentifizierung über HTW-Logins, sichere An- und Abmeldungsprozesse sowie den Schutz der Privatsphäre der Benutzer.

  

5. **Suchhistorie und Interaktionshistorie:** Die Anwendung soll eine Suchhistorie für HTW-Anwender bereitstellen, um vergangene Suchanfragen nachzuvollziehen. Die Möglichkeit, direkt zu den Ergebnissen vergangener Suchanfragen zu navigieren, trägt zur Effizienz und Nutzerfreundlichkeit bei.

  

Die erfolgreiche Umsetzung dieser Ziele wird dazu beitragen, den Workflow der HTW-Anwender zu verbessern, die Effizienz in der Dateiverwaltung zu steigern und den Zugriff auf relevante Informationen durch KI-gestützte Suchanfragen zu erleichtern. 

  

# 2. Anforderungsanalyse

  

Im Rahmen eines kollaborativen Kundenworkshops wurde ein umfassendes Story Mapping durchgeführt, das als grundlegende Struktur für die Anforderungsanalyse der MindMachine-Anwendung dient. Dieser Workshop ermöglichte eine interaktive Zusammenarbeit zwischen den Stakeholdern und dem Entwicklungsteam, um die wesentlichen Funktionen und Anforderungen zu identifizieren. Das Story Mapping (s. Abbildung XX) diente dabei als Orientierungspunkt, um die verschiedenen Aspekte der Anwendung zu verstehen und zu strukturieren.

  

![Story Mapping Diagramm](Documentation/assets/20231118_Story_Mapping_DiaWIP.jpg)

**Übersicht über Epics und User Stories:**

  

Das Story Mapping ergab eine klare Strukturierung der Anforderungen in mehrere Epics, die jeweils einen größeren funktionalen Bereich der Anwendung repräsentieren. Die Epics und ihre zugehörigen User Stories sind:



### Epic 1: Benutzerzugriff und Authentifizierung

- **User Story 1.1: Website öffnen als Anwender (HTW-Anwender und Admin)**
- **User Story 1.2: Log-In für HTW-Anwender**
- **User Story 1.3: Log-Out-Funktionalität**

### Epic 2: Dateiverwaltung

- **User Story 2.1: Datenverzeichnis öffnen mit userspezifischer Ansicht**
- **User Story 2.2: Dateien hochladen mit Prüfung**
- **User Story 2.3: Dokumente öffnen**
- **User Story 2.4: Dokumente löschen**
- **User Story 2.5: Dokument umbenennen**

### Epic 3: Interaktion mit KI-gestützten Suchanfragen

- **User Story 3.1: Frage als Textprompt stellen**
- **User Story 3.2: Frage abändern**
- **User Story 3.3: Frage als Sprachprompt stellen**

### Epic 4: Anzeige von Suchergebnissen

- **User Story 4.1: Ergebnisse anzeigen lassen**
- **User Story 4.2: Relevante Passagen kopieren**

### Epic 5: Suchhistorie

- **User Story 5.1: Öffnen einer Suchhistorie**
- **User Story 5.2: Vergangene Suchanfragen erneut auslösen**

### Epic 6: Administration und Systemverwaltung

- **User Story 6.1: Log-In für HTW-Administrator**
- **User Story 6.2: Speicherkapazität global ändern**
- **User Story 6.3: Speicherkapazität anzeigen lassen**
- **User Story 6.4: Statistiken anzeigen lassen**
- **User Story 6.5: Automatisches Log-Out einstellen**
- **User Story 6.6: Logging-Protokollverwaltung**
  

Jedes Epic enthält spezifische Funktionen, die den Bedürfnissen der Benutzer entsprechen und gemeinsam die Gesamtfunktionalität der MindMachine-Anwendung bilden. Diese klare Strukturierung ermöglicht eine effektive Umsetzung und Priorisierung der Anforderungen im Entwicklungsprozess.

  

### Epic 1: Benutzeranmeldung und Authentifizierung (Webzugriff)

  

Das Epic 1 konzentriert sich auf den grundlegenden Benutzerzugriff und die Authentifizierung in der MindMachine-Webanwendung. Hierbei werden sowohl HTW-Anwender mit und ohne Administratoren-Status berücksichtigt. Die darin enthaltenen User Stories adressieren das Öffnen der Website, den sicheren Log-In von HTW-Anwendern, die Möglichkeit, sich manuell abzumelden oder automatisch bei Inaktivität auszuloggen. Durch diese Funktionen wird die Privatsphäre und Sicherheit der Benutzer gewährleistet, während ein benutzerfreundlicher Zugang zur Anwendung ermöglicht wird.
  

#### User Story 1.1: Website öffnen als Anwender (HTW-Anwender und Admin)

  

**Rolle:** Als HTW-Anwender oder Administrator

  

**Ich möchte:** die MindMachine-Website öffnen können.

  

**So dass:** ich auf die Anmeldeseite zugreifen und mich anmelden kann.

  

**Akzeptanzkriterien:**

1. Die MindMachine-Website ist öffentlich zugänglich.

2. Beim Öffnen der Website wird der Benutzer auf die Anmeldeseite weitergeleitet.


---

  

#### User Story 1.2: Log-In für HTW-Anwender

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** mich mit meinem HTW-Account auf der MindMachine-Website anmelden können.

  

**So dass:** ich Zugang zu meinen privaten Dateien erhalte.

  

**Akzeptanzkriterien:**

1. Auf der MindMachine-Website gibt es eine klare und benutzerfreundliche Anmeldeseite.

2. Der Benutzer kann seinen HTW-Account-Namen und sein Passwort eingeben.

3. Das System authentifiziert den Benutzer mit den HTW-Anmeldedaten.

4. Bei erfolgreicher Anmeldung wird der Benutzer auf seine persönliche Startseite weitergeleitet.

5. Der Zugriff auf die persönliche Startseite ist nur für authentifizierte HTW-Benutzer möglich.

6. Im Falle von fehlerhaften Anmeldedaten erhält der Benutzer eine klare Fehlermeldung.

7. Die Anmeldung ist sicher und schützt die Privatsphäre des Benutzers.

  

---

#### User Story 1.3: Log-Out-Funktionalität

  

**Rolle:** Als HTW-Anwender oder Administrator

  

**Ich möchte:** mich manuell von der MindMachine-Website abmelden können und automatisch ausgeloggt werden, wenn eine spezifische Inaktivitätsdauer überschritten wird.

  

**So dass:** meine Privatsphäre und Sicherheit gewährleistet sind.

  

**Akzeptanzkriterien:**

1. Als Benutzer möchte ich die Möglichkeit haben, mich manuell von der MindMachine abzumelden.

2. Der "Abmelden"-Button ist klar und einfach zugänglich.

3. User wird gefragt, ob er sich ausloggen will.

4. Bei manueller Abmeldung wird der Benutzer auf eine Bestätigungsseite weitergeleitet.

5. Benutzer erhalten vor der automatischen Abmeldung aufgrund von Inaktivität eine Benachrichtigung.

6. Benutzer werden automatisch abgemeldet, wenn sie innerhalb der festgelegten Inaktivitätsdauer keine Aktionen durchführen.

7. Die Inaktivitätsdauer (Kundenwunsch: 60 Minuten bis zum Log-Out) betrifft alle Benutzer.
  

---

### Epic 2: Dateieverzeichnis

Dieses Epic konzentriert sich auf die Umsetzung der Funktionen rund um das Dateiverzeichnis in der MindMachine-Anwendung. Hierbei stehen die Bereiche Dateiverzeichnis öffnen mit userspezifischer Ansicht, Dateien hochladen mit Prüfung, Dokumente öffnen, Dokumente löschen und Dokument umbenennen im Fokus. Das Ziel ist es, den Benutzern eine intuitive und personalisierte Möglichkeit zu bieten, ihre Dateien zu verwalten und auf diese zuzugreifen.


#### User Story 2.1: Datenverzeichnis öffnen mit userspezifischer Ansicht

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** mein privates Dateiverzeichnis öffnen können und eine Ansicht erhalten, die spezifisch für mich ist.

  

**So dass:** ich einen klaren und personalisierten Überblick über meine Dateien erhalte.

  

**Akzeptanzkriterien:**

1. Auf der MindMachine-Website gibt es eine Option zum Öffnen des privaten Dateiverzeichnisses.

2. Die Ansicht des Dateiverzeichnisses ist spezifisch für den angemeldeten Benutzer.

3. Der Benutzer sieht nur Dateien, auf die er Zugriff hat.

4. Die Ansicht bietet klare Informationen über Dateinamen, Typen und ggf. Datum der letzten Änderung.

5. Die Ansicht ist benutzerfreundlich und einfach zu navigieren.

  

---

  

#### User Story 2.2: Dateien hochladen mit Prüfung

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** Dateien in mein privates Verzeichnis hochladen können.

  

**So dass:** ich meine Dateien sicher und effizient verwalten kann.

  

**Akzeptanzkriterien:**

1. Auf der MindMachine-Website gibt es eine Funktion zum Hochladen von Dateien.

2. Der Benutzer kann Dateien auswählen und hochladen.

3. Das System prüft das Dateiformat auf Gültigkeit, zugelassen sind nur PDF-Dateien mit optischer Zeichenerkennung (OCR) sind für den Upload zugelassen.

4. Falls die Prüfung fehlschlägt, erhält der Benutzer eine klare Fehlermeldung.

5. Die Benutzeroberfläche zeigt den Erfolg des Uploads für jede Datei an.

6. Bei erfolgreichem Upload werden die Dateien sofort in der Ansicht des privaten Verzeichnisses aktualisiert.

7. Der Benutzer erhält Feedback über den Erfolg oder etwaige Fehler während des Upload-Vorgangs.

8. Die OCR-Prüfung respektiert die Privatsphäre des Benutzers und erfasst nur notwendige Informationen.

  

---

#### User Story 2.3: Dokumente öffnen

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** die Möglichkeit haben, Dokumente in meinem privaten Verzeichnis zu öffnen.

  

**So dass:** ich den Inhalt meiner Dateien anzeigen und bearbeiten kann.

  

**Akzeptanzkriterien:**

1. Auf der MindMachine-Website gibt es eine Option zum Öffnen von Dokumenten im privaten Verzeichnis.

2. Der Benutzer kann ein Dokument auswählen und öffnen.

3. Das System unterstützt nur OCR-PDF-Dateien.

4. Die Benutzeroberfläche für das Öffnen von Dokumenten ist benutzerfreundlich gestaltet.

5. Bei Änderungen an einem Dokument wird der Benutzer darauf hingewiesen und kann die Änderungen speichern.

6. Falls das Dokument schreibgeschützt ist, kann der Benutzer es dennoch anzeigen.

7. Die Dokumentenanzeige respektiert die Sicherheitsrichtlinien und schützt die Privatsphäre des Benutzers.

---

#### User Story 2.4: Dokumente löschen

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** die Möglichkeit haben, Dokumente aus meinem privaten Verzeichnis zu löschen.

  

**So dass:** ich mein Dateiverzeichnis aufräumen und unerwünschte Dateien entfernen kann.

  

**Akzeptanzkriterien:**

1. Auf der MindMachine-Website gibt es eine Option zum Löschen von Dokumenten im privaten Verzeichnis.

2. Der Benutzer kann ein Dokument auswählen und löschen.

3. Das System bestätigt das Löschen und warnt den Benutzer vor, um versehentliche Löschungen zu vermeiden.

4. Bei Bestätigung wird das Dokument aus dem privaten Verzeichnis entfernt.

5. Das System protokolliert das Löschen von Dokumenten für Sicherheitszwecke.

6. Der Benutzer erhält eine Bestätigung über den erfolgreichen Löschvorgang.

7. Das Löschen von Dokumenten respektiert die Sicherheitsrichtlinien und schützt die Privatsphäre des Benutzers.

  

---

#### User Story 2.5: Dokument umbenennen

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** die Möglichkeit haben, den Namen eines Dokuments in meinem privaten Verzeichnis zu ändern.

  

**So dass:** ich meine Dateien besser organisieren und individuell benennen kann.

  

**Akzeptanzkriterien:**

1. Auf der MindMachine-Website gibt es eine Option zum Umbenennen von Dokumenten im privaten Verzeichnis.

2. Der Benutzer kann ein Dokument auswählen und den Namen bearbeiten.

3. Die Benutzeroberfläche für das Umbenennen von Dokumenten ist benutzerfreundlich gestaltet.

4. Änderungen am Dokumentennamen werden sofort im privaten Verzeichnis angezeigt.

5. Der Benutzer erhält eine Bestätigung über den erfolgreichen Umbenennungsvorgang.

6. Das Umbenennen von Dokumenten respektiert die Sicherheitsrichtlinien und schützt die Privatsphäre des Benutzers.

---

  

### Epic 3: Fragen stellen

  

Dieses Epic widmet sich der Funktion, Fragen an die MindMachine zu stellen. Die User Stories innerhalb dieses Epics ermöglichen es den HTW-Anwendern, über das Interface Fragen als Text- oder Sprachprompt zu formulieren. Dabei wird eine Benutzeroberfläche geschaffen, die klar und benutzerfreundlich ist. Die KI verarbeitet die Fragen und generiert Suchanfragen, deren Ergebnisse direkt auf der Benutzeroberfläche angezeigt werden. Der Fokus liegt darauf, eine effiziente Interaktion zwischen den Benutzern und der KI zu ermöglichen, wobei Sicherheitsrichtlinien und Datenschutz beachtet werden.

#### User Story 3.1: Frage als Textprompt stellen

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** über das Interface eine Frage als Textprompt stellen können.

  

**So dass:** meine Suchanfrage für die ML-Integration vorbereitet wird, um Auszüge aus meinen Dateien zu generieren.

  

**Akzeptanzkriterien:**

1. Auf der MindMachine-Website gibt es eine klare und benutzerfreundliche Konsole für die Eingabe von Text-Fragen.

2. Der Benutzer kann seine Frage als Text eingeben. Sonderzeichen erzeugen keinen Absturz der Website

3. Die Benutzeroberfläche ermöglicht dem Benutzer, die Frage vor dem Senden zu überprüfen.

4. Nach dem Absenden wird die Frage an die KI weitergeleitet.

5. Die KI verarbeitet die eingegebene Frage und generiert eine Suchanfrage.

6. Die Ergebnisse der Suchanfrage werden direkt auf der Benutzeroberfläche angezeigt.

7. Die Interaktion respektiert die Sicherheitsrichtlinien und schützt die Privatsphäre des Benutzers.
  

---

#### User Story 3.2: Frage abändern

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** die Möglichkeit haben, meine gestellte Frage zu bearbeiten.

  

**So dass:** ich Anpassungen vornehmen kann, ohne eine komplett neue Suchanfrage zu stellen.

  

**Akzeptanzkriterien:**

1. Nachdem die Ergebnisse meiner gestellten Frage angezeigt wurden, gibt es eine Option zur Bearbeitung der Frage.

2. Die Benutzeroberfläche ermöglicht es mir, den Text meiner Frage zu ändern.

3. Nach der Bearbeitung wird die modifizierte Frage an die KI weitergeleitet.

4. Die KI verarbeitet die geänderte Frage und generiert eine aktualisierte Suchanfrage.

5. Die neuen Ergebnisse werden direkt auf der Benutzeroberfläche angezeigt.

6. Die Interaktion respektiert die Sicherheitsrichtlinien und schützt die Privatsphäre des Benutzers.

  

---

#### User Story 3.3: Frage als Sprachprompt stellen

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** die Möglichkeit haben, eine Frage als Sprachprompt zu stellen.

  

**So dass:** ich mithilfe von Sprachbefehlen meine Suchanfrage für die KI formulieren kann.

  

**Akzeptanzkriterien:**

1. Auf der MindMachine-Website gibt es eine klare und benutzerfreundliche Option, eine Frage per Sprachprompt zu stellen.

2. Der Benutzer kann die Sprachoption aktivieren und seine Frage sprechen.

3. Das System wandelt die gesprochene Frage in Text um und leitet sie an die KI weiter.

4. Die KI verarbeitet die gesprochene Frage und generiert eine entsprechende Suchanfrage.

5. Die Ergebnisse der Sprachanfrage werden direkt auf der Benutzeroberfläche angezeigt.

6. Die Benutzeroberfläche gibt Feedback zum Spracherkennungsstatus.

7. Die Interaktion respektiert die Sicherheitsrichtlinien und schützt die Privatsphäre des Benutzers.

  

---

  

### Epic 4: Ergebnisse auswerten

  

Dieses Epic konzentriert sich darauf, die Ergebnisse von Suchanfragen auszuwerten. Die User Stories beschreiben die Anzeige der Suchergebnisse, das Öffnen von Dokumenten, das Kopieren relevanter Passagen und das Löschen von Dokumenten. Ziel ist es, den Benutzern eine umfassende Kontrolle über die gefundenen Informationen zu geben und dabei Sicherheitsrichtlinien zu respektieren. Die Benutzeroberfläche ermöglicht es, relevante Passagen zu kopieren und Dokumente zu öffnen, während die Sicherheit und Privatsphäre der Benutzer gewahrt bleiben.

#### User Story 4.1: Ergebnisse anzeigen lassen

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** die Ergebnisse meiner Suchanfrage angezeigt bekommen.

  

**So dass:** ich eine übersichtliche und priorisierte Auflistung der gefundenen Dokumente sowie relevante Passagen erhalte.

  

**Akzeptanzkriterien:**

1. Nachdem ich eine Frage gestellt habe, werden die Ergebnisse auf der Benutzeroberfläche angezeigt.

2. Die Ergebnisse umfassen eine Liste der gefundenen Dokumente.

3. Die Dokumente sind nach Relevanz priorisiert.

4. Zu jedem Dokument gibt es eine Zusammenfassung der relevanten Passagen.

5. Die Passagen sind farblich hervorgehoben und für eine bessere Sichtbarkeit gekennzeichnet.

6. Oberhalb der Ergebnisse wird eine zusammenfassende Antwort auf die gestellte Frage präsentiert.

7. Die Benutzeroberfläche ermöglicht das Öffnen von Dokumenten an den markierten Passagen.

8. Die Interaktion respektiert die Sicherheitsrichtlinien und schützt die Privatsphäre des Benutzers.

  

---

  

#### User Story 4.2: Relevante Passagen kopieren

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** die relevanten Passagen aus den Ergebnissen meiner Suchanfrage kopieren können.

  

**So dass:** ich spezifische Informationen aus den gefundenen Dokumenten extrahieren und anderweitig verwenden kann.

  

**Akzeptanzkriterien:**

1. Nachdem die Ergebnisse meiner Suchanfrage angezeigt wurden, gibt es eine Option zum Kopieren der relevanten Passagen.

2. Der Benutzer kann eine oder mehrere Passagen auswählen und kopieren.

3. Die kopierte Passagen werden mit klare Quellenangaben ergänzt.

4. Das Kopieren der Passagen respektiert die Sicherheitsrichtlinien und schützt die Privatsphäre des Benutzers.

  

---

### Epic 5: Suchhistorie

  

Dieses Epic befasst sich mit der Möglichkeit für Benutzer, ihre Suchhistorie zu verwalten. Die User Stories beschreiben das Öffnen der Suchhistorie und das Anzeigen vergangener Ergebnisse. Die Benutzer haben die Möglichkeit, vergangene Suchanfragen in einem Verzeichnis nachzuvollziehen und sich die Ergebnisse erneut anzeigen zu lassen. Hierbei wird darauf geachtet, eine übersichtliche und benutzerfreundliche Darstellung zu schaffen, die den Datenschutz berücksichtigt.

#### User Story 5.1: Öffnen einer Suchhistorie

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** eine Ansicht meiner Suchhistorie öffnen können.

  

**So dass:** ich meine vergangenen Suchanfragen nachvollziehen und bei Bedarf erneut verwenden kann.

  

**Akzeptanzkriterien:**

1. Auf der MindMachine-Website gibt es eine Option zum Öffnen der Suchhistorie.

2. Der Benutzer kann eine Übersicht seiner vergangenen Suchanfragen einsehen.

3. Die Ansicht enthält Angaben zum Datum jeder Suchanfrage.

4. Der Benutzer kann direkt in der Auflistung vergangene Suchanfragen auswählen, um eine erneute Suche zu triggern.

  

---

  

#### User Story 5.2: Vergangene Suchanfragen erneut auslösen

  

**Rolle:** Als HTW-Anwender

  

**Ich möchte:** über einen Direktlink in meiner Suchhistorie die vergangene Suchanfragen erneut triggern.

  

**So dass:** ich direkt zu den neu getriggerten Ergebnissen einer bestimmten vergangenen Suchanfrage navigieren kann.

  

**Akzeptanzkriterien:**

1. In der Suchhistorie gibt es für jede vergangene Suchanfrage einen Direktlink zu den Ergebnissen.

2. Der Benutzer kann durch Auswahl des Direktlinks die Suchanfrage neu auslösen. 

3. Die Ansicht der, auf Grundlage der aktuell vorliegenden Dokumente, generierten Ergebnisse enthält klare Informationen zu den gefundenen Dokumenten und markierten Passagen.

4. Der Benutzer kann durch die Ergebnisse navigieren und bei Bedarf weitere Aktionen wie das Kopieren relevanter Passagen durchführen.
  

---

### Epic 6: Admin-Verwaltung

  

Dieses Epic adressiert die Verwaltungsfunktionen für Administratoren. Die User Stories beschreiben die globale Änderung der Speicherkapazität, das Anzeigen von Statistiken und Logging-Protokollen und das Einstellen eines automatischen Log-Outs für Benutzer. Das Ziel ist es, Administratoren die Kontrolle über systemweite Einstellungen zu geben und gleichzeitig eine effiziente Verwaltung der MindMachine zu ermöglichen. Dabei werden Sicherheitsaspekte und Datenschutz berücksichtigt.

#### User Story 6.1: Log-In für HTW-Administrator

  

**Rolle:** Als HTW-Anwender mit Administrator-Status

  

**Ich möchte:** mich mit meinem speziellen Admin-Account auf der MindMachine-Website anmelden können.

  

**So dass:** ich privilegierten Zugang zum Admin-Dashboard erhalte.

  

**Akzeptanzkriterien:**

1. Auf der MindMachine-Website gibt es eine klare und benutzerfreundliche Anmeldeseite.

2. Der Administrator kann seinen HTW-Account-Namen und sein Passwort eingeben.

3. Das System authentifiziert den Benutzer mit den HTW-Anmeldedaten und verifiziert seinen Administrator-Status.

4. Bei erfolgreicher Anmeldung wird der Benutzer auf seine persönliche Startseite weitergeleitet. Auf der persönlichen Startseite wird das Admin-Panel angezeigt.

5. Der Zugriff auf die persönliche Startseite mit Admin-Panel ist nur für authentifizierte HTW-Benutzer mit Administratorrecht möglich.

6. Im Falle von fehlerhaften Anmeldedaten erhält der Administrator eine klare Fehlermeldung.

7.  Die Admin-Anmeldung ist sicher und schützt die Privatsphäre des Administrators.


---

#### User Story 6.2: Speicherkapazität global ändern

  

**Rolle:** Als HTW-Anwender mit Administrator-Status

  

**Ich möchte:** globale die maximale Speicherkapazität für alle Benutzer anpassen können.

  

**So dass:** ich die Ressourcen effizient verwalten und die Gesamtspeicherkapazität kontrollieren kann.

  

**Akzeptanzkriterien:**

1. Der Administrator kann die globale Speicherkapazität über die Admin-Verwaltungsfunktion ändern.

2. Die Änderung der Speicherkapazität wird sofort wirksam und betrifft alle Benutzer.

3. Die Reduzierung der globalen Speicherkapazität ist begrenzt.

5. Benutzer, deren aktuelle Speichernutzung die neue globale Speicherkapazität überschreitet, erhalten eine Benachrichtigung.

6. Die globale Speicherkapazität kann nur in einem vordefinierten Bereich geändert werden. Die Mindestanforderung an die Speicherkapazität stellt der Speicherplatz des Users mit der größten Speicherplatzbelegung dar. 

7. Der Administrator erhält eine Bestätigung über die erfolgreiche Änderung der globalen Speicherkapazität.

8. Die Änderung der globalen Speicherkapazität respektiert die Sicherheitsrichtlinien und schützt die Privatsphäre der Benutzer.

---

#### User Story 6.3: Speicherkapazität anzeigen lassen

  

**Rolle:** Als HTW-Anwender mit Administrator-Status

  

**Ich möchte:** die globale Speicherkapazität des Servers anzeigen können.

  

**So dass:** ich einen Überblick über die Gesamtspeicherkapazität erhalte und Ressourcen effizient verwalten kann.

  

**Akzeptanzkriterien:**

1. Der Administrator kann die globale Speicherkapazität auf der Admin-Verwaltungsseite einsehen.

2. Die angezeigte globale Speicherkapazität entspricht der tatsächlichen Kapazität des Servers.

3. Die Anzeige umfasst Informationen über den aktuellen Speicherstand und verfügbaren Speicherplatz.

4. Die globale Speicherkapazität wird in einem leicht verständlichen Format präsentiert.

5. Das System aktualisiert die Anzeige regelmäßig, um genaue Informationen bereitzustellen.

6. Der Administrator kann auf der Admin-Verwaltungsseite den Verlauf der globalen Speicherkapazität überprüfen.

7. Die Anzeige der globalen Speicherkapazität respektiert die Sicherheitsrichtlinien und schützt die Privatsphäre der Benutzer.

---

#### User Story 6.4: Statistiken anzeigen lassen

  

**Rolle:** Als HTW-Anwender mit Administrator-Status

  

**Ich möchte:** Statistiken zu gestellten Frage-Prompts, Nutzerzahlen und Speicherkapazität anzeigen lassen können.

  

**So dass:** ich einen umfassenden Überblick über die Nutzung der MindMachine erhalte und strategische Entscheidungen treffen kann.

  

**Akzeptanzkriterien:**

1. Der Administrator kann auf der Admin-Verwaltungsseite Statistiken zu gestellten Frage-Prompts einsehen.

2. Die Statistiken zu Frage-Prompts umfassen Informationen wie Anzahl der gestellten Fragen global und userspezifisch.

3. Der Administrator kann auf der Admin-Verwaltungsseite Statistiken zu den Nutzerzahlen einsehen.

4. Die Nutzerstatistiken umfassen Informationen wie Gesamtzahl der aktiven Benutzer.

5. Der Administrator kann auf der Admin-Verwaltungsseite Statistiken zur globalen und userspezifischen Speicherplatzbelegung einsehen.

6. Die Speicherkapazitätsstatistiken zeigen den aktuellen Speicherstand und verfügbaren Speicherplatz an.

7. Die Statistik-Ansichten sind benutzerfreundlich und leicht verständlich gestaltet.

8. Das System aktualisiert die Statistiken regelmäßig, um genaue Informationen bereitzustellen.

9. Der Administrator kann den Zeitraum für die angezeigten Statistiken auswählen.

10. Die Statistik-Ansichten respektieren die Sicherheitsrichtlinien und schützen die Privatsphäre der Benutzer.

---

#### User Story 6.5: Automatisches Log-Out einstellen

  

**Rolle:** Als HTW-Anwender mit Administrator-Status

  

**Ich möchte:** das maximale Zeitfenster von Benutzer-Inaktivität bis zum automatischen Logout für alle Nutzer global vorgeben können.

  

**So dass:** ich die Sicherheit der Anwendung erhöhen und Ressourcen effizient verwalten kann.

  

**Akzeptanzkriterien:**

1. Der Administrator kann auf der Admin-Verwaltungsseite das maximale Zeitfenster für Benutzer-Inaktivität einstellen.

2. Das festgelegte Zeitfenster bestimmt, wie lange ein Benutzer inaktiv sein kann, bevor er automatisch ausgeloggt wird.

3. Die Änderung des automatischen Log-Outs wird sofort wirksam und betrifft alle Benutzer.

4. Benutzer erhalten eine Benachrichtigung über das automatische Log-Out.

5. Der Administrator kann das automatische Log-Out global für alle Benutzer festlegen und anpassen.

6. Das automatische Log-Out respektiert die Sicherheitsrichtlinien und schützt die Privatsphäre der Benutzer.

  ---
### 6.6 User Story: Logging-Protokollverwaltung


**Rolle:** Als HTW-Anwender mit Administrator-Status

**Ich möchte:** die Möglichkeit haben, alle relevanten Aktionen und Ereignisse im System über ein Logging-Protokoll nachverfolgen zu können.

**So dass:** die Sicherheit und Integrität des Systems gewährleistet und mögliche Probleme schnell identifiziert werden können.

**Akzeptanzkriterien:**

1. Die Anmeldung und Abmeldung von Benutzern wird im Logging-Protokoll erfasst und protokolliert.
2. Jeder Dateiupload, Dateiöffnung, Dateilöschung und Dateiumbenennung wird im Logging-Protokoll dokumentiert.
3. Suchanfragen, insbesondere semantische Suchanfragen, werden im Protokoll mit relevanten Details aufgezeichnet.
4. Alle vom Administrator durchgeführten Aktionen, wie das Zurücksetzen von Passwörtern oder das Hinzufügen/Entfernen von Benutzern, werden im Logging-Protokoll festgehalten.
5. Änderungen an der Speicherkapazität, einschließlich Erweiterungen oder Reduzierungen, werden im Logging-Protokoll erfasst und sind für den Administrator einsehbar.
6. Das Logging-Protokoll ist über die Administrationsseite zugänglich und ermöglicht die Filterung nach Datum, Benutzeraktionen und Ereignistypen.
7. Das System protokolliert Fehler und Ausnahmen, um eine umfassende Fehleranalyse zu ermöglichen.
8. Das Logging-Protokoll respektiert die Datenschutzrichtlinien und zeigt nur die Informationen an, die für Administratoren relevant sind.
9. Die Protokolldaten werden sicher gespeichert und sind vor unbefugtem Zugriff geschützt.
10. Es besteht die Möglichkeit, Protokolldaten zu exportieren oder auszudrucken, um externe Analysen durchzuführen oder für Auditzwecke.

 _Hinweis: Die Administratorrolle hat Vollzugriff auf das Logging-Protokoll, um eine umfassende Überwachung und Analyse des Systemverhaltens sicherzustellen._
 
---

## 2.1 Funktionale Anforderungen / Use-Cases 

  

Beschreiben Sie die wesentlichen funktionalen Anforderungen bzw. Use-Cases Ihres Systems. Dies können Sie als Use-Case-Diagramm (geeignet bei mehreren Typen von Anwendern der Software) oder als Tabelle mit funktionalen Anforderungen darstellen. 

Legen Sie fest, welches Teammitglied für welchen Use-Case bzw. welche funktionale Anforderung verantwortlich ist. In diesem Abschnitt dreht sich alles um die Anforderungen aus Nutzersicht. Eine Definition von internen Abläufen ist hier nicht sinnvoll.  

  

Alle funktionalen Anforderungen bzw. Use-Cases sollten nummeriert werden, damit man sich im Abschnitt 4 darauf beziehen kann. 

  

## 2.2 Nicht-funktionale Anforderungen 

  
  

Führen Sie an dieser Stelle alle nicht-funktionalen Anforderungen Ihres Systems auf. Zum Beispiel unter welchem Betriebssystem die Software laufen soll, oder welche Anforderungen an Antwort- oder Verarbeitungszeiten gestellt werden. 



## 2.3. Risiken

 
  

Beschreiben Sie mögliche Risiken für die erfolgreiche Umsetzung Ihres Projektes! Welche Maßnahmen können Sie ergreifen, um die Risiken zu reduzieren? Diese Darstellung sollte in einer Tabelle erfolgen. 

  

## 2.4. GUI

  

  

Erstellen Sie einen Mockup Ihrer GUI. Dazu sollen für die wichtigen Anwendungsfälle die Oberflächen entworfen und ihre Funktion beschrieben werden. Das Mockup kann mit einem beliebigen Tool umgesetzt werden (Powerpoint, inkscape, Figma, Paint, WPF, egal!). 

  

# 3. Realisierung 

  

## 3.1. Komponenten 

  

Legen Sie die für Ihr System zu erstellenden Komponenten fest. Ordnen Sie die Komponente dem verantwortlichen Teammitglied zu. Legen Sie fest, welche Use-Cases in welcher Komponente oder welchen Komponenten aus heutiger Sicht zu realisieren sind.  

  

Erstellen Sie ggfs. ein Komponenten-Diagramm des zu realisierenden Programms mit den dazu erforderlichen Komponenten und zeigen Sie die Abhängigkeiten zwischen den Komponenten auf. 

  

2. Interne Schnittstellen / Klassendiagramm 

  

Erstellen Sie ein Klassendiagramm, um die zu realisierenden Schnittstellen konkret zu spezifizieren. Überlegen Sie, welche Funktionen von welcher Klasse bereitgestellt werden müssen und achten Sie auf eine sinnvolle Softwarearchitektur und ggfs. passende Entwurfsmuster. 

  

3. Externe Schnittstellen 

  

Beschreiben Sie die externen Schnittstellen Ihres Systems. Erstellen Sie dazu eine Tabelle, in der Sie den Namen der Schnittstelle, die Art der Schnittstelle (das könnte eine Datei, eine Serveranwendung, ein KI-Modell, eine Datenbank, eine Website etc. sein), den Typ der Schnittstellenimplementierung (Dateizugriff, http-Zugriff, COM-Zugriff o.ä.) und die Komponente oder Klasse, die für die Realisierung der externen Anbindung zuständig ist, auflisten. 

  

4. Datenbank-Schema 

  

Wenn Sie eine Datenbank verwenden, erklären und skizzieren Sie hier Ihr Datenbank-Schema. 

  

5. Tests und Qualitätssicherung 

  

Beschreiben Sie hier, welche Aspekte Ihrer Software Sie wie testen könnten. Aus Zeitgründen verzichten wir auf eine detaillierte Test-Strategie. Nutzen Sie diesen Abschnitt jedoch für Vorschläge, wie man (rein hypothetisch) essenzielle Funktionalitäten testen könnte. Sie müssen die hier gemachten Vorschläge nicht umsetzen. 

  

# 3.6. Lizenz 

 ### Verwendete Lizenzen

#### Qdrant 

Die MindMachine-Anwendung verwendet Qdrant, eine Open-Source-Software, die unter der [Apache License 2.0](https://github.com/qdrant/qdrant/blob/master/LICENSE) veröffentlicht ist.

**Anwendung der Lizenz in der MindMachine-Anwendung:**

1. **Reproduktion und Distribution:** Die MindMachine-Anwendung reproduziert und verteilt Qdrant gemäß den Bedingungen der Apache License 2.0.

2. **Erstellung abgeleiteter Werke:** Die MindMachine-Anwendung kann abgeleitete Werke von Qdrant erstellen und verteilen, solange diese Werke den Bedingungen der Apache License 2.0 entsprechen.

3. **Öffentliche Anzeige und Aufführung:** Die MindMachine-Anwendung kann Qdrant öffentlich anzeigen und aufführen.

4. **Patentlizenz:** Durch die Verwendung von Qdrant gemäß der Apache License 2.0 erhalten die Benutzer automatisch eine Patentlizenz für eventuell patentierte Teile von Qdrant.

Stellen Sie sicher, dass Sie die vollständigen Bedingungen der Apache License 2.0 sorgfältig überprüfen und einhalten. Bei Fragen oder Unklarheiten ist es ratsam, rechtlichen Rat einzuholen.
