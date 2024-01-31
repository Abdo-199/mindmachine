# 1.Teststrategie

Diese Dokumentation richtet sich an Entwickler, Tester und Betreuer des Backends und bietet einen detaillierten und strukturierten Überblick über die strategische Testlandschaft, Testfälle und ihre Ergebnisse. Es beschreibt die Testmethodik für das Backend der Webanwendung, einschließlich der Verwendung von Qdrant für Datenverarbeitung und Abruf. Ziel der Teststrategie ist es, die Zuverlässigkeit, Funktionalität und Integrität der Backend-Dienste sicherzustellen.

# 2. Testfälle und -szenarien

Im Rahmen unserer Testumgebung wurde vorrangig auf Mock- und Unittests zurückgegriffen, die bereits in der Dokumentation erwähnt sind. Die Unittests werden zu Beginn definiert und am Ende hinsichtlich des erwarteten Ergebnisses überprüft. Sie resultieren in einer klaren Aussage: bestanden oder nicht bestanden, ohne eine tiefergehende Bewertung. 

Verschiedene Testszenarien wurden durchgeführt, darunter:

- **Datenbankinteraktionen und CRUD-Operationen**
	  Tests im Zusammenhang mit CRUD-Operationen (Erstellen, Lesen, Aktualisieren, Löschen) für Benutzerentitäten und Suchverlauf mit SQLAlchemy ORM mit SQLite.
- **Dateisystemoperationen und Dateimanipulationen**
	  Tests, die die korrekte Handhabung von Datei-Uploads, Löschungen und Dateisystem-Manipulationen sicherstellen, einschließlich Datei-Metadaten-Abruf und Dateisystem-Struktur-Integrität.
- **Integration des Qdrant-Clients und Funktionalitätstests**
	  Tests, die die Integration und Funktionalität des Qdrant-Clients für den Umgang mit Dokumentvektoren, Benutzerverifizierung und Suchfunktionen validieren.
- **Dienstprogrammfunktionen und deren Genauigkeit**
	  Tests für verschiedene Dienstprogrammfunktionen wie Dateigrößenkonvertierungen und Datumsabrufe, um Genauigkeit und Zuverlässigkeit bei der Dateihandhabung und Anzeige zu gewährleisten.

## 1. Testfall: test_pdfReader.py

#pleasecheck Hier fehlt die Beschreibung zum Anwendungsfall bzw zu den Testszenarien (s. Testfall 2 und 3)

**Testumgebung:** Ausgeführt in einer Python-Umgebung mit PyPDF2 und anderen notwendigen Bibliotheken.

**High-Level Beschreibung**: Die TestPdfProcessingSuite sorgt für die genaue Extraktion von Text und die Konvertierung in Dokumentvektoren aus PDF-Dateien. Es testet Funktionalität unter normalen Bedingungen, verschiedene Formate, große Dateien und Fehlerszenarien.

**Testframework:** Python unittest framework.

**Testausführung:** Ausführen der Tests mit python -m unittest [test_file_name].py.

### Struktur des allgemeinen Testfalls

**Setup:** Vorbereiten von Mock-PDF-Dateien oder Objekten.

**Ausführung:** Ausführen der spezifischen PDF Verarbeitungsfunktion, die getestet wird.

**Assertion:** Überprüfen, ob die Funktion's mit den erwarteten Ergebnissen übereinstimmt.

**Teardown:** Aufgrund der Verwendung von Mock-Objekten in der Regel nicht erforderlich.

### Übersicht der Testfälle

**1.1 Testfall:** Konvertierung von PDF in Text

**1.2 Testfall:** PDF zu Dokument-Vektor Konvertierung

**1.3 Testfall:** PDF zu Dokument Vektor mit verschiedenen Absätzen

**1.4 Testfall:** PDF zu Text Konvertierung für große PDF

**1.5 Testfall:** PDF zu Text Ausnahmebehandlung

**1.6 Testfall:** PDF zu Dokument Vektor Ausnahmebehandlung

#### 1.1 Testfall: Konvertierung von PDF in Text

**Zweck:** Dieser Test überprüft, ob die pdf_to_text-Funktion Text aus einer Standard-PDF-Datei präzise extrahiert.

**Voraussetzungen:** Eine Mock-PDF-Datei mit vordefiniertem Text auf verschiedenen Seiten.

**Testschritte:**

-  Erstellen Sie ein Mock-PDF-Reader-Objekt mit Seiten mit vordefiniertem Text.

-   Führen Sie die Funktion pdf_to_text auf diesem Mock-PDF aus.

**Erwartete Ergebnisse:** Die Funktion gibt eine Textzeichenfolge zurück, die den gesamten Text der Mock-PDF-Seiten enthält, und die Anzahl der Absätze sollte mit der Anzahl der Seiten übereinstimmen.

**Pass/Fail Kriterien:** Bestanden, wenn der extrahierte Text Inhalte von allen Seiten enthält und die Anzahl der Absätze korrekt ist.

#### 1.2 Testfall: PDF zu Dokument-Vektor Konvertierung

**Zweck:** Um die pdf_to_docVec-Funktion und die Fähigkeit, PDF-Inhalte in Dokumentvektoren zu konvertieren, zu testen.

**Voraussetzungen:** Ein Mock-PDF-Reader und ein Mock-Encoder zur Erzeugung von Dokumentvektoren.

**Testschritte:**

-  Mock ein PDF-Reader mit einer einzigen Seite mit Text.

- Verwenden Sie einen Mock-Encoder, um Dokumentvektoren zu generieren.

- Führen Sie die Funktion pdf_to_docVec mit diesen Mocks aus.

**Erwartete Ergebnisse:** Die Funktion sollte ein DocVec-Objekt mit korrekten Dokument- und Absatzvektoren zurückgeben.

**Pass/Fail-Kriterien:** Bestanden, wenn das zurückgegebene DocVec-Objekt die erwarteten Vektoren aufweist.

#### 1.3 Testfall: PDF zu Dokument Vektor mit verschiedenen Absätzen

**Zweck:** Dieser Test prüft die Fähigkeit von pdf_to_docVec function's, PDFs mit unterschiedlichen Absatzstrukturen zu handhaben und in Dokumentvektoren zu konvertieren.

**Voraussetzungen:** Ein Mock-PDF-Reader mit Seiten mit mehreren Absätzen und einem Mock-Encoder.

**Testschritte:**

-  Mock ein PDF-Reader mit Seiten mit verschiedenen Absätzen.

- Passen Sie den Mock-Encoder an verschiedene Textformate an.

-  Führen Sie die Funktion pdf_to_docVec aus.

**Erwartete Ergebnisse:** Das DocVec-Objekt sollte für jeden Absatz separate Vektoren enthalten, die ihren Inhalt genau widerspiegeln.

**Pass/Fail Kriterien:** Bestanden, wenn die Absatzvektoren die verschiedenen Absätze korrekt darstellen.

#### 1.4 Testfall: PDF zu Text Konvertierung für große PDF**

**Zweck:** Damit die pdf_to_text-Funktion große PDF-Dateien effizient und genau verarbeiten kann.

**Voraussetzungen:** Ein Mock-PDF-Reader, der eine große PDF-Datei mit vielen Seiten simuliert.

**Testschritte:**

- Erstellen Sie einen Mock-PDF-Reader mit einer großen Anzahl von Seiten.

- Führen Sie die Funktion pdf_to_text auf diesem Mock-PDF aus.

**Erwartete Ergebnisse:** Die Funktion sollte Text zurückgeben, der Inhalt der ersten und letzten Seiten und die richtige Anzahl von Absätzen enthält.

**Pass/Fail-Kriterien:** Bestanden, wenn der Text Inhalte von beiden Enden des PDF enthält und die Anzahl der Absätze mit der Seitenzahl übereinstimmt.

#### 1.5 Testfall: PDF zu Text Ausnahmebehandlung

**Zweck:** Dieser Test stellt sicher, dass die Funktion pdf_to_text Exception , wie Fehler beim Lesen des PDF, korrekt behandelt.

**Voraussetzungen:** Ein Szenario, in dem der PDF-Reader eine Exception  auslöst.

**Testschritte:**

- Simulation einer Execption im PDF-Leseprozess.

- Versuch, die Funktion pdf_to_text unter dieser Bedingung auszuführen.

**Erwartete Ergebnisse:** Die Funktion sollte eine entsprechende Exception  auslösen, die einen Fehler beim lesen von Pdf  anzeigt.

**Pass/Fail Kriterien:** Bestanden, wenn eine Ausnahme wie erwartet ausgelöst wird.

#### 1.6 Testfall: PDF zu Dokument-Vektor Ausnahmebehandlung

**Zweck:** Um zu überprüfen, ob die Funktion pdf_to_docVec Exception  effektiv behandelt, insbesondere wenn Fehler im PDF-Leseprozess auftreten.

Voraussetzungen: Ein Mock-Szenario, in dem das Lesen der PDF-Datei zu einer Exception führt.

**Testschritte:**

- Simulieren Sie eine Exception  beim Lesen einer PDF-Datei.

- Versuchen Sie, die Funktion pdf_to_docVec unter dieser Bedingung auszuführen.

**Erwartete Ergebnisse:** Die Funktion sollte die Ausnahme ordnungsgemäß behandeln, wahrscheinlich durch eine Auslösung, damit die aufrufende Funktion sie behandeln kann.

**Pass/Fail Kriterien:** Bestanden, wenn die Exception  gemäß dem Design der Funktion behandelt wird.

### Mock Objects und Testdaten

Mock PDF Reader und Encoder: Wird verwendet, um verschiedene Szenarien für die PDF-Verarbeitung und Vektorerzeugung zu simulieren.

### Testergebnis für Testfall 1

![Testergebnisbericht Testfall 1](Testbericht_TF1.jpg)

## 2. Testfall:  test_Qdrant.py

**Testfälle und -szenarien:*** **Qdrant-Client Integration und Funktionalitätstests**
    - Überprüfung vorhandener und nicht existierender Benutzer
    - Hinzufügen von Dokumentvektoren
    - Abrufen von Suchergebnissen aus der Qdrant-Datenbank 
      #pleasecheck meines Erachtens Doppelung mit Auflistung der Testfälle
      #pleasecheck es gilt auch bei den inhaltlichen Vorleistungen auf eine allgemeingültige Struktur zu achten. Bitte einheitliche Bezeichnung für diesen Abschnitt Testfälle und -szenarien bzw. Anwendungsfälle in allen Testfall-Abschnitten einarbeiten

**Testumgebung:** Die Tests wurden in einer Python-Umgebung mit dem Qdrant-Client und den erforderlichen Bibliotheken durchgeführt.

**High-Level Beschreibung:** Die TestQdrant-Suite stellt sicher, dass der Qdrant-Client korrekt integriert ist und Funktionen wie Benutzerüberprüfung, Dokumentvektorbehandlung und Suchfunktionalitäten richtig funktionieren.

**Testframework:** Python unittest framework.

**Testausführung:** Ausführen der Tests mit `python -m unittest [test_file_name].py`.


### Struktur des allgemeinen Testfalls

**Setup:** Einrichten des Qdrant-Clients und der notwendigen Mock-Objekte.

**Ausführung:** Ausführen der spezifischen Methode oder Funktion des zu testenden Qdrant-Clients.

**Assertion:** Überprüfen, ob die Ausgabe oder das Verhalten der Methode's mit den erwarteten Ergebnissen übereinstimmt.

**Teardown:** Zurücksetzen von Zuständen oder Objekten, die während des Tests geändert wurden (in der Regel von unittest framework behandelt).
### Übersicht der Testfälle

**2.1 Testfall:** Überprüfung der vorhandenen Benutzer

**2.2 Testfall:** Überprüfung von nicht vorhandene Benutzer

**2.3 Testfall:**  Dokument Vektor hinzufügen

**2.4 Testfall:** Abfrage von Treffen des Qdrant-Clients #pleasecheck korrekte Testbezeichnung?

**2.5 Testfall:** Abrufen von Ergebnissen aus Treffern

**2.6 Testfall:** Suchfunktionalität

#### 2.1 Testfall: Überprüfung der vorhandenen Benutzer

-  Erhalten Sie Ergebnisse von Hits
-    Suchfunktionalität 
#pleasecheck Warum steht das hier?

**Zweck:** Überprüfen, ob der Qdrant-Client einen vorhandenen Benutzer in der Datenbank korrekt identifizieren und die Vektorzählung abrufen kann.

**Voraussetzungen:** Qdrant-Client-Setup mit vorgetäuschten Antworten.

**Testschritte:**

-   Simulieren Sie ein Szenario, in dem der Benutzer bereits in der Qdrant-Datenbank vorhanden ist.

- Rufen Sie die check_user-Methode mit einem vorhandenen user's-Bezeichner auf.

**Erwartete Ergebnisse:** Die Methode sollte die Anzahl der Vektoren zurückgeben, die dem vorhandenen Benutzer zugeordnet sind.

**Pass/Fail-Kriterien:** Bestanden, wenn die zurückgegebene Vektorzählung mit den simulierten Daten übereinstimmt.

#### 2.2 Testfall: Überprüfung von nicht vorhandene Benutzer

**Zweck:** Um sicherzustellen, dass der Qdrant-Client ein Szenario korrekt verarbeitet, in dem ein Benutzer nicht in der Datenbank vorhanden ist, was möglicherweise zur Erstellung eines neuen Benutzers führt.

**Voraussetzungen:** Qdrant-Client-Setup mit angedeuteter Ausnahmebehandlung.

**Testschritte:**

-  Simulieren Sie ein nicht vorhandenes Benutzerszenario, indem Sie im Qdrant-Client eine Exception einrichten.

- Führen Sie die Methode check_user mit der Kennung eines nicht vorhandenen Benutzers aus.

**Erwartete Ergebnisse:** Die Methode sollte die Exception  behandeln und eine Null-Vektor-Zählung zurückgeben, die einen neuen Benutzer anzeigt.

**Pass/Fail-Kriterien:** Übergibt, wenn die Methode Null zurückgibt und das nicht vorhandene Benutzerszenario wie erwartet verarbeitet.

#### 2.3 Testfall: Dokument Vektor hinzufügen

**Zweck:** Dieser Test prüft, ob der Qdrant-Client erfolgreich Dokumentvektoren für einen bestimmten Benutzer hinzufügen kann.

**Voraussetzungen:** Mocked Qdrant-Client und ein Dummy-Dokumentvektorobjekt.

**Testschritte:**

-  Erstellen Sie ein Dummy-Dokumentvektorobjekt mit angegebenen Attributen.

- Rufen Sie die add_docVec-Methode auf, um den Dokumentvektor zu einer user's-Sammlung hinzuzufügen.

**Erwartete Ergebnisse:** Der Qdrant-Client sollte die upload_records-Methode für jeden Vektor im Dokument (Dokument- und Absatzvektoren) korrekt aufrufen.

**Pass/Fail Criteria**: Besteht, wenn die upload_records-Methode die richtige Anzahl von Malen (einmal für das Dokument und einmal für jeden Absatz) aufgerufen wird.

#### 2.4 Testfall: Abfrage von Treffern des Qdrant-Clients #pleasecheck 

**Zweck:** Validierung der Funktionalität zum Abrufen von Suchtreffern vom Qdrant-Client anhand einer Abfrage.

**Voraussetzungen:** Mocked Encoder und Qdrant client's Suchmethode.

**Testschritte:**

- Simulieren Sie den Encoder, um ein Dummy-Numpy-Array zurückzugeben.

- Rufen Sie die get_hits-Methode mit einer Testabfrage und -sammlung auf.

**Erwartete Ergebnisse:** Die Suchmethode Qdrant client's sollte mit entsprechenden Parametern aufgerufen werden.

**Pass/Fail Kriterien:** Bestanden, wenn die Suchmethode mit den Mock-Parametern korrekt aufgerufen wird.

#### 2.5 Testfall: Abrufen von Ergebnissen aus Treffern

**Zweck:** Zum Testen der Extraktion relevanter Dokumentnamen anhand von Ergebnissen aus Suchtreffern.

**Voraussetzungen:** Eine Reihe von Mocked Search Hits mit Scores und Payloads.

**Testschritte:**

- Erstellen Sie Mock-Suchtreffer mit vordefinierten Scores und Payloads.

- Rufen Sie die get_scores-Methode mit diesen Treffern auf.

**Erwartete Ergebnisse:** Die Methode sollte den Namen des Dokuments mit der höchsten Punktzahl zurückgeben.

**Pass/Fail-Kriterien:** Bestanden, wenn der zurückgegebene Dokumentname mit dem höchsten Wert in den Mock-Daten übereinstimmt.

#### 2.6 Testfall: Funktionalität der Suche

**Zweck:** Dieser Test stellt sicher, dass die Gesamtfunktionalität der Suche, die die Abrufung von Treffern und die Verarbeitung von Bewertungen kombiniert, wie erwartet funktioniert.

**Voraussetzungen:** Mocked get_hits and get_scores methods.

**Testschritte:**

- Simulieren Sie die Methoden get_hits und get_scores, um vordefinierte Werte zurückzugeben.

- Rufen Sie die Suchmethode mit einer Testabfrage und -sammlung auf.

**Erwartete Ergebnisse:** Die Methode sollte den Suchvorgang korrekt orchestrieren und relevante Dokumente und Absätze basierend auf der Abfrage zurückgeben.

**Pass/Fail-Kriterien:** Bestanden, wenn die Suchmethode Ergebnisse liefert, die mit den get_hits- und get_scores-Methoden übereinstimmen.
### Mock Objects und Testdaten

- Mock Qdrant Client: Für die Simulation der Interaktion mit der Qdrant-Datenbank
- Mock Document Vectors und Encoder: Für das Testen von Dokumentvektor-Uploads und Suchfunktionalitäten

### Testergebnis für Testfall 2

![Testergebnisbericht Testfall 2](Testbericht_TF2.jpg)

## Testfall 3: test_databaseHandler.py

**Anwendungsbereich:** Die Tests umfassen verschiedene Vorgänge wie das Hinzufügen, Abrufen, Aktualisieren und Löschen von Benutzerdatensätzen sowie das Protokollieren und Abrufen des Suchverlaufs und das Ermitteln aktiver und inaktiver Benutzer.

**Testumgebung:** Die Tests werden in einer Python-Umgebung mit SQLAlchemy für Datenbankoperationen durchgeführt, wobei eine SQLite-Datenbank zu Testzwecken eingerichtet wird.

**High-Level-Beschreibung:** Die TestUserCRUD-Suite umfasst Tests, um die ordnungsgemäße Funktion von Datenbankoperationen im Zusammenhang mit der Benutzerverwaltung und der Protokollierung der Suchhistorie mithilfe von SQLAlchemy ORM sicherzustellen.

**Test Framework:** Python unittest framework.

**Testausführung:** Führen Sie diese Tests mit dem Befehl python -m unittest [test_file_name].py.aus

### Struktur des allgemeinen Testfalls

**Setup:** Initialisieren der Datenbank-Engine, Erstellen von Tabellen und Einrichten der Sitzung.

**Ausführung:** Ausführen spezifischer CRUD-Operationen oder Protokollierung der Benutzeraktivität.

**Assertion:** Überprüfen, ob das Ergebnis der Operation's mit den erwarteten Ergebnissen übereinstimmt.

**Teardown:** Zurücksetzen von Transaktionen und Schließen der Sitzung zur Aufrechterhaltung der Testisolierung.

### Übersichtsliste der Testfälle

**3.1 Testfall:** Add User

**3.2 Testfall:** Get User

**3.3 Testfall:** Update User

**3.4 Testfall:** Delete User

**3.5 Testfall:** Get All Users

**3.6 Testfall:** Log Search

**3.7 Testfall:** Update Last Login

**3.8 Testfall:** Get Active Users

**3.9 Testfall:** Get Inactive Users

**3.10 Testfall:** Detailed Test Cases

#### 3.1 Testfall: Add User

**Zweck:** Überprüfen, ob das System einen neuen Benutzer korrekt zur Datenbank hinzufügen kann.

**Voraussetzungen:** Datenbanksitzungseinrichtung.

**Testschritte:**

- Fügen Sie der Datenbank einen neuen Benutzer hinzu.

- Abfrage der Datenbank, um den neu hinzugefügten Benutzer abzurufen.

**Erwartete Ergebnisse:** Der Benutzer sollte erfolgreich hinzugefügt werden, und der Abruf sollte den hinzugefügten Benutzerdetails entsprechen.

**Pass/Fail Kriterien:** Bestanden, wenn der Benutzer korrekt hinzugefügt und abgerufen wird.

#### 3.2 Testfall: Get User

**Zweck:** Zum Testen des Abrufs eines bestimmten Benutzers aus der Datenbank.

**Voraussetzungen:** Ein Benutzer wird zur Datenbank hinzugefügt.

**Testschritte:**

- Rufen Sie einen vorhandenen Benutzer aus der Datenbank ab.

**Erwartete Ergebnisse:** Die korrekten Benutzerdaten werden zurückgegeben.

**Pass/Fail Kriterien:** Bestanden, wenn der abgerufene Benutzer die erwarteten Details erfüllt.

#### 3.3 Testfall: Update User

**Zweck:** Damit Benutzerdaten in der Datenbank korrekt aktualisiert werden können.

**Voraussetzungen:** Ein Benutzer wird zur Datenbank hinzugefügt.

**Testschritte:**

- Aktualisieren Sie den Namen eines vorhandenen Benutzers.

- Rufen Sie den Benutzer ab, um das Update zu überprüfen.

**Erwartete Ergebnisse:** Die Details des Benutzers's sollten wie angegeben aktualisiert werden.

**Pass/Fail Kriterien:** Bestanden, wenn der Benutzer' s aktualisierte Details korrekt sind.

#### 3.4 Testfall: Delete User

**Zweck:** Überprüfen, ob ein Benutzer erfolgreich aus der Datenbank gelöscht werden kann.

**Voraussetzungen:** Ein Benutzer wird von Datenbank gelöscht.

**Testschritte:**

- Löschen Sie einen vorhandenen Benutzer aus der Datenbank.

- Versuchen Sie, den gelöschten Benutzer abzurufen.

**Erwartete Ergebnisse:** Der Benutzer sollte nach dem Löschen nicht in der Datenbank gefunden werden.

**Pass/Fail Kriterien:** Bestanden, wenn der Benutzer erfolgreich gelöscht wurde.

#### 3.5 Testfall: Get All Users

**Zweck:** Überprüfen, ob das System alle Benutzer aus der Datenbank abrufen kann.

**Voraussetzungen:** Mehrere Benutzer werden zur Datenbank hinzugefügt.

**Testschritte:**

- Rufen Sie alle Benutzer aus der Datenbank ab.

**Erwartete Ergebnisse:** Eine Liste aller Benutzer in der Datenbank sollte zurückgegeben werden.

**Pass/Fail Kriterien:** Bestanden, wenn alle Benutzer abgerufen werden.

#### 3.6 Testfall: Log Search

**Zweck:** Überprüfen, ob das System eine Suchabfrage des Benutzers's in der Datenbank protokollieren kann.

**Voraussetzungen:** Ein Benutzer wird zur Datenbank hinzugefügt.

**Testschritte:**

- Protokollieren Sie eine Suchabfrage für den Benutzer.

- Rufen Sie die protokollierte Suche aus der Datenbank ab.

**Erwartete Ergebnisse:** Die Suchanfrage sollte korrekt unter dem user's Datensatz protokolliert werden.

**Pass/Fail-Kriterien:** Bestanden, wenn die Suchabfrage protokolliert und korrekt abgerufen wird.

#### 3.7 Testfall: Update Last Login

**Zweck:** Um die Funktionalität der Aktualisierung eines Benutzers's letzte Anmeldung Zeit zu testen.

**Voraussetzungen:** Ein Benutzer wird zur Datenbank hinzugefügt.

**Testschritte:**

- Aktualisieren Sie die letzte Anmeldezeit des Benutzers.

- Rufen Sie den Benutzer ab, um die letzte Anmeldezeit zu überprüfen.

**Erwartete Ergebnisse:** Der Benutzer's letzte Login-Zeit sollte auf die aktuelle Zeit aktualisiert werden.

**Pass/Fail Kriterien:** Bestanden, wenn die letzte Anmeldezeit korrekt aktualisiert wurde.

#### 3.8 Testfall: Get Active Users

**Zweck:** Um sicherzustellen, dass das System aktive Benutzer anhand ihrer letzten Anmeldezeit identifizieren und abrufen kann.

**Voraussetzungen:** Benutzer mit unterschiedlichen Anmeldezeiten werden der Datenbank hinzugefügt.

**Testschritte:**

- Aktive Benutzer aus der Datenbank abrufen.

Erwartete Ergebnisse: Es sollten nur Benutzer zurückgegeben werden, die sich kürzlich angemeldet haben (basierend auf einem definierten Schwellenwert).

**Pass/Fail Kriterien:** Bestanden, wenn nur aktive Benutzer abgerufen werden.

#### 3.9 Testfall: Get Inactive Users #pleasecheck FEHLT!!!!!

#### 3.10 Testfall: Detailed Test Cases #pleasecheck FEHLT!!!!

### Mock Objects und Testdaten

**Keine erforderlich:** Echte Datenbankinteraktionen werden getestet.

### Testergebnis für Testfall 3 #pleasecheck hier fehlt ein Testbericht in der Übersicht (9/10 abgebildet)

![Testergebnisbericht Testfall 1](Testbericht_TF3.jpg)



## Testfall 4: test_fileSystemHandler.py

#pleasecheck einheitliche Bezeichnung.....

**Umfang:** Die Tests umfassen Initialisierungsprüfungen, Hochladen und Löschen von Dateien, Manipulation des Dateisystems und Dienstprogrammmethoden wie Dateigrößenkonvertierung und Abruf des letzten Änderungsdatums. 

**Testumgebung:** Die Tests werden in einer Python-Umgebung mit simulierten Dateioperationen und -pfaden durchgeführt.

Beschreibung: Die TestFileSystemHandler-Suite wurde entwickelt, um die Funktionalität von Dateisystemoperationen zu validieren und die korrekte Handhabung von Benutzerdokumenten, Dateimetadaten und Dateisystemstruktur sicherzustellen.

**Test Framework:** Python unittest framework.

**Testausführung:** Führen Sie diese Tests mit dem Befehl python -m unittest [test_file_name].py.aus

### Struktur des allgemeinen Testfalls

**Setup:** Einrichten der FileSystemHandler-Instanz und Simulieren der erforderlichen Dateisystemoperationen.

**Ausführung:** Ausführen verschiedener Dateisystemoperationen durch FileSystemHandler.

**Assertion**: Überprüfen, ob jede Operation das erwartete Ergebnis liefert.

**Teardown:** Bereinigung von Mock-Einstellungen oder Objekten.

### Übersichtsliste der Testfälle

**4.1 Testfall:** Überprüfung der Initialisierung

**4.2 Testfall:** Erfolg beim Hochladen von Dateien

**4.3 Testfall:** Löschen von Dateien

**4.4 Testfall:** Abrufen Dateisystem für Benutzer

**4.5 Testfall:** Dokumentenname bearbeiten

**4.6 Testfall:** Abrufen des Dokumentpfads

**4.7 Testfall:** Überprüfen der Dateisystemexistenz

**4.8 Testfall:** Konvertieren von Bytes in ein lesbares Format

**4.9 Testfall:** Datum der letzten Änderung der Datei

#### 4.1 Testfall: Überprüfung der Initialisierung

**Zweck:** Überprüfen, ob FileSystemHandler mit dem richtigen Qdrant-Client initialisiert wurde.

**Testschritte:**

- Überprüfen Sie, ob das FileSystemHandler instance's Qdrant-Clientattribut mit dem erwarteten Client übereinstimmt.

**Erwartete Ergebnisse:** Der FileSystemHandler sollte mit dem bereitgestellten Qdrant-Client initialisiert werden.

**Pass/Fail-Kriterien:** Bestanden, wenn der Qdrant-Client während der Initialisierung korrekt zugewiesen wurde.

#### 4.2 Testfall: Erfolg beim Hochladen von Dateien

**Zweck:** Um den erfolgreichen Upload von Dateien mit FileSystemHandler zu testen.

**Testschritte:**

- Mock-Datei öffnen und PDF zu Dokument Vektor-Konvertierung.

- Versuchen Sie, Dateien für einen bestimmten Benutzer hochzuladen.

**Erwartete Ergebnisse:** Der Datei-Upload-Prozess sollte korrekt aufgerufen werden und zugehörige Funktionen wie das Öffnen und Konvertieren von Dateien sollten aufgerufen werden.

**Pass/Fail Kriterien:** Übergibt, wenn alle Mock-Funktionen während des Datei-Upload-Prozesses wie erwartet aufgerufen werden.

#### 4.3 Testfall: Löschen von Dateien

**Zweck:** Um sicherzustellen, dass FileSystemHandler eine Datei korrekt aus dem Dateisystem löschen kann.

**Testschritte:**

- Mock-Datei Existenz und Löschung.

- Versuchen Sie, eine angegebene Datei zu löschen.

**Erwartete Ergebnisse:** Das Dateisystem sollte die Existenz der Datei&#39 bestätigen und dann löschen.

**Pass/Fail Kriterien:** Bestanden, wenn die Datei korrekt als vorhanden identifiziert und dann gelöscht wurde.

#### 4.4 Testfall: Abrufen von Dateisystem für Benutzer

**Zweck:** Überprüfen der Funktionalität des Abrufs eines Dateisystems des Benutzers's, einschließlich Dateinamen und Metadaten.

**Testschritte:**

- Mock-Datei Auflistung, Größe Abruf und zuletzt geändert Datum.

- Abrufen des Dateisystems für einen bestimmten Benutzer.

**Erwartete Ergebnisse:** Die Dateisysteminformationen sollten die angedeuteten Dateidetails genau wiedergeben.

**Pass/Fail-Kriterien:** Bestanden, wenn die zurückgegebenen Dateisysteminformationen mit den erwarteten Daten übereinstimmen.

#### 4.5 Testfall: Dokumentennamen bearbeiten

**Zweck:** Testen der Fähigkeit von FileSystemHandler, ein Dokument umzubenennen.

**Testschritte:**

- Mock-Datei Existenz und Umbenennung.

- Versuchen Sie, ein Dokument umzubenennen.

**Erwartete Ergebnisse:** Das Dokument sollte korrekt identifiziert und wie angegeben umbenannt werden.

**Pass/Fail Kriterien:** Bestanden, wenn die Datei erfolgreich umbenannt wurde.

#### 4.6 Testfall: Abrufen des Dokumentpfads

**Zweck:** Um sicherzustellen, dass der korrekte Dateipfad für ein bestimmtes Dokument abgerufen wird.

**Testschritte:**

- Mock File Existenz.

- Rufen Sie den Pfad eines bestimmten Dokuments ab.

**Erwartete Ergebnisse:** Der korrekte Dateipfad sollte für das angegebene Dokument zurückgegeben werden.

**Pass/Fail Kriterien:** Bestanden, wenn der abgerufene Pfad dem erwarteten Pfad entspricht.

#### 4.7 Testfall: Überprüfen der Dateisystemexistenz

**Zweck:** Um zu überprüfen, ob FileSystemHandler ein Dateisystemverzeichnis von user's korrekt überprüfen und erstellen kann, wenn es nicht vorhanden ist't.

**Testschritte:**

- Mock-Verzeichnis Existenz und Erstellung.

- Überprüfen Sie die Existenz eines user's Dateisystems.

**Erwartete Ergebnisse: Das Verzeichnis sollte erstellt werden, wenn es nicht vorhanden ist't**

**Pass/Fail Kriterien:** Übergibt, wenn das Verzeichnis erstellt wird, wenn es nicht vorhanden ist.

#### 4.8 Testfall: Konvertieren von Bytes in ein lesbares Format

**Zweck:** Testen der Umwandlung von Byte-Größen in ein für Menschen lesbares Format.

**Testschritte:**

- Konvertieren Sie verschiedene Byte-Größen in lesbare Formate.

**Erwartete Ergebnisse:** Jede Bytegröße sollte in das korrekte lesbare Format konvertiert werden.

**Pass/Fail Kriterien:** Durchläuft, wenn alle Byte-Größen korrekt konvertiert werden.

#### 4.9 Testfall: Datum der letzten Änderung der Datei 

**Zweck:** Um sicherzustellen, dass das letzte Änderungsdatum einer Datei genau abgerufen werden kann.

**Testschritte:**

- Mock file stat, um einen zuletzt geänderten Zeitstempel bereitzustellen.

- Abrufen des letzten Änderungsdatums einer Datei.

**Erwartete Ergebnisse:** Das zuletzt geänderte Datum sollte dem angedeuteten Zeitstempel entsprechen.

**Pass/Fail Kriterien:** Bestanden, wenn das abgerufene Datum dem erwarteten Wert entspricht.

### Mock Objects und Testdaten

**Mock Files:** Mock-Objekte, die Dateien zum Testen von Dateioperationen simulieren.

**Mock File System:** Mocked Dateisystemfunktionen wie Dateiexistenz, Löschung und Metadatenabruf.

### Testergebnis für Testfall 4

![Testergebnis für Testfall 4](Testbericht_TF4.jpg)

# 5. Qualitätssicherung

Unsere Testhierarchie ist in drei Ebenen gegliedert, wobei 90% Unittests, 8% Integrationstests und 2% Softwarequalitätstests sind. Softwarequalitätstests, wie beispielsweise die simultane Anmeldung einer hohen Anzahl von Benutzern, sind umfangreiche Tests, die in unserem Rahmen nicht durchführbar sind und üblicherweise von größeren Unternehmen umgesetzt werden. Diese Einschränkungen spiegeln die Skalierbarkeit und Ressourcen eines kleineren Projektes wider.

Die Dokumentation dient als Leitfaden für aktuelle und zukünftige Entwickler und Tester, um die Qualität der Backend-Funktionen zu gewährleisten und zu überprüfen, dass alle Funktionen den Standards entsprechen. 