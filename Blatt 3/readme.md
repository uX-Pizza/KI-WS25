# Aufgabe 1:
## 1.1:
Werte der Knoten:  
B = 3  
E = 9  
F = 2  
G = 6  
C = 2  
D = 1  
A = 3

## Aufgabe 1.2:
(Siehe 01_05_trees.jpg)

## Aufgabe 1.3:
Eine andere Anordnung würde hier keinen Unterschied machen, da durch B und E bereits die niedrigsten Grenzen festgelegt werden, und so bereits die meist möglichen Knoten abgeschnitten werden.


# Aufgabe 2/3:
(Siehe 02_minimax.py)

Ohne Pruning durchläuft der Algorithmus 740.170 Knoten, mit Pruning 14.506 Knoten


# Aufgabe 4:
  
| x | x | x |  
| o | o | - |  
| - | - | - |  
Eval = 1

| o | - | x |  
| x | o | - |  
| x | - | o |  
Eval = -1

| x | o | x |  
| o | x | o |  
| o | x | o |  
Eval = 0

| x | x | - |  
| o | o | x |  
| - | - | - |  
Eval = 3 * 1 + 1 - (3 * 1 + 0) = 1

| x | o | - |  
| o | o | x |  
| - | x | - |  
Eval = 3 * 0 + 3 - (3 * 1 + 1) = -1

| o | x | - |  
| o | o | x |  
| x | x | - |  
Eval = 3 * 1 + 2 - (3 * 1 + 1) = 1

Eine solche Evaluierungsfunktion könnte sinnvoll sein, da sie gegebenenfalls vorliegende Vorteile für den einen oder anderen Spieler heraushebt, und so im wechsel von Minimieren und Maximieren weniger Werte "verloren" gehen.

# Aufgabe 5:
(Siehe 01_05_trees.jpg)