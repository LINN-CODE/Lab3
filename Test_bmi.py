import Lab2.bmi as bmi 

print("Testing Lab3")

def test_bmi_normal_weight():
    result = 0
    input_height = 1.8
    input_weight = 60
    test_result = bmi.calculate_bmi(input_height,input_weight)
    assert(result == test_result)
    

def test_bmi_over_weight():
    result = 1
    input_height = 1.8
    input_weight = 90
    test_result = bmi.calculate_bmi(input_height,input_weight)
    assert(result == test_result)

def test_bmi_under_weight():
    result = -1
    input_height = 1.8
    input_weight = 35
    test_result = bmi.calculate_bmi(input_height,input_weight)
    assert(result == test_result)
