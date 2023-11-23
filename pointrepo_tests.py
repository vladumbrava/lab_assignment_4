from mypoint import MyPoint
from pointrepo import PointRepository


def test_add_new_point():
    repository = PointRepository()
    valid_point = MyPoint(-1, 2, "red")
    repository.add_new_point(valid_point)

    assert len(repository.points_list) == 1
    assert valid_point in repository.points_list


def test_get_list_of_points():
    repository = PointRepository()

    sample_points = [
        MyPoint(-1, 2, "red"),
        MyPoint(3, 4, "blue"),
        MyPoint(0, 0, "green")
    ]

    repository.set_list_of_points(sample_points)
    retrieved_points = repository.get_list_of_points()
    assert retrieved_points == sample_points


def test_set_list_of_points():
    repository = PointRepository()
    points = [
        MyPoint(-1, 2, "red"),
        MyPoint(-1, 2, "red"),
        MyPoint(3, 4, "blue"),
        MyPoint(0, 0, "green")
    ]
    repository.set_list_of_points(points)
    assert repository.points_list == points


def test_get_point_given_index():
    repository = PointRepository()
    point1 = MyPoint(1, 2, "red")
    point2 = MyPoint(3, 4, "blue")
    point3 = MyPoint(5, 6, "green")
    repository.add_new_point(point1)
    repository.add_new_point(point2)
    repository.add_new_point(point3)

    index = len(repository.get_list_of_points()) - 1
    point = repository.get_point_given_index(index)

    assert point == point3


def test_get_points_given_color():
    repository = PointRepository()
    color_list = repository.get_points_given_color("red")
    assert color_list == []

    repository = PointRepository()
    point1 = MyPoint(1, 2, "red")
    repository.add_new_point(point1)
    color_list = repository.get_points_given_color("red")
    assert color_list == [point1]


def test_get_points_inside_square():
    repository = PointRepository()

    point1 = MyPoint(1, 2, "red")
    point2 = MyPoint(3, 4, "blue")
    point3 = MyPoint(5, 6, "green")
    repository.add_new_point(point1)
    repository.add_new_point(point2)
    repository.add_new_point(point3)

    corner = MyPoint(-5, 5, "black")
    length = 10

    result = repository.get_points_inside_square(corner, length)

    assert "The points inside the given square are:" in result

    corner = MyPoint(0, 0, "black")
    length = -5
    result = repository.get_points_inside_square(corner, length)
    assert result == ""

def test_get_min_dist_between_points():
    repository = PointRepository()

    point1 = MyPoint(0, 0, "red")
    point2 = MyPoint(0, 0, "red")

    repository.add_new_point(point1)
    repository.add_new_point(point2)

    assert repository.get_min_dist_between_points() == 0.0

def test_update_point_given_index():
    repository = PointRepository()

    point1 = MyPoint(1, 2, "red")
    point2 = MyPoint(3, 4, "blue")
    point3 = MyPoint(5, 6, "green")

    repository.add_new_point(point1)
    repository.add_new_point(point2)
    repository.add_new_point(point3)

    updated_point = repository.update_point_given_index(-1, 7, 8, "yellow")

    assert updated_point is None

def test_delete_point_by_index():
    repository = PointRepository()
    point1 = MyPoint(1, 2, "red")
    point2 = MyPoint(3, 4, "blue")
    point3 = MyPoint(5, 6, "green")
    repository.add_new_point(point1)
    repository.add_new_point(point2)
    repository.add_new_point(point3)

    repository.delete_point_by_index(2)

    assert len(repository.get_list_of_points()) == 2
    assert repository.get_list_of_points()[0] == point1
    assert repository.get_list_of_points()[1] == point2

def test_delete_points_inside_square():
    repository = PointRepository()

    corner = MyPoint(2, 3, "black")
    length = 3

    removed_points = repository.delete_points_inside_square(corner, length)

    assert len(repository.get_list_of_points()) == 0
    assert removed_points == []

def test_extra_delete_points_within_distance_from_point():
    repository = PointRepository()

    point1 = MyPoint(1, 2, "red")
    point2 = MyPoint(3, 4, "blue")
    point3 = MyPoint(5, 6, "green")
    point4 = MyPoint(7, 8, "red")

    repository.add_new_point(point1)
    repository.add_new_point(point2)
    repository.add_new_point(point3)
    repository.add_new_point(point4)

    given_point = MyPoint(12, 20, "red")
    distance = 1
    removed_points = repository.extra_delete_points_within_distance_from_point(given_point, distance)

    assert removed_points == []
    assert repository.get_list_of_points() == [point1, point2, point3, point4]

def test_extra_maximum_distance_2_points():
    repository = PointRepository()
    point1 = MyPoint(0, 0, "red")
    point2 = MyPoint(3, 4, "blue")
    point3 = MyPoint(6, 8, "green")
    repository.add_new_point(point1)
    repository.add_new_point(point2)
    repository.add_new_point(point3)

    assert repository.extra_maximum_distance_2_points() == 10.0

def test_extra_shift_on_x():
    repository = PointRepository()
    point1 = MyPoint(1, 2, "red")
    point2 = MyPoint(3, 4, "blue")
    point3 = MyPoint(5, 6, "green")
    repository.add_new_point(point1)
    repository.add_new_point(point2)
    repository.add_new_point(point3)

    repository.extra_shift_on_x(2)

    assert point1.coord_x == 3
    assert point2.coord_x == 5
    assert point3.coord_x == 7