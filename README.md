# Car Insurance Management System

A command-line application for managing clients, their cars, car accident claim requests, and processed claims. This system uses data structures such as a **Binary Search Tree** (BST) for storing clients, a **Linked List** for storing each client’s cars, a **Queue** for storing each car’s pending claim requests, and a **Stack** for storing processed claims.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Data Files](#data-files)
- [System Overview](#system-overview)

---

## Project Structure

```
car_insurance_system/
├── main.py
├── models/
│   ├── client.py
│   ├── car.py
│   ├── claim_request.py
│   ├── claim_processed.py
├── utils/
│   ├── binary_search_tree.py
│   ├── linked_list.py
│   ├── queue.py
│   ├── stack.py
│   └── file_loader.py
├── data/
│   ├── clients.txt
│   ├── cars.txt
│   ├── claimRequests.txt
│   └── claimsProcessed.txt
└── README.md
```

1. **`main.py`**  
   Entry point for the CLI application. Presents a menu system to manage clients, cars, and claims.

2. **`models/`**  
   - **`client.py`**: Defines the `Client` class and `ClientManager` for adding/deleting/editing/searching clients in a BST.  
   - **`car.py`**: Defines the `Car` class and methods for adding/deleting/editing cars.  
   - **`claim_request.py`**: Defines the `ClaimRequest` class and methods for adding/printing pending requests.  
   - **`claim_processed.py`**: Defines logic for processing claims and printing processed claims.

3. **`utils/`**  
   - **`binary_search_tree.py`**: BST implementation used to store and retrieve `Client` objects.  
   - **`linked_list.py`**: Singly linked list implementation used to store each client’s `Car` objects.  
   - **`queue.py`**: Queue implementation for managing pending claim requests (FIFO).  
   - **`stack.py`**: Stack implementation for managing processed claims (LIFO).  
   - **`file_loader.py`**: Logic to load data from `.txt` files in `data/`.

4. **`data/`**  
   Contains sample text files for **clients**, **cars**, **claimRequests**, and **claimsProcessed**.

---

## Prerequisites

- **Python 3.8+** (any recent version of Python should work)
- Basic familiarity with the command line.

---

## Installation

1. **Clone** or **download** this repository:
   ```bash
   git clone https://github.com/Jad-Traboulsi/Car-Insurance-System.git
   ```
2. **Navigate** to the project directory:
   ```bash
   cd Car-Insurance-System
   ```

No external Python dependencies are required beyond the standard library, so you can run the code immediately.

---

## Usage

1. **Populate the data files** (optional):

   - Edit the `.txt` files in the `data/` folder (`clients.txt`, `cars.txt`, etc.) to fit your use case.

2. **Run the application**:

   ```bash
   python main.py
   ```

   The application will:

   1. Load data from the `data/` directory (if the files exist).
   2. Present a menu system in the terminal.

3. **Navigate the menu** by typing the corresponding option numbers. Some examples:

   - **1. Clients**
     - Add a new client
     - Delete a client
     - Edit client data
     - Print all clients
   - **2. Cars**
     - Add a car to a client
     - Delete a car from a client
     - Edit car data
     - Print all cars of a client
     - Print all cars at the company
   - **3. Claims**
     - Add a claim request to a car
     - Process a claim request from a car
     - Print all pending claim requests linked to a car
     - Print all claims processed linked to a car

4. **Exit** the program by choosing option **4** on the main menu or pressing **Ctrl + C**.

---

## Data Files

By default, the system loads four files from the `data/` folder:

1. **`clients.txt`**  
   Format:

   ```
   name,address,license_number
   ```

   Example:

   ```
   John Doe,123 Maple Street,AB12345
   Jane Smith,456 Oak Avenue,CD67890
   ```

2. **`cars.txt`**  
   Format:

   ```
   license_plate,license_number,model,year
   ```

   Example:

   ```
   234122B,zei133,Honda CRV,2008
   651223O,fad221,Mercedes-Benz 320E,2005
   ```

3. **`claimRequests.txt`**  
   Format:

   ```
   license_number,license_plate,report_number,date,location
   ```

   Example:

   ```
   fad221,651223O,22,13-2-2016,Beirut
   abb442,445643S,15,16-2-2016,Zahle
   ```

4. **`claimsProcessed.txt`**  
   Format:

   ```
   license_number,license_plate,report_number,date,location
   ```

   Example:

   ```
   fad221,651223O,22,13-2-2016,Beirut
   abb442,445643S,15,16-2-2016,Zahle
   ```

When **`main.py`** starts, it calls the loader in `file_loader.py` to parse these files and populate the internal data structures.

---

## System Overview

1. **Clients** are stored in a **Binary Search Tree** keyed by the client’s name in lowercase.
2. Each client has a **Linked List** of cars.
3. Each car has a **Queue** of pending claim requests and a **Stack** of processed claims.

### Data Structures

- **BST** (Binary Search Tree): efficiently inserts/finds clients by name.
- **Linked List**: allows clients to maintain a variable number of cars.
- **Queue**: ensures **FIFO** order for claim requests.
- **Stack**: records processed claims in **LIFO** order.

### Workflow

- When the program loads, it **reads** existing `.txt` files to populate the data structures.
- Users can **add** new clients, **add** cars to clients, **add** claims, **process** claims, and **print** the data in the terminal.
- Processed claims are **moved** from a car’s queue to its stack.
