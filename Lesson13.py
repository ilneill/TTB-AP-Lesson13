# Using an Arduino with Python LESSON 13: Understanding Parametric Design.
# https://www.youtube.com/watch?v=GFCk_JemuVA
# https://toptechboy.com/

# Internet References:
# https://www.glowscript.org/docs/VPythonDocs/index.html

import time
from vpython import *
import numpy as np

# vPython refresh rate.
vPythonRefreshRate = 100
# XYZ Scale Axis toggle.
showAxis = False

# A place on which to put our things...
canvas(title = "<b><i>Arduino with Python - Boxes containing bouncing balls!</i></b>", background = color.cyan, width = 800, height = 600)

# An XYZ axis to help us get our bearings.
if showAxis:
    arrow(color = color.blue, round = True, pos = vector(-0.5, 0, 0), axis = vector(1, 0, 0), shaftwidth = 0.02) # X axis.
    arrow(color = color.blue, round = True, pos = vector(0, -0.5, 0), axis = vector(0, 1, 0), shaftwidth = 0.02) # Y axis.
    arrow(color = color.blue, round = True, pos = vector(0, 0, -0.5), axis = vector(0, 0, 1), shaftwidth = 0.02) # Z axis.

def buildBox(rPos = vector(0, 0, 0), boxSize = 1):
    boxH = boxSize      # Y Axis
    boxL = boxSize * 2  # Z Axis
    boxW = boxSize * 3  # X Axis
    wallThickness = (boxL + boxW + boxH) / 200
    wallLeft   = box(color = color.gray(0.5), opacity = 1, pos = vector(-boxW / 2, 0, 0) + rPos, size = vector(wallThickness, boxH, boxL + wallThickness))
    wallRight  = box(color = color.gray(0.5), opacity = 1, pos = vector(boxW / 2, 0, 0) + rPos, size = vector(wallThickness, boxH, boxL + wallThickness))
    wallTop    = box(color = color.gray(0.5), opacity = 1, pos = vector(0, boxH / 2, 0) + rPos, size = vector(boxW, wallThickness, boxL + wallThickness))
    wallBottom = box(color = color.gray(0.5), opacity = 1, pos = vector(0, -boxH / 2, 0) + rPos, size = vector(boxW, wallThickness, boxL + wallThickness))
    wallRear   = box(color = color.gray(0.5), opacity = 1, pos = vector(0, 0, -boxL / 2)+ rPos, size = vector(boxW, boxH, wallThickness))
    tlCornerTrim = cylinder (color = color.gray(0.5), opacity = 1, radius = wallThickness / 2, pos = vector(-boxW / 2, boxH / 2, -(boxL + wallThickness) / 2) + rPos, axis = vector(0, 0, boxL + wallThickness))
    trCornerTrim = cylinder (color = color.gray(0.5), opacity = 1, radius = wallThickness / 2, pos = vector(boxW / 2, boxH / 2, -(boxL + wallThickness) / 2) + rPos, axis = vector(0, 0, boxL + wallThickness))
    blCornerTrim = cylinder (color = color.gray(0.5), opacity = 1, radius = wallThickness / 2, pos = vector(-boxW / 2, -boxH / 2, -(boxL + wallThickness) / 2) + rPos, axis = vector(0, 0, boxL + wallThickness))
    brCornerTrim = cylinder (color = color.gray(0.5), opacity = 1, radius = wallThickness / 2, pos = vector(boxW / 2, -boxH / 2, -(boxL + wallThickness) / 2) + rPos, axis = vector(0, 0, boxL + wallThickness))
    return([(-boxW / 2 + wallThickness / 2 + rPos.x), (boxW / 2 - wallThickness / 2 + rPos.x),
            (-boxH / 2 + wallThickness / 2 + rPos.y), (boxH / 2 - wallThickness / 2 + rPos.y),
            (-boxL / 2 + wallThickness / 2 + rPos.z), (boxL / 2 - wallThickness / 2 + rPos.z)])

#Main arena in the center of the cavnas.
arena1Size = 10
arena1Centre = vector(0, 0, 0)
arena1 = buildBox(arena1Centre, arena1Size)
ball1Radius = 0.05 * arena1Size
ball1 = sphere(color = color.green, opacity = 1, radius = ball1Radius, pos = arena1Centre, make_trail = True, retain = arena1Size * 10)
ball1Change = vector((np.random.rand() - 0.5) / arena1Size, (np.random.rand() - 0.5) / arena1Size, (np.random.rand() - 0.5) / arena1Size)

#Upper arena.
arena2Size = 5
arena2Centre = vector(-arena1Size / arena2Size - 3, arena1Size, arena1Size / arena2Size)
arena2 = buildBox(arena2Centre, arena2Size)
ball2Radius = 0.05 * arena2Size
ball2 = sphere(color = color.blue, opacity = 1, radius = ball2Radius, pos = arena2Centre, make_trail = True, retain = arena2Size * 10)
ball2Change = vector((np.random.rand() - 0.5) / arena2Size, (np.random.rand() - 0.5) / arena2Size, (np.random.rand() - 0.5) / arena2Size)

#Lower arena.
arena3Size = 7.5
arena3Centre = vector(arena1Size / arena3Size, -arena1Size, arena1Size / arena3Size)
arena3 = buildBox(arena3Centre, arena3Size)
ball3Radius = 0.05 * arena3Size
ball3 = sphere(color = color.red, opacity = 1, radius = ball3Radius, pos = arena3Centre, make_trail = True, retain = arena3Size * 10)
ball3Change = vector((np.random.rand() - 0.5) / arena3Size, (np.random.rand() - 0.5) / arena3Size, (np.random.rand() - 0.5) / arena3Size)

#Mini arena.
arena4Size = 2.5
arena4Centre = vector(arena1Size / arena4Size + 3, arena1Size, arena1Size / arena4Size)
arena4 = buildBox(arena4Centre, arena4Size)
ball4Radius = 0.05 * arena4Size
ball4 = sphere(color = color.white, opacity = 1, radius = ball4Radius, pos = arena4Centre, make_trail = True, retain = arena4Size * 10)
ball4Change = vector((np.random.rand() - 0.5) / arena4Size, (np.random.rand() - 0.5) / arena4Size, (np.random.rand() - 0.5) / arena4Size)

# An infinite loop: When is True, True? It is always True!
while True:
    #pass
    rate(vPythonRefreshRate) # The vPython rate command is obligatory in animation loops.

    ball1.pos += ball1Change
    if ((arena1[0] + ball1Radius) >= ball1.pos.x or ball1.pos.x >= (arena1[1] - ball1Radius)):
        ball1Change.x = -ball1Change.x
    if ((arena1[2] + ball1Radius) >= ball1.pos.y or ball1.pos.y >= (arena1[3] - ball1Radius)):
        ball1Change.y = -ball1Change.y
    if ((arena1[4] + ball1Radius) >= ball1.pos.z or ball1.pos.z >= (arena1[5] - ball1Radius)):
        ball1Change.z = -ball1Change.z

    ball2.pos += ball2Change
    if ((arena2[0] + ball2Radius) >= ball2.pos.x or ball2.pos.x >= (arena2[1] - ball2Radius)):
        ball2Change.x = -ball2Change.x
    if ((arena2[2] + ball2Radius) >= ball2.pos.y or ball2.pos.y >= (arena2[3] - ball2Radius)):
        ball2Change.y = -ball2Change.y
    if ((arena2[4] + ball2Radius) >= ball2.pos.z or ball2.pos.z >= (arena2[5] - ball2Radius)):
        ball2Change.z = -ball2Change.z

    ball3.pos += ball3Change
    if ((arena3[0] + ball3Radius) >= ball3.pos.x or ball3.pos.x >= (arena3[1] - ball3Radius)):
        ball3Change.x = -ball3Change.x
    if ((arena3[2] + ball3Radius) >= ball3.pos.y or ball3.pos.y >= (arena3[3] - ball3Radius)):
        ball3Change.y = -ball3Change.y
    if ((arena3[4] + ball3Radius) >= ball3.pos.z or ball3.pos.z >= (arena3[5] - ball3Radius)):
        ball3Change.z = -ball3Change.z

    ball4.pos += ball4Change
    if ((arena4[0] + ball4Radius) >= ball4.pos.x or ball4.pos.x >= (arena4[1] - ball4Radius)):
        ball4Change.x = -ball4Change.x
    if ((arena4[2] + ball4Radius) >= ball4.pos.y or ball4.pos.y >= (arena4[3] - ball4Radius)):
        ball4Change.y = -ball4Change.y
    if ((arena4[4] + ball4Radius) >= ball4.pos.z or ball4.pos.z >= (arena4[5] - ball4Radius)):
        ball4Change.z = -ball4Change.z

# EOF
