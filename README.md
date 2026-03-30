# 🧠 Hill Climbing Optimization

This project demonstrates the implementation of **Hill Climbing algorithms** in Artificial Intelligence using Python. It visualizes how different variants of hill climbing explore and optimize a function.

---

## 📌 Overview

Hill Climbing is a **local search optimization algorithm** used to find the maximum (or minimum) of a function. This project applies hill climbing techniques to a mathematical function and visualizes the search process.

The function used in this project is:

f(x) = -(x - 3)² + 9

This is a **parabolic function** with a maximum at **x = 3**.

---

## 🎯 Objectives

- Understand local search algorithms
- Compare different hill climbing strategies
- Visualize optimization paths
- Analyze performance of random restarts

---

## 🧩 Algorithms Implemented

### 1. Simple Hill Climbing
- Moves step-by-step in one direction
- Stops when no better neighbor is found

---

### 2. Steepest Ascent Hill Climbing
- Evaluates all neighbors
- Moves to the best possible option

---

### 3. Random Restart Hill Climbing
- Runs hill climbing multiple times
- Starts from random positions
- Helps escape local maxima

---

## ⚙️ How It Works

1. A mathematical function is defined
2. Different hill climbing algorithms are applied
3. Paths taken by each algorithm are recorded
4. Results are plotted using Matplotlib

---

## 📊 Visualization

The graph shows:

- 📉 Function curve (dashed line)
- 🔵 Simple Hill Climbing path
- 🟠 Random Restart paths

This helps in comparing how each algorithm explores the search space.

---

## 🛠️ Technologies Used

- Python
- NumPy
- Matplotlib
- Random module

---

## ▶️ How to Run

1. Make sure Python is installed

2. Install required libraries:
```bash
pip install numpy matplotlib
