import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

import numpy as np
import itertools
import json

from drawing import *
from check_functions import *


def read_data():
    f = open("data.json", "r")
    raw = f.read()
    data = json.loads(raw)
    arr = []

    for value in data.values():
        arr.append([float(value['length']), float(value['width']), float(value['height']), int(value['count']), float(value['weight'])])

    return arr


def main():
    unique_count = 4  # int(input())  # количество грузов
    name = 'efvef'  # input("Название груза: ")  # название груза
    # params_list = [[int(i) for i in input().split()] for _ in range(unique_count)]  # длина, ширина, высота, кол-во, вес 1 шт
    params_list = read_data()
    shipments_numbers = []

    for i in range(unique_count):
        shipments_numbers += params_list[i][3] * [i + 1]

    correct_permutation_params = []

    for permutation in itertools.permutations(shipments_numbers):
        correct_permutation_params = check_shipments_order(permutation, params_list)

        if len(correct_permutation_params):
            break

    if not len(correct_permutation_params):
        print("Данные грузы невозможно разместить на платформе")
        return -1

    pygame.init()
    display = (1200, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 52.0)
    glTranslatef(0, -2, -15)
    glClearColor(background_color[0], background_color[1], background_color[2], 0.5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

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

        pygame.display.flip()
        pygame.time.wait(10)


main()
