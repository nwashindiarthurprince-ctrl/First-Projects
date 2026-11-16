print("Welcome to the Vehicle Rental System")
# Each vehicle stores its name, daily price and availability. 
vehicles = [ 
    {"name": "Ford Fiesta", "price": 30, "available": True}, 
    {"name": "Volkswagen Golf", "price": 40, "available": True}, 
    {"name": "Toyota Corolla", "price": 45, "available": True} 
]

def show_vehicles(): 
    print("\nAvailable vehicles:") 
    for number, vehicle in enumerate(vehicles, start=1): 
        if vehicle["available"]: 
            print(
                f"{number}. {vehicle['name']} " 
                f"- £{vehicle['price']} per day" 
            )

def book_vehicle(): 
    # Check whether any vehicles are available. 
    if not any(vehicle["available"] for vehicle in vehicles): 
        print("\nNo vehicles are currently available.") 
        return 
        
    show_vehicles()

    # Get and validate the vehicle number and rental duration.
    try:
        choice = int(input("\nEnter the vehicle number: "))
        days = int(input("How many days do you need it? "))
    except ValueError:
        print("Please enter whole numbers.")
        return

    if choice < 1 or choice > len(vehicles):
        print("Invalid vehicle number.")
        return

    if days < 1:
        print("You must rent the vehicle for at least one day.")
        return

    # List positions start at 0, so subtract 1.
    vehicle = vehicles[choice - 1]

    if not vehicle["available"]:
        print("That vehicle is already booked.")
        return

    customer = input("Enter the customer's name: ").strip()
    if customer == "":
        print("A customer name is required.")
        return

    total_cost = vehicle["price"] * days

    vehicle["available"] = False

    print("\n--- Booking confirmation ---") 
    print(f"Customer: {customer}") 
    print(f"Vehicle: {vehicle['name']}") 
    print(f"Rental duration: {days} days") 
    print(f"Total cost: £{total_cost:.2f}")

# Keep showing the menu until the user chooses to exit. 
while True: 
    print("\n--- Vehicle Rental System ---") 
    print("1. View available vehicles") 
    print("2. Book a vehicle") 
    print("3. Exit") 
    
    option = input("Choose an option: ") 
    
    if option == "1": 
        show_vehicles() 
    elif option == "2": 
        book_vehicle() 
    elif option == "3": 
        print("Goodbye!") 
        break
    else: 
        print("Please choose 1, 2 or 3.")
