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
    return [each["name"] for each in spicy_foods]
    
def get_spiciest_foods(spicy_foods):
    return [each for each in spicy_foods if each["heat_level"]>5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        new_list=[]
        heat_level = "🌶" * food["heat_level"]
        food["heat_level"]=heat_level
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {heat_level} ')
        new_list.append(food)
        return [new_list]

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"]==cuisine:
            return food
    

def print_spiciest_foods(spicy_foods):
    pass

def get_average_heat_level(spicy_foods):
    heat_levels=list()
    for food in spicy_foods:
        heat_levels.append(food["heat_level"])
        total=0
    for heat in heat_levels:
        total+=heat
    average=total/len(heat_levels)
    return average
    


def create_spicy_food(spicy_foods, spicy_food):
    pass
