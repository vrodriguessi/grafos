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

## 🏁 Etapa 3 - Otimização da Solução

A partir da solução inicial gerada na Etapa 2, aplicamos uma heurística de melhoria local baseada no **2-opt**, buscando otimizar a sequência dos serviços dentro de cada rota, visando reduzir o custo total sem violar as restrições do problema.

### 🔧 Funcionamento da Otimização

- Após a geração das rotas pelo **Path Scanning**, cada rota é submetida ao algoritmo **2-opt**, que tenta melhorar a ordem de visita dos serviços, eliminando cruzamentos e percursos desnecessários.
- O **2-opt** realiza trocas de pares de arestas dentro da mesma rota, mantendo a viabilidade da solução.
- Essa otimização reduz o custo total das rotas, resultando em soluções mais eficientes.

---

## 🎯 Objetivos da Etapa 3

✅ Reduzir o custo total da solução inicial  
✅ Manter a viabilidade das rotas (sem exceder a capacidade dos veículos)  
✅ Preservar o atendimento de todos os serviços obrigatórios  
✅ Aumentar a qualidade da solução com baixo custo computacional  

---

## 🔧 Funcionalidades Implementadas

- 📥 Geração de solução inicial com **Path Scanning**  
- 🔧 Otimização das rotas com **2-opt**  
- 🔄 Processamento de múltiplas rotas, aplicando melhoria local em cada uma delas  
- ✅ Validação final das soluções otimizadas, garantindo que continuam respeitando todas as restrições  

---

## 🚀 Como Usar?

### ▶️ Execução
Para rodar o algoritmo e gerar as soluções:

```bash
python main.py 
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

