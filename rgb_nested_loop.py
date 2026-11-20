#!/usr/bin/env python3
# Created by: Adrian student
# Created on: 19th NOV 2026
# This program uses nested loops to print out all the valid RGB colour


def main():
    # set the red loop
    for r in range(0, 11):
        for g in range(0, 11):
            for b in range(0, 11):
                print(
                    "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(
                        r, g, b, "RGB(" + str(r) + "," + str(g) + "," + str(b) + ")"
                    )
                )


if __name__ == "__main__":
    main()
