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

## 🎯 Definição do Problema

O projeto busca solucionar problemas de logística utilizando conceitos de grafos. Imagine uma cidade onde diversas mercadorias precisam ser entregues em diferentes pontos. As ruas conectam esses locais, mas algumas vias têm restrições ou custos diferentes para o transporte. O objetivo é encontrar a melhor maneira de organizar essas entregas para minimizar o custo e garantir que todas as demandas sejam atendidas.

Neste contexto, um grafo é utilizado para representar as interseções e vias da região, onde cada ponto representa um local e cada conexão entre eles é uma rua ou avenida. Algumas dessas vias têm demandas específicas, ou seja, devem obrigatoriamente ser percorridas para realizar as entregas. O desafio é planejar rotas eficientes considerando restrições como custos, direção das vias e capacidade dos veículos.

Este projeto se propõe a modelar e resolver esse tipo de problema, aplicando algoritmos que auxiliam na identificação das melhores soluções para diferentes cenários de transporte e distribuição.

---

## 📌 Sobre o Projeto

Este projeto tem como objetivo a manipulação e análise de **grafos aplicados a problemas de logística**, focando especialmente no pré-processamento dos dados.

### Etapa 1 - Pré-processamento dos dados

Na **Etapa 1**, o sistema realiza a leitura de instâncias no formato `.dat`, constrói a estrutura do grafo e extrai métricas e estatísticas relevantes que podem auxiliar na resolução de desafios logísticos, como o planejamento de rotas e a análise de conexões.

Além disso, o projeto conta com uma visualização gráfica interativa por meio de **Jupyter Notebooks**, permitindo que os usuários explorem visualmente a estrutura da rede. Isso facilita a análise das rotas de forma mais intuitiva e dinâmica, promovendo insights mais claros sobre os dados processados.

### Etapa 2 - Solução Inicial

Na **Etapa 2** do projeto, foi desenvolvido um algoritmo construtivo com base na heurística **Path Scanning** para gerar uma solução inicial viável para o problema de roteamento com restrições. 
O algoritmo constrói rotas partindo de uma solução vazia e adicionando serviços de forma iterativa, garantindo que cada serviço seja atendido por apenas uma rota e que nenhuma rota exceda a capacidade dos veículos. Caso um serviço seja visitado mais de uma vez, sua demanda e custo são contabilizados apenas uma vez. 
As soluções geradas seguem um formato padronizado, incluindo informações detalhadas como custo total, número de rotas, tempo de execução e a sequência de visitas em cada rota.

---

## 🔧 Funcionalidades Implementadas

- ✔ Leitura e interpretação de arquivos `.dat`
- ✔ Construção e visualização de grafos
- ✔ Cálculo de estatísticas do grafo
- ✔ Visualização com Jupyter Notebook
- ✔ Algoritmo baseado na heurística `Path Scanning` para geração de soluções iniciais
- ✔ Geração de arquivos de solução formatados conforme padrão da disciplina

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
│
├── 📁 Etapa 1/
│   ├── 📁 data/
│   │   └── 📁 selected_instances/         # Instâncias de entrada no formato .dat
│   ├── 📁 src/
│   │   ├── 📁 algorithms/
│   │   │   ├── 📄 estatisticas.py         # Cálculo de métricas do grafo
│   │   │   └── 📄 floyd_warshall.py       # Algoritmo de caminhos mínimos
│   │   ├── 📁 models/                     
│   │   ├── 📁 utils/                      # Funções auxiliares
│   │   │   ├── 📄 leitura_dados.py        # Parser de instâncias .dat
│   │   │   ├── 📄 visualizacao.py         # Visualização interativa dos grafos
│   │   │   └── 📄 visualizacao_matrizes.py
│   │   └── 📄 Grafos.py                   # Classe `Grafo` com representação e métodos
│   ├── 📄 main.py                         # Execução da Etapa 1
│   ├── 📄 processamento_grafos_com_visualizacao.ipynb  # Notebook com análise visual
│   └── 📄 README.md                       # Descrição da Etapa 1
│
├── 📁 Etapa 2/
│   ├── 📁 MCGRP/                          # Instâncias e arquivos de entrada
│   ├── 📁 Solucoes/                       # Soluções geradas 
│   ├── 📁 src/
│   │   ├── 📁 algorithms/                 
│   │   │   ├── 📄 floyd_warshall.py       # Reutilização do algoritmo de caminhos mínimos
│   │   │   └── 📄 path_scanning.py        # Algoritmo construtivo (Path Scanning)
│   │   ├── 📁 models/                     
│   │   ├── 📁 utils/
│   │   │   ├── 📄 leitura_dados.py        # Leitura das instâncias de teste da Etapa 2
│   │   │   ├── 📄 imprimir_resultados.py  # Impressão da solução no formato exigido
│   │   └── 📄 Grafos.py                   # Estruturas e utilidades de grafo
│   ├── 📄 main.py                         # Execução da Etapa 1
│   └── 📄 README.md                       # Descrição da Etapa 2
│
└── 📄 README.md                           # README geral do projeto


```
---
## 💬 Considerações Finais
Este projeto representa o nosso esforço em aplicar, na prática, os conceitos aprendidos ao longo da disciplina de Grafos. Exploramos algoritmos clássicos e estruturas fundamentais para solucionar um problema real de logística, unindo teoria e prática em um trabalho significativo.

Acreditamos que este tipo de aplicação contribui não apenas para a compreensão dos grafos, mas também para a construção de soluções inteligentes e eficientes no mundo real.



