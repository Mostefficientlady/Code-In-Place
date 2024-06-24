from tkinter import *

import math

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 500
GOLDEN_RATIO = (1 + math.sqrt(5)) / 2

def main():
    root = Tk()
    canvas = Canvas(root, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    patch_size = CANVAS_WIDTH / 1.75
    start_x = 0
    start_y = 0
    for i in range(3):
        draw_fibinacci_patch(canvas, start_x, start_y, patch_size)
        start_x = start_x + patch_size
        patch_size = patch_size / GOLDEN_RATIO
        start_y = start_y + patch_size
        patch_size = patch_size / GOLDEN_RATIO**3
    canvas.pack(side=TOP, padx=50, pady=50)
    root.mainloop()

def draw_fibinacci_patch(canvas, start_x, start_y, patch_size):
    # square 1
    left_x = start_x
    top_y = start_y
    patch_size1 = patch_size
    patch_size2 = patch_size1 / GOLDEN_RATIO
    patch_size3 = patch_size2 / GOLDEN_RATIO
    patch_size4 = patch_size3 / GOLDEN_RATIO
    right_x = left_x + patch_size1
    bottom_y = top_y + patch_size1
    rect = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="powderblue")
    right_x = left_x + patch_size1 * 2
    bottom_y = top_y + patch_size1 * 2
    arc = canvas.create_arc(left_x, top_y, right_x, bottom_y, start=90, extent=90, fill="lightyellow")
    # square 2
    left_x = start_x + patch_size1
    top_y = start_y
    right_x = left_x + patch_size2
    bottom_y = top_y + patch_size2
    rect = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="plum")
    left_x = start_x + patch_size1 - patch_size2
    right_x = left_x + patch_size2 * 2
    bottom_y = top_y + patch_size2 * 2
    arc = canvas.create_arc(left_x, top_y, right_x, bottom_y, start=0, extent=90, fill="palegreen")
    # square 3
    left_x = start_x + patch_size1 + patch_size2 - patch_size3
    top_y = start_y + patch_size2
    right_x = left_x + patch_size3
    bottom_y = top_y + patch_size3
    rect = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="mistyrose")
    left_x = start_x + patch_size1 + patch_size2 - patch_size3*2
    top_y = start_y + patch_size2 - patch_size3
    right_x = left_x + patch_size3 * 2
    bottom_y = top_y + patch_size3 * 2
    arc = canvas.create_arc(left_x, top_y, right_x, bottom_y, start=270, extent=90, fill="lightcyan")
    # square 4
    left_x = start_x + patch_size1
    top_y = start_y + patch_size2 + patch_size3 - patch_size4
    right_x = left_x + patch_size4
    bottom_y = top_y + patch_size4
    rect = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill="navajowhite")
    left_x = start_x + patch_size1 + patch_size2 - patch_size3 - patch_size4
    top_y = start_y + patch_size2 + patch_size3 - patch_size4*2
    right_x = left_x + patch_size4 * 2
    bottom_y = top_y + patch_size4 * 2
    arc = canvas.create_arc(left_x, top_y, right_x, bottom_y, start=180, extent=90, fill="linen")

if __name__ == '__main__':
    main()