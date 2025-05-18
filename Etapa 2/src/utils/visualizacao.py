import matplotlib.pyplot as plt
import math
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

def desenhar_grafo(grafo, titulo="Visualização do Grafo"):
    num_vertices = grafo.num_vertices
    angulo = 2 * math.pi / num_vertices

    posicoes = {
        i + 1: (
            math.cos(i * angulo),
            math.sin(i * angulo)
        )
        for i in range(num_vertices)
    }

    fig, ax = plt.subplots(figsize=(8, 8))

    for v, (x, y) in posicoes.items():
        cor = 'mediumpurple' if v in grafo.ReN else 'deepskyblue'
        ax.plot(x, y, 'o', markersize=12, color=cor, zorder=2)
        ax.text(x, y + 0.08, str(v), ha='center', va='center', fontsize=10, weight='bold')

    for (u, v, custo, _) in grafo.ReE + grafo.EDGE:
        x1, y1 = posicoes[u]
        x2, y2 = posicoes[v]
        ax.plot([x1, x2], [y1, y2], 'k-', linewidth=1.5, alpha=0.6, zorder=1)
        xm, ym = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(xm, ym, str(custo), color='dimgray', fontsize=9, ha='center', va='center')

    for (u, v, custo, _) in grafo.ReA + grafo.ARC:
        x1, y1 = posicoes[u]
        x2, y2 = posicoes[v]
        dx, dy = x2 - x1, y2 - y1
        ax.arrow(
            x1, y1, dx * 0.85, dy * 0.85,
            head_width=0.05, head_length=0.1,
            length_includes_head=True,
            fc='forestgreen', ec='forestgreen', linewidth=1.2, zorder=1
        )
        xm, ym = x1 + dx * 0.5, y1 + dy * 0.5
        ax.text(xm, ym, str(custo), color='firebrick', fontsize=9, ha='center', va='center')


    legenda = [
        mpatches.Patch(color='mediumpurple', label='Vértice relevante (ReN)'),
        mpatches.Patch(color='deepskyblue', label='Vértice comum'),
        mlines.Line2D([], [], color='black', label='Aresta não direcionada (ReE / EDGE)'),
        mlines.Line2D([], [], color='forestgreen', marker='>', markersize=7, linestyle='-', label='Aresta direcionada (ReA / ARC)'),
        mpatches.Patch(color='dimgray', label='Custo de aresta não direcionada'),
        mpatches.Patch(color='firebrick', label='Custo de aresta direcionada')
    ]

    ax.legend(
        handles=legenda,
        loc='upper left',
        bbox_to_anchor=(-0.3, 1.15),
        fontsize=9,
        frameon=True
    )

    ax.set_aspect('equal')
    ax.axis('off')
    plt.title(titulo, fontsize=14, weight='bold')
    plt.tight_layout()
    plt.subplots_adjust(top=0.85)
    plt.show()