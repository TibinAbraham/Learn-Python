#Write a program that asks user to enter dish name and it should print which cuisine is that dish

indian = ["samosa","daal","naan"]
chinese = ["egg roll","pot sticker","fried rice"]
italian = ["pizza","pasta"]

dish=input("Enter the dish name: ")

if dish in indian:
    print("Dish is indian")
elif dish in chinese:
    print("Dish is chinese")
elif dish in italian:
    print("Dish is italian")
else:
    print("Not in the list")