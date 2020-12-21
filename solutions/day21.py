from collections import Counter

if __name__ == "__main__":
    with open("day21.input") as f:
        ingredients = []
        allergens = []
        for line in f.readlines():
            ing, alg = line[:-2].split(" (")
            ingredients.append(ing.split(" "))
            allergens.append(alg[9:].split(", "))
    
    candidates = {}
    # build list of candidates
    for i in range(len(ingredients)):
        for allergen in allergens[i]:
            if allergen in candidates:
                candidates[allergen] = candidates[allergen] & set(ingredients[i])
            else:
                candidates[allergen] = set(ingredients[i])
    
    confirmed = {}
    confirmed_set = set()
    while candidates:
        cand_keys = list(candidates.keys())
        for el in cand_keys:
            candidates[el] -= confirmed_set
            if len(candidates[el]) == 1: # found unique!
                ingr = candidates[el].pop()
                confirmed[el] = ingr
                confirmed_set.add(ingr)
                del candidates[el]
    
    ingredients_occurrences = [ b for a in ingredients for b in a ]
    print(sum([ v for k,v in Counter(ingredients_occurrences).items() if k not in confirmed_set ]))
    print(",".join([ i for a,i in sorted(list(confirmed.items()), key=lambda x: x[0]) ]))