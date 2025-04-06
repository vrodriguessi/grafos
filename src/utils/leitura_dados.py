import re

def parse_arcos(lines):
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

def parse_arestas(lines):
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
        elif line == "":
            ren_section = False
            continue

        if ren_section:
            parts = re.split(r'\s+', line)
            if len(parts) >= 1 and re.match(r'^N\d+$', parts[0]):
                node_number = int(parts[0][1:])  # Remove o "N" e converte para inteiro
                ren.append(node_number)

    return ren

def parse_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        ReA = parse_arcos(lines)     # ReA.
        ARC = parse_arestas(lines) # ARC
        ReE = parse_rees(lines)        # ReE.
        EDGE = parse_edges(lines)      # EDGE
        ReN = parse_ren(lines)         # ReN.

        return ReA, ARC, ReE, EDGE, ReN

    except FileNotFoundError:
        print(f"Erro: O arquivo {file_path} não foi encontrado.")
        return [], [], [], [], []
    except Exception as e:
        print(f"Erro ao processar o arquivo {file_path}: {e}")
        return [], [], [], [], []
