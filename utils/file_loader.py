import os

from models.client import Client
from models.client import ClientManager
from models.car import Car
from models.claim_request import ClaimRequest
from utils.queue import Queue
from utils.stack import Stack

class FileLoader:
    """
    A utility class to handle loading data from text files into our data structures.
    """
    @staticmethod
    def load_all_data():
        """
        Load data for:
          - clients (clients.txt)
          - cars (cars.txt)
          - claim requests (claimRequests.txt)
          - processed claims (claimsProcessed.txt)
        """
        base_dir = "data"
        FileLoader.load_clients(os.path.join(base_dir, "clients.txt"))
        FileLoader.load_cars(os.path.join(base_dir, "cars.txt"))
        FileLoader.load_claim_requests(os.path.join(base_dir, "claimRequests.txt"))
        FileLoader.load_claims_processed(os.path.join(base_dir, "claimsProcessed.txt"))

    @staticmethod
    def load_clients(filepath):
        """
        Reads each line from clients.txt in the format:
            name,address,license_number
        Creates and inserts a Client object into ClientManager’s BST.
        """
        if not os.path.isfile(filepath):
            print(f"Warning: '{filepath}' not found. Skipping client load.")
            return

        with open(filepath, "r") as file:
            line_number = 0
            for line in file:
                line_number += 1
                line = line.strip()
                if not line:
                    continue  # skip empty lines

                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 3:
                    print(f"Skipping invalid client line {line_number}: '{line}'")
                    continue

                name, address, license_number = parts
                client = Client(name, address, license_number)
                ClientManager.client_bst.insert(client.name, client)

        print(f"Clients loaded from '{filepath}'.")

    @staticmethod
    def load_cars(filepath):
        """
        Reads each line from cars.txt in the format:
            license_plate,license_number,model,year

        Appends a Car to the linked list of the matching client, 
        where 'license_number' identifies the client.
        """
        if not os.path.isfile(filepath):
            print(f"Warning: '{filepath}' not found. Skipping car load.")
            return

        with open(filepath, "r") as file:
            line_number = 0
            for line in file:
                line_number += 1
                line = line.strip()
                if not line:  # Skip empty lines
                    continue

                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 4:
                    print(f"Skipping invalid car line {line_number}: '{line}'")
                    continue

                license_plate, license_number, model, year = parts

                # Find client by license_number
                client = ClientManager.get_client_by_license_number(license_number)
                if not client:
                    print(
                        f"Client with license number '{license_number}' "
                        f"not found; skipping line {line_number}."
                    )
                    continue

                # Create and append the car
                car = Car(license_plate, model, year)
                client.cars.append(car)

        print(f"Cars loaded from '{filepath}'.")

    @staticmethod
    def load_claim_requests(filepath):
        """
        Reads each line from claimRequests.txt in the format:
            license_number,license_plate,report_number,date,location

        Enqueues a ClaimRequest for the specified car.
        """
        import os
        if not os.path.isfile(filepath):
            print(f"Warning: '{filepath}' not found. Skipping claim requests load.")
            return

        with open(filepath, "r") as file:
            line_number = 0
            for line in file:
                line_number += 1
                line = line.strip()
                if not line:  # Skip empty lines
                    continue

                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 5:
                    print(f"Skipping invalid claim request line {line_number}: '{line}'")
                    continue

                license_number, license_plate, report_number, date, location = parts

                # Find the client by license_number
                client = ClientManager.get_client_by_license_number(license_number)
                if not client:
                    print(f"Client with license number '{license_number}' not found; skipping line {line_number}.")
                    continue

                # Find the car in the client’s linked list by license_plate
                car = client.cars.find(license_plate, key=lambda c: c.license_plate)
                if not car:
                    print(f"Car '{license_plate}' not found for license number '{license_number}'; skipping line {line_number}.")
                    continue

                # Ensure the car has a queue for claim requests
                if car.claim_requests is None:
                    car.claim_requests = Queue()

                # Create and enqueue the claim request
                claim = ClaimRequest(report_number, date, location)
                car.claim_requests.enqueue(claim)

        print(f"Claim requests loaded from '{filepath}'.")

    @staticmethod
    def load_claims_processed(filepath):
        """
        Reads each line from claimsProcessed.txt in the format:
            license_number,license_plate,report_number,date,location

        Meaning we want to process that specific pending claim from the car's queue
        (i.e., remove it from claim_requests and push it onto processed_claims).
        """
        import os
        if not os.path.isfile(filepath):
            print(f"Warning: '{filepath}' not found. Skipping processed claims load.")
            return

        with open(filepath, "r") as file:
            line_number = 0
            for line in file:
                line_number += 1
                line = line.strip()
                if not line:
                    continue

                parts = [p.strip() for p in line.split(",")]
                if len(parts) != 5:
                    print(f"Skipping invalid processed claim line {line_number}: '{line}'")
                    continue

                license_number, license_plate, report_number, date, location = parts

                # 1. Find the client by license_number
                client = ClientManager.get_client_by_license_number(license_number)
                if not client:
                    print(f"Client with license number '{license_number}' not found; skipping line {line_number}.")
                    continue

                # 2. Find the car in the client’s linked list by license_plate
                car = client.cars.find(license_plate, key=lambda c: c.license_plate)
                if not car:
                    print(f"Car '{license_plate}' not found for license number '{license_number}'; skipping line {line_number}.")
                    continue

                # 3. Check for a non-empty claims queue
                if not car.claim_requests or car.claim_requests.is_empty():
                    print(f"No pending claims for car '{license_plate}' at line {line_number}.")
                    continue

                # 4. Search the queue for a claim matching 'report_number'
                #    (You could also match date/location if needed.)
                queue_items = []
                target_claim = None

                # Dequeue all items until we find a match
                while not car.claim_requests.is_empty():
                    claim = car.claim_requests.dequeue()
                    if claim.report_number == report_number:
                        # Optionally verify date/location match, e.g.:
                        # if claim.date == date and claim.location == location:
                        target_claim = claim
                        break
                    else:
                        queue_items.append(claim)

                # Put the non-matching items back in the queue
                for item in queue_items:
                    car.claim_requests.enqueue(item)

                if target_claim:
                    # 5. Push the found claim onto processed_claims stack
                    if car.processed_claims is None:
                        car.processed_claims = Stack()
                    car.processed_claims.push(target_claim)
                    print(f"Processed claim '{report_number}' for car '{license_plate}'.")
                else:
                    print(f"Claim report_number='{report_number}' not found in car '{license_plate}' queue at line {line_number}.")

        print(f"Claims processed from '{filepath}'.")

    # ----------------------- SAVE METHODS -----------------------

    @staticmethod
    def save_all_data():
        """
        Re-save all current data (clients, cars, claims) to the text files.
        Call this after any add/edit/delete operation to keep files in sync.
        """
        base_dir = "data"
        FileLoader.save_clients(os.path.join(base_dir, "clients.txt"))
        FileLoader.save_cars(os.path.join(base_dir, "cars.txt"))
        FileLoader.save_claim_requests(os.path.join(base_dir, "claimRequests.txt"))
        FileLoader.save_claims_processed(os.path.join(base_dir, "claimsProcessed.txt"))

    @staticmethod
    def save_clients(filepath):
        """
        Traverse the BST of clients; for each client, write:
            name,address,license_number
        """
        def gather_clients(client_list, client_obj):
            # Reconstruct the line as it was in clients.txt
            name = client_obj.name  # remember we store in lowercase
            address = client_obj.address
            license_number = client_obj.license_number
            # If you prefer to keep the original case for the name, store it separately.
            client_list.append(f"{name},{address},{license_number}")

        clients_data = []
        ClientManager.client_bst.in_order_traversal(lambda c: gather_clients(clients_data, c))

        with open(filepath, "w") as file:
            for line in clients_data:
                file.write(line + "\n")

    @staticmethod
    def save_cars(filepath):
        """
        For each client, for each car, write:
            license_plate,license_number,model,year
        """
        cars_data = []

        def gather_cars(client_obj):
            license_number = client_obj.license_number
            current = client_obj.cars.head
            while current:
                car = current.data
                line = f"{car.license_plate},{license_number},{car.model},{car.year}"
                cars_data.append(line)
                current = current.next

        # Traverse all clients
        ClientManager.client_bst.in_order_traversal(gather_cars)

        with open(filepath, "w") as file:
            for line in cars_data:
                file.write(line + "\n")

    @staticmethod
    def save_claim_requests(filepath):
        """
        For each car's claim_requests queue, write each pending claim as:
            license_number,license_plate,report_number,date,location
        """
        requests_data = []

        def gather_requests(client_obj):
            license_number = client_obj.license_number
            # iterate each car
            current = client_obj.cars.head
            while current:
                car = current.data
                if car.claim_requests:  # a Queue
                    for claim in car.claim_requests.items:
                        line = (
                            f"{license_number},"
                            f"{car.license_plate},"
                            f"{claim.report_number},"
                            f"{claim.date},"
                            f"{claim.location}"
                        )
                        requests_data.append(line)
                current = current.next

        ClientManager.client_bst.in_order_traversal(gather_requests)

        with open(filepath, "w") as file:
            for line in requests_data:
                file.write(line + "\n")

    @staticmethod
    def save_claims_processed(filepath):
        """
        For each car's processed_claims stack, write each processed claim as:
            license_number,license_plate,report_number,date,location
        """
        processed_data = []

        def gather_processed(client_obj):
            license_number = client_obj.license_number
            current = client_obj.cars.head
            while current:
                car = current.data
                if car.processed_claims:  # a Stack
                    # The stack is LIFO in memory, but writing order is your choice
                    # We'll just write from oldest to newest. That's arbitrary.
                    for claim in car.processed_claims.items:
                        line = (
                            f"{license_number},"
                            f"{car.license_plate},"
                            f"{claim.report_number},"
                            f"{claim.date},"
                            f"{claim.location}"
                        )
                        processed_data.append(line)
                current = current.next

        ClientManager.client_bst.in_order_traversal(gather_processed)

        with open(filepath, "w") as file:
            for line in processed_data:
                file.write(line + "\n")
