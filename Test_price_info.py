import price_info

price_list={'apple' : 1, 'orange':2, 'watermelon': 2.50}

quantity_list= {'apple': 10, 'orange':5, 'watermelon': 4}

print("Testing price_info.py")

def test_total_cost_shopping():
    test_reult = price_info.cost_of_fruits('apple',2,price_list)
    result = 2
    assert(test_reult == result)

def test_cost_of_fruit():
    result = 30
    test_result = price_info.total_cost_shopping(price_list,quantity_list)
    assert(result == test_result)