# 🚀 Q-Orbit: Quantum Space Mission Designer

> **NASA Space Apps Challenge 2026 — Space Mission Design Game**  
> An open-source Python astrodynamics and quantum-inspired mission simulator created by a 10-year-old space enthusiast. Balance orbital physics, propulsion mass, and budget constraints using real NASA JPL data.

📺 **[Watch the 30-Second Official Pitch & Gameplay Video](PASTE_YOUR_YOUTUBE_LINK_HERE)**

---

## 🎯 Overview
Designing an interplanetary mission requires strict engineering trade-offs. Every kilogram of payload increases propellant mass exponentially, and strict mission budgets limit propulsion choices.

**Q-Orbit** turns real NASA orbital equations and datasets into an interactive mission design simulator. Players select a planetary target, configure payload mass and mission budget, and use a **Quantum-Inspired QUBO Solver** to select the optimal rocket propulsion stage before launching.

---

## 💻 Playable Python Engine & Game Benchmarks
* **Q-Orbit Core Game Engine:** [`game.py`](https://github.com) — Interactive Python mission designer driven by NASA JPL Horizons constants, Vis-Viva & Hohmann transfer math, and Quantum QUBO stage optimization.
* **Benchmark Simulator 1:** [Space Agency (Google Play)](https://google.com) — Benchmarked for multi-stage rocket assembly, fuel-to-mass ratios, and budget management.
* **Benchmark Simulator 2:** [Spaceflight Simulator (Google Play)](https://google.com) — Benchmarked for 2D orbital trajectories and Hohmann interplanetary transfer burns.

---

## 🧮 Authentic NASA Equations Implemented
1. **Vis-Viva Orbital Energy Equation:** Computes instantaneous spacecraft velocity ($v^2 = \mu (\frac{2}{r} - \frac{1}{a})$) at any point along a heliocentric trajectory.
2. **Hohmann Interplanetary Transfer ($\Delta v$):** Calculates minimum-energy two-impulse departure and arrival burns between Earth ($1.000\text{ AU}$), Mars ($1.524\text{ AU}$), and Venus ($0.723\text{ AU}$).
3. **Tsiolkovsky Rocket Propellant Equation:** Solves exact required propellant mass ($\Delta v = I_{sp} g_0 \ln(\frac{m_0}{m_f})$) based on stage specific impulse and dry mass.
4. **Quantum-Inspired QUBO Stage Selector:** Minimizes a Hamiltonian objective function ($H(x)$) to select the best propulsion stage (`LOX/LH2 Cryogenic`, `LOX/CH4 Methalox`, or `Nuclear Thermal Propulsion`) within mission budget limits.

---

## 🛰️ Official NASA Datasets Used
* **NASA JPL Horizons System:** Planetary orbital radii ($AU$), solar gravitational parameter ($\mu_\odot$), and heliocentric transfer constants.
* **NASA Launch Services Program (LSP):** Launch vehicle payload capacities and propulsion performance benchmarks.
* **NASA Technical Reports Server (NTRS):** Entry, Descent & Landing (EDL) ballistic coefficient modeling.

---

## 🚀 Quick Start (Run in 60 Seconds)

### Prerequisites
* Python 3.8 or higher (uses only Python's built-in `math` and `time` libraries—zero external installations required!)

### Installation & Launch
1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd The-nasa-challanger-
   ```

2. **Run the Q-Orbit Mission Designer:**
   ```bash
   python game.py
   ```

---

## 📄 License
This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.




video link: https://youtube.com/shorts/V2p379qel28?si=7rFgMLsynvtD8oiU
