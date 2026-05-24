import time
import diamondfunctions as df

print("You have 5 seconds to open MS Paint...")

time.sleep(df.START_DELAY)

df.select_pencil_tool()

start_x, start_y = df.get_starting_position()

size = df.INITIAL_SIZE

for layer in range(df.TOTAL_LAYERS):

    if size <= 0:
        break

    df.select_random_color()

    df.draw_diamond(start_x, start_y, size)

    start_y += df.VERTICAL_SHIFT
    size -= df.SIZE_DECREASE

print("Drawing complete.")