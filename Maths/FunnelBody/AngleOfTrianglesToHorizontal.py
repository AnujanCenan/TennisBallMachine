#!/usr/bin/python3

# Based on the working done in " TODO: write working  "

# Initially we found the sizes of the triangles that will be used to form the funnel
# body. Using cardboard and paper models, we are able to confirm whether or not 
# such triangle sizes are suitable to the container we are using for ball feeding.
# However, for the use of wood, it is essential to know at what angle the different 
# triangles intersect each other. That is the purpose of this program.

# INPUT
# Length and width of the rectangular base of the pyramid
# Shortest horizontal distance from the smaller isosceles triangle to the apex

# OUTPUT
# Each line provides the angle between the XY plane (the horizontal/floor plane)
# and plane that one of the triangles lies in.
# General output
# T1: <angle between XY-Plane and T1 (small isosceles) Plane>
# T2: <angle between XY-Plane and T2 (large isosceles) Plane>
# T31: <angle between XY-Plane and T31 (scalene 1) Plane>
# T32: <angle between XY-Plane and T32 (scalene 2) Plane>

import math
import numpy as np
import sys

class InvalidVectorSize(Exception):
    def __init__(self):
        super().__init__("Ensure vectors are of the same size\n")


def subractVectors(a: list[float], b: list[float]) -> list[float]:
    if len(a) != len(b):
        raise InvalidVectorSize()
    return [x - y for x, y in list(zip(a, b))]

def generatePlaneEquation(a: list[float], b: list[float], c: list[float]) -> list[list[float]]:
    return [a, subractVectors(b, a), subractVectors(c, a)]

def solveForPlaneNormal(plane):
    directionVector1 = plane[1]
    directionVector2 = plane[2]

    linearMatrix = np.array([
        directionVector1, 
        directionVector2,
        [0, 0, 1]
    ])

    return np.linalg.solve(linearMatrix, [0, 0, 100])

def dotProduct(a: list[float], b: list[float]):
    if len(a) != len(b):
        raise InvalidVectorSize()
    
    return sum([x * y for x, y in list(zip(a, b))])
    
def vectorMagnitude(vector):
    return math.sqrt(sum([pow(x, 2) for x in vector]))

def angleBetweenTwoVectors(a, b):
    
    return math.degrees(
        math.acos( 
            dotProduct(a, b) / (vectorMagnitude(a) * vectorMagnitude(b)) 
            )
    )


def main(pyramidLength=52, pyramidWidth=34, pyramidHeight=2, horizontalApexDistance=9):

    # generate plane equations
    apexPositionVector = [horizontalApexDistance, pyramidLength / 2, -pyramidHeight]
    planeT1 = generatePlaneEquation(a=[0,0,0], b=[0, pyramidLength, 0], c=apexPositionVector)
    planeT2 = generatePlaneEquation(a=[pyramidWidth,0,0], b=[pyramidWidth, pyramidLength, 0], c=apexPositionVector)
    planeT31 = generatePlaneEquation(a=[0, 0, 0], b=[pyramidWidth, 0, 0], c=apexPositionVector)
    planeT32 = generatePlaneEquation(a=[0, pyramidLength, 0], b=[pyramidWidth, pyramidLength, 0], c=apexPositionVector)

    # by construction, the normal of the rectangular face
    rectangleNormal = [0, 0, 1]     

    # solve for the normal of each plane
    t1Normal = solveForPlaneNormal(planeT1)
    t2Normal = solveForPlaneNormal(planeT2)
    t31Normal = solveForPlaneNormal(planeT31)
    t32Normal = solveForPlaneNormal(planeT32)

    # # find the angle between each plane (or normal) and the xy plane
    t1Angle = angleBetweenTwoVectors(t1Normal, rectangleNormal)
    t2Angle = angleBetweenTwoVectors(t2Normal, rectangleNormal)
    t31Angle = angleBetweenTwoVectors(t31Normal, rectangleNormal)
    t32Angle = angleBetweenTwoVectors(t32Normal, rectangleNormal)

    # Output
    print(f"Calculated Angles for each triangle:")
    print(f"______________________________________________")
    print(f"T1: {t1Angle}")
    print(f"T2: {t2Angle}")
    print(f"T31: {t31Angle}")
    print(f"T32: {t32Angle}")

    return 0

if __name__ == "__main__":

    PYRAMID_LENGTH = 52
    PYRAMID_WIDTH = 34
    PYRAMID_HEIGHT = 2
    HORIZONTAL_APEX_DISTANCE = 9

    if len(sys.argv) != 1 and len(sys.argv) != 5:
        sys.stderr.write(
            f"Usage:\n./{sys.argv[0]}\n\tor\n./{sys.argv[0]} <Pyramid_Length> <Pyramid_Width> <Pyramid_Height> <Horizontal_Apex_Distance>"
        )
        sys.exit(1)
    
    if len(sys.argv) == 5:
        PYRAMID_LENGTH = float(sys.argv[1])
        PYRAMID_WIDTH = float(sys.argv[2])
        PYRAMID_HEIGHT = float(sys.argv[3])
        HORIZONTAL_APEX_DISTANCE = float(sys.argv[4])
    
    main(PYRAMID_LENGTH, PYRAMID_WIDTH, PYRAMID_HEIGHT, HORIZONTAL_APEX_DISTANCE)
