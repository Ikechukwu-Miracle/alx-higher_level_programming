#!/usr/bin/python3

#prints the alphabet except 'q' and 'e'
for alpha in range(97, 123):
    if chr(alpha) != "q" and chr(alpha) != "e":
        print(f"{chr(alpha)}", end="")
