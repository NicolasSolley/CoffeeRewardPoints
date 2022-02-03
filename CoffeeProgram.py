print("Hello, welcome to Owl Coffee Shop rewards! What is your name?")
print()
FirstName = input("Enter your first name: ")
LastName = input("Enter your last name: ")
print()
print("Lets get started, " + FirstName + " " + LastName + ". We will now see how many reward points you have earned "
                                                          "this month.")
print()
Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
          "December"]
TotalPoints = 0
for x in Months:
    print("How many coffees did you order in " + x + "?")

    print()
    CoffeesPurchased = int(input("Amount: "))

    if CoffeesPurchased < 1:
        PointsThisMonth = 0
        print()
        print("Points for this month: " + str(PointsThisMonth))
        TotalPoints = PointsThisMonth + TotalPoints
        print("Total points: " + str(TotalPoints))
        print()
    elif CoffeesPurchased == 1 or CoffeesPurchased == 2:
        PointsThisMonth = 20
        print()
        print("Points for this month: " + str(PointsThisMonth))
        TotalPoints = PointsThisMonth + TotalPoints
        print("Total points: " + str(TotalPoints))
        print()
    elif CoffeesPurchased == 3 or CoffeesPurchased == 4:
        PointsThisMonth = 45
        print()
        print("Points for this month: " + str(PointsThisMonth))
        TotalPoints = PointsThisMonth + TotalPoints
        print("Total points: " + str(TotalPoints))
        print()
    elif CoffeesPurchased == 5 or CoffeesPurchased == 6:
        PointsThisMonth = 75
        print()
        print("Points for this month: " + str(PointsThisMonth))
        TotalPoints = PointsThisMonth + TotalPoints
        print("Total points: " + str(TotalPoints))
        print()
    elif CoffeesPurchased == 7 or CoffeesPurchased == 8:
        PointsThisMonth = 110
        print()
        print("Points for this month: " + str(PointsThisMonth))
        TotalPoints = PointsThisMonth + TotalPoints
        print("Total points: " + str(TotalPoints))
        print()
    elif CoffeesPurchased > 8:
        PointsThisMonth = 150
        print()
        print("Points for this month: " + str(PointsThisMonth))
        TotalPoints = PointsThisMonth + TotalPoints
        print("Total points: " + str(TotalPoints))
        print()
print("A total of " + str(TotalPoints) + " points has been earned this month.")