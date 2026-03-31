# 🧬 Conway's Game of Life

> *"The universe is not only stranger than we suppose, but stranger than we can suppose."* — J.B.S. Haldane

A fully interactive implementation of **Conway's Game of Life** — the classic zero-player cellular automaton — built in **two flavours**: a desktop app powered by **Pygame**, and a browser-based app powered by **Streamlit**.

Simple rules. Infinite complexity.

---

## 📸 Screenshots

| Drawing Phase | Simulation Running | Stabilized State |
|---|---|---|

| ![Start](https://github.com/user-attachments/assets/5f7c200c-1ef4-4f92-8c88-2df206404ae8) | ![Running](https://github.com/user-attachments/assets/3e12c523-0384-49cf-bebd-4936d98dfc09) | ![Final](https://github.com/user-attachments/assets/5b467221-5ecb-41fc-9d74-0406254bcd3e) |
|⚪ Paint alive cells with your mouse | 🟢 Green = newly born · 🔴 Red = just died | Stable patterns emerge over time |

---

## ✨ Two Versions

### 🖥️ Desktop — `Conway's Game Of Life.py` (Pygame)
A real-time interactive window where you paint cells, watch them evolve, and see births and deaths highlighted frame-by-frame in color.

### 🌐 Web App — `Conway_app.py` (Streamlit)
A browser-based version with a sidebar control panel, adjustable canvas size, toroidal (wrap-around) grid toggle, and one-click presets for classic patterns.

---

## 🎮 Controls

### Pygame (Desktop)

| Action | Input |
|---|---|
| Play / Pause | `Space` |
| Clear Grid | `C` |
| Increase Speed | `↑` Arrow |
| Decrease Speed | `↓` Arrow |
| Draw Cell | Left Click / Drag |
| Erase Cell | Right Click |

> **Color coding:** White = alive · 🟢 Green = born this tick · 🔴 Red = died this tick

### Streamlit (Web)

| Action | How |
|---|---|
| Start / Stop | "Running" checkbox in sidebar |
| Step once | "Step" button |
| Randomize | "Randomize" button + probability slider |
| Clear | "Clear" button |
| Adjust Speed | FPS slider (1–30) |
| Toggle wrap-around | "Toroidal wrap" checkbox |
| Load a preset | "Place blinker" / "Place glider" buttons |

---

## 🧬 The Rules

Each cell on the grid is either **alive** or **dead**. Every generation, these four rules are applied simultaneously to every cell:

| Rule | Condition | Outcome |
|---|---|---|
| Underpopulation | Live cell with < 2 live neighbours | Dies |
| Survival | Live cell with 2 or 3 live neighbours | Survives |
| Overpopulation | Live cell with > 3 live neighbours | Dies |
| Reproduction | Dead cell with exactly 3 live neighbours | Comes alive |

These four lines of logic are all it takes to produce **gliders**, **oscillators**, **still lifes**, and structures of unbounded complexity.

---

## ⚙️ How It Works

**Pygame version** — iterates over every cell each frame, counts neighbours in a bounded window using NumPy slicing, applies the rules, and renders color-coded overlays to distinguish births from deaths. Runs at an adjustable FPS (default 100, controllable with arrow keys).

**Streamlit version** — uses `np.roll` for fully vectorized 8-neighbour counting in a single pass, making it significantly faster. Supports **toroidal geometry** (the grid wraps — cells on the right edge are neighbours of cells on the left). Canvas size and cell pixel size are both configurable at runtime.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+

### Installation

```bash
git clone https://github.com/your-username/conways-game-of-life.git
cd conways-game-of-life
pip install -r requirements.txt
```

### Run the Desktop App (Pygame)

```bash
python "Conway's Game Of Life.py"
```

### Run the Web App (Streamlit)

```bash
streamlit run Conway_app.py
```
Then open `http://localhost:8501` in your browser.

---

## 📦 Dependencies

```
streamlit
numpy
pillow
pygame  # for the desktop version
```

> Install everything with `pip install -r requirements.txt`

---

## 🗂️ Project Structure

```
Conway-s-Game-Of-Life/
├── Conway's Game Of Life.py   # Pygame desktop simulation
├── Conway_app.py              # Streamlit web app
├── Conway_app.md              # Web app notes / documentation
├── requirements.txt           # Python dependencies
└── README.md
```

---

## 🌱 Background

This project was built in my **first semester of college** as my first real programming build from scratch. I wanted something that would let me practice the fundamentals: loops, arrays, state management and rendering, while also producing something visually interesting and mathematically deep.

Conway's Game of Life turned out to be a perfect fit: it is dead simple to describe, surprisingly hard to fully understand, and endlessly watchable.

Building it taught me how to think in grids, how to manage a real-time event loop, how NumPy vectorization can replace slow nested loops, and how much complexity can emerge from almost nothing.

---

## 🚀 Features

- Real-time simulation using Pygame  
- Interactive drawing & erasing of cells  
- Adjustable speed (FPS controls)  
- Grid randomization  
- Reset & clear functions  
- Support for common Life patterns (gliders, blinkers, etc.)  
- Clean and minimal UI  
- Efficient computation using NumPy  
- Implements all four official Game of Life rules

---

## 📘 How It Works

- The grid is represented as a 2D NumPy array.  
- Each frame, the simulation calculates neighbor counts for every cell using vectorized operations.  
- Based on the Game of Life rules, a new grid is generated and rendered onto the screen.  
- Pygame handles the window, drawing, mouse input, and frame updates.  
- The user can modify the grid at any time, even while the simulation is running.

This creates an interactive environment where the user can experiment with emergent patterns and real-time system evolution.

---

## 💡 Significance as My First Project

This project holds special significance for me because it marks my **first real programming build**, created in my first semester of college.  

It became my gateway to:  
- thinking about algorithms,  
- understanding how simulations work,  
- learning event-driven programming,  
- exploring visualization,  
- debugging real systems,  
- and gaining confidence in my ability to bring ideas to life.

It taught me that even beginner-level concepts can produce complex results when you implement them with clarity and consistency.

---

## 🧠 What I Learned

Working on this project taught me:

### ✔ Programming Fundamentals  
- Loops, conditions, array manipulation  
- How state-based systems work  
- Structuring and organizing code

### ✔ Game Loop & Event Handling  
- Handling keyboard/mouse events  
- Managing real-time updates  
- Using Pygame’s rendering pipeline

### ✔ Computational Thinking  
- Breaking big problems into simple rules  
- Understanding emergent behavior  
- Visualizing algorithmic logic

### ✔ NumPy & Optimization  
- Vectorized operations  
- Avoiding slow Python loops  
- Efficient memory handling

### ✔ Debugging & Problem Solving  
- Tracking logic bugs  
- Fixing rendering issues  
- Handling performance bottlenecks

This foundation helped me grow rapidly and inspired me to explore more advanced projects.

---
