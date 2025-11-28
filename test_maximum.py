from maximum import maximum

def test_maximum():
    print("Running test for positive numbers...")
    assert maximum(3, 9, 6) == 9

    print("Running test for negative numbers...")
    assert maximum(-1, -5, -2) == -1

    print("All test cases executed successfully.")
def test_minimum():
    print("Running test for positive numbers...")
    assert minimum(3, 9, 6) == 9

    print("Running test for negative numbers...")
    assert minimum(-1, -5, -2) == -1

    print("All test cases executed successfully.")
