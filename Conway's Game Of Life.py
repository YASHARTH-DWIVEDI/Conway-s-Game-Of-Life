import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game of Life")

# Set cell size and grid dimensions
cell_size = 10
cols, rows = width // cell_size, height // cell_size

# Create grid and initialize variables
grid = np.zeros((rows, cols), dtype=int)
running = False

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BORN_COLOR = (0, 220, 0)   # green = birth (prey appears)
DIED_COLOR = (220, 30, 30) # red = death (predator effect)

# Main loop
clock = pygame.time.Clock()
fps = 100  # persistent FPS variable you can adjust with Up/Down

# To hold the last generation's births/deaths to render for one frame
last_born = np.zeros_like(grid, dtype=bool)
last_died = np.zeros_like(grid, dtype=bool)

while True:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Allow painting while running (interactive)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button toggles cell
                row = event.pos[1] // cell_size
                col = event.pos[0] // cell_size
                if 0 <= row < rows and 0 <= col < cols:
                    grid[row, col] = 1 - grid[row, col]
        elif event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]:
            row = event.pos[1] // cell_size
            col = event.pos[0] // cell_size
            if 0 <= row < rows and 0 <= col < cols:
                grid[row, col] = 1
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running
            elif event.key == pygame.K_c:
                grid = np.zeros((rows, cols), dtype=int)
            elif event.key == pygame.K_UP:
                fps = min(60, fps + 2)  # increase speed
            elif event.key == pygame.K_DOWN:
                fps = max(1, fps - 2)   # decrease speed
    
    # Always draw current cells (so state / edits are visible even when paused)
    for r in range(rows):
        for c in range(cols):
            if grid[r, c] == 1:
                x = c * cell_size
                y = r * cell_size
                pygame.draw.rect(screen, WHITE, (x, y, cell_size, cell_size))
    
    # Update simulation and compute births/deaths when running
    if running:
        new_grid = np.copy(grid)
        born = np.zeros_like(grid, dtype=bool)
        died = np.zeros_like(grid, dtype=bool)
        
        for row in range(rows):
            for col in range(cols):
                # Count live neighbors safely
                r0 = max(0, row - 1)
                r1 = min(rows, row + 2)
                c0 = max(0, col - 1)
                c1 = min(cols, col + 2)
                neighbors = np.sum(grid[r0:r1, c0:c1]) - grid[row, col]
                
                # Apply Game of Life rules
                if grid[row, col] == 1 and (neighbors < 2 or neighbors > 3):
                    new_grid[row, col] = 0
                    died[row, col] = True
                elif grid[row, col] == 0 and neighbors == 3:
                    new_grid[row, col] = 1
                    born[row, col] = True
        
        # swap grids and store last changes for rendering
        grid = new_grid
        last_born = born
        last_died = died
    else:
        # when paused, clear last change overlays so births/deaths aren't shown indefinitely
        last_born = np.zeros_like(grid, dtype=bool)
        last_died = np.zeros_like(grid, dtype=bool)
    
    # Render birth/death overlays (one-frame highlights)
    # Draw births (green) on top of existing cells
    for r in range(rows):
        for c in range(cols):
            x = c * cell_size
            y = r * cell_size
            if last_born[r, c]:
                pygame.draw.rect(screen, BORN_COLOR, (x, y, cell_size, cell_size))
            elif last_died[r, c]:
                # draw death overlay (red) — if a cell died, it might be currently dead, so draw on black background
                pygame.draw.rect(screen, DIED_COLOR, (x, y, cell_size, cell_size))
    
    pygame.display.flip()
    
    clock.tick(fps)  # use persistent fps
