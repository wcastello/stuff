# A monochrome screen is stored as a single array of bytes, allowing eight consecutive
# pixels to be stored in one byte. The screen has width w, where w is divisible by 8 (that is, no byte will
# be split across rows). The height of the screen, of course, can be derived from the length of the array
# and the width. Implement a function that draws a horizontal line from (x1, y) to (x2, y).
# The method signature should look something like:
# drawline(byte[] screen, int width, int xl, int x2, int y)

# screen is a list of "8-bit integers", here numbers fro 0 to 255
def draw_h_line(screen, w, x1, x2, y):
    # get cols 
    col1 = w * y + x1//8
    col2 = w * y + x2//8
    for col in range(col1, col2+1):
        if col > col1 and col < col2:
            screen[col] = 0xff
        elif col < col2:
            start_px = 8 - ((x1+1) % 8)
            screen[col] = sum(1 << i for i in range(0, start_px+1))
        else:
            start_px = ((x2+1) % 8)
            screen[col] = sum(2**(7-i) for i in range(0, start_px))

def draw_v_line(screen, w, y1, y2, x):
    # get column
    col = x//8

    for row in range(y1, y2+1):
        # get idx on screen for number with this row and col
        i = row * w + col
        # get screen pixel bit position (x, row):
        px = 8 - ((x+1) % 8)
        # set it to 1
        screen[i] |= 1 << px

def print_screen(screen, w):
    h = len(screen)//w
    for idx, block in enumerate(screen):
        print('{:08b}'.format(block), end='')
        if (idx+1) % w == 0:
            print()