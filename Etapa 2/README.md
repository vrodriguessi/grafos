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

### Etapa 2 - Solução Inicial

Nesta segunda etapa do projeto, foi desenvolvido um **algoritmo construtivo** para gerar uma **solução inicial** viável para o problema de roteamento com restrições apresentado na Etapa 1.

Um algoritmo construtivo parte de uma solução vazia e, a partir de critérios definidos, constrói iterativamente uma solução completa e factível, respeitando as restrições operacionais do problema.

---


## 🎯 Objetivo

O objetivo principal desta etapa é produzir soluções iniciais que:

✅ Atendam todas as demandas obrigatórias do grafo;

✅ Não ultrapassem a capacidade dos veículos em cada rota;

✅ Atribuam cada serviço a exatamente uma rota;

✅ Não dupliquem o custo ou demanda de um serviço, mesmo que ele seja percorrido mais de uma vez.

---

## 🔧 Funcionalidades Implementadas - Algoritmo Construtivo baseado na heurística **Path Scanning**

O algoritmo implementado na Etapa 2 segue os seguintes princípios:

📥 Inicia com uma solução vazia;

🔄 Iterativamente seleciona os serviços a serem atendidos;

🧩 Agrupa os serviços em rotas respeitando a capacidade dos veículos;

🔁 Se um arco, aresta ou vértice for visitado mais de uma vez, a demanda e custo associados ao serviço são contabilizados apenas uma vez;

✅ Ao final, é garantido que todas as restrições do problema estão sendo respeitadas.

---

## 🚀 Como Usar?

### ▶️ Execução
Para rodar o algoritmo e gerar uma solução:

```bash
python main.py nome_instancia.dat`
```
### 💾 Saída
As soluções geradas são salvas no diretório **Solucoes** no formato padrão especificado pelo professor, com o seguinte formato de nome:

```bash
sol-nomeinstancia.dat
```

### ✅ Informações presentes no arquivo de solução:
- Custo total da solução

- Número total de rotas

- Total de clocks para a execução do algoritmo de referência

- Total de clocks para encontrar a melhor solução encontrada (referência)

### 🔧 Estrutura de cada rota:

```bash
índice_do_depósito dia_da_roteirização identificador_da_rota demanda_total_da_rota custo_total_da_rota total_de_visitas (X i,j,k) ...
```
- índice_do_depósito: sempre 0

- dia_da_roteirização: sempre 1

- identificador_da_rota: inicia em 1 e incrementa para cada rota

- demanda_total_da_rota: soma das demandas dos serviços na rota

- custo_total_da_rota: soma dos custos dos deslocamentos e atendimentos

- total_de_visitas: quantidade total de visitas realizadas (incluindo o depósito)

### 🔧 Formato das visitas:
- As visitas são representadas por triplas do tipo (X i,j,k), com o seguinte significado:
```bash
(D 0,1,1): visita ao depósito
(S id_serviço,extremidade1,extremidade2): visita a um serviço requerido
```
### Exemplos:
- 📌 Serviço 2 do arquivo BHW1.dat corresponde ao nó requerido:

```bash
N3 1 1
Representado na rota como: (S 2,3,3)
```
- 📌 Serviço 14 do arquivo BHW1.dat corresponde à aresta requerida:
```bash  
E7 7 8 8 1 9
Se percorrida de 7 para 8: (S 14,7,8)
```
- 📌 Serviço 26 do arquivo BHW1.dat corresponde ao arco requerido:
```bash  
A8 7 6 4 1 5
Se percorrido de 7 para 6: (S 26,7,6)
```
⚠️ Importante: Apenas visitas a serviços são registradas no detalhamento da rota — deslocamentos intermediários entre serviços ou retorno ao depósito não são listados como (S ...).

