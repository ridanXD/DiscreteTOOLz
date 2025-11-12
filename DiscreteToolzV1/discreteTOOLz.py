import itertools
import math
import re
from collections import deque

print('''    ____  _                     __          __________  ____  __     
   / __ /(_)_________________  / /____     /_  __/ __ // __ // / ____
  / / / / / ___/ ___/ ___/ _ // __/ _ /     / / / / / / / / / / /_  /
 / /_/ / (__  ) /__/ /  /  __/ /_/  __/    / / / /_/ / /_/ / /___/ /_
/_____/_/____//___/_/   /___//__//___/    /_/  /____//____/_____/___/
                                                                     
       ___
 _   _<  /
/ / / / / 
/ // / /  
/___/_/   
          
''')

print("Follow more my project on GitHub: ridanXD")

def normalize(expr):
    return (
        expr.replace("->", "<=")
            .replace("<->", "==")
            .replace("&", " and ")
            .replace("|", " or ")
            .replace("~", " not ")
    )

def eval_logic(expr, values):
    expr = normalize(expr)
    for k, v in values.items():
        expr = expr.replace(k, str(v))
    return eval(expr)

def truth_table(expr):
    vars = sorted(set(re.findall(r"[A-Z]", expr)))
    rows = []
    for combo in itertools.product([True, False], repeat=len(vars)):
        m = dict(zip(vars, combo))
        result = eval_logic(expr, m)
        rows.append((combo, result))
    return vars, rows

def to_set(s):
    return set(s.split(","))

def power_set(s):
    lst = list(s)
    return [set(combo) for r in range(len(lst)+1) for combo in itertools.combinations(lst, r)]

def is_reflexive(R, A):
    return all((a, a) in R for a in A)

def is_symmetric(R):
    return all((b, a) in R for (a, b) in R)

def is_transitive(R):
    return all(((a, d) in R) for (a, b) in R for (c, d) in R if b == c)

def is_antisymmetric(R):
    return all(a == b or (b, a) not in R for (a, b) in R)

def is_injective(f):
    return len(set(f.values())) == len(f.values())

def is_surjective(f, codomain):
    return set(f.values()) == codomain

def P(n, r):
    return math.factorial(n) // math.factorial(n - r)

def C(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def bfs(graph, start):
    visited = []
    q = deque([start])
    while q:
        v = q.popleft()
        if v not in visited:
            visited.append(v)
            q.extend(graph[v])
    return visited

def dfs(graph, start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for n in graph[start]:
        if n not in visited:
            dfs(graph, n, visited)
    return visited

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def main():
    while True:
        print("""
=== Discrete TOOLz v1.0 ===
===   Made by ridanXD   ===
1. Logika: Evaluasi Proposisi
2. Logika: Tabel Kebenaran
3. Operasi Himpunan
4. Relasi & Fungsi
5. Kombinatorika
6. Graf
7. Aritmetika Modular
8. Keluar
""")

        p = input("Pilih: ")

        if p == "1":
            expr = input("Ekspresi: ")
            vars = sorted(set(re.findall(r"[A-Z]", expr)))
            values = {}
            for v in vars:
                values[v] = input(f"{v} (1/0): ") == "1"
            print("Hasil =", eval_logic(expr, values))

        elif p == "2":
            expr = input("Ekspresi: ")
            vars, rows = truth_table(expr)
            print(" | ".join(vars) + " || Hasil")
            for combo, result in rows:
                print(" | ".join(str(int(c)) for c in combo) + " || " + str(int(result)))

        elif p == "3":
            A = to_set(input("A (pisah koma): "))
            B = to_set(input("B (pisah koma): "))
            print("A ∪ B =", A | B)
            print("A ∩ B =", A & B)
            print("A - B =", A - B)
            print("B - A =", B - A)
            print("P(A) =", power_set(A))

        elif p == "4":
            print("1. Relasi")
            print("2. Fungsi")
            sub = input("Pilih: ")

            if sub == "1":
                A = to_set(input("Himpunan A: "))
                R_in = input("Relasi R (format a-b,a-c,...): ").split(",")
                R = {(r.split("-")[0], r.split("-")[1]) for r in R_in}
                print("Reflexive:", is_reflexive(R, A))
                print("Symmetric:", is_symmetric(R))
                print("Antisymmetric:", is_antisymmetric(R))
                print("Transitive:", is_transitive(R))

            elif sub == "2":
                f_in = input("Fungsi (a->1,b->2,...): ").split(",")
                f = {}
                for pair in f_in:
                    x, y = pair.split("->")
                    f[x] = y
                C = set(f.values())
                print("Injective:", is_injective(f))
                print("Surjective:", is_surjective(f, C))

        elif p == "5":
            n = int(input("n = "))
            r = int(input("r = "))
            print("Permutasi =", P(n, r))
            print("Kombinasi =", C(n, r))

        elif p == "6":
            g = {}
            nodes = input("Daftar node (pisah koma): ").split(",")
            for node in nodes:
                g[node] = input(f"Neighbor {node} (pisah koma): ").split(",")
            start = input("Mulai dari: ")
            print("BFS:", bfs(g, start))
            print("DFS:", dfs(g, start))

        elif p == "7":
            print("1. GCD")
            print("2. Invers Modulo")
            sub = input("Pilih: ")

            if sub == "1":
                a = int(input("a = "))
                b = int(input("b = "))
                print("GCD =", gcd(a, b))

            elif sub == "2":
                a = int(input("a = "))
                m = int(input("mod = "))
                print("Invers =", mod_inverse(a, m))

        elif p == "8":
            break

        else:
            print("Tidak valid\n")

main()
