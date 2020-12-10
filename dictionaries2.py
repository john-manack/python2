meal = {
    "drink": "beer",
    "appetizer": "nachos",
    "entree": "tacos",
    "dessert": "cake"
}

print(meal)

meal["water"] = "fizzy"
meal["quesadilla"] = False

print(meal)

if "quesadilla" in meal and "quesadilla" == True:
    print("John had a quesadilla.")
else:
    print("John did not have a quesadilla.")