from utils.linked_list import LinkedList
from models.client import ClientManager

class Car:
    def __init__(self, license_plate, model, year):
        self.license_plate = license_plate
        self.model = model
        self.year = year
        self.claim_requests = None  # Will be a Queue
        self.processed_claims = None  # Will be a Stack

    def __str__(self):
        return f"Car(plate={self.license_plate}, model={self.model}, year={self.year})"

class CarManager:
    @classmethod
    def add_car_to_client(cls):
        client_name = input("Enter client name: ")
        client = ClientManager.get_client_by_name(client_name)
        if client:
            license_plate = input("Enter car license plate: ")
            model = input("Enter car model: ")
            year = input("Enter car year: ")
            car = Car(license_plate, model, year)
            client.cars.append(car)  # Use linked list's append method
            print(f"Car '{license_plate}' added to client '{client_name}'.")
        else:
            print(f"Client '{client_name}' not found.")

    @classmethod
    def delete_car_from_client(cls):
        client_name = input("Enter client name: ")
        client = ClientManager.get_client_by_name(client_name)
        if client:
            license_plate = input("Enter car license plate to delete: ")
            removed = client.cars.remove(license_plate, key=lambda c: c.license_plate)
            if removed:
                print(f"Car '{license_plate}' removed from client '{client_name}'.")
            else:
                print(f"Car '{license_plate}' not found for client '{client_name}'.")
        else:
            print(f"Client '{client_name}' not found.")

    @classmethod
    def edit_car_data(cls):
        client_name = input("Enter client name: ")
        client = ClientManager.get_client_by_name(client_name)
        if client:
            license_plate = input("Enter car license plate to edit: ")
            found_car = client.cars.find(license_plate, key=lambda c: c.license_plate)
            if found_car:
                new_model = input("Enter new model: ")
                new_year = input("Enter new year: ")
                found_car.model = new_model
                found_car.year = new_year
                print("Car data updated.")
            else:
                print("Car not found.")
        else:
            print("Client not found.")

    @classmethod
    def print_client_cars(cls):
        client_name = input("Enter client name: ")
        client = ClientManager.get_client_by_name(client_name)
        if client:
            print(f"\nCars for client '{client_name}':")
            current = client.cars.head
            if not current:
                print("No cars found.")
            while current:
                car = current.data
                print(car)
                current = current.next
        else:
            print(f"Client '{client_name}' not found.")

    @classmethod
    def print_all_cars(cls):
        """
        Print all cars at the company by traversing all clients and listing their cars.
        """
        print("\nAll Cars in the Company:")
        def visit_fn(client):
            # For each client, print all their cars
            current = client.cars.head
            while current:
                print(f"{current.data} (Owner: {client.name})")
                current = current.next

        ClientManager.client_bst.in_order_traversal(visit_fn)
