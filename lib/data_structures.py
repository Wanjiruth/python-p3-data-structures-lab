spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_str = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_level_str}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods

# Add test cases to see the output in the terminal
if __name__ == "__main__":
    print("Names of spicy foods:")
    print(get_names(spicy_foods))
    
    print("\nSpiciest foods:")
    print(get_spiciest_foods(spicy_foods))
    
    print("\nPrint spicy foods:")
    print_spicy_foods(spicy_foods)
    
    print("\nGet spicy food by cuisine (American):")
    print(get_spicy_food_by_cuisine(spicy_foods, "American"))
    
    print("\nPrint spiciest foods:")
    print_spiciest_foods(spicy_foods)
    
    print("\nAverage heat level:")
    print(get_average_heat_level(spicy_foods))
    
    print("\nCreate new spicy food:")
    new_food = {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    }
    print(create_spicy_food(spicy_foods, new_food))
    print("\nUpdated list of spicy foods:")
    print_spicy_foods(spicy_foods)