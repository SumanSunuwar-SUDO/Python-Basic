def get_marks():
    marks = []
    for i in range(1, 4):
        mark = int(input("Enter your marks: "))
        marks.append(mark)
    return marks

def calculate_total(marks):
    return sum(marks)

def average(total, num_subjects):
    return total / num_subjects

def print_result(name, result):
    print("\nResult for " + name)
    print("Average Marks: "  + str(result))
    if result >= 60:
        print("Result: Pass")
    else:
        print("Result: Fail")
