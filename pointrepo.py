from math import sqrt
import matplotlib.pyplot as plt


class PointRepository:

    """Initialize an empty list to store points."""
    def __init__(self):
        self.points_list = []

    """Get the list of points in the repository.

        Returns:
            list: The list of points.
    """
    def get_list_of_points(self):
        return self.points_list

    """Set the list of points in the repository.

        Args:
            points_list (list): The list of points to set.
    """
    def set_list_of_points(self, points_list):
        self.points_list = points_list

    """Add a new point to the repository.
    
        Args:
            new_point (MyPoint): The point to be added.
    """
    def add_new_point(self, new_point):
        self.points_list.append(new_point)

    """Get a point from the repository based on its index.
        Args:
            index (int): The index of the point.
        Returns:
            MyPoint: The point at the specified index.
    """
    def get_point_given_index(self, index):
        return self.points_list[index]

    """Get all points of a given color from the repository.
        Args:
            color (str): The color to filter points.
        Returns:
            list: List of points with the specified color.
    """
    def get_points_given_color(self, color):
        color_list = []
        for i in range(len(self.points_list)):
            if self.points_list[i].color == color:
                color_list.append(self.points_list[i])
        return color_list

    """Get all points inside a given square from the repository.
        Args:
            corner (MyPoint): The upper left corner of the square.
            length (float): The length of the square.
        Returns:
            str: A formatted string with points inside the square.
    """
    def get_points_inside_square(self, corner, length):
        list = []
        for point in self.points_list:
            if corner.coord_x <= point.coord_x <= corner.coord_x + length \
                    and corner.coord_y - length <= point.coord_y <= corner.coord_y:
                list.append(point)

        if len(list) == 0:
            return ""
        result = "The points inside the given square are: "
        for point in list:
            result += f"\n{point}"

        return result

    """Get the minimum distance between any two points in the repository.

        Returns:
            float: The minimum distance rounded to two decimal places.
    """
    def get_min_dist_between_points(self):
        min_distance = sqrt(pow(self.points_list[1].coord_x - self.points_list[0].coord_x, 2) +
                            pow(self.points_list[1].coord_y - self.points_list[0].coord_y, 2))
        for point1 in self.points_list:
            for point2 in self.points_list:
                if point1 != point2:
                    dist = sqrt(pow(point2.coord_x - point1.coord_x, 2) + pow(point2.coord_y - point1.coord_y, 2))
                    if dist < min_distance:
                        min_distance = dist
        return round(min_distance, 2)

    """Update a point in the repository at a given index.
        Args:
            index (int): The index of the point to be updated.
            x (float): The updated X coordinate.
            y (float): The updated Y coordinate.
            color (str): The updated color.
        Returns:
            MyPoint: The updated point if successful, None otherwise.
    """
    def update_point_given_index(self, index, x, y, color):
        if 0 <= index < len(self.points_list):
            self.points_list[index].coord_x = x
            self.points_list[index].coord_y = y
            self.points_list[index].color = color
            return self.points_list[index]
        else:
            return None

    """Delete a point from the repository based on its index.

        Args:
            index (int): The index of the point to be deleted.
    """
    def delete_point_by_index(self, index):
        if 0 <= index < len(self.points_list):
            self.points_list.pop(index)

    """Delete points inside a given square from the repository.
        Args:
            corner (MyPoint): The upper left corner of the square.
            length (float): The length of the square.
        Returns:
            list: List of points removed from the repository.
    """
    def delete_points_inside_square(self, corner, length):
        points_to_remove = [point for point in self.points_list
                            if corner.coord_x <= point.coord_x <= corner.coord_x + length
                            and corner.coord_y - length <= point.coord_y <= corner.coord_y]

        for point in points_to_remove:
            self.points_list.remove(point)
        return points_to_remove

    """Plot all points in the repository on a chart."""
    def plot_all_points(self):
        colors = {'red': 'r', 'blue': 'b', 'black': 'k', 'green': 'g', 'yellow': 'y', 'purple': 'm', 'cyan': 'c',
                  'white': 'w'}

        for point in self.points_list:
            x = point.coord_x
            y = point.coord_y
            color = colors.get(point.get_color(), 'b')  # Default to blue if color is not recognized

            plt.scatter(x, y, c=color, marker='o', label=f'Point ({x},{y})')

        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        plt.title('Plot of Points')
        plt.legend()
        plt.show()

    """Delete points within a certain distance from a given point.
        Args:
            given_point (MyPoint): The reference point.
            distance (float): The maximum distance for point removal.
        Returns:
            list: List of points removed from the repository.
    """
    def extra_delete_points_within_distance_from_point(self, given_point, distance):
        points_to_remove = [point for point in self.points_list
                            if sqrt(pow(given_point.coord_x - point.coord_x, 2) +
                                    pow(given_point.coord_y - point.coord_y, 2)) <= distance]
        for point in points_to_remove:
            self.points_list.remove(point)
        return points_to_remove

    """Get the maximum distance between any two points in the repository.

        Returns:
            float: The maximum distance rounded to two decimal places.
    """
    def extra_maximum_distance_2_points(self):
        max_distance = sqrt(pow(self.points_list[1].coord_x - self.points_list[0].coord_x, 2) +
                            pow(self.points_list[1].coord_y - self.points_list[0].coord_y, 2))
        for point1 in self.points_list:
            for point2 in self.points_list:
                if point1 != point2:
                    dist = sqrt(pow(point2.coord_x - point1.coord_x, 2) + pow(point2.coord_y - point1.coord_y, 2))
                    if dist > max_distance:
                        max_distance = dist
        return round(max_distance, 2)

    """Shift all points on the X axis by a specified value.

        Args:
            x_value (float): The amount to shift points on the X axis.
    """
    def extra_shift_on_x(self, x_value):
        for point in self.points_list:
            point.coord_x += x_value

    """Return a string representation of the points list.

        Returns:
            str: A formatted string containing information about each point.
    """
    def __str__(self):
        result = "The points list is: "
        for point in self.points_list:
            result += f"\n{point}"
        return result
