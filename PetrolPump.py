petrol_price=94.77
Tank_capacity=1000.0

remaining_capacity=Tank_capacity

while True:
    print("---Petrol Pupm Machine---")
    print(f"Remaining Petrol in Tank: {remaining_capacity:.2f} liters" )

    if(remaining_capacity<=0):
        print("Tank is Empty, Refill")
        break
    amount= float(input("Enter amount or 0 to Stop:"))
    if amount==0:
        print("Transaction Stopped.")
        break
    liters=amount/petrol_price

    if liters>remaining_capacity:
        print("Not enough petrol in tank!")
        print(f"Available Petrol: {remaining_capacity:.2f} liters only.")
        continue

    remaining_capacity-=liters

    print("----Transaction Summary----")
    print("Petrol Price:",petrol_price)
    print(f"Entered Amount: Rs. {amount:.2f}")
    print(f"Pertrol filled:{liters:.2f}")
    print(f"Remaining Petrol:{remaining_capacity:.2f}")
    