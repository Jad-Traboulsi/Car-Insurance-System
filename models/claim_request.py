from utils.queue import Queue
from models.car import CarManager
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
        client_name = input("Enter client name: ")
        client = ClientManager.get_client_by_name(client_name)
        if client:
            license_plate = input("Enter car license plate: ")
            car = client.cars.find(license_plate, key=lambda c: c.license_plate)
            if car:
                if car.claim_requests is None:
                    car.claim_requests = Queue()
                report_number = input("Enter report number: ")
                date = input("Enter accident date: ")
                location = input("Enter accident location: ")
                claim = ClaimRequest(report_number, date, location)
                car.claim_requests.enqueue(claim)
                print(f"Claim request '{report_number}' added to car '{license_plate}'.")
            else:
                print(f"Car '{license_plate}' not found.")
        else:
            print("Client not found.")

    @classmethod
    def print_pending_claims(cls):
        client_name = input("Enter client name: ")
        client = ClientManager.get_client_by_name(client_name)
        if client:
            license_plate = input("Enter car license plate: ")
            car = client.cars.find(license_plate, key=lambda c: c.license_plate)
            if car and car.claim_requests:
                print(f"\nPending claims for car '{license_plate}':")
                car.claim_requests.print_items()
            else:
                print("No pending claims or car not found.")
        else:
            print("Client not found.")
