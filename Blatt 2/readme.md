# Aufgabe 1:
## 8 Queens:
Das Problem wird von den Individuen wie folgt beschrieben:  
Alle Positionen der Damen werden in einem Array gespeichert, der Index beschreibt die Spalte und die Zahl am bestimmten Index beschreibt die Spalte, in der die Dame steht.
Die indizes, welche die Zeile der Dame beschreiben befinden sich im Raum 0-7, um den Indizes des Arrays zu ähneln, und um im Binärstring von 000 bis 111 dargestellt werden zu können, was das Crossover erleichtert.


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
