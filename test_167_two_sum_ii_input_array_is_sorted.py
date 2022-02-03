import code_167_two_sum_ii_input_array_is_sorted as c1

def test_base_case():
    s = c1.Solution()
    assert s.twoSum([2,7,11,15], 9) == [1,2]

def test_example_2():
    s = c1.Solution()
    assert s.twoSum([2,3,4,], 6) == [1,3]

def test_example_3():
    s = c1.Solution()
    assert s.twoSum([-1,0], -1) == [1,2]

def test_failed_17():
    s = c1.Solution()
    assert s.twoSum([5,25,75], 100) == [2,3]