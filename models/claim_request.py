from utils.queue import Queue
from models.client import ClientManager

class ClaimRequest:
    def __init__(self, report_number, date, location):
        self.report_number = report_number
        self.date = date
        self.location = location

    def __str__(self):
        return f"ClaimRequest(report={self.report_number}, date={self.date}, location={self.location})"

class ClaimRequestManager:

    @classmethod
    def add_claim_request(cls):
        license_number = input("Enter client license number: ")
        client = ClientManager.get_client_by_license_number(license_number)
        if not client:
            print(f"Client with license '{license_number}' not found.")
            return

        plate = input("Enter car license plate: ")
        car = client.cars.find(plate, key=lambda c: c.license_plate)
        if not car:
            print(f"Car '{plate}' not found.")
            return

        if car.claim_requests is None:
            car.claim_requests = Queue()

        report_number = input("Enter report number: ")
        date = input("Enter date: ")
        location = input("Enter location: ")
        claim = ClaimRequest(report_number, date, location)
        car.claim_requests.enqueue(claim)
        print(f"Claim request '{report_number}' added to car '{plate}'.")

    @classmethod
    def print_pending_claims(cls):
        license_number = input("Enter client license number: ")
        client = ClientManager.get_client_by_license_number(license_number)
        if not client:
            print(f"Client with license '{license_number}' not found.")
            return

        plate = input("Enter car license plate: ")
        car = client.cars.find(plate, key=lambda c: c.license_plate)
        if car and car.claim_requests:
            print(f"\n--- Pending claims for car '{plate}' ---")
            car.claim_requests.print_items()
        else:
            print("No pending claims or car not found.")
