from typing import List
from collections import defaultdict, Counter


# 2115. Find All Possible Recipes from Given Supplies
# Kahn's algorithm
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        available = set(supplies)
        ans, ingredient_to_recipe, in_degree = [], defaultdict(set), Counter()
        for rcp, ingredient in zip(recipes, ingredients):
            non_available = 0
            for ing in ingredient:
                if ing not in available:
                    non_available += 1
                    ingredient_to_recipe[ing].add(rcp)
            if non_available == 0:
                ans.append(rcp)
            else:
                in_degree[rcp] = non_available
        # print(ingredient_to_recipe)
        # print(in_degree)
        for rcp in ans:
            # print(ans)
            for recipe in ingredient_to_recipe.pop(rcp, set()):
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    ans.append(recipe)
        return ans

# DFS
# class Solution:
#     def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
#         supplies = set(supplies)
#         index = {r:i for i, r in enumerate(recipes)}
#         visited = set()

#         def find(i, visited, supplies):
#             if recipes[i] in supplies:
#                 return True
#             if recipes[i] in visited:
#                 return False

#             visited.add(recipes[i])
#             for ing in ingredients[i]:
#                 if ing not in supplies and (ing not in index or not find(index[ing], visited, supplies)):
#                     return False

#             supplies.add(recipes[i])
#             return True
                
#         res = []
#         for i, r in enumerate(recipes):
#             if find(i, visited, supplies):
#                 res.append(r)
#         return res

# Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
# Output: ["bread","sandwich","burger"]
# Explanation:
# We can create "bread" since we have the ingredients "yeast" and "flour".
# We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
# We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
if __name__ == '__main__':
    sol = Solution()
    recipes = ["bread","sandwich","burger"]
    ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
    supplies = ["yeast","flour","meat"]
    print(sol.findAllRecipes(recipes, ingredients, supplies))
