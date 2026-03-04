# 3. მოცემულია სტუდენტების ლექსიკონი {name: score}; დაწერეთ ფუნქცია,
# რომელიც აბრუნებს ახალ ლექსიკონს {grade_letter: [names...]} (მაგ. "A": ["Nino", ...]),
# სადაც სახელების სიები დაალაგეთ ანბანურად.

students = {
    "Nino": 95,
    "Giorgi": 82,
    "Anna": 91,
    "Luka": 74,
    "Mari": 88,
    "Dato": 55
}


def sorted_students(students_list):
    grades = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": []}

    for name, score in students_list.items():
        if score > 90:
            grades["A"].append(name)
        elif score > 80:
            grades["B"].append(name)
        elif score > 70:
            grades["C"].append(name)
        elif score > 60:
            grades["D"].append(name)
        elif score > 50:
            grades["E"].append(name)
        else:
            grades["F"].append(name)

    for grade in grades:
        grades[grade].sort()

    final_grades = {k: v for k, v in grades.items() if v}

    return final_grades


print(sorted_students(students))

