from django.shortcuts import render

# Create your views here.
remaining_capacity=1000.0
def pump_index(request):
    global remaining_capacity
    filled_liters = 0

    if request.method=="POST":
        amount=float(request.POST.get("amount"))
        Petrol_Price=94.77

        liters=amount/Petrol_Price

        if liters>remaining_capacity:
            liters<=remaining_capacity

        remaining_capacity-=liters
        filled_liters=liters

    return render(request, "index.html",{
        "remaining_capacity": remaining_capacity,
        "filled_liters":filled_liters
        })
   