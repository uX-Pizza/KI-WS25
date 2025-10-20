from graph import Node, Edge


# Implementation zur Tiefensuche
def dfs(start, end):
    dfs_stack = [start]
    explored = set()
    cycles = 0
    max_stack_size = 0

    while dfs_stack:
        cycles += 1
        if len(dfs_stack) > max_stack_size:
            max_stack_size = len(dfs_stack)
        curr = dfs_stack.pop()
        if curr == end:
            print(f"Found {end.name}\nCycles {cycles}, Max Stack Size {max_stack_size}")
            break
        else:
            explored.add(curr)
            dfs_stack.extend(i for i in curr.children if i not in explored and i not in dfs_stack)


# Implementation zur Breitensuche
def bfs(start, end):
    dfs_queue = [start]
    explored = set()
    cycles = 0
    max_stack_size = 0

    while dfs_queue:
        cycles += 1
        if len(dfs_queue) > max_stack_size:
            max_stack_size = len(dfs_queue)
        curr = dfs_queue.pop(0)
        if curr == end:
            print(f"Found {end.name}\nCycles {cycles}, Max Stack Size {max_stack_size}")
            break
        else:
            explored.add(curr)
            dfs_queue.extend(i for i in curr.children if i not in explored and i not in dfs_queue)


"""def astar(start, end):
    ordered_queue = [start]
    explored = set()
    cycles = 0
    max_queue_size = 0

    while ordered_queue:
        cycles += 1
        if len(ordered_queue) > max_queue_size:
            max_queue_size = len(ordered_queue)
        curr = ordered_queue.pop(0)"""

def astar(start, end):
    open_list = [start]
    explored = set()
    cycles = 0
    max_queue_size = 0

    # g-Werte (Kosten vom Start)
    g_score = {start: 0}
    # Pfadrekonstruktion
    came_from = {}

    while open_list:
        cycles += 1
        if len(open_list) > max_queue_size:
            max_queue_size = len(open_list)

        # Knoten mit minimalem f(n) = g(n) + h(n) auswählen
        """current = min(open_list, key=lambda n: g_score.get(n, float('inf')) + n.h)
        open_list.remove(current)"""
        open_list.sort(key= lambda x: (g_score.get(x, float('inf')) + x.h, x.name)) # Erst nach f(n), dann nach alphabetischer Reihenfolge sortieren
        current = open_list.pop(0)

        if current == end:
            # Pfad zurückverfolgen
            path = [current]
            total_cost = g_score[current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()

            print("A* found path:", " -> ".join(n.name for n in path))
            print(f"Total cost: {total_cost}")
            print(f"Cycles: {cycles}, Max Queue Size: {max_queue_size}")
            return path

        explored.add(current)

        # Alle Nachbarn untersuchen
        for neighbor in current.children:
            if neighbor in explored:
                continue

            # Verbindung (Edge) zwischen current und neighbor finden
            edge = next((e for e in current.connections if (e.a == neighbor or e.b == neighbor)), None)
            if edge is None:
                continue

            tentative_g = g_score[current] + edge.cost

            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                if neighbor not in open_list:
                    open_list.append(neighbor)

    print("A* found no path.")
    return None



if __name__ == '__main__':
    # Graph erstellen
    fra = Node("Frankfurt", 100)
    man = Node("Mannheim", 200)
    wur = Node("Würzburg", 170)
    stu = Node("Stuttgart", 300)
    kas = Node("Kassel", 460)
    kar = Node("Karlsruhe", 10)
    erf = Node("Erfurt", 400)
    nur = Node("Nürnberg", 537)
    aug = Node("Augsburg", 0)
    mun = Node("München", 0)

    fra_man = Edge("FraMan", 85, fra, man)
    fra.add_connection(fra_man)
    man.add_connection(fra_man)

    fra_wur = Edge("FraWur", 217, fra, wur)
    fra.add_connection(fra_wur)
    wur.add_connection(fra_wur)

    fra_kas = Edge("FraKas", 173, fra, kas)
    fra.add_connection(fra_kas)
    kas.add_connection(fra_kas)

    man_kar = Edge("ManKar", 80, man, kar)
    man.add_connection(man_kar)
    kar.add_connection(man_kar)

    wur_erf = Edge("WurErf", 186, wur, erf)
    wur.add_connection(wur_erf)
    erf.add_connection(wur_erf)

    wur_nur = Edge("WurNur", 103, wur, nur)
    wur.add_connection(wur_nur)
    nur.add_connection(wur_nur)

    nur_stu = Edge("NurStu", 183, nur, stu)
    nur.add_connection(nur_stu)
    stu.add_connection(nur_stu)

    kas_mun = Edge("KasMun", 502, kas, mun)
    kas.add_connection(kas_mun)
    mun.add_connection(kas_mun)

    kar_aug = Edge("KarAug", 250, kar, aug)
    kar.add_connection(kar_aug)
    aug.add_connection(kar_aug)

    nur_mun = Edge("NurMun", 167, nur, mun)
    nur.add_connection(nur_mun)
    mun.add_connection(nur_mun)

    aug_mun = Edge("AugMun", 85, aug, mun)
    aug.add_connection(aug_mun)
    mun.add_connection(aug_mun)

    # Suchalgorithmen mit Startpunkt Frankfurt und Endpunkt München ausführen
    dfs(fra, mun)
    bfs(fra, mun)

    # Achtung! Heuristik nur gültig für den Zielpunkt München

    astar(fra, mun)

    nur.h = 100

    astar(fra, mun)