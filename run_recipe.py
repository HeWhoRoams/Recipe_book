import json
import sys
from pathlib import Path


def load_recipe(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def print_recipe(recipe):
    print(f"Recipe: {recipe.get('title')}")
    print(f"Servings: {recipe.get('servings')}")
    print('\nIngredients:')
    for ing in recipe.get('ingredients', []):
        print(f" - {ing}")
    print('\nSteps:')
    for i, step in enumerate(recipe.get('steps', []), 1):
        print(f" {i}. {step}")


def main():
    if len(sys.argv) < 2:
        print('Usage: python run_recipe.py <path-to-recipe.json>')
        return
    path = Path(sys.argv[1])
    if not path.exists():
        print(f'Recipe file not found: {path}')
        return
    recipe = load_recipe(path)
    print_recipe(recipe)


if __name__ == '__main__':
    main()
