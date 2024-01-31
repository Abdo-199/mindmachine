# 1. Einleitung
Kurze Einführung in das Dokument, Zweck und Inhalt der SAD.

# 2. Architekturübersicht
Allgemeine Übersicht über die Architektur der Anwendung.

# 3. Technologie-Stack

### Testing-Infrastruktur und Evaluierung der Suchalgorithmen

Im Rahmen der Weiterentwicklung der **MindMachine**-Anwendung wurde eine umfangreiche Testing-Pipeline etabliert, die es ermöglicht, die Effektivität unterschiedlicher Suchmethoden zu evaluieren. Folgende Hyperparameter können für jeden Test konfiguriert werden:

1. **Encoder**: Definition des spezifischen Encoders, der zur Kodierung der Texte eingesetzt wird.
2. **Distance**: Auswahl der Distanzfunktion, entweder COS oder DOT, die die Ähnlichkeitsmessung bestimmt.
3. **Chunk Size**: Festlegung, ob und wie Dokumente in kleinere Segmente aufgeteilt werden, um die maximale Sequenzlänge des Encoders nicht zu überschreiten.
4. **Remove Stop-Words**: Entscheidung über das Entfernen von Füllwörtern aus dem Text zur Optimierung der Suchergebnisse.
5. **Overlap**: Bestimmung des Überlappungsgrades zwischen aufeinanderfolgenden Textsegmenten, falls eine Aufteilung stattfindet.

Diese Pipeline analysiert die eingereichten Fragen aus einem definierten Datensatz, kodiert die zugehörigen Dokumente und integriert diese in Qdrant, wobei jeder Testlauf einem spezifischen Collectionnamen zugewiesen wird. Anschließend erfolgt eine systematische Abfrage dieser Kollektion, um die Präzision der Suchergebnisse zu bestimmen. Die Genauigkeit wird pro Sprache und Kategorie dargestellt und in einem Genauigkeitsplot visualisiert, der die durchschnittliche Präzision über alle Kategorien hinweg zeigt.

![](https://lh7-us.googleusercontent.com/Oluzaa4uyx8aGQtn-9J5o5c2GjD9t49FkhKtnZWYq3wkXo5q4kA9XlHh99crsd1PPYAZNdi7k7kLB4Ir2RrtitnaOYmKktXbAfrXAOn-ZXz4aO4lfYULYijKjyNoPmic_4UDErERW9qeQeWzWCssG1Q)


Die höchste Präzision wurde mit dem Modell 'multi-qa-mpnet-base-dot-v1' erreicht, bei Verwendung der DOT-Distanzfunktion, einem Überlappungswert von 30 und ohne Entfernung von Stop-Words. Diese Konfiguration erzielte eine Genauigkeit von 100 % bei englischen und 58 % bei deutschen Dokumenten. Basierend auf den Anforderungen, die Suche primär in Englisch durchzuführen, wurde diese Methode für die Implementierung ausgewählt.

Die Suchanfragen in Qdrant geben eine Passage von maximal 512 Wörtern zurück, was der maximalen Sequenzlänge des 'mpnet'-Modells entspricht. Zur Extraktion der spezifischen Antworten aus diesen Passagen wird ein Extractive Question-Answering BERT-Modell ('distilbert-base-cased-distilled-squad') verwendet, das nach einem Satzende sucht, um eine vollständige Antwort zu liefern. Schließlich wird dem Frontend ein Dictionary bereitgestellt, das Dokumentennamen, Passagen und den extrahierten Satz enthält.

# 4. Architekturdiagramme und Beschreibung


## 4.1 Systemstruktur

Die Systemstruktur wurde im Hinblick auf Gewährleistung der optimierten Flexibilität und Effizienz und unter Berücksichtigung der geltenden Richtlinien gewählt. Dabei wurden Aspekte der Modularität, Wiederverwendbarkeit, Erweiterbarkeit, Sicherheit, Performance und Spezialisierung berücksichtigt. 

![[Strukturdiagramm.png]]
*Abb. X: Strukturdiagramm der **MindMachine**-Anwendung* #endsprint #link

Das Strukturdiagramm illustriert den Aufbau der Software-Architektur für das **MindMachine**-Projekt. Es zeigt, wie das System in mehrere Schichten und Komponenten unterteilt ist:

**GUI-Schicht:** Diese Ebene umfasst die Nutzer-GUI, die Anmeldung-GUI, die Admin-GUI und eine spezielle Komponente für die Sprache-zu-Text-KI-Transformation, welche die Benutzerschnittstellen zur Interaktion mit dem System darstellen.

**Fachkonzeptschicht:** In dieser Schicht befindet sich die Geschäftslogik, repräsentiert durch die Sessionverwaltung, Timeoutverwaltung, Gesprächsverwaltung, Statistikverwaltung und die Dateiverwaltung. Diese Komponenten verarbeiten Nutzeraktionen, verwalten Sitzungsdaten, Zeitüberschreitungen, statistische Daten und Dateioperationen.

**NLP-KI:** Eine Komponente, die für die Verarbeitung und Analyse von natürlicher Sprache und die Umwandlung in nutzbare Daten zuständig ist.

**Datenschicht:** Diese Ebene besteht aus der Datenbank, der Vektordatenbank und dem FileSystem. Sie speichert und verwaltet alle Daten, die für die Anwendung erforderlich sind, einschließlich Benutzerdaten, Suchanfragen und Dokumenteninhalte.

**HTW LDAP Server:** Ein externes System zur Authentifizierung und Verwaltung von Benutzerzugriffen.

Jede Komponente und jedes Subsystem ist durch Linien miteinander verbunden, die ihre Interaktionen und Abhängigkeiten aufzeigen. Die Verwendung von Standardsymbolen deutet auf die Art der Beziehungen hin, wobei Pfeile die Richtung des Datenflusses oder der Kontrolle anzeigen.

### Begründung der gewählten Systemstruktur

**Modularität:** Die Aufteilung in GUI, Fachkonzept und Datenschicht folgt dem Prinzip der Trennung von Anliegen. Dies ermöglicht es, die Benutzeroberfläche von der Geschäftslogik und der Datenspeicherung zu trennen, was die Wartung und Skalierung des Systems vereinfacht.

**Wiederverwendbarkeit:** Durch die Verwendung von Komponenten wie der Sessionverwaltung oder der Dateiverwaltung kann Code wiederverwendet werden, was die Effizienz der Entwicklung steigert.

**Erweiterbarkeit:** Die Architektur ist so konzipiert, dass sie leicht um neue Funktionen oder Module erweitert werden kann, ohne bestehende Systeme zu stören.

**Sicherheit und Compliance:** Die Integration des HTW LDAP Servers deutet darauf hin, dass Authentifizierung und Autorisierung wichtig sind und dass das System wahrscheinlich an spezifische Sicherheitsrichtlinien und Compliance-Standards angepasst ist.

**Performanz:** Die Trennung von datenintensiven Komponenten in einer eigenen Datenschicht könnte eine perspektivische Optimierung für hohe Leistung und schnelle Datenverarbeitung ermöglichen.

**Spezialisierung:** Durch die Verwendung von spezifischen Komponenten wie NLP-KI und Sprache-zu-Text-KI spezialisierte Diensten ermöglicht es fortschrittliche Funktionen wie natürliche Sprachverarbeitung in das System mit einzubinden.

## 4.2 Deployment-Architektur

Das Verteilungsdiagramm stellt die Deployment-Architektur für eine Webanwendung dar, die auf einer Reihe von Docker-Containern basiert. 

![[Verteilungsdiagramm.png]]
*Abb XX: Verteilungsdiagramm der **MindMachine**-Anwendung* #endsprint #link

Die Architektur ist in drei Hauptbereiche gegliedert: 

- **Client Workstation**: Der Client greift über einen Webbrowser, ausgeführt auf einem Windows 10 Home System, mittels HTTP auf die Anwendung zu.
    
- **Application Server**: Der Server nutzt eine moderne Hardwareumgebung mit einer spezifischen Ubuntu-Version. Hier werden die Frontend- und Backend-Docker-Container ausgeführt, die die Nutzer-GUI, die Anmeldung-GUI und die Admin-GUI bereitstellen. Die Frontend-Container nutzen React mit TypeScript, während die Backend-Container auf Python FastAPI und SQLAlchemy für Datenbankoperationen setzen.
    
- **Execution Environments**: Weitere Docker-Container sind für die Vektordatenbank (QDrant) und das Filesystem vorgesehen. Die Backend-Container verwalten Sessions, Gespräche, Statistiken und Dateien und interagieren mit der QDrant Vektordatenbank und dem Filesystem, wo Daten und Dokumente gespeichert werden.
## 6. Datenarchitektur
Beschreibung der Datenbankstruktur und des Datenmodells.

## 7. Sicherheit
Informationen zur Sicherheitsarchitektur der Anwendung.

## 8. Skalierbarkeit und Leistung
Beschreibung der Reaktion auf Skalierbarkeits- und Leistungsanforderungen.

## 9. Betrieb und Wartung
Informationen zur Bereitstellung, Konfiguration und Wartung.

## 10. Integration


## 11. Compliance und Standards
Informationen zur Einhaltung von Standards und Vorschriften.

## 12. Änderungsverlauf
Protokollierung von Änderungen an der Architektur.

## 13. Referenzen
Verweise auf relevante Dokumente und Ressourcen.



Speicherauswertung vom Server-Festplatte auf der das System drauf ist

Wie viel von anderen Programmen genutzt, wie viel von unserer Anwendung genutzt und wie viel noch frei

-> Storage Capacity anzeigen lassen 



Die gewünschten architektonischen Eigenschaften definieren (Long List):  

- Verfügbarkeit
- Performance: FastAPI Web Framework für das Backend, um eine schnelle Entwicklung und gute Performance zu ermöglichen. React nutzt Virtual DOM(Document Object Model), um die Seite optimal zu aktualisieren und nur an Stellen, wo es Änderungen gibt. Das führt zur erhöhten Performance.
- Erweiterbarkeit
- Wartbarkeit: React ist eine komponenten basierte Technologie. Außerdem wurde der Code in Backend modularisiert, um vereinfacht neue Funktionalitäten hinzuzufügen.
- Unterstützbarkeit: das wurde mittels Logging geschafft
- Authentifizierung: die Nutzer müssen ein HTW Konto haben


### Nicht im Umfang enthalten
Klare Angabe dessen, was nicht im Projekt enthalten ist, um Missverständnisse zu vermeiden.

- jwt ggf
- wir machen nur pdfs
für das System ist extrem wichtig, dass keiner externe auf die API Endpoints Zugriff hat, deswegen wird bei jedem Endpoint mittels JWT(JSON Web Token) geprüft, ob der Nutzer bzw. der Admin Zugriffrechte hat #pleasecheck #scoping

- Archivierbarkeit
- - Wiederherstellbarkeit