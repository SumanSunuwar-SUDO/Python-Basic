import printing_functions as pf

student_name = input("Enter student name: ")
marks = pf.get_marks()
total = pf.calculate_total(marks)
average = pf.average(total, len(marks))
pf.print_result(student_name, average)
