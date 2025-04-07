# Mancala Game Project

## Overview

This project implements the classic **Mancala** game, also known as **Awalé**, using adversarial search techniques. Mancala is a traditional African board game involving strategy and seed sowing. The objective is to capture more seeds than your opponent.

This implementation focuses on modeling the game using Python and solving it using the **Minimax algorithm with Alpha-Beta pruning**.

![Mancala Board Example](https://i.pinimg.com/originals/e7/23/07/e72307019ac8c6bf2501877bfb28bafc.gif)  
<br>  

---

## **📌 About**  

**Mancala** is an ancient strategy game where players capture the most seeds 🌱. 
This project implements a smart AI opponent using **Minimax algorithm with Alpha-Beta pruning** to outplay you 🤯.

![explain the game](https://i.pinimg.com/736x/07/f5/66/07f56656594d41042b81aba3d432e15c.jpg)
---

## **🧩 Features**  
- ✅ **Minimax Algorithm**: Implements adversarial search to determine the best moves.  
- ✅ **Alpha-Beta Pruning**: Optimizes the search by reducing unnecessary computations.  
- ✅ **Two Game Modes**:  
  - **AI vs AI**: Watch two AI opponents compete.  
  - **Human vs AI**: Play against the AI.  
- ✅ **Interactive Gameplay**: Provides a clear interface for both modes.  

## Game Setup

- The Mancala board has **6 pits per player** and **one store per player**.
- Each pit initially contains **4 seeds**.
- The players sit opposite each other, and each player's store is on their **right**.
- The game begins with the board arranged in such a way that each pit has **4 seeds**.

## Objective

The goal is to collect **more seeds** in your store than your opponent by the end of the game.

## Game Rules

1. The player selects a pit on their side and collects all the seeds.
2. Moving **counterclockwise**, they drop one seed in each following pit.
3. A player **cannot place a seed** in the opponent's store.
4. If the last seed lands in an **empty pit** on the player's side, they capture:
   - That seed
   - All seeds in the directly **opposite pit**
   - All captured seeds are placed in their **store**
5. The game ends when **a player has no seeds** left in any of their pits.
6. The opponent collects all remaining seeds into their store.
7. The winner is the player with the **most seeds in their store**.

