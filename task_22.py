#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    while not wall_is_on_the_right():
        fill_cell()
        move_right()
    right = False
    while not wall_is_beneath():
        fill_cell()
        move_down()
        if right:
            while not wall_is_on_the_right():
                fill_cell()
                move_right()
        else:
            while not wall_is_on_the_left():
                fill_cell()
                move_left()
        right = not right
    fill_cell()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
