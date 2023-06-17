# """Print out all the melons in our inventory."""


from melons import melon_names, melon_prices, melon_seedlessness, melons


# def print_melon(name, price, seedless):
#     """Print each melon with corresponding attribute information."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])

def print_melons(melons):

    for key, value in melons.items():
        # print(
        #     key, value["price"], value["seedless"], value["flesh_color"], value["rind_color"],
        #     value["average_weight"] 
            # )
        
        
        print(key.upper())
        print("price:", value["price"])
        print("seedless:", value["seedless"])
        print("flesh_color:", value["flesh_color"])
        print("rind_color:", value["rind_color"])
        print("average_weight:", value["average_weight"])
        print("")


    # print(
    #     f"{key.upper()} \nprice: \nseedless: \nflesh_color:"
    #       )




# for key, value in melons_info.items():
#     print(key)
#     print(f"price: {value[0]}")
#     print(f"seedless: {value[1]}")
#     print(f"flesh_color: {value[2]}")
#     print(f"rind_color: {value[3]}")
#     print(f"average_weight: {value[4]}")
#     print("")
    

    
print_melons(melons)