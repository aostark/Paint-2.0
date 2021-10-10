from utils import *

win = pygame.display.set_mode((width, height))  # create/initialize a window
pygame.display.set_caption("Paint v1.01")


def init_grid(rows, cols, color):
    grid = []
    for i in range(rows):
        grid.append([])
        for _ in range(cols):
            grid[i].append(color)
    return grid


def draw_grid(win, grid):
    for i, row in enumerate(grid):  # giving you the element and the index of that element
        for j, pixel in enumerate(row):  # same as above
            pygame.draw.rect(win, pixel, (j * pixel_size, i * pixel_size, pixel_size, pixel_size))

    if draw_grid_lines:
        for i in range(rows + 1):
            pygame.draw.line(win, black, (0, i * pixel_size), (width, i * pixel_size))
        for j in range(cols + 1):
            pygame.draw.line(win, black, (j * pixel_size, 0), (j * pixel_size, height - toolbar_height))


def draw(win, grid, buttons):
    win.fill(bg_color)
    draw_grid(win, grid)
    for button in buttons:
        button.draw(win)
    pygame.display.update()


def get_row_col_from_pos(pos):
    x, y = pos  # will decompose the tuple from above and give us x and y
    row = y // pixel_size
    col = x // pixel_size

    if row >= rows:
        raise IndexError

    return row, col


run = True
clock = pygame.time.Clock()
grid = init_grid(rows, cols, bg_color)
drawing_color = black

button_y = height - toolbar_height / 2 - 25
button_x = width
buttons = [
    Button(10, button_y, 50, 50, black),
    Button(70, button_y, 50, 50, red),
    Button(130, button_y, 50, 50, green),
    Button(190, button_y, 50, 50, blue),
    Button(250, button_y, 50, 50, white, "Erase", black),
    Button(310, button_y, 50, 50, white, "Clear", black)
]

# the event loop will continually run until the game ends.
while run:
    clock.tick(fps)  # sets frame rate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()  # gives us the x, y position of where the user pressed the left mouse button
            try:
                row, col = get_row_col_from_pos(pos)
                grid[row][col] = drawing_color
            except IndexError:
                for button in buttons:
                    if not button.clicked(pos):
                        continue
                    drawing_color = button.color
                    # clear the screen and reset everything
                    if button.text == "Clear":
                        grid = init_grid(rows, cols, bg_color)
                        drawing_color = black

    draw(win, grid, buttons)

pygame.quit()
