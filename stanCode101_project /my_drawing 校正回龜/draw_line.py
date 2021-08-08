"""
File: draw_line.py
Name:Fanny
-------------------------

    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked, onmousemoved

SIZE = 20
window = GWindow()
# remember the first point
point = GOval(SIZE, SIZE)
count = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(function)


def function(m):
    global count
    # count how many point are there
    count += 1
    if count % 2 == 1:
        # means it's the 1st point
        point.color = 'black'
        window.add(point, m.x-SIZE/2, m.y-SIZE/2) # 1st point
    else:
        # means it's the second point
        line = GLine(point.x+SIZE/2, point.y+SIZE/2, m.x, m.y)
        window.add(line)
        window.remove(point)







if __name__ == "__main__":
    main()
