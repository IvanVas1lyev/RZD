import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import itertools
import json

from drawing import *
from check_functions import *
from generate_docx import *


def read_data() -> list:
    """
    read data from inputs and convert to list of lists
    """
    f = open("data.json", "r")
    raw = f.read()
    data_dict = json.loads(raw)
    data_arr = []

    for key, value in data_dict.items():
        if key != 'name' and key != 'cargoCount':
            data_arr.append([float(value['length']), float(value['width']), float(value['height']), int(value['count']), float(value['weight'])])
        if key == 'name':
            data_arr.append(value)

    return data_arr


def main():
    params_list = read_data()

    name = params_list[-1]
    params_list.pop()
    unique_count = len(params_list)

    shipments_numbers = []
    res = []

    for i in range(unique_count):
        shipments_numbers += params_list[i][3] * [i + 1]

    for permutation in itertools.permutations(shipments_numbers):
        res = check_shipments_order(permutation, params_list)

        if len(res):
            break

    if not len(res):
        print('Данные грузы невозможно разместить на платформе')
        return -1

    generate_doc(params_list, res[1], name)

    correct_permutation_params = res[0]

    pygame.init()
    display = (1500, 900)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 52.0)
    glTranslatef(0, -2.5, -20)
    glClearColor(background_color[0], background_color[1], background_color[2], 0.5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_field(0, -0.6, 0)

        draw_wheel(1, -0.6, 3.5)
        draw_wheel(1, -0.6, 4.5)
        draw_wheel(-1, -0.6, 3.5)
        draw_wheel(-1, -0.6, 4.5)

        draw_wheel(1, -0.6, -3.5)
        draw_wheel(1, -0.6, -4.5)
        draw_wheel(-1, -0.6, -3.5)
        draw_wheel(-1, -0.6, -4.5)

        draw_back_wheels()
        draw_front_wheels()

        draw_platform()


        draw_shipments(correct_permutation_params)

        pygame.display.set_caption(name)
        pygame.display.flip()

        pygame.time.wait(10)


main()
