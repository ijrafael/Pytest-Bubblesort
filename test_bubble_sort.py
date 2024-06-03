from bubble_sort import bubbleSort

def test_case_1():
    test_list = [20, -1, 15, 18, -92, 13, 102, -11, 0, 3, 15]
    bubbleSort(test_list)
    assert test_list == [-92, -11, -1, 0, 3, 13, 15, 15, 18, 20, 102]
    
def test_case_2():
    test_list = [100, 99, 14, 10, 3, 8, -53, 4, -32, 72, -20, 18]
    bubbleSort(test_list)
    assert test_list == [-53, -32, -20, 3, 4, 8, 10, 14, 18, 72, 99, 100]


