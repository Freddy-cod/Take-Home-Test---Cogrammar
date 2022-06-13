from say_number import say_number

def test_say_number(data, expected_output):
    """Test cases for say_number(number)."""
    output = say_number(data)
    assert output == expected_output, \
        "\n    for:      {}\n    expected: {}\n    got:      {}".format(
            data, expected_output, output)


# test_say_number(0, 'zero')
# test_say_number(1, 'one')
# test_say_number(-1, 'negative one')
# test_say_number(10, 'ten')
# # test_say_number(11, 'eleven')
# # print(test_say_number(99, 'ninety nine'))