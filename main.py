from utils.file_loader import FileLoader
from models.client import ClientManager
from models.car import CarManager
from models.claim_request import ClaimRequestManager
from models.claim_processed import ClaimProcessedManager

def main_menu():
    """
    Main menu for the Car Insurance System.
    """
    while True:
        print("\nMain Menu:")
        print("1. Clients")
        print("2. Cars")
        print("3. Claims")
        print("4. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            client_menu()
        elif choice == "2":
            car_menu()
        elif choice == "3":
            claim_menu()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def client_menu():
    """
    Menu for client-related actions.
    """
    while True:
        print("\nClients Menu:")
        print("1. Add Client")
        print("2. Delete Client")
        print("3. Edit Client Data")
        print("4. Print All Clients")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == "1":
            ClientManager.add_client()
            FileLoader.save_all_data()
        elif choice == "2":
            ClientManager.delete_client()
            FileLoader.save_all_data()
        elif choice == "3":
            ClientManager.edit_client()
            FileLoader.save_all_data()
        elif choice == "4":
            ClientManager.print_all_clients()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def car_menu():
    """
    Menu for car-related actions.
    """
    while True:
        print("\nCars Menu:")
        print("1. Add Car to Client")
        print("2. Delete Car from Client")
        print("3. Edit Car Data")
        print("4. Print All Cars of Client")
        print("5. Print All Cars at Company")
        print("6. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == "1":
            CarManager.add_car_to_client()
            FileLoader.save_all_data()
        elif choice == "2":
            CarManager.delete_car_from_client()
            FileLoader.save_all_data()
        elif choice == "3":
            CarManager.edit_car_data()
            FileLoader.save_all_data()
        elif choice == "4":
            CarManager.print_client_cars()
        elif choice == "5":
            CarManager.print_all_cars()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

def claim_menu():
    """
    Menu for claim-related actions.
    """
    while True:
        print("\nClaims Menu:")
        print("1. Add Claim Request to Car")
        print("2. Process Claim Request from Car")
        print("3. Print All Pending Claim Requests Linked to Car")
        print("4. Print All Claims Processed Linked to Car")
        print("5. Back to Main Menu")

        choice = input("Choose an option: ")
        if choice == "1":
            ClaimRequestManager.add_claim_request()
            FileLoader.save_all_data()
        elif choice == "2":
            ClaimProcessedManager.process_claim()
            FileLoader.save_all_data()
        elif choice == "3":
            ClaimRequestManager.print_pending_claims()
        elif choice == "4":
            ClaimProcessedManager.print_processed_claims()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Load data from text files
    FileLoader.load_all_data()
    # Start main menu
    main_menu()
