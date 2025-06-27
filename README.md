# 🌍 Orbital Visualizer

A space tech project to simulate and visualize satellite orbits using real-world TLE (Two-Line Element) data. This tool is designed to help users understand orbital mechanics and track satellite trajectories in space.

---

## 🚀 Features

- Parse and propagate TLE data using Skyfield
- Simulate satellite position over time
- Modular Python backend for orbit physics
- Prototype notebook for quick exploration
- Planned: 2D ground track and 3D orbit visualizations (CesiumJS / Plotly)

---

## 📁 Project Structure

```
orbital-visualizer/
├── backend/             # Orbit propagation and simulation logic
│   └── orbit_engine.py
├── data/                # TLE files (e.g., ISS)
│   └── sample.tle
├── notebooks/           # Jupyter notebooks for prototyping
│   └── orbit_demo.ipynb
├── requirements.txt     # Python dependencies
├── README.md            # Project description and instructions
└── .gitignore
```

---

## 📡 TLE Data Sources

- [Celestrak](https://celestrak.org)
- [Space-Track.org](https://www.space-track.org) *(registration required)*

---

## 🤝 Contributions

Ideas, suggestions, and PRs are welcome! If you'd like to help build the frontend or integrate a satellite database, feel free to fork and collaborate.

---