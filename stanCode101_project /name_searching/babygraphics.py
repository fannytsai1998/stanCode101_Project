"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # space between vertical lines
    space = (width-GRAPH_MARGIN_SIZE*2)/len(YEARS)
    return space*year_index+GRAPH_MARGIN_SIZE


def get_y_coordinate(rank):
    if rank == '*':
        return CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
    else:
        # resize 
        return int(int(rank)*(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)//1000+GRAPH_MARGIN_SIZE)

def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # the upper & lower line
    canvas.create_line(0+GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    canvas.create_line(0+GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill='black')

    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        # Vertical lines
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        # year text
        year = YEARS[i]
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=year, anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        # use the first year == 1900
        if str(YEARS[0]) in name_data[name]:
            rank = name_data[name][str(YEARS[0])]
        else:
            # if there is no data, mean rank over1000
            rank = '*'
        # control color loop
        if i > len(COLORS):
            color_i = i % len(COLORS)
        else:
            color_i = i
        # set first point
        pre_x = get_x_coordinate(CANVAS_WIDTH, 0)
        pre_y = get_y_coordinate(rank)
        # adjust text position if rank =*
        if rank == '*':
            canvas.create_text(pre_x+TEXT_DX, pre_y, text=name+' '+rank, anchor=tkinter.SW, fill=COLORS[color_i])
        else:
            canvas.create_text(pre_x + TEXT_DX, pre_y, text=name + ' ' + rank, anchor=tkinter.NW, fill=COLORS[color_i])

        for j in range(1, len(YEARS)):
            if str(YEARS[j]) in name_data[name]:
                rank = name_data[name][str(YEARS[j])]
            else:
                rank = '*'

            x = get_x_coordinate(CANVAS_WIDTH, j)
            y = get_y_coordinate(rank)

            canvas.create_line(pre_x, pre_y, x, y, width=LINE_WIDTH, fill=COLORS[color_i])
            if rank == '*':
                canvas.create_text(x + TEXT_DX, y, text=name + ' ' + rank, anchor=tkinter.SW,
                                   fill=COLORS[color_i])
            else:
                canvas.create_text(x + TEXT_DX, y, text=name + ' ' + rank, anchor=tkinter.NW,
                                   fill=COLORS[color_i])

            pre_x = x
            pre_y = y
            #



# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()