import re
from src.Grafos import Grafo

def parse_arcos_obrigatorios(lines):
    arcos = []
    arc_section = False

    for line in lines:
        line = line.strip()

        if re.match(r'^ReA\.', line):
            arc_section = True
            continue
        elif line == "":
            arc_section = False
            continue

        if arc_section:
            parts = re.split(r'\s+', line)
            if len(parts) >= 4 and parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit():
                from_node = int(parts[1])
                to_node = int(parts[2])
                cost = int(parts[3])
                arcos.append((from_node, to_node, cost))

    return arcos

def parse_arcos_nao_obrigatorios(lines):
    arestas = []
    edge_section = False

    for line in lines:
        line = line.strip()

        if re.match(r'^ARC', line):
            edge_section = True
            continue
        elif line == "":
            edge_section = False
            continue

        if edge_section:
            parts = re.split(r'\s+', line)
            if len(parts) >= 4 and parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit():
                from_node = int(parts[1])
                to_node = int(parts[2])
                cost = int(parts[3])
                arestas.append((from_node, to_node, cost))

    return arestas

def parse_rees(lines):
    ree = []
    ree_section = False

    for line in lines:
        line = line.strip()

        if re.match(r'^ReE\.', line):
            ree_section = True
            continue
        elif line == "":
            ree_section = False
            continue

        if ree_section:
            parts = re.split(r'\s+', line)
            if len(parts) >= 4 and parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit():
                from_node = int(parts[1])
                to_node = int(parts[2])
                cost = int(parts[3])
                ree.append((from_node, to_node, cost))

    return ree

def parse_edges(lines):
    edges = []
    edge_section = False

    for line in lines:
        line = line.strip()

        if re.match(r'^EDGE', line):
            edge_section = True
            continue
        elif line == "":
            edge_section = False
            continue

        if edge_section:
            parts = re.split(r'\s+', line)
            if len(parts) >= 4 and parts[1].isdigit() and parts[2].isdigit() and parts[3].isdigit():
                from_node = int(parts[1])
                to_node = int(parts[2])
                cost = int(parts[3])
                edges.append((from_node, to_node, cost))

    return edges

def parse_ren(lines):
    ren = []
    ren_section = False

    for line in lines:
        line = line.strip()

        if re.match(r'^ReN\.', line):
            ren_section = True
            continue

        if re.match(r'^(ReE\.|ReA\.|EDGE|ARC)', line):
            ren_section = False

        if ren_section:
            parts = re.split(r'\s+', line)
            if len(parts) >= 1 and re.fullmatch(r'N\d+', parts[0]):
                node_number = int(parts[0][1:])
                ren.append(node_number)

    return ren

def calcular_num_vertices(ReA, ARC, ReE, EDGE, ReN):
    vertices = set()

    for u, v, _ in ReA + ARC + ReE + EDGE:
        vertices.add(u)
        vertices.add(v)

    vertices.update(ReN)

    return max(vertices) if vertices else 0

def parse_capacidade(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith("Capacity:"):
                capacidade = int(line.split(":")[1].strip())
                return capacidade
        return None 

    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
        return None
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_path}: {e}")
        return None

def parse_file_into_grafo(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        ReA = parse_arcos_obrigatorios(lines)     # ReA.
        ARC = parse_arcos_nao_obrigatorios(lines) # ARC
        ReE = parse_rees(lines)                   # ReE.
        EDGE = parse_edges(lines)                 # EDGE
        ReN = parse_ren(lines)                    # ReN.

        num_vertices = calcular_num_vertices(ReA, ARC, ReE, EDGE, ReN)

        grafo = Grafo(num_vertices)

        for u, v, custo in ReA:
            grafo.adicionar_arco_obrigatorio(u, v, custo, demanda=0)

        for u, v, custo in ReE:
            grafo.adicionar_aresta_obrigatoria(u, v, custo, demanda=0)

        for u, v, custo in ARC:
            grafo.adicionar_arco_nao_obrigatorio(u, v, custo, demanda=0)

        for u, v, custo in EDGE:
            grafo.adicionar_aresta_nao_obrigatoria(u, v, custo, demanda=0)

        for no in ReN:
            grafo.adicionar_no_obrigatorio(no)
        
        capacidade = parse_capacidade(file_path)
        grafo.capacidade = capacidade

        return grafo

    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_path}: {e}")
        return None
