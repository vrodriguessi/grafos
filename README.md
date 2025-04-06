<p align="center">
  <img src="https://img.icons8.com/fluency/96/graph.png" width="100" alt="Logo do Projeto"/>
</p>

<h1 align="center">🚀 Projeto de Grafos para Problemas de Logística</h1>

<p align="center">
  <i>Disciplina: GCC262 - Grafos e suas Aplicações</i><br>
  <i>Universidade Federal de Lavras (UFLA)</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-blue" alt="Status do Projeto"/>
  <img src="https://img.shields.io/badge/python-3.13.2-blue.svg" alt="Python Version"/>
</p>

---

## 👩‍💻 Equipe

- **Professor:** Mayron César de O. Moreira  
- **Alunas:** Érika Mara de Morais Machado e Veronica Rodrigues da Silva França

---

## 📌 Sobre o Projeto

### Etapa 1 - Pré-processamento dos dados

Este projeto tem como objetivo a manipulação e análise de **grafos aplicados a problemas de logística**, focando especialmente no pré-processamento dos dados.

Na **Etapa 1**, o sistema realiza a leitura de instâncias no formato `.dat`, constrói a estrutura do grafo e extrai métricas e estatísticas relevantes que podem auxiliar na resolução de desafios logísticos, como o planejamento de rotas e a análise de conexões.

Além disso, o projeto conta com uma visualização gráfica interativa por meio de **Jupyter Notebooks**, permitindo que os usuários explorem visualmente a estrutura da rede. Isso facilita a análise das rotas de forma mais intuitiva e dinâmica, promovendo insights mais claros sobre os dados processados.

---


## 🎯 Definição do Problema

O projeto busca solucionar problemas de logística utilizando conceitos de grafos. Imagine uma cidade onde diversas mercadorias precisam ser entregues em diferentes pontos. As ruas conectam esses locais, mas algumas vias têm restrições ou custos diferentes para o transporte. O objetivo é encontrar a melhor maneira de organizar essas entregas para minimizar o custo e garantir que todas as demandas sejam atendidas.

Neste contexto, um grafo é utilizado para representar as interseções e vias da região, onde cada ponto representa um local e cada conexão entre eles é uma rua ou avenida. Algumas dessas vias têm demandas específicas, ou seja, devem obrigatoriamente ser percorridas para realizar as entregas. O desafio é planejar rotas eficientes considerando restrições como custos, direção das vias e capacidade dos veículos.

Este projeto se propõe a modelar e resolver esse tipo de problema, aplicando algoritmos que auxiliam na identificação das melhores soluções para diferentes cenários de transporte e distribuição.

---

## 🔧 Funcionalidades Implementadas

- ✔ Leitura e interpretação de arquivos `.dat`
- ✔ Construção e visualização de grafos
- ✔ Cálculo de estatísticas do grafo
- ✔ Visualização com Jupyter Notebook

---

## 🚀 Como Usar?

### 📥 Instalação

Clone o repositório e acesse a pasta do projeto:

```bash
git clone https://github.com/vrodriguessi/grafos.git
cd grafos
```
---
## ▶️ Execução

Para executar a aplicação principal:
```bash
python main.py
```
---
## 📂 Estrutura do Projeto
```bash
📁 root/
├── 📁 data/
│   └── 📁 selected_instances/            # Instâncias em formato `.dat` com os dados de entrada
│       ├── 📄 BHW3.dat
│       ├── 📄 BHW4.dat
│       ├── 📄 BHW5.dat
│       ├── 📄 BHW6.dat
│       ├── 📄 BHW7.dat
│       ├── 📄 BHW8.dat
│       ├── 📄 BHW9.dat
│       └── 📄 BHW10.dat
│
├── 📁 src/
│   ├── 📁 algorithms/                    # Implementações dos algoritmos de grafos
│   │   ├── 📄 __init__.py
│   │   ├── 📄 estatisticas.py            # Estatísticas como grau, densidade, etc.
│   │   └── 📄 floyd_warshall.py          # Algoritmo de caminhos mínimos
│   │
│   ├── 📁 models/                        # (Reservado para estruturas futuras)
│   │   └── 📄 __init__.py
│   │
│   └── 📁 utils/                         # Funções auxiliares
│       ├── 📄 __init__.py
│       ├── 📄 leitura_dados.py           # Parser de arquivos `.dat`
│       └── 📄 visualizacao.py            # Visualização gráfica dos grafos
│
├── 📄 Grafos.py                          # Classe `Grafo` com representação e métodos
├── 📄 main.py                            # Script principal para execução dos testes
├── 📄 processamento_grafos_com_visualizacao.ipynb  # Notebook com visualizações interativas
└── 📄 README.md                          # Documentação do projeto

```
---
## 💬 Considerações Finais
Este projeto representa o nosso esforço em aplicar, na prática, os conceitos aprendidos ao longo da disciplina de Grafos. Exploramos algoritmos clássicos e estruturas fundamentais para solucionar um problema real de logística, unindo teoria e prática em um trabalho significativo.

Acreditamos que este tipo de aplicação contribui não apenas para a compreensão dos grafos, mas também para a construção de soluções inteligentes e eficientes no mundo real.



