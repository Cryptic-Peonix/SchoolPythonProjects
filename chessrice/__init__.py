# Program to calculate the amount of grains of rice for famous chess
# board problem.
#
# Author: Connor Clark
# 3/1/2022

def main():
    """Our main function. Calculates how much rice for chessboard."""
    grains = 1
    totalgrains = 0
    for square in range(1, 64 + 1):
        print(square, grains)
        grains *= 2
        if square != 64:
            totalgrains = totalgrains + grains
    print("\n" + "Total grains of rice: " + str(totalgrains))
    vol = dovolume(totalgrains)
    print("Total volume of rice: " + str(round(vol, 2)) + " km^3")
    cov = dosurfacearea(vol)
    print("Total depth is: " + str(cov) + " ft")
    produce = dobonus(totalgrains)
    if produce:
        print("We can produce this amount of rice today!")
    else:
        print("We cant produce this amount of rice today...")


def dovolume(totalrice):
    """Calulates the volume of all of the rice. Volume of a single grain
    of rice is about 16.25mm^3
    Source: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/fsn3.746"""
    volume = 16.25  # in mmm
    totalvolume = volume * totalrice
    totalvolume = totalvolume / (1 * 10 ** 18)  # Convert mm^3 to km^3
    return totalvolume


def dosurfacearea(totalvol):
    """Calculates the depth that the rice would cover the state of SC in.
    Area of SC: 32,020 mi^2 (8.927 * 10^11 ft^2)
    Source: https://www.britannica.com/place/South-Carolina"""
    area = (8.927 * 10 ** 11)  # area in square feet
    volume = totalvol * (3.531 * 10 ** 10)  # volume in cubic feet
    coverage = (volume / area) * 1.15  # total depth
    return coverage


def dobonus(totalgrain):
    """Does the bonus. Sees if rice production is possible in the modern age"""
    grainweight = 0.01976 / 1000  # weight of a gram of rice in kg
    chinap = 211.86 * 1000  # Chinese production of rice in kg
    indiap = 107.04 * 1000  # Indian production of rice in kg
    totalweight = grainweight * totalgrain  # weight of all the rice
    totalp = chinap + indiap  # total production
    print("production: " + str(totalp))
    print("weight: " + str(totalweight))
    if totalp >= totalweight:
        return True
    else:
        return False


main()
