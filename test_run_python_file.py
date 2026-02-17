from functions.run_python_file import run_python_file

test_1 = run_python_file("calculator", "main.py")
test_2 = run_python_file("calculator", "main.py", ["3 + 5"])
test_3 = run_python_file("calculator", "tests.py")
test_4 = run_python_file("calculator", "../main.py")
test_5 = run_python_file("calculator", "nonexistent.py")
test_6 = run_python_file("calculator", "lorem.txt")

print(test_1)
print(test_2)
print(test_3)
print(test_4)
print(test_5)
print(test_6)

