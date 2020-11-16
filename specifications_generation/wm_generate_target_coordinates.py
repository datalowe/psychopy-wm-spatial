"""
Script for generating specifications of, for each trial, in which sequence 
targets should light up. Note that target numbering is arbitrary and has 
nothing to do with where targets are placed. This script is for helping 
you make sure that targets are placed in the same positions every time 
the experiment is run.

Use this script if you want the targets to be in the same positions for every
participant. If you instead want sequences to be randomly generated
for each experiment run, you don't need this.

Make specifications by changing the values given to constants (in ALL CAPS)
below. Then run the script, and the result will be saved to
'generated_target_coordinates.txt' in this folder. Then, open up the experiment's
.psyexp file with PsychoPy Builder, go to the 'instructions' routine and open up
'code_constants'. Scroll down to 'TARGET_SEQUENCES = []'. Copy->paste in the
.txt file's content, replacing the square brackets ('[]').
"""
from random import uniform

# width/height of area where targets
# can appear, in degrees
AREA_WIDTH_DEG = 22
AREA_HEIGHT_DEG = 13

# target size, in degrees
TARGET_SIZE_DEG = 2.5

# minimum distance between targets.
# this is the distance between targets' CENTRES,
# meaning a distance of 0 would indicate that two
# targets perfectly overlap.
# PLEASE NOTE that if you set this minimum distance
# to a value that's too high, PsychoPy will become stuck
# in an infinite loop. so please think carefully about
# how much space is available (area width/height) for
# distanced targets to fit
MIN_TARGET_DISTANCE = TARGET_SIZE_DEG * 2.2

# number of potential targets to show in each trial
NUM_TARGETS = 9


class Point:
    """
    Represents (x, y) coordinates in 2-dimensional space.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        """
        Returns the euclidean distance between this and the
        other passed point.
        """
        dist = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** (1 / 2)
        return dist

    def __str__(self):
        """
        Returns a string representation '(x, y)' of this point.
        """
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        """
        Returns a description of how this point can be
        recreated.
        """
        return "Point({}, {})".format(self.x, self.y)

    def as_tuple(self):
        """
        Returns a (x, y) tuple with this point's x/y coordinates.
        """
        return self.x, self.y


def points_collide(point_ls, new_point):
    """
    Goes through a list of Point instances and compares
    the new_point to see if the new_point is too close
    to one of the points in the point_ls. Returns True if
    there is a collision, otherwise False.
    """
    collides = False
    for old_point in point_ls:
        if (new_point - old_point) < MIN_TARGET_DISTANCE:
            collides = True
            break
    return collides


def gen_rand_point():
    """
    Generates a random point within the target area.
    """
    x_coord = uniform(-AREA_WIDTH_DEG // 2, AREA_WIDTH_DEG // 2)
    y_coord = uniform(-AREA_HEIGHT_DEG // 2, AREA_HEIGHT_DEG // 2)
    x_coord, y_coord = round(x_coord, 3), round(y_coord, 3)
    return Point(x_coord, y_coord)


def gen_point_ls():
    """
    Generates a list of (x, y) coordinate Point instances until
    there are as many instances as there should be targets/trial.
    """
    finished_list = False
    while not finished_list:
        collision_counter = 0
        point_ls = []
        while len(point_ls) < NUM_TARGETS:
            new_point = gen_rand_point()
            if points_collide(point_ls, new_point):
                collision_counter += 1
            else:
                point_ls.append(new_point)
            if collision_counter > 200:
                break
        if len(point_ls) == NUM_TARGETS:
            finished_list = True
    return point_ls


# randomly generate (x, y) coordinates for the targets
point_ls = gen_point_ls()

out_str = '(\n'
for point in point_ls:
    out_str += f'    {str(point)},\n'
out_str += ')'

with open('generated_target_coordinates.txt', 'w') as f:
    f.write(out_str)
