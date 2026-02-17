from functions.get_files_info import get_files_info

case_1 = get_files_info("calculator", ".")
case_2 = get_files_info("calculator", "pkg")
case_3 = get_files_info("calculator", "/bin")
case_4 = get_files_info("calculator", "../")

print(f"Result for current directory\n{case_1}")
print(f"Result for 'pkg' directory\n{case_2}")
print(f"Result for '/bin/' directory\n{case_3}")
print(f"Result for '../' directory\n{case_4}")
