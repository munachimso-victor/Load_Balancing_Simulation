from Load_Balancer import *
import time


def automated_main():
    print("""
    Welcome to the Automated Scenario Simulation!
    \n""")

    print(
        "\nIn this Automated Simulation, we have a Company that makes use a web service to perform daily functions "
        "and processes "
        "\nThe company is a big company, and has numerous employees\n")
    time.sleep(3)

    print("\nEvery employee needs access to the service, so to ensure every employee gains access to the web service, "
          "\nthe comapany makes use of a server pool instead of just using a single server.\n")
    time.sleep(3)

    print("\nThe goal of using multiple servers(a server pool) is to prevent server crashes and increase the life span"
          "\nof the servers by reducing the load of each server\n")
    time.sleep(3)

    print("\nTo properly distribute load among every server, the company makes use of a Load balancer"
          "\nThe goal of the Load balancer is to distribute the traffic load among the servers in the Server pool "
          "\nefficiently without putting much stress on a single server.")
    time.sleep(3)

    print(
        "\nThe goal of this simulation is to see the load "
        "balancing process in action on a regular day at the Company\n")
    time.sleep(3)

    print("\nThis simulation expresses a balancer as a list with square brackets '[]'."
          "\nEvery element in this list represent a current load of each server")
    time.sleep(3)

    print(
        "\nThe load balancer performs an action when any user tries accessing the service by deciding where the load "
        "should be distributed to\n")
    time.sleep(3)

    print("\nThe load Distribution will begin to run in 5 seconds.....")
    time.sleep(5)

    print("\n")
    print("*"*130)
    print("In the morning, different employees log in to the server, around the same time"
          "\nEvery computer in the network has an ip address, that uniquely identifies the computer"
          "\nP.S. the company has employees from different parts of the country accessing the web server")
    print("*" * 130)
    time.sleep(3)

    my_load = LoadBalancing()
    my_load.add_set_of_computers_to_the_load_balancer_Automatically(30)
    my_load.report_on_computers_connected()
    time.sleep(3)
    my_load.report_on_total_traffic_on_each_server()
    time.sleep(3)

    print("\n")
    print("*" * 130)
    print("In the middle of the day, the Load balancer would experience random connections and disconnections."
          "\nThis is can be because of lunch breaks, meetings, job completion or any other activities that might "
          "occur in the midddle of the day "
          "\nThe load balancer behaves in the following way reacting to the events")
    print("*" * 130)
    time.sleep(4)

    my_load.add_or_remove_a_connection(20)

    print("\n")
    print("*" * 130)
    print(
        "At the end of the work day, every connection to the server pool is either manually disconnected or "
        "automatically disconnected")
    print("*" * 130)
    time.sleep(4)

    my_load.close_all_connections()
    my_load.report_on_computers_connected()
    my_load.report_on_total_traffic_on_each_server()

    print("\n")
    print("*" * 130)
    print("Thank you for running the Simulation!!")
    print("*" * 130)

if __name__ == "__main__":
    automated_main()
