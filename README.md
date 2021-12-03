# Advent-Pi

## Schritt 1 -  Materialliste:
- 1x Relais (Empfohlen: Low-Level-Trigger Relais)
- 1x Raspberry Pi 3b+
- 1x Bewegungsmelder KY032
- 1x Lichterkette
- 6x Jumper-Kabel

## Schritt 2 - Sensor
Der Sensor erkennt, wann eine Person an unserem Weihnachtsbaum vorbeigeht. Dann wird ein Signal an Pin 24 gesendet, worauf unser Programm reagiert. Um unseren Sensor mit Strom zu versorgen, wird der Anschluss "+" des Sensors mit dem passenden 3.3 Volt PWR-Anschluss auf dem Raspberry Pi verbunden. Des Weiteren wird zur Stromversorgung des Sensors der "GND" also Ground/-Erdung Anschluss mit einem beliebigen GND Steckplatz des Pis verbunden.

## Schritt 3 - Relais
Das Relais wird über den 5V Pin und einem Ground Pin mit Strom versorgt. Der Input Pin am Relais dient zum Schalten.
Der Pin 15 sendet ein Signal um den Relais zu schaltet.
Das Stromkabel vom Weihnachtsbaum wird an der Stelle wie im Bild gezeigt geteilt und mit dem Relais zusammengeführt.
Befinden sich die Kabel in COM (Common) und NO (Normally open) ist der Stromkreis offen und die Lichterkette ist ausgeschaltet. Sendet der Pin 15 ein Signal würde der Stromkreis schließen und schaltet die Lichterkette an.
Befinden sich die Kabel in COM und NC (Normally closed) ist der Stromkreis geschlossen und die Lichterkette leuchtet.

## Schritt 4 - Der Code
Erstelle eine Datei mit dem Namen "main.py" --> nano main.py.
Kopiere den folgenden Code hinein: [Advents-Pi](https://github.com/talentpierre/adventspi/blob/main/main.py)

## Schritt 5 - Code Ausführen
Führe den Code mit python3 main.py aus.
