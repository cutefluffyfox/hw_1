#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    y = 0
    x = 0
    size = 0
    while not wall_is_on_the_right():
        move_right()
        size += 1
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_beneath():
        while not wall_is_on_the_right():
            if y != x and size - x != y:
                fill_cell()
            x += 1
            move_right()
        if y != x and size - x != y:
            fill_cell()
        x = 0
        while not wall_is_on_the_left():
            move_left()
        y += 1
        move_down()
    while not wall_is_on_the_right():
        if y != x and size - x != y:
            fill_cell()
        x += 1
        move_right()
    if y != x and size - x != y:
        fill_cell()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
