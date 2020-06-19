from Automated_Simulator import *
from Simulator import *
import sys

print("""
Welcome to the Load Balancing simulation

This simulation has two modes:
=> The Regular Simulation mode
=> The Automated Scenario Simulation mode

To understand how this Simulator works, it is recommended to run the Automated Scenario mode first
before running the Regular Simulaton mode
""")

while True:
    print("To run the Regular Simulation mode type 'regular' or 'r'")
    print("To run the Automated Scenario mode type 'auto' or 'a'")
    print("To exit out of the entire simulation type 'exit' or 'e'")

    mode = input("\n Type mode here: ")

    if mode[0] == "r":
        simulation_main()

    elif mode[0] == "a":
        automated_main()

    elif mode[0] == "e":
        print("Thank you for running this simulator!")
        sys.exit()

    elif mode is None:
        continue

    else:
        continue
