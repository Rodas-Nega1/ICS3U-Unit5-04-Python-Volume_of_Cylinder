# /usr/bin/env python3

# Created by: Rodas Nega
# Created on: Oct 2021
# This program asks the user for their radius and height of cylinder
# and outputs the volume


import math


def volume_of_cylinder(radius, height):
    # calculate volume

    # process
    volume = round(math.pi * pow(radius, 2), 2) * height

    return volume


def main():
    # this function calls the precedent function

    # input & output
    user_radius = input("Enter the radius of the cylinder (cm): ")
    user_height = input("Enter the height of the cylinder (cm): ")

    try:
        user_radius_int = int(user_radius)
        user_height_int = int(user_height)
        calculated_volume = volume_of_cylinder(
            radius=user_radius_int, height=user_height_int
        )  # call function
        print("")
        print("The volume of your cylinder is {0} cm³".format(calculated_volume))

    except Exception:
        print("")
        print("That is an invalid integer.")

    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
