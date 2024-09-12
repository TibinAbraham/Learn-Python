#Search for lost car key in home and when found stop searching

key_location = "chair"

locations=["garage","living room","chair","closet"]

for i in locations:
    if i == key_location:
        print("Key is found in",i)
        break
    else:
        print("Key not found")