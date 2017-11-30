"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and William Dalby.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    window = rg.RoseWindow(1500, 1500)
    center_one = rg.Point(750, 750)
    center_two = rg.Point(300, 450)
    circle = rg.Circle(center_one, 400)
    circle.fill_color = 'purple'
    circle.attach_to(window)
    circle_two = rg.Circle(center_two, 200)
    circle_two.attach_to(window)
    window.render()

    window.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    window = rg.RoseWindow(1500, 1500)
    center_x = 500
    center_y = 500
    rectangle_1_x = 0
    rectangle_1_y = 0
    rectangle_2_x = 250
    rectangle_2_y = 360
    center = rg.Point(center_x, center_y)
    point_1 = rg.Point(0, 0)
    point_2 = rg.Point(250, 360)
    rectangle = rg.Rectangle(point_1, point_2)
    circle = rg.Circle(center, 250)
    circle.fill_color = 'blue'
    thicc = 3
    thicc_2 = 1
    circle.pen = rg.Pen('black', thicc)
    rectangle.pen = rg.Pen('black', thicc_2)
    circle.attach_to(window)
    rectangle.attach_to(window)
    window.render()
    print(thicc)
    print('blue')
    print(center)
    print(center_x)
    print(center_y)
    print(thicc_2)
    print('None')
    rectangle_center_x = (rectangle_1_x+rectangle_2_x)/2
    rectangle_center_y = (rectangle_1_y+rectangle_2_y)/2
    rectangle_center = rg.Point(rectangle_center_x,rectangle_center_y)
    print(rectangle_center)
    print(rectangle_center_x)
    print(rectangle_center_y)
    window.close_on_mouse_click()
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(1500,1500)
    point_1 = rg.Point(0,0)
    point_2 = rg.Point(100,100)
    point_3 = rg.Point (500,500)
    point_4 = rg.Point(300,150)
    line_1 = rg.Line(point_1,point_2)
    line_2 = rg.Line(point_3,point_4)
    line_2.pen = rg.Pen('black',5)
    line_1.attach_to(window)
    line_2.attach_to(window)
    print(line_2.get_midpoint())
    print(line_2.get_midpoint().x)
    print(line_2.get_midpoint().y)
    window.render()

    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
