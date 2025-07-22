# Deprecated program for calculating the size of triangles involved in the formation
# of the funnel body. This program was written when I thought I would use a bucket
# as the container for storing balls.

# Since writing this program, I saw it was cheaper to use a large plastic box 
# (rectangular prism) instead, so I have since written an alternative program 
# "BallFeedingBodyDesignParametersBox.py" to handle this kind of container instead 

import math
import sys



### Constants (should be based on the bucket and the position of the rotor hole)
BUCKET_DIAMETER = 76
BUCKET_RADIUS = BUCKET_DIAMETER / 2
R1 = 25
R2 = BUCKET_DIAMETER - R1


### Hyperparameters (I decide these values)
Z = 18
ALPHA = 10

if ALPHA >= R1:
    sys.stderr.write("ALPHA should be set to a value smaller than R1\n")
    exit(1)

### Math Formulas ###
def pythag(a, b):
    return math.sqrt(pow(a, 2) + pow(b, 2))

def pythagShortSide(c, a):
    return math.sqrt(pow(c, 2) - pow(a, 2))

def chordLength(radius: float, perpendicular_distance: float):
    return 2 * pythagShortSide(radius, perpendicular_distance)

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
    x1 = R1 - ALPHA
    x2 = R2 - ALPHA

    h1 = pythag(Z, x1)
    h2 = pythag(Z, x2)

    base_length = chordLength(BUCKET_RADIUS, BUCKET_RADIUS - ALPHA)

    return (h1, h2, base_length)

def getSideLengthKnowledgeIsosceles(perp_height, base):
    a = pythag(base / 2, perp_height)
    return (a, a, base)

def getAngleKnowledgeIsosceles(a, base):
    return getAnglesOfTriangle(a, a, base)


# returns the 3 side lengths of the scalene triangles
def getFundamentalKnowledgeScalene(a: float, b: float):
    return (a, b, BUCKET_DIAMETER - 2 * ALPHA)

def getAngleKnowledgeScalene(a, b, c):
    return getAnglesOfTriangle(a, b, c)



def main():
    h1, h2, isoscelese_base = getFundamentalKnowledgeIsosceles()
    a, a, isoscelese_base = getSideLengthKnowledgeIsosceles(h1, isoscelese_base)
    b, b, isoscelese_base = getSideLengthKnowledgeIsosceles(h2, isoscelese_base)

    t1, t2, t3 = getAngleKnowledgeIsosceles(a, isoscelese_base)
    s1, s2, s3 = getAngleKnowledgeIsosceles(b, isoscelese_base)

    a, b, c = getFundamentalKnowledgeScalene(a, b)

    u1, u2, u3 = getAngleKnowledgeScalene(a, b, c)

    print(f"Triangle 1:\nSides: {a}, {a}, {isoscelese_base}\nAngles: {t1}, {t2}, {t3}\n")
    print(f"Triangle 2:\nSides: {b}, {b}, {isoscelese_base}\nAngles: {s1}, {s2}, {s3}\n")
    print(f"Triangle 3:\nSides: {a}, {b}, {c}\nAngles: {u1}, {u2}, {u3}")


    return 0

if __name__ == "__main__":
    main()
    exit(0)