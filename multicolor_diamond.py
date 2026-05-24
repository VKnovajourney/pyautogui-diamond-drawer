import diamondfunctions as df

# Prepare MS Paint
df.wait_for_paint()
df.select_pencil_tool()

# User selects drawing point
start_x, start_y = df.get_starting_position()

# Initial shape size
size = df.INITIAL_SIZE

# Palette tracking
color_index = 0

# Draw multicolor diamonds
for layer in range(df.TOTAL_LAYERS):

    if size <= 0:
        break

    # Cycle through colors
    color_x = df.COLOR_POSITIONS[color_index]
    df.select_color(color_x)

    # Draw current layer
    df.draw_diamond(start_x, start_y, size)

    # Move to next palette color
    color_index += 1

    if color_index >= len(df.COLOR_POSITIONS):
        color_index = 0

    # Prepare next layer
    start_y += df.VERTICAL_SHIFT
    size -= df.SIZE_DECREASE

print("Multicolor diamond drawing complete.")
