from functions.get_file_content import get_file_content

test_1 = get_file_content("calculator", "main.py")
test_2 = get_file_content("calculator", "pkg/calculator.py")
test_3 = get_file_content("calculator", "/bin/cat")
test_4 = get_file_content("calculator", "pkg/does_not_exist.py")

print(test_1)
print(test_2)
print(test_3)
print(test_4)
