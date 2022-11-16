#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in November 2022
# A program that finds the sum of a number of positive integers the user inputs


def main():
    # Finds the sum of a number of positive integers the user inputs

    try:
        number_of_loops = input(
            "\nEnter the amount of integers you wish to enter to find the sum of only the positives: "
        )
        integer_of_loops = int(number_of_loops)
        print("")
        if integer_of_loops > 0:
            sum_of_numbers = 0
            while not integer_of_loops == 0:
                integer_of_loops = integer_of_loops - 1
                chosen_number = input("Enter an integer: ")
                chosen_integer = int(chosen_number)
                if chosen_integer >= 0 and not integer_of_loops == 0:
                    sum_of_numbers = sum_of_numbers + chosen_integer
                    continue
                elif chosen_integer < 0 and not integer_of_loops == 0:
                    continue
                sum_of_numbers = sum_of_numbers + chosen_integer
                print(
                    "\nThe sum of all of the positive integers is {}.".format(
                        sum_of_numbers
                    )
                )
        else:
            print("This input isn't a positive integer.")
    except ValueError:
        print("\nError: This input isn't an integer.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
