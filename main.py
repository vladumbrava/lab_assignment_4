from mypoint import MyPoint
from pointrepo import PointRepository


def main():
    repository = PointRepository()
    point1 = MyPoint(-1, 5, "red")
    point2 = MyPoint(-10, 2, "red")
    point3 = MyPoint(4, 6, "blue")
    point4 = MyPoint(1, -2, "blue")
    point5 = MyPoint(2, 4, "magenta")
    point6 = MyPoint(-6, 14, "yellow")
    point7 = MyPoint(-20, 6, "green")
    pointlist = [point1, point2, point3, point4, point5, point6, point7]

    repository.set_list_of_points(pointlist)

    while True:
        print("\nMenu")
        print("1. Add a point")
        print("2. Get all points")
        print("3. Get a point at a given index")
        print("4. Get all points of a given color")
        print("5. Get all points inside a given square")
        print("6. Get the minimum distance between two points")
        print("7. Update a point at a given index")
        print("8. Delete a point by index")
        print("9. Delete all points that are inside a given square")
        print("10. Plot all points in a chart")
        print("11. Extra functions")
        print("12. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            while True:
                print("Choose the properties of your point:")
                try:
                    coord_x = float(input("Enter the X: "))
                    coord_y = float(input("Enter the Y: "))
                except ValueError:
                    print("Invalid input. Please enter proper properties.")
                    break
                color = input("Enter the color('red', 'green', 'blue', 'yellow', 'magenta'): ")
                if color != "red" and color != "green" and color != "blue" and color != "yellow" and color != "magenta":
                    print("Invalid input. Please enter proper properties.")
                    break
                else:
                    repository.add_new_point(MyPoint(coord_x, coord_y, color))
                    print(repository)
                    break

        if choice == 2:
            print(f"The points in the repository are:")
            for point in repository.get_list_of_points():
                print(point)

        if choice == 3:
            try:
                index = int(input("Please enter the index:"))
                if 0 <= index <= len(repository.get_list_of_points()) - 1:
                    print(f"The point at index {index} is: {repository.get_point_given_index(index)}")
                else:
                    print("Invalid input. Please enter an appropriate value for index.")
            except ValueError:
                print("Invalid input. Please enter an integer value.")

        if choice == 4:
            color = input("Please enter a color: ")
            points_of_given_color = repository.get_points_given_color(color)
            if color != "red" and color != "green" and color != "blue" and color != "yellow" and color != "magenta":
                print("Invalid input. Please enter a proper color.")
            else:
                if len(points_of_given_color) == 0:
                    print(f"There are no points of color {color}.")
                else:
                    print(f"The points of color {color} are the following:")
                    for point in points_of_given_color:
                        print(point)

        if choice == 5:
            while True:
                print("Enter the coordinates of the upper left corner of the square: ")
                try:
                    corner_x = float(input("Enter the X: "))
                    corner_y = float(input("Enter the Y: "))
                except ValueError:
                    print("Invalid input. Please enter proper coordinates.")
                    break
                try:
                    length = float(input("Enter the length of the square: "))
                    print(repository.get_points_inside_square(MyPoint(corner_x, corner_y, None), length))
                    break
                except ValueError:
                    print("Invalid input. Please enter a proper length.")
                    break

        if choice == 6:
            print(f"The minimum distance between 2 points from our list is: {repository.get_min_dist_between_points()}")

        if choice == 7:
            while True:
                try:
                    index = int(input("Enter the index of the point: "))
                    if 0 <= index < len(repository.get_list_of_points()):
                        try:
                            updated_x = float(input("Enter the updated X: "))
                            updated_y = float(input("Enter the updated Y: "))
                        except ValueError:
                            print("Invalid input. Please enter proper coordinates.")
                            break
                        color = input("Enter the updated color: ")
                        if color != "red" and color != "green" and color != "blue" and color != "yellow" and color != "magenta":
                            print("Invalid input. Please enter proper properties.")
                            break
                        else:
                            repository.update_point_given_index(index, updated_x, updated_y, color)
                            print(f"The point at index {index} is now: ")
                            print(repository.update_point_given_index(index, updated_x, updated_y, color))
                            break
                    else:
                        print("Invalid input. Enter a proper index.")
                        break
                except ValueError:
                    print("Invalid input. Enter a proper index.")
                    break

        if choice == 8:
            try:
                index = int(input("Enter the index: "))
                if 0 <= index < len(repository.get_list_of_points()):
                    repository.delete_point_by_index(index)
                else:
                    print("Invalid input. Please enter a proper index.")
            except ValueError:
                print("Invalid input. The index should be an integer.")

        if choice == 9:
            print("Enter the coordinates of the upper left corner of the square: ")
            try:
                corner_x = float(input("Enter the X: "))
                corner_y = float(input("Enter the Y: "))
                try:
                    length = float(input("Enter the length of the square: "))
                    points_removed = repository.delete_points_inside_square(MyPoint(corner_x, corner_y, None), length)
                    print("The following points were removed: ")
                    for point in points_removed:
                        print(point)
                except ValueError:
                    print("Invalid input. Please enter a proper length.")
            except ValueError:
                print("Invalid input. Please enter proper coordinates.")

        if choice == 10:
            repository.plot_all_points()

        if choice == 11:

            print("1. Delete all points within a certain distance from a given point")
            print("2. Get the maximum distance between 2 points")
            print("3. Shift all points on the X axis")

            try:
                extra_choice = int(input("Enter your choice: "))
                if extra_choice in [1, 2, 3]:
                    if extra_choice == 1:
                        print("Enter the coordinates of the point: ")
                        try:
                            x = float(input("Enter the X: "))
                            y = float(input("Enter the Y: "))
                            try:
                                distance = float(input("Enter the distance: "))
                                points_removed = repository.extra_delete_points_within_distance_from_point(MyPoint(x, y, None), distance)
                                print("The following points were removed: ")
                                for point in points_removed:
                                    print(point)
                            except ValueError:
                                print("Invalid input. Please enter a proper distance.")
                        except ValueError:
                            print("Invalid input. Please enter proper coordinates.")

                    if extra_choice == 2:
                        print(f"The maximum distance between 2 points from our list is: {repository.extra_maximum_distance_2_points()}")

                    if extra_choice == 3:
                        try:
                            x_value = float(input("Enter the amount you want to shift the points by: "))
                            repository.extra_shift_on_x(x_value)
                        except ValueError:
                            print("Invalid input. You should enter a proper value.")
                else:
                    print("Invalid input. Please choose a value between 1, 2 and 3.")
            except ValueError:
                print("Invalid input. Please enter a proper choice value.")

        if choice == 12:
            break


if __name__ == "__main__":
    main()
