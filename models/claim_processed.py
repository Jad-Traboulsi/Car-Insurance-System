from models.client import ClientManager
from utils.stack import Stack

class ClaimProcessedManager:

    @classmethod
    def process_claim(cls):
        license_number = input("Enter client license number: ")
        client = ClientManager.get_client_by_license_number(license_number)
        if not client:
            print(f"Client with license number '{license_number}' not found.")
            return

        plate = input("Enter car license plate: ")
        car = client.cars.find(plate, key=lambda c: c.license_plate)
        if not car:
            print(f"Car '{plate}' not found for client with license '{license_number}'.")
            return

        if not car.claim_requests or car.claim_requests.is_empty():
            print(f"No pending claims to process for car '{plate}'.")
            return

        # Dequeue the oldest claim
        claim = car.claim_requests.dequeue()
        if car.processed_claims is None:
            car.processed_claims = Stack()

        car.processed_claims.push(claim)
        print(f"Processed claim '{claim.report_number}' for car '{plate}'.")

    @classmethod
    def print_processed_claims(cls):
        license_number = input("Enter client license number: ")
        client = ClientManager.get_client_by_license_number(license_number)
        if not client:
            print(f"Client with license '{license_number}' not found.")
            return

        plate = input("Enter car license plate: ")
        car = client.cars.find(plate, key=lambda c: c.license_plate)
        if car and car.processed_claims:
            print(f"\n--- Processed claims for car '{plate}' ---")
            car.processed_claims.print_items()
        else:
            print("No processed claims or car not found.")
