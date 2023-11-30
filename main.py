def read_recipes(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    cook_book = {}
    current_recipe = None

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if line.isdigit():
            num_ingredients = int(line)
            current_recipe = []
            continue

        if current_recipe is not None and len(current_recipe) < num_ingredients:
            ingredient = line.split(' | ')
            ingredient_name = ingredient[0]
            quantity = int(ingredient[1])
            measure = ingredient[2]

            current_recipe.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })

        if current_recipe is not None and len(current_recipe) == num_ingredients:
            recipe_name = current_recipe[0]['ingredient_name']
            cook_book[recipe_name] = current_recipe
            current_recipe = None

    return cook_book


cook_book = read_recipes('recipes.txt')

print(cook_book)