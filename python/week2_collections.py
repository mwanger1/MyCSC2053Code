coordinates = (5,25)
print(coordinates)
x, y = coordinates
print(x,y)
print(coordinates[0])

set1 = {1,2,3,3,2}
print(set1)
list1 = [1,2,2,3,3,4,4]
list_remove_dups = set(list1)
print(list_remove_dups)

list1 = []
for i in range(0,50):
    list1.append(i)
print(list1)
# printing the same list as above only using list comprehension
list2 = [x for x in range(0,50) if x > 40]
print(list2)

evens = [i for i in range(0,50) if i % 2 == 0]
odds = [i for i in range(0,50) if i % 2 > 0]
print(evens)
print(odds)

favorite_foods = {"Maddie":"Popcorn", "Annika":"Potatoes", "Virginia":"Pasta"}
favorite_foods["Guy"] = "Salad"
print(favorite_foods)

for key,value in favorite_foods.items():
    print(key+"'s favorite food is "+value)

if "Mary" in favorite_foods:
    print("Mary in dictionary")
else:
    favorite_foods["Mary"] = "Cake"

foods = ["pizza", "tacos", "sushi", "bagels", "bagels", "pizza", "sushi", "pasta", "ice cream", "sushi"]
food_count = {}

for foods in foods:
    if foods not in food_count:
        food_count[foods] = 1
    else:
        food_count[foods] += 1
for foods in sorted(food_count, key = food_count.get, reverse=True):
    print(foods, "appears ", food_count[foods], "time" if food_count[foods] == 1 else "times")

# comprehension
keys = ["one", "two", "three"]
nums = {keys[i]: i+1 for i in range(len(keys))}
print(nums)