import random
import math


def generate_moons(n, rad):
    all_moons = [
        (220, 100, 10),
    ]
    while len(all_moons) < n:
        new_moon = (
            random.randint(50, 180),
            random.randint(50, 160),
            random.randint(10, 25),
        )
        able = True
        for moon in all_moons:
            if ((moon[0] - new_moon[0]) ** 2 + (moon[1] - new_moon[1]) ** 2) ** 0.5 <= (
                moon[2] + new_moon[2] + 2 * rad
            ):
                able = False
        if able:
            all_moons.append(new_moon)
    return all_moons


def get_forces(all_moons, x, y, rad):
    fx = 0
    fy = 0
    stop = False
    for moon in all_moons:
        ax = moon[0] - x
        ay = moon[1] - y
        m = 1 * moon[2] ** 3 / 30
        f = rad * m * 0.25 / (ax ** 2 + ay ** 2)
        o = math.atan(ay / ax)
        fx += math.copysign(f * abs(math.cos(o)), ax)
        fy += math.copysign(f * abs(math.sin(o)), ay)
        if (ay ** 2 + ax ** 2) ** 0.5 < moon[2] + rad:
            stop = True
    return fx, fy, stop