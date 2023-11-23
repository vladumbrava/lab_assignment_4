class MyPoint:

    """Initialize a point with coordinates and color.

        Args:
            coord_x (float): The X-coordinate of the point.
            coord_y (float): The Y-coordinate of the point.
            color (str): The color of the point.
    """
    def __init__(self, coord_x, coord_y, color):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.color = color

    """Create a point using specified coordinates.

        Args:
            coord_x (float): The X-coordinate of the point.
            coord_y (float): The Y-coordinate of the point.
    """
    def create_point_by_coordinates(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    """Get the X-coordinate of the point.

        Returns:
            float: The X-coordinate of the point.
    """
    def get_coord_x(self):
        return self.coord_x

    """Set the X-coordinate of the point.

        Args:
            x (float): The new X-coordinate of the point.
    """
    def set_coord_x(self, x):
        self.coord_x = x

    """Get the Y-coordinate of the point.

        Returns:
            float: The Y-coordinate of the point.
    """
    def get_coord_y(self):
        return self.coord_y

    """Set the Y-coordinate of the point.

        Args:
            y (float): The new Y-coordinate of the point.
    """
    def set_coord_y(self, y):
        self.coord_y = y

    """Get the color of the point.

        Returns:
            str: The color of the point.
    """
    def get_color(self):
        return self.color

    """Set the color of the point.

        Args:
            color (str): The new color of the point.
    """
    def set_color(self, color):
        self.color = color

    """Return a string representation of the point.

        Returns:
            str: A formatted string containing information about the point.
    """
    def __str__(self):
        return f"Point [{self.coord_x},{self.coord_y}] of color {self.color}"
