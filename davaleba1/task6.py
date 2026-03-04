# 6. შექმენით Student კლასი (ველებით name, scores სია ნიშნების) და მეთოდები:
# add_score(score), average(), best_score(), grade(); დაამატეთ ვალიდაცია რომ
# ქულა იყოს 0-დან 100-მდე, წინააღმდეგ შემთხვევაში გამონაკლისი (ValueError).

# 7. შექმენით Course კლასი, რომელიც ინახავს სტუდენტებს ლექსიკონში {name: Student};
# დაამატეთ მეთოდები: add_student(student), remove_student(name), top_k(k)
# (აბრუნებს საუკეთესო k სტუდენტს საშუალოს მიხედვით), და distribution()
# (აბრუნებს შეფასებების განაწილებას "A".."F"-ზე, იგულისხმება A რანდენმა სტუდენტმა აიღო, B რამდენმა და ა.შ.).


class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, score):
        if not (0 <= score <= 100):
            raise ValueError(f"არასწორი ქულა: {score}. ქულა უნდა იყოს 0-დან 100-მდე.")
        self.scores.append(score)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def best_score(self):
        if not self.scores:
            return None
        return max(self.scores)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


try:
    student1 = Student("Luka")
    student1.add_score(85)
    student1.add_score(92)
    student1.add_score(78)

    print(f"სტუდენტი: {student1.name}")
    print(f"საშუალო ქულა: {student1.average():.2f}")
    print(f"საბოლოო შეფასება: {student1.grade()}")
    print(f"საუკეთესო ქულა: {student1.best_score()}")

    # შევამოწმოთ ვალიდაცია არასწორი ქულით
    student1.add_score(150)
except ValueError as e:
    print(f"შეცდომა - {e}")


# 7)
class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = {}

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("ობიექტი უნდა იყოს Student კლასის წარმომადგენელი")
        self.students[student.name] = student

    def remove_student(self, name):
        if name in self.students:
            del self.students[name]
        else:
            print(f"სტუდენტი სახელით '{name}' ვერ მოიძებნა.")

    def top_k(self, k):
        sorted_students = sorted(
            self.students.values(),
            key=lambda s: s.average(),
            reverse=True
        )
        return sorted_students[:k]

    def distribution(self):
        dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
        for student in self.students.values():
            g = student.grade()
            if g in dist:
                dist[g] += 1
        return dist


ML_course = Course("Machine Learning")

s1 = Student("Nino")
s1.add_score(95)
s1.add_score(98)

s2 = Student("Giorgi")
s2.add_score(70)
s2.add_score(85)

s3 = Student("Anna")
s3.add_score(60)
s3.add_score(65)

ML_course.add_student(s1)
ML_course.add_student(s2)
ML_course.add_student(s3)

print(f"საუკეთესო სტუდენტები: {[s.name for s in ML_course.top_k(2)]}")

print(f"შეფასებების განაწილება: {ML_course.distribution()}")