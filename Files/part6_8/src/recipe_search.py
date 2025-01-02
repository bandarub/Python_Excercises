def search_by_name(filename: str, word: str):
  found_recipes = []
  with open(filename, "r") as file:
    recipe_name = None
    for line in file:
      line = line.strip()
      if line == '':
        recipe_name = None
      elif recipe_name is None:
        recipe_name = line
        if word.lower() in recipe_name.lower():
          found_recipes.append(recipe_name)

  return found_recipes

def search_by_time(filename: str, prep_time: int):
  found_recipes = []
  with open(filename, "r") as file:
    recipe_name = None
    recipe_time = None
    for line in file:
      line = line.strip()
      if line == '':
        recipe_name = None
        recipe_time = None
      elif recipe_name is None:
        recipe_name = line
      elif recipe_time is None:
        recipe_time = int(line)
        if recipe_time <= prep_time:
          found_recipes.append(f"{recipe_name}, preparation time {recipe_time} min")

  return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
  found_recipes = []
  with open(filename, "r") as file:
    recipe_name = None
    recipe_time = None
    ingredients = []
    for line in file:
      line = line.strip()
      if line == '':
        if ingredients:
          if any(ingredient.lower() in ing.lower() for ing in ingredients):
            found_recipes.append(f"{recipe_name}, preparation time {recipe_time} min")
        recipe_name = None
        recipe_time = None
        ingredients = []
      elif recipe_name is None:
        recipe_name = line
      elif recipe_time is None:
        recipe_time = int(line)
      else:
        ingredients.append(line)
    if ingredients:
      if any(ingredient.lower() in ing.lower() for ing in ingredients):
        found_recipes.append(f"{recipe_name}, preparation time {recipe_time} min")

  return found_recipes



if __name__ == "__main__":
  found_recipes = search_by_name("recipes1.txt", "cake")
  for recipe in found_recipes:
    print(recipe)
  found_recipes_time = search_by_time("recipes1.txt", 20)
  for recipe in found_recipes_time:
    print(recipe)

  found_recipes_ingredient = search_by_ingredient("recipes1.txt", "eggs")

  for recipe in found_recipes_ingredient:
      print(recipe)