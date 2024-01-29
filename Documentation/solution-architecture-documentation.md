
- Server-  und Docker-Struktur hat Auswirkung auf die Webanwendung
	- wir haben 3 Dockercontainer in unserem System (nicht relevant: alle Linux)
		- python3.9-Dockercontainer
		- nginX-Dockercontainer
		- qdrant-Dockercontainer
	- nur für Installation wird noch zusätzlich der node-Container verwendet
	- alle 4 Docker-Container sind die neuesten offiziellen Images 
	- Änderung an den Docker-Container von offizieller Seite würden somit unweigerlich auch Auswirkungen haben


Speicherauswertung vom Server-Festplatte auf der das System drauf ist

Wie viel von anderen Programmen genutzt, wie viel von unserer Anwendung genutzt und wie viel noch frei

-> Storage Capacity anzeigen lassen 


qdrant vektorbasierte datenbank 
open source -> apache 2.0 licence

qdrant datenbank ist separat von nutzerdatenbank, weil es vektordatenbank ist und kombination wäre nicht günstig


herausforderungen bei der implementierung von qdrant: 

- nutzen von qdrant -> das erkennen der limits von der von qdrant bereitgestellten vektordatenbank -> aufsetzen einer zusätzlichen sql-light datenbank zur qdrtant datenbank 
- die datenstruktur für die vektorenspeicherung um die notwendige information für die suche richtig zu übergeben - die informationszuordnung der rückgabe auf fragen #endsprint

suchalgorithmus
- ceo reporting von abdehl zugesendet bekommen
- token pro vektor zu begrenzt -> abschnitte -> abschnitt zu dokumente 
	  -> mittwoch, 10.01. lieferung von report 
- evaluation der suchergebnisse für scoping document 
  metric die testet, wie genau das modell ist pro Sprache pro Kategorie 4 Stk alle pdf: ppt, chatgpt generiert, bachelorarbeit, studienordnung #endsprint 
	  unterscheidung zwischen dokument-suche und passagen-suche


architektur

-  python fastapi weil schnell und performant für performance fürs backend framework entsprechend gewählt 
- erstmal service architektur, aber es wäre zu aufwendig für unsere ressourcen, daher 3 schichten architektur gewählt 
- long list von geron mit ausführung 
- ch weiß es nicht, welche Dateiformat du bevorzugst, deswegen erstmal den Link...  
- Short List kommt statt Archivierbarkeit die Unterstützbarkeit--> das wurde mittels Logging geschafft
- Authentifizierung und Authorisierung--> für das System ist extrem wichtig, dass keiner externe auf die API Endpoints Zugriff hat, deswegen wird bei jedem Endpoint mittels JWT(JSON Web Token) geprüft, ob der Nutzer bzw. der Admin Zugriffrechte hat
- Verfügbarkeit: --  
- Performance: FastAPI Web Framework für das Backend, um eine schnelle Entwicklung und gute Performance zu ermöglichen. React nutzt Virtual DOM(Document Object Model), um die Seite optimal zu aktualisieren und nur an Stellen, wo es Änderungen gibt. Das führt zur erhöhten Performance.  
- Wiederherstellbarkeit: --  
- Erweiterbarkeit:  
- Wartbarkeit: React ist eine komponenten basierte Technologie. Außerdem wurde der Code in Backend modularisiert, um vereinfacht neue Funktionalitäten hinzuzufügen.  
- Der Rest steht schon da... Archivierbarkeit lasse ich komplett weg

CEO Reporting vom Software Architekten 
- Kennenlernen mit den Entwicklern
- Komponenten nach der Anforderungsanalyse ermitteln (noch kein Architekturstil ausgewählt)
- Use Case Diagramm erstellen
- Aktivitätsdiagramm erstellen
- Auswahl des Technologiestacks:
- FastAPI Web Framework (Fast steht für schnelle Entwicklung und auch gute Performance) mit der Programmiersprache Python für das Backend
- React Bibliothek im TypeScript für das Frontend
- Klassendiagramm erstellen (Moritz Köhler und Abdelrahman Elsharkawi haben Beitrag geleistet)

Die gewünschten architektonischen Eigenschaften definieren (Long List):  

- Verfügbarkeit
- Performance
- Wiederherstellbarkeit
- Erweiterbarkeit
- Wartbarkeit
- Unterstützbarkeit
- Archivierbarkeit
- Authentifizierung
- Authorisierung

Die 3 wichtigsten architektonischen Eigenschaften auswählen (Short List):  

- Authentifizierung (die Nutzer müssen ein HTW Konto haben)
- Authorisierung (verschiedene Rollen)
- Archivierbarkeit (die Dateien müssen gespeichert werden)

Architekturstil auswählen --> Schichten Architektur  
Strukturdiagramm erstellen  
Die Diagramme nach dem Gespräch mit dem Kunde und Team anpassen (der Admin verfügt über die Funktionalitäten des normalen Nutzers)  
Nach Absprache mit dem Team das Deploymentplatform auswählen --> Docker  
Verteilungsdiagramm erstellen

- Code Refactoring vornehmen
- SOLID Prinzipien überprüfen
- Schlechtes Codedesign vermeiden

### Nicht im Umfang enthalten
Klare Angabe dessen, was nicht im Projekt enthalten ist, um Missverständnisse zu vermeiden.

- jwt ggf
- wir machen nur pdfs