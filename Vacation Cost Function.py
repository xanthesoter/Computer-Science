# Vactions Cost

# Functions and Parameters example

while True:
    days = int(input("How many days do you plan to stay?: "))
    def hotel_cost():
        cost = 95 * days
        if days > 10:
            cost = cost - 35
        return cost

    def plane_ride_cost():
        print("Los Angeles, Washington D.C., Pittsburgh, San Francisco, St. Louis or Chicago")
        city = input("Enter which city you want to travel to: ")
        if city == "Los Angeles":
            return(430)
        elif city == "Washington D.C.":
            return(200)
        elif city == "Pittsburgh":
            return(175)
        elif city == "San Francisco":
            return(400)
        elif city == "St. Louis":
            return(300)
        elif city == "Chicago":
            return(250)
    
    def rental_car_cost():
        cost = 40 * days
        if days > 7:
            cost = cost - 40
        elif days >= 3 and days < 7:
            cost = cost - 20
        return cost
    
    def spending_money():
        budget = int(input("How much do you plan on bringing to spend?: "))
        return budget
    
    total = hotel_cost() + plane_ride_cost() + rental_car_cost() + spending_money()
    
    discount = input("Do you have a discount code? If so, enter here: ")
    if discount == "15OFF":
        new_total = total - (total * 0.15)
    else:
        new_total = total + 0
    
    tax = 0.07
    total_tax = int(new_total * tax)
    final_total = new_total + total_tax

    print("")
    print("RECIEPT:")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("| Total: $",total)
    print("| Total with any discounts: $",new_total)
    print("| Tax: $",total_tax,)
    print("| Your total trip cost is",final_total,"dollars.")
    print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    answer = input("Do you want to calculate the cost of another trip?: ")
    if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
        continue
    else:
        print("Have a good trip!")
        break
