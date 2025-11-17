# app.py
import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
import time

# ------------------------
# Helpers: Game logic
# ------------------------
def step_toroidal(g: np.ndarray) -> np.ndarray:
    # fast neighbor count with np.roll (wrap-around)
    # Convert to int for counting, then apply rules
    g_int = g.astype(int)
    neighbors = (
        np.roll(np.roll(g_int,  1, 0),  1, 1) +
        np.roll(np.roll(g_int,  1, 0),  0, 1) +
        np.roll(np.roll(g_int,  1, 0), -1, 1) +
        np.roll(np.roll(g_int,  0, 0),  1, 1) +
        np.roll(np.roll(g_int,  0, 0), -1, 1) +
        np.roll(np.roll(g_int, -1, 0),  1, 1) +
        np.roll(np.roll(g_int, -1, 0),  0, 1) +
        np.roll(np.roll(g_int, -1, 0), -1, 1)
    )
    # Apply Conway's rules
    survive = g & ((neighbors == 2) | (neighbors == 3))
    born = (~g) & (neighbors == 3)
    return survive | born

def grid_to_image(g: np.ndarray, cell_px: int = 8, alive_color=(255,255,255), bg_color=(8,10,15)):
    rows, cols = g.shape
    img = Image.new("RGB", (cols * cell_px, rows * cell_px), bg_color)
    draw = ImageDraw.Draw(img)
    for r in range(rows):
        for c in range(cols):
            if g[r, c]:
                x0 = c * cell_px
                y0 = r * cell_px
                draw.rectangle(((x0, y0), (x0 + cell_px - 1, y0 + cell_px - 1)), fill=alive_color)
    return img

# ------------------------
# Streamlit UI / state
# ------------------------
st.set_page_config(layout="wide", page_title="Game of Life (Streamlit)")
st.title("Conway's Game of Life — Streamlit edition")

# left panel: controls
col_ctrl, col_view = st.columns([1, 2])

with col_ctrl:
    st.header("Controls")
    width = st.number_input("Canvas width (px)", value=800, step=100)
    height = st.number_input("Canvas height (px)", value=600, step=100)
    cell_size = st.slider("Cell size (px)", min_value=4, max_value=20, value=8)
    cols = int(width // cell_size)
    rows = int(height // cell_size)

    # initialize session state grid if needed
    if "grid" not in st.session_state or st.session_state.get("grid_shape") != (rows, cols):
        st.session_state.grid = np.zeros((rows, cols), dtype=bool)
        st.session_state.grid_shape = (rows, cols)
        st.session_state.running = False
        st.session_state.fps = 5
        st.session_state.toroidal = True
    
    # Random fill probability slider (always visible)
    random_prob = st.slider("Random fill probability", 0.01, 0.8, 0.35, step=0.01, 
                            help="Higher values = more alive cells. Try 0.35-0.40 for stable patterns.")

    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        if st.button("Step"):
            st.session_state.grid = step_toroidal(st.session_state.grid) if st.session_state.toroidal else st.session_state.grid # handled below
        if st.button("Clear"):
            st.session_state.grid = np.zeros_like(st.session_state.grid, dtype=bool)
    with btn_col2:
        if st.button("Randomize"):
            st.session_state.grid = (np.random.random((rows, cols)) < random_prob)
        if st.button("Reset & Resize"):
            st.session_state.grid = np.zeros((rows, cols), dtype=bool)
            st.session_state.grid_shape = (rows, cols)

    # runtime toggles
    run_toggle = st.checkbox("Running (auto-advance)", value=st.session_state.running)
    st.session_state.running = run_toggle
    st.session_state.fps = st.slider("Speed (FPS)", min_value=1, max_value=30, value=st.session_state.fps)

    st.session_state.toroidal = st.checkbox("Toroidal wrap (edges wrap)", value=st.session_state.toroidal)
    st.markdown("---")
    st.markdown("**Quick presets**")
    if st.button("Place blinker (center)"):
        r0, c0 = rows//2, cols//2
        g = np.zeros((rows, cols), dtype=bool)
        g[r0, c0-1:c0+2] = True
        st.session_state.grid = g
    if st.button("Place glider (corner)"):
        g = np.zeros((rows, cols), dtype=bool)
        # small glider pattern
        g[1,2] = g[2,3] = g[3,1] = g[3,2] = g[3,3] = True
        st.session_state.grid = g

    st.markdown("---")
    st.markdown("**Notes**")
    st.markdown("- Left-click the image to toggle a cell (if using `streamlit-drawable-canvas` see optional steps).")
    st.markdown("- Streamlit keeps a session state, use Reset/Resize if you change canvas size.")

with col_view:
    st.header("Canvas")
    # draw image from current grid
    img = grid_to_image(st.session_state.grid, cell_px=cell_size)
    # show image
    st.image(img, width='stretch')

    # display stats and live auto-run loop
    st.markdown(f"**Alive:** {int(st.session_state.grid.sum())}   |   **FPS:** {st.session_state.fps}   |   **Toroidal:** {st.session_state.toroidal}")

    # Auto-run: advance frame if running
    if st.session_state.running:
        # compute next step, update session state, sleep according to fps, then rerun
        if st.session_state.toroidal:
            st.session_state.grid = step_toroidal(st.session_state.grid)
        else:
            # non-wrapping fallback (simple vectorized via pad)
            p = np.pad(st.session_state.grid, 1, mode="constant", constant_values=0)
            neighbors = (
                p[0:-2, 0:-2] + p[0:-2, 1:-1] + p[0:-2, 2:] +
                p[1:-1, 0:-2] +               p[1:-1, 2:] +
                p[2:  , 0:-2] + p[2:  , 1:-1] + p[2:  , 2:]
            )
            survive = (st.session_state.grid & ((neighbors == 2) | (neighbors == 3)))
            born = (~st.session_state.grid & (neighbors == 3))
            st.session_state.grid = (survive | born)

        # sleep to control speed, then rerun to update UI
        time.sleep(1.0 / max(1, st.session_state.fps))
        st.rerun()
