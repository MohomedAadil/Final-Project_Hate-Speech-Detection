# Import the function to be tested
from FlaskRestAPI.app import clean_text

def test_clean_text_function():
    # Test the clean_text function
    input_text = "Hello, World!>*/]} "
    cleaned_text = clean_text(input_text)
    expected_result = "hello world"
    assert cleaned_text == expected_result

if __name__ == '__main__':
    test_clean_text_function()