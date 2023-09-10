from OpenGL.GL import *
from constants import *
import math


def draw_platform() -> None:
    """
    draw platform of railway carriage
    """
    # правая и левая части
    glColor3f(platform_sides_color[0], platform_sides_color[1], platform_sides_color[2])

    glBegin(GL_TRIANGLES)
    glVertex3fv((1.4, 0.2, 6.7))
    glVertex3fv((1.4, 0.2, -6.7))
    glVertex3fv((1.4, -0.2, 5.5))

    glVertex3fv((1.4, 0.2, -6.7))
    glVertex3fv((1.4, -0.2, -5.5))
    glVertex3fv((1.4, -0.2, 5.5))

    glVertex3fv((-1.4, 0.2, 6.7))
    glVertex3fv((-1.4, 0.2, -6.7))
    glVertex3fv((-1.4, -0.2, 5.5))

    glVertex3fv((-1.4, 0.2, -6.7))
    glVertex3fv((-1.4, -0.2, -5.5))
    glVertex3fv((-1.4, -0.2, 5.5))
    glEnd()

    # передняя и задняя части
    glColor3f(platform_sides_color[0], platform_sides_color[1], platform_sides_color[2])

    glBegin(GL_TRIANGLES)
    glVertex3fv((1.4, 0.2, 6.7))
    glVertex3fv((1.4, -0.2, 5.5))
    glVertex3fv((-1.4, 0.2, 6.7))

    glVertex3fv((-1.4, 0.2, 6.7))
    glVertex3fv((-1.4, -0.2, 5.5))
    glVertex3fv((1.4, -0.2, 5.5))

    glVertex3fv((1.4, 0.2, -6.7))
    glVertex3fv((1.4, -0.2, -5.5))
    glVertex3fv((-1.4, 0.2, -6.7))

    glVertex3fv((-1.4, 0.2, -6.7))
    glVertex3fv((-1.4, -0.2, -5.5))
    glVertex3fv((1.4, -0.2, -5.5))
    glEnd()

    # верхняя часть
    glColor3f(platform_top_color[0], platform_top_color[1], platform_top_color[2])

    glBegin(GL_TRIANGLES)
    glVertex3fv((-1.4, 0.2, 6.7))
    glVertex3fv((-1.4, 0.2, -6.7))
    glVertex3fv((1.4, 0.2, 6.7))

    glVertex3fv((-1.4, 0.2, -6.7))
    glVertex3fv((1.4, 0.2, -6.7))
    glVertex3fv((1.4, 0.2, 6.7))
    glEnd()


def draw_back_wheels() -> None:
    """
    draw back wheels platform of railway carriage
    """
    # правая и левая части
    glColor3f(platform_wheels_color[0], platform_wheels_color[1], platform_wheels_color[2])

    glBegin(GL_TRIANGLES)
    glVertex3fv((1, -0.2, -3))
    glVertex3fv((1, -0.2, -5))
    glVertex3fv((1, -0.8, -3.5))

    glVertex3fv((1, -0.2, -5))
    glVertex3fv((1, -0.8, -4.5))
    glVertex3fv((1, -0.8, -3.5))

    glVertex3fv((-1, -0.2, -3))
    glVertex3fv((-1, -0.2, -5))
    glVertex3fv((-1, -0.8, -3.5))

    glVertex3fv((-1, -0.2, -5))
    glVertex3fv((-1, -0.8, -4.5))
    glVertex3fv((-1, -0.8, -3.5))
    glEnd()

    # передняя и задняя части
    glColor3f(platform_wheels_color[0], platform_wheels_color[1], platform_wheels_color[2])

    glBegin(GL_TRIANGLES)
    glVertex3fv((1, -0.2, -3))
    glVertex3fv((1, -0.8, -3.5))
    glVertex3fv((-1, -0.2, -3))

    glVertex3fv((-1, -0.2, -3))
    glVertex3fv((-1, -0.8, -3.5))
    glVertex3fv((1, -0.8, -3.5))

    glVertex3fv((1, -0.2, -5))
    glVertex3fv((1, -0.8, -4.5))
    glVertex3fv((-1, -0.2, -5))

    glVertex3fv((-1, -0.2, -5))
    glVertex3fv((-1, -0.8, -4.5))
    glVertex3fv((1, -0.8, -4.5))
    glEnd()


def draw_front_wheels() -> None:
    """
    draw back wheels platform of railway carriage
    """
    # правая и левая части
    glColor3f(platform_wheels_color[0], platform_wheels_color[1], platform_wheels_color[2])

    glBegin(GL_TRIANGLES)
    glVertex3fv((1, -0.2, 3))
    glVertex3fv((1, -0.2, 5))
    glVertex3fv((1, -0.8, 3.5))

    glVertex3fv((1, -0.2, 5))
    glVertex3fv((1, -0.8, 4.5))
    glVertex3fv((1, -0.8, 3.5))

    glVertex3fv((-1, -0.2, 3))
    glVertex3fv((-1, -0.2, 5))
    glVertex3fv((-1, -0.8, 3.5))

    glVertex3fv((-1, -0.2, 5))
    glVertex3fv((-1, -0.8, 4.5))
    glVertex3fv((-1, -0.8, 3.5))
    glEnd()

    # передняя и задняя части
    glColor3f(platform_wheels_color[0], platform_wheels_color[1], platform_wheels_color[2])

    glBegin(GL_TRIANGLES)
    glVertex3fv((1, -0.2, 3))
    glVertex3fv((1, -0.8, 3.5))
    glVertex3fv((-1, -0.2, 3))

    glVertex3fv((-1, -0.2, 3))
    glVertex3fv((-1, -0.8, 3.5))
    glVertex3fv((1, -0.8, 3.5))

    glVertex3fv((1, -0.2, 5))
    glVertex3fv((1, -0.8, 4.5))
    glVertex3fv((-1, -0.2, 5))

    glVertex3fv((-1, -0.2, 5))
    glVertex3fv((-1, -0.8, 4.5))
    glVertex3fv((1, -0.8, 4.5))
    glEnd()


def draw_wheel(cx, cy, cz) -> None:
    """
    draw wheels of railway carriage
    :param cx: x-coordinate of center of wheel
    :param cy: y-coordinate of center of wheel
    :param cz: z-coordinate of center of wheel
    """
    n = 50
    radius = 0.4

    glColor3f(wheels_color[0], wheels_color[1], wheels_color[2])
    glBegin(GL_TRIANGLES)

    for i in range(n):
        theta1 = 2.0 * 3.1415926 * i / n
        theta2 = 2.0 * 3.1415926 * (i + 1) / n

        y1 = radius * math.sin(theta1)
        z1 = radius * math.cos(theta1)
        y2 = radius * math.sin(theta2)
        z2 = radius * math.cos(theta2)

        glVertex3fv((cx, y1 + cy, z1 + cz))
        glVertex3fv((cx, y2 + cy, z2 + cz))
        glVertex3fv((cx, cy, cz))

    glEnd()

def draw_field(cx, cy, cz) -> None:
    """
    draw field
    :param cx: x-coordinate of center of field
    :param cy: y-coordinate of center of field
    :param cz: z-coordinate of center of field
    """
    n = 50
    radius = 8

    glColor3f(field_color[0], field_color[1], field_color[2])
    glBegin(GL_TRIANGLES)

    for i in range(n):
        theta1 = 2.0 * 3.1415926 * i / n
        theta2 = 2.0 * 3.1415926 * (i + 1) / n

        x1 = radius * math.sin(theta1)
        z1 = radius * math.cos(theta1)
        x2 = radius * math.sin(theta2)
        z2 = radius * math.cos(theta2)

        glVertex3fv((x1 + cx, cy, z1 + cz))
        glVertex3fv((x2 + cx, cy, z2 + cz))
        glVertex3fv((cx, cy, cz))

    glEnd()


def draw_shipments(correct_permutation_params: list) -> None:
    """
    draw shipments with correct permutation order
    :param correct_permutation_params: list of shipments params: start and end coordinates, width and height in mm
    """

    for shipment in correct_permutation_params:
        start = (shipment[0] - 6700) / 1000
        end = (shipment[1] - 6700) / 1000
        width = shipment[2] / 1000
        height = shipment[3] / 1000

        glColor3f(shipments_color[0], shipments_color[1], shipments_color[2])
        glBegin(GL_TRIANGLES)
        # боковые стороны груза
        glVertex3fv((width / 2, 0.2, start))
        glVertex3fv((width / 2, 0.2 + height, start))
        glVertex3fv((width / 2, 0.2 + height, end))

        glVertex3fv((width / 2, 0.2, start))
        glVertex3fv((width / 2, 0.2 + height, end))
        glVertex3fv((width / 2, 0.2, end))

        glVertex3fv((- width / 2, 0.2, start))
        glVertex3fv((- width / 2, 0.2 + height, start))
        glVertex3fv((- width / 2, 0.2 + height, end))

        glVertex3fv((- width / 2, 0.2, start))
        glVertex3fv((- width / 2, 0.2 + height, end))
        glVertex3fv((- width / 2, 0.2, end))

        # верхняя часть груза
        glVertex3fv((width / 2, 0.2 + height, start))
        glVertex3fv((- width / 2, 0.2 + height, start))
        glVertex3fv((- width / 2, 0.2 + height, end))

        glVertex3fv((width / 2, 0.2 + height, start))
        glVertex3fv((- width / 2, 0.2 + height, end))
        glVertex3fv((width / 2, 0.2 + height, end))

        # передняя и задняя стороны груза
        glVertex3fv((width / 2, 0.2, start))
        glVertex3fv((- width / 2, 0.2, start))
        glVertex3fv((- width / 2, 0.2 + height, start))

        glVertex3fv((width / 2, 0.2 + height, start))
        glVertex3fv((- width / 2, 0.2 + height, start))
        glVertex3fv((width / 2, 0.2, start))

        glVertex3fv((width / 2, 0.2, end))
        glVertex3fv((- width / 2, 0.2, end))
        glVertex3fv((- width / 2, 0.2 + height, end))

        glVertex3fv((width / 2, 0.2 + height, end))
        glVertex3fv((- width / 2, 0.2 + height, end))
        glVertex3fv((width / 2, 0.2, end))
        glEnd()
