import numpy as np
import matplotlib.pyplot as plt
import random
from datetime import datetime

def printId():
    print(datetime.now())
    print("F24-0621")

printId()

def f(x):
    return -(x - 3)**2 + 9

def simple(x0, stepSize):
    path = [x0]
    currentX = x0
    while True:
        if f(currentX + stepSize) > f(currentX):
            currentX += stepSize
            path.append(currentX)
        elif f(currentX - stepSize) > f(currentX):
            currentX -= stepSize
            path.append(currentX)
        else:
            break
    return path

def steepestAscent(x0, stepSize):
    path = [x0]
    currentX = x0
    while True:
        neighbors = [currentX + stepSize, currentX - stepSize]
        bestNeighbor = max(neighbors, key=f)
        if f(bestNeighbor) > f(currentX):
            currentX = bestNeighbor
            path.append(currentX)
        else:
            break
    return path

def randomRestart(restarts, stepSize):
    globalBestVal = -float('inf')
    globalBestX = None
    bestStart = None
    allTrajectories = []
    for i in range(restarts):
        startX = random.uniform(-10, 10)
        path = steepestAscent(startX, stepSize)
        allTrajectories.append(path)
        if f(path[-1]) > globalBestVal:
            globalBestVal = f(path[-1])
            globalBestX = path[-1]
            bestStart = startX
    return globalBestX, globalBestVal, bestStart, allTrajectories

step = 0.1
pathA = simple(0.0, step)
bestX, bestVal, startPt, trajectories = randomRestart(10, step)

print(f"Simple HC Path: {[round(x, 1) for x in pathA]}")
print(f"Random Restart Best Solution: x={bestX:.4f}, Value={bestVal:.4f}")
print(f"Best solution found from start point: {startPt:.4f}")

xRange = np.linspace(-10, 15, 500)
plt.figure(figsize=(12, 6))
plt.plot(xRange, f(xRange), 'k--', alpha=0.3, label='Dashed Line: Function Curve f(x)')
for i, trajectory in enumerate(trajectories):
    if i == 0:
        plt.plot(trajectory, [f(px) for px in trajectory], color='orange', marker='o', markersize=3, label='Orange: Random Restart Paths', alpha=0.5)
    else:
        plt.plot(trajectory, [f(px) for px in trajectory], color='orange', marker='o', markersize=3, alpha=0.5)
plt.plot(pathA, [f(px) for px in pathA], color='blue', marker='o', markersize=6, linewidth=2, label='Blue: Simple HC Path')

plt.title("Hill Climbing")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()