# 1. Projektbeschreibung: MindMachine - Projekt der HTW Berlin

## Überblick

Die **MindMachine** ist ein innovatives Webanwendungsprojekt, das im Rahmen des Wintersemester 2023/24 gestarteten Masterstudiengangs "Informatik in den Ingenieurwissenschaften" an der Hochschule für Technik und Wirtschaft (HTW) Berlin entsteht. Dieses Projekt wird von Studierenden als Teil eines Moduls entwickelt, um fortgeschrittene Informatikkenntnisse in den Ingenieurwissenschaften zu fördern.

## Ziele 

Die Vision für das MindMachine-Projekt ist die Schaffung einer intuitiven und leistungsstarken Browseranwendung, die es HTW-Anwendern ermöglicht, ihre Dateien effizient zu verwalten und mithilfe von KI-gestützten Suchanfragen relevante Informationen aus den Dokumenten zu extrahieren. Das Hauptziel besteht darin, eine benutzerfreundliche Plattform zu entwickeln, die nahtlos in den Arbeitsalltag der HTW-Anwender integriert werden kann.


Die wesentlichen Ziele des Projekts sind:

  

1. **Benutzerfreundlichkeit:** Die Anwendung soll eine leicht verständliche Benutzeroberfläche bieten, die eine intuitive Navigation und Interaktion ermöglicht. Sowohl HTW-Anwender als auch Administratoren sollen sich mühelos auf der Plattform zurechtfinden können.

  

2. **Effiziente Dateiverwaltung:** HTW-Anwender sollen in der Lage sein, ihr privates Dateiverzeichnis mithilfe der Anwendung effizient zu öffnen, Dateien hochzuladen, zu öffnen, zu löschen und umzubenennen. Die Ansicht des Dateiverzeichnisses soll dabei individuell auf den angemeldeten Benutzer zugeschnitten sein.

  

3. **KI-gestützte Suchanfragen:** Die Anwendung soll HTW-Anwendern die Möglichkeit bieten, Fragen in Form von Text- oder Sprachprompten zu stellen. Die KI verarbeitet diese Anfragen, generiert Suchanfragen und zeigt relevante Ergebnisse direkt auf der Benutzeroberfläche an.

  

4. **Sicherheit und Datenschutz:** Die Plattform muss höchsten Sicherheitsstandards genügen, insbesondere im Hinblick auf die Authentifizierung über HTW-Logins, sichere An- und Abmeldungsprozesse sowie den Schutz der Privatsphäre der Benutzer. #delete?

  

5. **Suchhistorie und Interaktionshistorie:** Die Anwendung soll eine Suchhistorie für HTW-Anwender bereitstellen, um vergangene Suchanfragen nachzuvollziehen. Die Möglichkeit, direkt zu den Ergebnissen vergangener Suchanfragen zu navigieren, trägt zur Effizienz und Nutzerfreundlichkeit bei.

  

Die erfolgreiche Umsetzung dieser Ziele wird dazu beitragen, den Workflow der HTW-Anwender zu verbessern, die Effizienz in der Dateiverwaltung zu steigern und den Zugriff auf relevante Informationen durch KI-gestützte Suchanfragen zu erleichtern. 

## Funktionen und Nutzung #scoping? #pleasecheck 

- **Benutzerzugriff und Authentifizierung:**
  - Öffnen der Website für HTW-Anwender und Administratoren.
  - Sicheres Anmelden für HTW-Anwender mit personalisierten Startseiten.
  - Manuelle Abmeldung und automatisches Ausloggen bei Inaktivität für erhöhte Privatsphäre und Sicherheit. 

- **Dateiverwaltung:**
  - Privates Dateiverzeichnis für HTW-Anwender mit benutzerspezifischer Ansicht.
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


---
# 2. Installation

Da es sich um eine Webanwendung handelt, ist keine lokale Installation erforderlich. Sie können einfach die [MindMachine-Website](https://mindmachine.htw-berlin.de/) besuchen und auf die entsprechenden Funktionen zugreifen.

Bitte beachten Sie, dass eine Internetverbindung erforderlich ist, um auf die Anwendung zuzugreifen. Zusätzlich ist ein HTW-Account erforderlich, um sich anzumelden. Die manuelle Registrierung ist nicht möglich; verwenden Sie bitte Ihre vorhandenen HTW-Anmeldeinformationen.

**Hinweis: Die Nutzung der MindMachine erfordert eine Verbindung zum HTW-Netzwerk.** #pleasecheck Ist es noch erforderlich? 

---
# 3. Verweise auf detaillierte Dokumentation

- Verweis zu Anforderungsanalyse in Requirement Docu
- Verweis zu im Projektumfang enthalten und Grenzen in Scoping
- Verweis zu Abhängigkeiten in SAD
- Verweis zu Beispielen in UI: 
    
    - Ein einfaches Beispiel oder eine Schnellstartanleitung, um Benutzern den Einstieg zu erleichtern.
===Verweis auf detaillierte Dokumentation mit Direktlinks etc, wenn diese fertig gestellt ist=== #endsprint

---

# 4. Fehlersuche

## Probleme bei der Anmeldung

1. **HTW-Account erforderlich:** Stelle sicher, dass du einen aktiven HTW-Account besitzt. Unsere Anwendung erfordert eine Anmeldung mit den HTW-Anmeldedaten.
    
2. **Richtige Anmeldedaten verwenden:** Überprüfe, ob du die korrekten Benutzername und das korrekte Passwort für deinen HTW-Account verwendest.
    
3. **Internetverbindung überprüfen:** Stelle sicher, dass deine Internetverbindung stabil ist.
    

## Technische Probleme

1. **Browser-Kompatibilität:** Die Anwendung wurde erfolgreich in den neuesten Versionen von Chrome, Firefox und Safari getestet. Überprüfe, ob du einen dieser Browser verwendest und versuche es gegebenenfalls mit einem anderen.
    
2. **Cache leeren:** Wenn unerklärliche Fehler auftreten, versuche, den Browser-Cache zu leeren, um sicherzustellen, dass du die neueste Version der Anwendung verwendest.
    
3. **JavaScript aktiviert:** Stelle sicher, dass JavaScript in deinem Browser aktiviert ist.
    
4. **Pop-up-Blocker:** Deaktiviere Pop-up-Blocker, da diese möglicherweise die Anmeldung oder andere Funktionen beeinträchtigen.

## Weitere Unterstützung

Wenn die oben genannten Schritte das Problem nicht lösen, zögere nicht, ===[unser Support-Team](mailto:memorymachine.softeng@gmail.com)===  zu kontaktieren, um weitere Unterstützung zu erhalten.

---

# 5. Kontakt

SOFTENG MemoryMachine
memorymachine.softeng@gmail.com
Hochschule für Technik und Wirtschaft
Campus Wilhelminenhof
Wilhelminenhofstraße 75A, 12459 Berlin

## Mitwirkende und Projekthintergrund

Die **MindMachine** ist ein Projekt im Masterstudiengang "Informatik in den Ingenieurwissenschaften" an der Hochschule für Technik und Wirtschaft (HTW) Berlin. In diesem praxisorientierten Modul können Studierende ihre Softwareentwicklungskompetenzen vertiefen und den modernen Softwareentwicklungsprozess in eigenen Projekten anwenden.

Die Studierenden lernen verschiedene Rollen im agilen Prozess kennen und setzen moderne Tools für Requirements-Management, Konfigurations-Management, automatisiertes Testen und Projektmanagement ein. Besonderes Augenmerk liegt auf der Förderung von Teamarbeit in gemeinsamen Projekten, um die Studierenden optimal auf ihre zukünftige Berufswahl vorzubereiten. #pleasecheck

Die enge Zusammenarbeit zwischen der HTW Berlin und den Studierenden bei der Entwicklung der **MindMachine** spiegelt den kooperativen Ansatz des Moduls wider. Ziel ist es, innovative Lösungen für Herausforderungen in den Ingenieurwissenschaften zu schaffen und gleichzeitig sicherzustellen, dass die Studierenden bestmöglich auf ihre berufliche Zukunft vorbereitet werden.

---
# 6. Lizenzierung und Urheberrecht

## Hinweis zur Verwendung von qdrant

Die MindMachine-Anwendung verwendet Qdrant, eine Open-Source-Software, die unter der [Apache License 2.0](https://github.com/qdrant/qdrant/blob/master/LICENSE) veröffentlicht ist.

**Anwendung der Lizenz in der MindMachine-Anwendung:**

1. **Reproduktion und Distribution:** Die MindMachine-Anwendung reproduziert und verteilt Qdrant gemäß den Bedingungen der Apache License 2.0.
    
2. **Erstellung abgeleiteter Werke:** Die MindMachine-Anwendung kann abgeleitete Werke von Qdrant erstellen und verteilen, solange diese Werke den Bedingungen der Apache License 2.0 entsprechen.
    
3. **Öffentliche Anzeige und Aufführung:** Die MindMachine-Anwendung kann Qdrant öffentlich anzeigen und aufführen.
    
4. **Patentlizenz:** Durch die Verwendung von Qdrant gemäß der Apache License 2.0 erhalten die Benutzer automatisch eine Patentlizenz für eventuell patentierte Teile von Qdrant.
    

Stellen Sie sicher, dass Sie die vollständigen Bedingungen der Apache License 2.0 sorgfältig überprüfen und einhalten. Bei Fragen oder Unklarheiten ist es ratsam, rechtlichen Rat einzuholen.

Die MindMachine-Webanwendung unterliegt der [Apache 2.0 Lizenz](https://www.apache.org/licenses/LICENSE-2.0).

===© 2023 SOFTENG MemoryMachine. Alle Rechte vorbehalten.=== #pleasecheck 