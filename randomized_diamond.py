import diamondfunctions as df

# Prepare MS Paint
df.wait_for_paint()
df.select_pencil_tool()

# User selects drawing point
start_x, start_y = df.get_starting_position()

# Initial shape size
size = df.INITIAL_SIZE

# Draw randomized diamonds
for layer in range(df.TOTAL_LAYERS):

    if size <= 0:
        break

    # Random color for each layer
    df.select_random_color()

    # Draw current layer
    df.draw_diamond(start_x, start_y, size)

    # Prepare next layer
    start_y += df.VERTICAL_SHIFT
    size -= df.SIZE_DECREASE

print("Randomized diamond drawing complete.")
