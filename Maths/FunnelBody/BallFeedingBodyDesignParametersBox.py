#!/usr/bin/python3

# This program is based on maths conducted in "Ball Feeding - Designing Funnel Body.pdf"
# It involves calculating the shape of the 4 triangles that come together to form
# the rectangular pyramid of the funnel.

# INPUT:
# Currently, input parameters are provided via constants within the program itself
# rather than via command line arguments

# OUTPUT:
# The program uses standard output to describe each isosceles triangle and the 
# scalene triangle. For a particular triangle that looks like this:
#                       A
#                       /\
#                   a  /  \  b
#                     /____\
#                   B   c   C
# the program will 'print' this triangle, by printing the side lengths first in
# the order a, b and c, before printing the angle sizes next in the order 
# ABC, BAC, ACB.

#   General output:

#   Triangle 1 (isosceles 1):
#   Sides: {side_1}, {side_2}, {side_3}
#   Angles: {angle_1}, {angle_2}, {angle_3}
#
#   Triangle 2 (isosceles 2):
#   Sides: {side_1}, {side_2}, {side_3}
#   Angles: {angle_1}, {angle_2}, {angle_3}
#
#   Triangle 3 (scalene):
#   Sides: {side_1}, {side_2}, {side_3}
#   Angles: {angle_1}, {angle_2}, {angle_3}


# EXECUTION:
# To run the program, either do 
#       python3 BallFeedingFunnelParametersTake2.py 
# or ensure you provide exuction permissions via 
#       chmod +x BallFeedingFunnelParametersTake2.py (one time only)
# before running 
#       ./BallFeedingFunnelParametersTake2.py


# NOTE: Dimensions are in centimetres because I don't have the brain power to handle 
# millimetres

import math

### Constants (should be based on the container and the position of the rotor hole) ###

CONTAINER_SIDE_1 = 52       # will be used as the base length for the isosceles triangles
CONTAINER_SIDE_2 = 34       # will be used as the 'base' length for the scalene triangles

HOLE_DIST_1 = 9           # corresponds to x1 in the accompanying working out
HOLE_DIST_2 = CONTAINER_SIDE_2 - HOLE_DIST_1          # corresponds to x2 in the accompanying working out

### Hyperparameters (I decide these values) ###

Z = 2                       # refers to the perpendicular height of the pyramid


### Math Formulas ###
def pythag(a, b):
    return math.sqrt(pow(a, 2) + pow(b, 2))

# Using the form, c^2 = a^2 + b^2 - 2 a b cos(theta), solves for theta in degrees
def cosineFindAngle(c, a, b):
    return math.degrees(
        math.acos(
            (pow(c, 2) - pow(a, 2) - pow(b, 2)) / (-2 * a * b)
        )
    )

### Helpers ###
# Diagram:
#                       A
#                       /\
#                   a  /  \  b
#                     /____\
#                   B   c   C
# gets the angles ABC, BAC and ACB in that order, given side lengths a, b, c in that order
def getAnglesOfTriangle(a, b, c):
    angle1 = cosineFindAngle(b, a, c)
    angle2 = cosineFindAngle(c, a, b)
    angle3 = cosineFindAngle(a, b, c)

    return (angle1, angle2, angle3)


# returns the perpendicular heights of each isosceles triangle and the common base length
def getFundamentalKnowledgeIsosceles():

    h1 = pythag(Z, HOLE_DIST_1)
    h2 = pythag(Z, HOLE_DIST_2)

    return (h1, h2, CONTAINER_SIDE_1)

def getSideLengthKnowledgeIsosceles(perp_height, base):
    a = pythag(base / 2, perp_height)
    return (a, a, base)

def getAngleKnowledgeIsosceles(a, base):
    return getAnglesOfTriangle(a, a, base)


# returns the 3 side lengths of the scalene triangles
def getFundamentalKnowledgeScalene(a: float, b: float):
    return (a, b, CONTAINER_SIDE_2)

def getAngleKnowledgeScalene(a, b, c):
    return getAnglesOfTriangle(a, b, c)


def constructPoints():
    return


def main():
    h1, h2, isoscelese_base = getFundamentalKnowledgeIsosceles()
    a, a, isoscelese_base = getSideLengthKnowledgeIsosceles(h1, isoscelese_base)
    b, b, isoscelese_base = getSideLengthKnowledgeIsosceles(h2, isoscelese_base)

    t1, t2, t3 = getAngleKnowledgeIsosceles(a, isoscelese_base)
    s1, s2, s3 = getAngleKnowledgeIsosceles(b, isoscelese_base)

    a, b, c = getFundamentalKnowledgeScalene(a, b)

    u1, u2, u3 = getAngleKnowledgeScalene(a, b, c)

    print(f"Triangle 1 (isosceles 1):\nSides: {a}, {a}, {isoscelese_base}\nAngles: {t1}, {t2}, {t3}\n")
    print(f"Triangle 2 (isosceles 2):\nSides: {b}, {b}, {isoscelese_base}\nAngles: {s1}, {s2}, {s3}\n")
    print(f"Triangle 3 (scalene):\nSides: {a}, {b}, {c}\nAngles: {u1}, {u2}, {u3}")

    theta = (t2 + s2 + 2 * u2)


    # theta / 360 * c = 7 pi ==> c = 360 * 7 * pi / theta
    
    print(f"Sum of angles at a point = {t2 + s2 + 2 * u2}")

    print(f"Final circumference = {math.pi * 7}")
    print(f"Initial circumference = {(360 * 7 * math.pi) / theta}")
    initCircumference = (360 * 7 * math.pi) / theta
    print(f"init diameter = {initCircumference / ( math.pi)}")




    return 0

if __name__ == "__main__":
    main()
    exit(0)