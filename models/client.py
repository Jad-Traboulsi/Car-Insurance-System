from utils.binary_search_tree import BinarySearchTree
from utils.linked_list import LinkedList

class Client:
    def __init__(self, name, address, license_number):
        self.name = name.lower()
        self.address = address
        self.license_number = license_number
        self.cars = LinkedList()  # Linked list for the client's cars

    def __str__(self):
        return f"Client(name={self.name}, address={self.address}, license={self.license_number})"

class ClientManager:
    # A Binary Search Tree keyed by client.name (lowercase)
    client_bst = BinarySearchTree()

    @classmethod
    def add_client(cls):
        """
        Prompt user for client info and insert into BST.
        """
        name = input("Enter client name: ")
        address = input("Enter client address: ")
        license_number = input("Enter client license number: ")

        new_client = Client(name, address, license_number)
        cls.client_bst.insert(new_client.name, new_client)
        
        print(f"Client '{name}' added successfully.")

    @classmethod
    def delete_client(cls):
        name = input("Enter the client name to delete: ").lower()
        cls.client_bst.delete(name)
        print(f"Client '{name}' deleted if it existed.")

    @classmethod
    def edit_client(cls):
        """
        Prompt user for a client name, and allow editing address/license.
        """
        name = input("Enter the client name to edit: ").lower()
        client = cls.client_bst.find(name)
        if client:
            new_address = input("Enter new address: ")
            new_license = input("Enter new license number: ")
            client.address = new_address
            client.license_number = new_license
            print(f"Client '{name}' updated.")
        else:
            print(f"Client '{name}' not found.")

    @classmethod
    def print_all_clients(cls):
        """
        In-order traversal to print all clients in BST.
        """
        print("\n--- All Clients ---")

        def visit_fn(client_obj):
            print(client_obj)

        print("\n--- All Clients ---")
        cls.client_bst.in_order_traversal(visit_fn)

    @classmethod
    def get_client_by_name(cls, name):
        """
        Retrieve a client from the BST by name (case-insensitive).
        """
        return cls.client_bst.find(name.lower())

    @classmethod
    def get_client_by_license_number(cls, license_num):
        """
        Searches the entire BST (in-order) for a client whose
        license_number matches 'license_num'. Returns the first match or None.
        
        Since our BST is keyed by client.name, we can't do a direct BST lookup 
        by license_number. This approach is O(n) in the worst case but is simple 
        to implement for smaller data sets.
        """
        result = [None]

        def visit_fn(client_obj):
            if client_obj.license_number == license_num:
                result[0] = client_obj

        cls.client_bst.in_order_traversal(visit_fn)
        return result[0]
