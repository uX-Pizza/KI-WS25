# Bonus:

Beispiele für durch Computer- bzw. Robotereinsatz gelöste Probleme sind unter anderem die Luft- und Raumfahrt, da vor allem in der Raumfahrt zum Beispiel die Lagekontrolle von Satelliten und die Steuerung von Raketen komplett vollautomatisch funktionieren muss, da Menschen nicht in der Lage wären, schnell genug zu reagieren oder entscheidungen zu Treffen.

Gesellschaftlich wird sich in meinen Augen vor allem die Medienkompetenz verbessern müssen, wie zum Beispiel der Artikel "Mach dir selbst ein Video" der Zeit zeigt. In Zukunft werden KI-Generierte Bilder und Videos wahrscheinlich (vom Menschlichen Auge) nicht von echten unterschieden werden können. Ob sich die Gesellschaft durch die verschiedenen Effekte von KI negativ oder positiv verändert, lässt sich wahrscheinlich noch nicht sagen, allerdings bin ich der Meinung, dass man sich mit dem Thema ausseinander setzen muss, um negative Effekte (wie gefälschte Bilder oder Videos) zu erkennen und Maßnahmen dagegen treffen zu können.


# Aufgabe 1:


Startzustand: 3O 3E | 0O 0E (L)
Startzustand: 0O 0E | 3O 3E (R)

Graph: Siehe 01_Graph.png


# Aufgabe 2:

#### 1:
(Code in 02_Suchalgorithmen.py)
BFS: 3 Zyklen, Maximale Stack Größe 4
DFS: 8 Zyklen, Maximale Queue Größe 4
A* (Inkonsistent): 8 Zyklen, Maximale Queue Größe 4
A* (Konsistent): 3 Zyklen, Maximale Queue Größe 4

Man sieht hier, dass A* mit einer konsistenten Heuristik die besten Ergebnisse liefert, während BFS leicht besser als DFS arbeitet. Hier muss aber dazugesagt werden, dass BFS und DFS in ihrer Perfomance je nach Graph, sowie Start- und Zielknoten stark variieren können.

#### 2:
Die Heuristik ist so nicht zulässig, da der Weg von Nürnberg nach München deutlich überschätzt wird, was bedeutet, dass die Heuristik nicht konsistent ist (h(n) <= h*(n) ist nicht gegeben). Ich habe die Heuristik von 537Km auf 100Km verändert. Der Algorithmus findet zwar den selben Weg zum Ziel, beim ersten durchlauf allerdings in 8 Zyklen, während er mit der konsistenten Heuristik nur 3 Zyklen braucht.


# Aufgabe 3:

Eine Dominante Heuristik ist eine Heuristik, die in allen Wegschätzungen größer ist als die unterlegene Heuristik (Für alle n gilt: h1(n) > h2(n) --> h1 dominiert h2). Angenommen, dass beide Heuristiken konsistent sind, führt die dominante Heuristik durchschnittlich schneller zum Ziel als die unterlegene Heuristik, da sie genauere restkosten Schätzungen beinhaltet und f(n) so näher an die tatsächlichen Wegkosten g(Ziel) bringt. Der Algorithmus kann so Falsche verzweigungen vermeiden, und die Anzahl an Zyklen reduzieren.


# Aufgabe 4:

Gegeben sind 2 Endzustände A und B. Der tatsächliche Weg zu A ist günstiger gelegen als der Weg zu B (g(A) < g(B)) und die Heuristik ist konsistent. Durch die Konsistenz muss die Kostenfunktion kleiner oder gleich der tatsächlichen Wegkosten von n zu A sein (f(n) = g(n) + h(n) <= g(n) + h*(n) = g(A) = f(A)), da das Gleiche für B angewendet werden kann, bedeutet das f(A) < f(B), A wird also immer vor B erreicht, was bedeuten muss, dass A* optimal ist.