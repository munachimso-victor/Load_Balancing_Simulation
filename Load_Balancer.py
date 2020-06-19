# Begin Portion 1#
import random
import re
import time


class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id, connection_load):
        """Adds a new connection to this server."""
        self.connections[connection_id] = connection_load
        return ""

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        self.connections.pop(connection_id)

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        for val in self.connections.values():
            total += val
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}".format(self.load())

class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(", ".join(loads))

    def __connection_adding_process__(self, connection_id):
        """Processes the adding of a computer to a particular to the load balancer and a server"""
        if self.connections.get(connection_id):
            self.close_connection(connection_id)
        server = self.random_selection_of_server()
        connection_load = self.load_generator()

        if server.load() > 60:
            self.ensure_availability()
            server = self.random_selection_of_server()

        if server.load() + connection_load > 100:
            self.ensure_availability()
            server = self.random_selection_of_server()

        self.connections[connection_id] = server
        # Add the connection to the server
        server.add_connection(connection_id, connection_load)

        self.ensure_availability()
        print(f"\n{connection_id} has gained access to a web server")
        print("Load Distributed by Load Balancer: ", self.__str__())
        return time.sleep(0.4)

    def add_connection_manual(self):
        """Make a computer to access a server manually"""
        connection_id = self.ip_address()
        self.__connection_adding_process__(connection_id)

    def add_connection_auto(self):
        """Automatically make a computer access the server"""
        connection_id = self.generate_ip()
        self.__connection_adding_process__(connection_id)

    def add_set_of_computers_to_the_load_balancer_Automatically(self, number):
        """Add a specific number od COmputers to the load balancer"""
        for num in range(number):
            self.add_connection_auto()

    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        if not self.connections:
            print("There are no active connections")

        elif self.connections.get(connection_id):
            running_server = self.connections.get(connection_id)
            running_server.close_connection(connection_id)
            self.connections.pop(connection_id)
            print(f"\n{connection_id} has disconnected from the web server")
            time.sleep(0.4)
        else:
            print(f"The computer with the ip address '{connection_id}' is not connected to any active server ")


    def close_all_connections(self):
        """All connections to every server would be removed"""
        if not self.connections:
            print("There are no active connections")
        else:
            print("\n\nThe Server Would begin to remove all connections from the all servers")
            dictionary = list(self.connections.keys())
            for connection in dictionary:
                self.close_connection(connection)

    def close_a_random_connection(self):
        """remove a random connection"""
        if not self.connections:
            print("There are no active connections")
        else:
            choice = random.choice(list(self.connections.keys()))
            self.close_connection(choice)

    def add_or_remove_a_connection(self, number_of_times):
        """Add or remove a connection"""
        task = ["a", "b"]
        for action in range(number_of_times):
            pick = random.choice(task)
            if pick == "a":
                self.add_connection_auto()
            elif pick == "b":
                self.close_a_random_connection()

    def ip_address(self):
        """Manually inputs the ip address"""
        regex_to_verify_ip_address = re.compile(
            r"""^(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2})\."""
            r"""(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2})\."""
            r"""(25[0-5]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2})\."""
            r"""(25[0-4]|2[0-4][0-9]|[0-1][0-9][0-9]|[0-9]{1,2})$"""
        )
        while True:
            ip_address = input("ip_address: ")
            test = regex_to_verify_ip_address.fullmatch(ip_address)
            if test:
                return test.group()
            else:
                print("Invalid Ip Address")
                continue

    def generate_ip(self):
        """Generates random ip address"""
        ip = []
        ip.append(str(random.choice(range(1, 256))))
        ip.append(str(random.choice(range(256))))
        ip.append(str(random.choice(range(256))))
        ip.append(str(random.choice(range(255))))
        ip_address = ".".join(ip)
        return ip_address

    def load_generator(self):
        """Generates a random load for each computer to use from the server"""
        return (random.choice(range(4, 15)) + (random.random() * 10))

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        total = 0
        count = 0
        for serv in self.servers:
            total += serv.load()
            count += 1
        avg = total / count
        return avg

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            self.servers.append(Server())

    def random_selection_of_server(self):
        return random.choice(self.servers)

    def report_on_computers_connected(self):
        """Generates a Report showing All the computers that have access to the web server"""
        print("\n\n")
        space = " "
        print("REPORT SHOWING ALL COMPUTERS THAT HAVE ACCESS TO THE WEB SERVICE")
        print("\n")
        print(" " * 9, "{:>15} {:>4} {:>7} ".format("IP-ADDRESS", space, "TRAFFIC USED BY COMPUTER"))
        Non = "NO IP ADDRESS"
        No_load = "NO TRAFFIC"
        for indx, server in enumerate(self.servers):
            for ip, load in server.connections.items():
                print(" " * 9, f"{ip:>15} {space:>4} {load:>7.2f} (Server{indx + 1}) ")
        decision = False
        for server in self.servers:
            if not server.connections:
                decision = True
            else:
                decision = False
                break
        if decision:
            print(" " * 9, f"{Non:>15} {space:>4} {No_load:>7}  ")

    def report_on_total_traffic_on_each_server(self):
        print("\n\n")
        space = " "
        print("REPORT SHOWING TOTAL LOAD CARIES BY EACH SERVER")
        print("\n")
        print(" " * 13, "SERVER {:>4} {:>7}".format(space, "TOTAL LOAD IN SERVER"))
        if not self.servers:
            print(" " * 13, f"None{indx + 1} {space:>4} {None:>7}")
        for indx, server in enumerate(self.servers):
            print(" " * 13, f"Server{indx + 1} {space:>4} {str(server):>7}")
        




