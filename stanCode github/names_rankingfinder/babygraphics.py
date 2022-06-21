"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
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
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
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
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    #  The x of each vertical line should be determined by how many years we include and the width.
    #  While also adding margin on the sides.
    x_coordinate = GRAPH_MARGIN_SIZE + year_index * (width - 2 * GRAPH_MARGIN_SIZE) // len(YEARS)
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # Draw lines according to the requirement
    width = CANVAS_WIDTH
    height = CANVAS_HEIGHT
    margin = GRAPH_MARGIN_SIZE

    # Upper horizontal line
    canvas.create_line(margin, margin, width - margin, margin)
    # Bottom horizontal line
    canvas.create_line(margin, height - margin, width - margin, height - margin)

    # Vertical lines
    for year in YEARS:
        x = get_x_coordinate(width, YEARS.index(year))
        canvas.create_line(x, 0, x, height)
        #  Adding years label according to YEAR constant
        canvas.create_text(x + TEXT_DX, height - margin, text=year, anchor=tkinter.NW)


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
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # ----- Write your code below this line ----- #
    # Calculating how much y should increase when the number of rank increased by 1
    y_ratio = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE - GRAPH_MARGIN_SIZE) / MAX_RANK
    # Determining which color we are using by the remainder.
    # 0 =red, 1 = purple, 2 = green, 3 = blue and so on
    color_count = 0

    for name_l in lookup_names:
        # name_l stands for "name we are looking for"
        for name_d in name_data:
            # name_d stands for "names in the name_data"
            for y in YEARS:
                # If the name_l is not in the record in specific year, which means its rank is over 1000
                # We record it with *
                if str(y) not in name_data[name_l]:
                    name_data[name_l][str(y)] = "*"
            if name_l == name_d:
                # We found name_l in name_data, and we can draw the line

                # Draw the line

                # We need two pairs of (x, y) to draw a line, so we use old_y_r and old_x to store the info
                # from the previous data point
                old_y_r = 0
                new_y_r = 0
                old_x = 0
                new_x = 0
                for year in sorted(name_data[name_l]):
                    # replace the olds
                    old_y_r = new_y_r
                    old_x = new_x

                    # Get the new y
                    if name_data[name_l][year] is not '*':
                        # If the rank is not *, then save its rank as int.
                        new_y_r = int(name_data[name_l][year])
                    else:
                        # If the rank is *, save its rank as 1000(max), so the y will be at the bottom of the canvas.
                        new_y_r = 1000

                    # Get the new x according to the year
                    new_x = get_x_coordinate(CANVAS_WIDTH, YEARS.index(int(year)))

                    # Add the tag including name and rank.
                    canvas.create_text(new_x + TEXT_DX, new_y_r * y_ratio + GRAPH_MARGIN_SIZE,
                                       text=f'{name_l} {name_data[name_l][year]}', anchor=tkinter.SW,
                                       fill=COLORS[color_count % 4])
                    if old_x != 0:
                        # Drawing the line while we have two data points
                        canvas.create_line(old_x, old_y_r * y_ratio + GRAPH_MARGIN_SIZE, new_x,
                                           new_y_r * y_ratio + GRAPH_MARGIN_SIZE, width=LINE_WIDTH,
                                           fill=COLORS[color_count % 4])
                # Change the color
                color_count += 1


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
