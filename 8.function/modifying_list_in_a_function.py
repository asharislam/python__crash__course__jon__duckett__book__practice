"""unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following model have been printed:")
for completed_model in completed_models:
    print(completed_model)
"""
"""def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"printing model: {current_design}")
        completed_models.append(current_design)"""

"""def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

    unprinted_designs = ["phone case", "roboto pendant", "dodecahedron"]
    completed_models = []

    print_models(unprinted_designs, completed_models)
    show_completed_models(completed_models)"""

    #preventing a function from modifying a list
function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)


#147
        
