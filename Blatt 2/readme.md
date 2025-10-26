# Aufgabe 1/2:
## 8 Queens:
Das Problem wird von den Individuen wie folgt beschrieben:  
Alle Positionen der Damen werden in einem Array gespeichert, der Index beschreibt die Spalte und die Zahl am bestimmten Index beschreibt die Reihe, in der die Dame steht.
Die indizes, welche die Zeile der Dame beschreiben befinden sich im Raum 0-7, um den Indizes des Arrays zu ähneln, und um im Binärstring von 000 bis 111 dargestellt werden zu können, was das Crossover erleichtert.
Die Fitnessfunktion liefert einen Wert von 0 bis 56 entsprechend der Konflikte, die eine Lösung aufweist, pro Konflikt wird ein Punkt der Fitness abgezogen. Um die Lösungen zu weiterzuentwickeln habe ich mich für Crossover entschieden, da in den Bits leicht Grenzen gezogen und vertauscht werden kann. 


## Parameter:
Stichprobenmenge = 400 Durchläufe

### Unterschiedliche Populationsmengen:
##### population = 500, max_generations = 50, tournament_size = 10, pcross = 0.8:
AES: ~7.39  
SR: ~0.312

##### population = 250, max_generations = 50, tournament_size = 10, pcross = 0.8:
AES: ~8.77  
SR: ~0.175

##### population = 100, max_generations = 50, tournament_size = 10, pcross = 0.8:
AES: ~9.58  
SR: 0.065



### Unterschiedliche maximale Anzahl an Generationen:
##### population = 100, max_generations = 200, tournament_size = 10, pcross = 0.8:
AES: ~22.15  
SR: ~0.082

##### population = 100, max_generations = 400, tournament_size = 10, pcross = 0.8:
AES: ~77.23  
SR: ~0.085



### Unterschiedliche Turniergrößen:
##### population = 500, max_generations = 50, tournament_size = 20, pcross = 0.8:
AES: ~7.53  
SR: ~0.282

##### population = 500, max_generations = 50, tournament_size = 50, pcross = 0.8:
AES: ~8.82  
SR: ~0.2175




### Unterschiedliche Kreuzungswahrscheinlichkeiten:
##### population = 500, max_generations = 50, tournament_size = 10, pcross = 0.6:
AES: ~9.01  
SR: ~0.275

##### population = 500, max_generations = 50, tournament_size = 10, pcross = 0.9:
AES: ~7.95  
SR: ~0.385  

## Fazit:
Aus den Daten wird klar, dass vor allem die Population den Unterschied in der Erfolgsrate macht. Bei kleinerer Populationsgröße bestehen insgesamt weniger Möglichkeiten zum Kreuzen von Lösungen, ein defizit, was mehr Generationen nicht ausgleichen können.
Den geringsten Einfluss auf die Resultate hat die Turniergröße, und die Kreuzungswahrscheinlichkeit, was Sinn macht, da der durchschnittliche Durchlauf des Algorithmus schon nach 7-9 Generationen terminiert und beide Funktionen nur kleine, indirekte Effekte auf die Population haben.
Es scheint, als wären in meiner Implementation die besten Werte eine Populationsgröße von >500 eine maximale Laufzeit von rund 100 Generationen und einer Turniergröße von ca. 10.  
Die besten Ergebnisse habe ich erzielt, wenn ich das Kreuzen der Eltern mit einer Mutation der Kinder verbunden habe. Ich habe den erstellten pool an Kindern, jeweils mit der Mutationswahrscheinlichkeit 1/Länge des Bitstrings, mutieren lassen und konnte so die Erfolgsrate des Algorithmus auf über 92% steigern, bei einer durchschnittlichen Generationenzahl von ca. 79.  
(population=100, max_generations=500, tournament_size=10, pcross=0.8, pmut=1/24).



## Landkarten Einfärben:
Um das Problem zu lösen habe ich den Algorithmus vom 8 Damen Problem übernommen und die Fitnessfunktion angepasst, um die Anforderungen aus dem Constraint-Graphen abzubilden. Für jede richtige Farbanordnung wird der Fitness-Score um 3 erhöht, und für jede verwendete Farbe wird ein Punkt abgezogen. Wie oben sind verschiedenen Farben als Zahlen kodiert, im Bitstring belegt eine Zahl drei Bits und kann daher die Zahlen von 0 bis 7 (8 Farben) darstellen.

## Parameter:
Stichprobenmenge = 5000

### Unterschiedliche Populationsmengen:
##### population = 100, max_generations = 500, tournament_size = 10, pcross = 0.8:
AES: ~2.04  
SR: 1.0

##### population = 10, max_generations = 500, tournament_size = 5, pcross = 0.8:
AES: ~42.65  
SR: ~0.862


## Fazit:
Diese guten Werte lassen sich hauptsächlich auf die Verwendung von 8 verschieden möglichen Farben, und die einfachere Natur des Problems zurückführen. Es wird nach einer bestimmten Anordnung dreier Zahlen gesucht, was bei hohen Populationsmengen schon schnell in der Starteingabe enthalten ist.  
Ich habe auch hier das Mutieren der Kinder probiert. Hier konnte ich die Werte des 2. Beispiel von oben (population = 10, max_generations = 500, tournament_size = 5, pcross = 0.8, pmut=1/18) auf eine durchschnittliche Generationenzahl bis zur Lösung von ~13.87 und eine Erfolgsrate von 100 % Steigern.

## Simulated Annealing:
Um die Probleme mit Simulated Annealing lösen zu können, bräuchte man jeweils Abkühlungspläne, die an das jeweilige Problem angepasst sind, um das "festsetzen" in lokalen Maxima der Kostenfunktion (Fitnessfunktion) zu verhindern. 



# Aufgabe 3:

## Randal Olsons "Heres Waldo":
In dem gegebenen GitHub Repo habe ich mir den genetischen Algorithmus im Jupyter-Notebook angeschaut. Ein Individuum beschreibt hier einen Weg zwischen allen 68 Datenpunkten, die Fitnessfunktion berechnet den gesamtweg zwischen allen Punkten der Lösung, da hier nach dem kürzesten Weg gesucht wird, soll der Fitness-Wert so klein wie möglich sein. Er verwendet zwei arten von Mutationen: Eine Gen-Mutation, in der 1 bis 3 Anordnungen an Wegen verändert werden und eine Shuffle-Mutation, in der ein zufälliger Teil des Weges an eine andere Stelle im Pfad verschoben wird.
Die Gen-Mutation ist hier vergleichbar mit meiner Mutation, während die Shuffle-Mutation ähnlich zu Crossover mutation ist.


## Evolution Simulator:
Ein Individuum besteht aus Muskeln und Knoten. Die Muskeln haben verschiedenen Längen (Angespannt und Entspannt) und haben verschiedenen Zeiten zu denen sie sich Ent- oder Anspannen. Sie üben eine Kraft auf die Knoten aus, die sich dadurch bewegen. Die Individuen werden nach zurückgelegter Distanz innerhalb von 15 Sekunden bewertet. Eine Mutation kann eine Änderung der Muskelparameter, das Löschen eines Muskels oder eines Knotens, sowie das Hinzufügen von Knoten oder Muskeln sein.


## American Fuzzy Lop:
Die Website hat leider auf allen möglichen Geräten nicht funktioniert.
