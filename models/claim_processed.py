from utils.stack import Stack
from models.client import ClientManager

class ClaimProcessedManager:
    @classmethod
    def process_claim(cls):
        client_name = input("Enter client name: ")
        client = ClientManager.get_client_by_name(client_name)
        if client:
            license_plate = input("Enter car license plate: ")
            car = client.cars.find(license_plate, key=lambda c: c.license_plate)
            if car and car.claim_requests and not car.claim_requests.is_empty():
                # Lazily create processed_claims Stack if not present
                if car.processed_claims is None:
                    car.processed_claims = Stack()
                claim = car.claim_requests.dequeue()
                car.processed_claims.push(claim)
                print(f"Processed claim '{claim.report_number}' for car '{license_plate}'.")
            else:
                print("Car or pending claims not found.")
        else:
            print("Client not found.")

    @classmethod
    def print_processed_claims(cls):
        client_name = input("Enter client name: ")
        client = ClientManager.get_client_by_name(client_name)
        if client:
            license_plate = input("Enter car license plate: ")
            car = client.cars.find(license_plate, key=lambda c: c.license_plate)
            if car and car.processed_claims:
                print(f"\nProcessed claims for car '{license_plate}':")
                car.processed_claims.print_items()
            else:
                print("No processed claims or car not found.")
        else:
            print("Client not found.")
