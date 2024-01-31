Die Solution Architecture Documentation (SAD) dient als umfassender Leitfaden und Referenzdokument für die Architektur der entwickelten Softwarelösung. Ihr primäres Ziel ist es, ein klares Verständnis der Systemarchitektur, der verwendeten Technologien und der Interaktion zwischen den verschiedenen Systemkomponenten zu vermitteln. Die Dokumentation richtet sich an ein breites Publikum, darunter Entwickler, Projektmanager und technische Stakeholder, und ist so konzipiert, dass sie sowohl als Einführungsressource für neue Teammitglieder als auch als Nachschlagewerk für bestehende Teammitglieder dient.

---
# 1. Architekturübersicht

Die Komponentenermittlung dient als maßgebende Grundlage für die Architekturwahl. Hier bei werden die einzelnen Teile des Systems identifiziert, definiert und in Bezug auf ihre Funktionalität, Verantwortlichkeiten und Interaktionen beschrieben werden.

**Anmeldung GUI:** Unabhängig von der Rolle haben sowohl der Nutzer als auch der Admin die selbe Anmeldungsfenster. 

**Nutzer GUI:** In diesem Fenster werden die Funktionaltäten des Nutzers zur Verfügung gestellt.

**Admin GUI:** Da der Admin ein Nutzer mit extra Priviligen ist, werden 
in diesem Fenster die Funktionaltäten des Nutzers und des Admins zur Verfügung gestellt.

**Sprache zu Text KI:** Mithilfe dieser kann der Nutzer Anfragen über seine Stimme stellen.

**Sessionverwaltung:** Diese Komponente ermöglicht es, dass der Nutzer sich anmeldet und auf die Funktionalitäten zugreift.

**Timeoutverwaltung:** Diese Komponente ermöglicht den Admin die Einstellung der Unterbrechungszeit der Session (Timeout).

**Datenvolumenverwaltung:** Der Admin kann mithilfe dieser Komponente  Statistiken über Daten und Suchanfragen  anzeigen lassen. Außerdem kann der Admin die maximale Speicherkapazität einstellen.

**Loggingverwaltung:** Diese Komponente sorgt dafür, dass Logeinträge geschrieben werden und die Logdatei zur Verfügung steht.

**Gesprächsverwaltung:** Diese Komponente ermöglicht es, dass die Frage des Nutzers beantwortet wird.

**Dateiverwaltung:** Diese Komponente ist zuständig für das Überprüfen, Hochladen, Löschen und Umbenennen der PDF Dateien.

**NLP KI:** Das ist ein bereitgestelltes KI Modell für die Texterkennung.

**HTW LDAP Server:** Diese ist ein externes System, in dem die Anmeldedaten aller Nutzer bereitgestellt sind.

## 1.1 Die architektonischen Eigenschaften

| architektonische Eigenschaft  | Short List      | Implementierungsdetails |
|:-------------                 |:--------------- | :-------------          |
| Verfügbarkeit                 | nein            | -                  |
| Performance                   | nein          | Auswahl von FastAPI und React|
| Wiederherstellbarkeit         | nein          | -                  |
| Performance                   | nein          | Auswahl von React|
| Erweiterbarkeit               | nein          | Entscheidungsrolle für Architekturstil                 |
| Wartbarkeit                   | nein          |Entscheidungsrolle für Architekturstil |
| Archivierbarkeit              | nein          | -                  |
| **Unterstützbarkeit**         | ja            | Logging                  |
| **Authentifizierung**         | ja            | JSON Web Token           |
| **Authorisierung**            | ja            | JSON Web Token                  |


### 1.2 Begründung des gewählten Architekturstil

Die Entscheidung lag zwischen einem servicebasierten und 3 Schichten Architekturstil. Es wurde  für 3 Schichten Architektur aus folgenden Gründen ausgewählt:

**Einfachheit und Übersichtlichkeit:** Eine 3-Schichten-Architektur ist in der Regel einfacher und direkter zu verstehen. Sie besteht aus der Präsentationsschicht, der Logikschicht und der Datenspeicherschicht. Dies kann besonders für kleinere oder weniger komplexe Anwendungen vorteilhaft sein.

**Entwicklungsaufwand:** Die Entwicklung in einer 3-Schichten-Architektur ist schneller und weniger komplex, da sie nicht die zusätzliche Komplexität und Overhead von Diensten, die in einer servicebasierten Stil typisch sind, beinhaltet. Darüber hinaus ist der Zeitrahmen innerhalb des Semesters limitiert.

**Wartbarkeit und Erweiterbarkeit:** Durch die Trennung von Benutzeroberfläche, Geschäftslogik und Datenzugriff ist es einfacher, Änderungen oder Erweiterungen in einer Schicht vorzunehmen, ohne die anderen Schichten zu beeinflussen.

**Vereinfachtes Testing und Debugging:** Da die Schichten getrennt sind, kann jede Schicht unabhängig von den anderen getestet und debuggt werden, was die Komplexität reduziert und die Qualitätssicherung verbessert.

---
# 2. Technologie-Stack

**React** und **TypeScript** werden für das Frontend verwendet, um eine reaktive und typsichere Benutzeroberfläche zu gewährleisten. 

**FastAPI** ist eine leistungsstarke und einfach zu verwendende Bibliothek für das Erstellen von Python-APIs, die schnelle Ausführung und einfache Wartung verspricht. Diese Bibliothek steuert das Backend. 

Die Datenhaltung wird über zwei Systeme durchgeführt: **SQLite** für relationale Datenbankbedürfnisse und **Qdrant** für Vektorsuchfunktionen. Diese Systeme ermöglichen eine effektive Verwaltung sowohl strukturierter als auch komplexer Suchanfragen. Die gesamte Anwendung ist containerisiert und über Docker orchestriert, was eine nahtlose und konsistente Deployment-Umgebung sowohl für Entwicklung als auch für Produktion gewährleistet.
Zudem werden in PDF Dateien im Dateisystem des Rechners abgespeichert.

Die Daten für die Anmeldung sind in **HTW LDAP Server** angelegt.

---
# 3. Architekturdiagramme und Beschreibung

## 3.1 Systemstruktur

![[Strukturdiagramm.png]](./Strukturdiagramm.png) 
*Abb. 1: Strukturdiagramm der **MindMachine**-Anwendung* #link

Das Strukturdiagramm illustriert den Aufbau der Software-Architektur für das **MindMachine**-Projekt. Es zeigt, wie das System in mehrere Schichten und Komponenten unterteilt ist. Implementierungseinzelheiten sind für den Teil nicht relevant. Hier sind die Beziehungen und Zugehörigkeit der Komponenten im Fokus:

**GUI-Schicht:** Diese Ebene umfasst die Nutzer-GUI, die Anmeldung-GUI, die Admin-GUI und eine spezielle Komponente für die Sprache-zu-Text-KI-Transformation, welche die Benutzerschnittstellen zur Interaktion mit dem System darstellen.

**Fachkonzeptschicht:** In dieser Schicht befindet sich die Geschäftslogik, repräsentiert durch die Sessionverwaltung, Timeoutverwaltung, Gesprächsverwaltung, Statistikverwaltung und die Dateiverwaltung. Diese Komponenten verarbeiten Nutzeraktionen, verwalten Sitzungsdaten, Zeitüberschreitungen, statistische Daten und Dateioperationen.

**Datenschicht:** Diese Ebene besteht aus der Datenbank, der Vektordatenbank und dem FileSystem. Sie speichert und verwaltet alle Daten, die für die Anwendung erforderlich sind, einschließlich Benutzerdaten, Suchanfragen und Dokumenteninhalte.

**HTW LDAP Server:** Der externe Server, der dem System die Anmeldedaten zur Verfügung stellt. 


## 3.2 Deployment-Architektur

Das Verteilungsdiagramm stellt die Deployment-Architektur für das System dar. Hier sind nicht die Beziehungen zwischen Subsystem im Fokus, sondern werden Komponenten und Artefakte in Relation zu ihrem Einsatzort innerhalb des implementierten Systems angezeigt. 

![[Verteilungsdiagramm.png]](./Verteilungsdiagramm.png)
*Abb 2: Verteilungsdiagramm der **MindMachine**-Anwendung* #endsprint #link

Die Architektur ist in drei Hauptbereiche gegliedert: 

- **Client Workstation**: Der Client greift über einen Webbrowser, beispielsweise auf einem Windows 10 Home System, mittels HTTP auf die Anwendung zu.
    
- **Application Server**: Diese Knote beschreibt den Hardwareteil des Servers. Der Server hat als Betriebssystem Ubuntu.
    
- **Execution Environments**: Diese Knote gibt Informationen über die Ausführungsumgebung vom Subsystemen. Da Qdrant Schwierigkeiten bereitet hat, im selben Container 

## 3.3 Klassenstruktur

Die Wahl der Struktur ist auch auf spezifische Anforderungen des Projekts zurückzuführen, wie die Notwendigkeit, die Authentifizierung klar von den Geschäftslogiken zu trennen und eine flexible Datenverwaltung zu ermöglichen, die unterschiedliche Typen von Datenbanken (wie Vektor- und relationale Datenbanken) unterstützt.

![[Klassendiagramm.png]]
*Abb. 3.: Klassendiagramm der **MindMachine**-Anwendung* #link  

Hier einige Gründe für die gewählte Struktur:

1. **Kapselung**: Jede Klasse kapselt spezifische Daten und Verhaltensweisen, was die Datenintegrität verbessert und die Komplexität reduziert. Zum Beispiel verwaltet die Klasse `DatabaseHandler` alle Datenbankinteraktionen, während die Klasse `User` die Benutzerdaten hält.
    
2. **Wiederverwendbarkeit**: Durch die Definition klarer Schnittstellen können Klassen in verschiedenen Teilen der Anwendung wiederverwendet werden. Zum Beispiel könnte der `LogHandler` in verschiedenen Kontexten genutzt werden, um unterschiedliche Ereignisse zu loggen.
    
3. **Erweiterbarkeit**: Objektorientierte Systeme sind leichter erweiterbar. Neue Funktionalitäten können durch das Hinzufügen neuer Klassen oder das Erweitern bestehender Klassen implementiert werden, ohne bestehende Codebasis zu stören.
    
4. **Modularität**: Die klare Trennung von Verantwortlichkeiten ermöglicht es, das System in logische Module zu unterteilen, was die Wartung erleichtert. Zum Beispiel ist die `AuthAPI` ausschließlich für die Authentifizierung zuständig.
    
5. **Testbarkeit**: Isolierte Klassen können unabhängig voneinander getestet werden, was die Erstellung und Wartung von Tests vereinfacht und zur Gesamtstabilität des Systems beiträgt.
    
6. **Verständlichkeit**: Ein wohlstrukturiertes Klassendiagramm erleichtert das Verständnis der Systemarchitektur für neue Entwickler und Stakeholder und fördert die Kommunikation im Team.

---
# 4. Datenarchitektur

In diesem Kapitel wird die Datenspeicherung sowie Bearbeitung beschrieben.

## 4.1 SQLite

In SQLite beinhaltet die folgenden Tabellen:

**User:** Diese Tabelle speichert die Nutzerrolle jedes Nutzers und die Zeitstempel der letzten Anmeldungs.

**AdminSettings:** Diese Tabelle speichert die Systemkonfigurationen wie Timeout und die Speicherkapazität.

**SeachHistory:** Diese Tabelle speichert die Suchhistorie jedes Nutzers.


## 4.2 FileSystem

Die PDF Dateien, sowie die SQL Datei für oben erwähnte Datenbank wird direkt im Dateisystem des Servers abgespeichert. 

## 4.3 Qdrant

In dieser Datenbank werden die Vektordaten abgespeichert.

---
# 5. Sicherheit mit JTWs

Im Sicherheitskapitel unserer Solution Architecture Documentation liegt ein besonderer Fokus auf der Verwendung von **JSON Web Tokens (JWTs)** für Authentifizierung und Autorisierung. 

JWTs sind ein zentraler Bestandteil unserer Sicherheitsstrategie, um sicherzustellen, dass nur berechtigte Nutzer auf das System zugreifen und ihre Identität effektiv überprüft wird.
JWTs werden bei der Benutzeranmeldung erstellt. Der Token besteht aus einem Header, einem Payload und einer Signatur. Der Header definiert den Token-Typ und das verwendete Hash-Verfahren. 
Der Payload enthält die Claims, also Informationen wie Benutzer-ID, Rolle und Token-Ablaufzeit. 
Die Signatur, erzeugt durch das Hash-Verfahren mit einem geheimen Schlüssel, sichert die Integrität des Tokens.

Bei jeder Anfrage wird der Token vom Client gesendet und vom Server validiert. 
Die Validierung umfasst die Überprüfung der Signatur, die Bestätigung der Token-Ablaufzeit und die Überprüfung der Nutzerberechtigungen basierend auf den im Payload enthaltenen Claims.

**Schwachstellen**  
Der Authentifizierungstoken wird im `localStorage` eines Browsers abgespeichert. Das bringt das einige Schwachstellen mit sich. `localStorage` ist anfällig für XSS-Angriffe. Wenn eine Website eine Sicherheitslücke aufweist, die es einem Angreifer ermöglicht, schädlichen JavaScript-Code auszuführen, könnte dieser Code auf `localStorage` zugreifen und die darin gespeicherten Daten, einschließlich Tokens, stehlen.


