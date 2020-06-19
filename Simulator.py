from Load_Balancer import *
import sys

def simulation_main():
    load = LoadBalancing()
    print("""
    Welcome to the Load Balancer Simulation!
    \n""")
    print("\nThe goal of the Load balancer is to distribute the traffic load among a servers in a Server pool "
          "\nefficiently without putting much stress on a single server.")

    print("""
    \n To simulate a computer gaining access to the web service, we add a connection,
    and to close the connection we remove the connection
    """)
    while True:
        print("""
        Options:
        To add a connection type "add" or "a"
        To remove a connection type "remove" or "r"
        To view a report on computers connected to server type "computers" or "c"
        To view a report on the  Total Load on all the servers type "[l]oad" or "l"
        To quit from this Simulation mode type "quit" or "q"
        To exit out of the entire simulation type "exit" or "e"

        """)
        response = input("Type response here: ").lower()

        if response[0] == "a":
            print("""
            To add a connection manually (i.e. by typing the ip-adddress) type "manual" or "m"
            To add a connection by generating an ip-address type "auto" or "a"
            """)
            while True:
                response_2 = input("Type response here: ").lower()
                if response_2[0] == "m":
                    load.add_connection_manual()
                    break

                elif response_2[0] == "a":
                    print("""
                    How many connections do you want to create?
                    Type the number below(Response shoud be integers e.g. 1,9,12)
                    """)
                    while True:
                        try:
                            response_3 = int(input("Type response here: ").lower())
                            if response_3 < 1:
                                raise ValueError
                            if response_3 == 1:
                                load.add_connection_auto()
                            elif response_3 > 1:
                                load.add_set_of_computers_to_the_load_balancer_Automatically(response_3)
                        except:
                            print("Invalid response")
                            continue
                        else:
                            break
                    break

                elif response_2 is None:
                    print("Invalid response")
                    continue
                else:
                    print("Invalid response")
                    continue

        elif response[0] == "r":
            print("""
            To remove a connection manually type "manual" or "m"
            To remove a random connection type "random" or "r"
            To remove all connections type "all" or "a"
            """)
            while True:
                response_2 = input("Type response here: ").lower()
                if response_2[0] == "m":
                    address = load.ip_address()
                    load.close_connection(address)
                    break

                elif response_2[0] == "r":
                    load.close_a_random_connection()
                    break

                elif response_2[0] == "a":
                    load.close_all_connections()
                    break

                elif response_2 is None:
                    print("Invalid response")
                    continue
                else:
                    print("Invalid response")
                    continue

        elif response[0] == "c":
            load.report_on_computers_connected()

        elif response[0] == "l":
            load.report_on_total_traffic_on_each_server()

        elif response is None:
            print("Invalid response")
            continue

        elif response[0] == "q":
            print("\n\nThank you for running the Simulation!!\n\n")
            break

        elif response[0] == "e":
            print("Thank you for running this simulator!")
            sys.exit()
        else:
            print("Invalid response")
            continue


if __name__ == "__main__":
    simulation_main()
