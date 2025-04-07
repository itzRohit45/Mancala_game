# 🕹️ Mancala Game Project

## 📖 Overview

This project implements the classic **Mancala** game, also known as **Awalé**, using adversarial search techniques. Mancala is a traditional African board game involving strategy and seed sowing. The objective is to capture more seeds than your opponent.

This implementation focuses on modeling the game using **Python** and solving it using the **Minimax algorithm with Alpha-Beta pruning**.

![Mancala Board Example](https://i.pinimg.com/originals/e7/23/07/e72307019ac8c6bf2501877bfb28bafc.gif)

---

## 📌 About  

**Mancala** is an ancient strategy game where players capture the most seeds 🌱.  
This project implements a smart AI opponent using **Minimax algorithm with Alpha-Beta pruning** to outplay you 🤯.

![Game Illustration](https://i.pinimg.com/736x/07/f5/66/07f56656594d41042b81aba3d432e15c.jpg)

---

## 🧩 Features

- ✅ **Minimax Algorithm**: Implements adversarial search to determine the best moves.  
- ✅ **Alpha-Beta Pruning**: Optimizes the search by reducing unnecessary computations.  
- ✅ **Three Game Modes**:  
  - 🤖 **AI vs AI**: Watch two AI opponents compete.  
  - 🧑‍💻 **Player vs AI**: Play against the AI.  
  - 🧑‍🤝‍🧑 **Player vs Player**: Two players compete against each other.  
- ✅ **Interactive Gameplay**: Provides a clean and clear interface for both modes.  

---

## 🎮 Game Setup

- The board consists of:
  - **6 pits per player**
  - **1 store per player**
- Each pit starts with **4 seeds**.
- Players sit opposite each other.
- Each player's **store is on their right**.

---

## 🎯 Objective

Collect **more seeds** in your store than your opponent by the end of the game.

---

## 📜 Game Rules

1. A player selects a pit on their side and collects all seeds from it.
2. Seeds are sown **counterclockwise**, dropping one seed per pit.
3. **No seeds** are dropped into the opponent’s store.
4. If the last seed lands in an **empty pit** on the player’s side:
   - They capture that seed **plus** all seeds in the **opposite pit**.
   - All captured seeds go to their **store**.
5. The game ends when a player has **no seeds** in any pits.
6. The opponent collects all **remaining seeds** to their store.
7. The player with the **most seeds** in their store wins.

---

## 🧠 AI Implementation Details

### 🔍 Minimax Algorithm

- Explores all possible game states up to a certain **depth**.
- Assumes both players play optimally:
  - **Maximizing player**: tries to **maximize score**.
  - **Minimizing player**: tries to **minimize opponent's score**.

### ✂️ Alpha-Beta Pruning

- Skips unnecessary branches in the Minimax tree.
- Improves performance drastically — especially at deeper levels.

---

## 📈 Heuristic Function

Used to evaluate the board when the maximum search depth is reached or the game ends.

### 📊 Factors considered:
- **Store Difference**: Player 1's store - Player 2's store  
- **Seeds in Pits**: (Player 1 pits total - Player 2 pits total) × 0.5  

### 🎲 Example Calculation:

- **Player 1's store**: `20`  
- **Player 2's store**: `15`  
- **Player 1 pits**: `[3, 2, 1, 4, 5, 6]` → Total = `21`  
- **Player 2 pits**: `[2, 3, 4, 1, 0, 2]` → Total = `12`  

**Heuristic value**:
(20 - 15) + (21 - 12) × 0.5 = 5 + 9 × 0.5 = 5 + 4.5 = 9.5


👉 A **positive value** indicates a favorable position for **Player 1**,  
👉 A **negative value** indicates an advantage for **Player 2**.

---

## ⏳ Minimax Depth

- The depth determines how many moves ahead the AI evaluates. 
- A higher depth results in better decision-making but increases computation time.

---

## 🆚 AI vs AI Mode

- **AI-BOT 1** and **AI-BOT 2** compete with each other.
- **AI-BOT 2** introduces a 10% chance of making a **random valid move** to add unpredictability.

---

## 📊 Performance Highlights

- **Alpha-Beta Pruning** significantly reduces the number of nodes evaluated.
- The **heuristic function** ensures the AI makes smart decisions, focusing on:
  - Maximizing store seeds
  - Capturing opportunities
  - Avoiding vulnerable positions

---
