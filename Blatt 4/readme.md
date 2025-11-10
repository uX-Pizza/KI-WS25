# Aufgabe 1:


| Nr. | Alter      | Einkommen | Bildung  | Kandidat |
|:----|:-----------|:----------|:---------|:---------|
| 1   | $`\ge 35`$ | hoch      | Abitur   | O        |
| 2   | $`< 35`$   | niedrig   | Master   | O        |
| 3   | $`\ge 35`$ | hoch      | Bachelor | M        |
| 4   | $`\ge 35`$ | niedrig   | Abitur   | M        |
| 5   | $`\ge 35`$ | hoch      | Master   | O        |
| 6   | $`< 35`$   | hoch      | Bachelor | O        |
| 7   | $`< 35`$   | niedrig   | Abitur   | M        |

S1 = 4; S2 = 0,7

### Alter:
$`\ge 35`$: 1, 3, 4, 5 (O, M, M, O)  
O/M -> 0,5  
H = -1

$`< 35`$: 2, 6, 7 (O, O, M)  
O-> 0,66  
H = 0,918

Gain = 0,019


### Einkommen:
Hoch: 1, 3, 4, 6 (O, M, O, O)  
O -> 0,75  
H = 0,811

Niedrig: 2, 4, 7 (O, M, M)
M -> 0,67  
H = 0,918

Gain = 0,129

### Bildung:
Abitur: 1, 4, 7 (O, M, M)
M -> 0,66  
H = 0,918

Bachelor: 3, 6 (M, O)
O/M -> 0,5  
H = 1

Master: 2, 5 (O, O)
o -> 1  
H = 0

Gain = 0,304

____
M = 3/7;  
O = 4/7
Entropie = 0,985

Die Besten Informationen sind in den Daten der Bildung enthalten


# Aufgabe 2:

x3(x2(x1(C, A), x1(B, A)), x1(x2(C, B), A))  
->  
x1(x2(C, B), A)

Regeln: Transformation, Vereinfachung


# Aufgabe 3:
## 1:
### Restaurant:
Fehlerrate = 25%
Die Confusion Matrix sagt aus, dass zu wenig Werte zur verfügung stehen und so nicht genug Informationen vorliegen um alle Randfälle einordnen zu können

### Zoo:
Fehlerrate = 0,9901%
Confusion Matrix: Nur das Reptil wird als Amphibie Klassifiziert

## 2:
Nominale Attribute: Angegebene Menge an Werten
String Attribute: Strings
Numeric Attribute: Zahlen

## 3:
Der Baum für den Zoo ist gleich geblieben, der Restaurant-Baum ist jedoch nur noch 3 Kanten für (None, Some, Full)
Die Fehlerrate ist auf rund 16% gesunken.

### ID3:
ID3 Schein geeigneter für dieses Problem zu sein, mein erstellter Baum hat eine 100%ige genauigkeit.