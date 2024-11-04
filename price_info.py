
price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}


def total_cost_shopping(parameter_one, parameter_two):
    total_cost = 0
    for key in parameter_one.keys():
        if key in parameter_one:
            
            total_cost = total_cost + cost_of_fruits(key, parameter_two[key], parameter_one)
            # complete the implementation below:
    print("total cost = ", total_cost)
    return total_cost


def cost_of_fruits(fruit, quantity, parameter_one):
    for key in parameter_one.keys():
        if key == fruit:
            cost = quantity*parameter_one[key]
            break

    print("cost of ", quantity, fruit, "=", cost)
    return cost


def main():

    cost_of_fruits('apple', 10,price_list)
    total_cost_shopping(price_list,quantity_list)


if __name__ == "__main__":
    main()