# Conway's Game of Life - Streamlit Web App

## Overview
This is an interactive web-based implementation of **Conway's Game of Life**, a zero-player cellular automaton. The project was originally created as a first semester college project using Pygame, and has been adapted to run as a web application using Streamlit on Replit.

## Project Structure
- `conway_app.py` - Main Streamlit web application (active)
- `Conway's Game Of Life.py` - Original Pygame desktop version
- `requirements.txt` - Python dependencies
- `Conway's Game of Life.pdf` - Documentation
- `README.md` - Original project README

## Current State
**Status**: ✅ Fully functional and deployed
- Web application running on Streamlit
- Accessible via web browser on port 5000
- All dependencies installed (streamlit, numpy, pillow, pygame)
- Interactive controls for playing/pausing, randomizing, and stepping through generations

## Features
- Real-time Game of Life simulation
- Interactive web-based UI
- Adjustable canvas size and cell size
- Speed control (FPS slider)
- Toroidal (wrap-around) mode toggle
- Step-by-step advancement
- Random grid generation
- Preset patterns (blinker, glider)
- Live cell counter

## Architecture
**Language**: Python 3.11
**Framework**: Streamlit (web UI)
**Libraries**: 
- NumPy (efficient grid operations)
- Pillow (image rendering)
- Streamlit (web interface)

**Key Components**:
1. `step_toroidal()` - Implements Game of Life rules with wrap-around edges
2. `grid_to_image()` - Renders the grid as an image
3. Streamlit session state manages grid, running state, and parameters

## Game Rules (Conway's Game of Life)
1. **Underpopulation**: Live cell with <2 neighbors dies
2. **Survival**: Live cell with 2-3 neighbors survives
3. **Overpopulation**: Live cell with >3 neighbors dies
4. **Reproduction**: Dead cell with exactly 3 neighbors becomes alive

## Recent Changes
- **Nov 17, 2024**: Initial Replit setup
  - Installed Python 3.11 and dependencies
  - Fixed Windows line endings (CRLF → LF)
  - Fixed Pillow rectangle API usage (list → tuple)
  - Updated deprecated `st.experimental_rerun()` → `st.rerun()`
  - Updated deprecated `use_column_width` → `use_container_width`
  - Configured Streamlit workflow on port 5000
  - Created .gitignore for Python project

## Development Notes
- The application uses Streamlit's session state to persist the grid across reruns
- Auto-run mode continuously steps through generations at the specified FPS
- Grid is represented as a NumPy boolean array for efficiency
- Toroidal mode uses `np.roll()` for fast neighbor counting with wrap-around
