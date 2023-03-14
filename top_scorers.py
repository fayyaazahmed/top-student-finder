import sys, argparse


class Student:
    def __init__(self, fn, sn, s):
        self.first_name = fn
        self.second_name = sn
        self.score = s
    
    def __str__(self):
        return self.first_name + " " +self.first_name + "\n" + \
                "Score: " + self.score

def read_csv(file_name, header=True):
    try:
        with open(file_name, "r") as f:
            csv_file = f.readlines()
    except IOError:
        sys.stdout.write("Could not read file \'" + file_name + "\'\n")
        sys.exit()

    students = []

    if header:
        csv_file = csv_file[1:]

    for line in csv_file:
        try:
            first_name, second_name, score = line.strip().split(',')
            score = int(score)
            student = Student(first_name, second_name, score)
            students.append(student)
        except ValueError:
            sys.stdout.write("Format mismatch. Check that the input_file matches the required format. Check help using -h\n")
            sys.exit()
    return students

def get_top_students(list_of_students):
    top_students = []
    max_score = float('-inf')

    for student in list_of_students:
        if student.score > max_score:
            top_students = [student]
            max_score = student.score
        elif student.score == max_score:
            top_students.append(student)
    
    return top_students

def quicksort(list_of_students):
    if len(list_of_students) <= 1:
        return list_of_students

    pivot = list_of_students[0]
    less_than_pivot = [student for student in list_of_students[1:] if (student.first_name < pivot.first_name) or (student.first_name == pivot.first_name and student.last_name < pivot.last_name)]
    greater_than_pivot = [student for student in list_of_students[1:] if (student.first_name > pivot.first_name) or (student.first_name == pivot.first_name and student.last_name >= pivot.last_name)]
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

def main():
    parser = argparse.ArgumentParser(description="Top Perfoming Student Finder - Uses a max algorthim to find top students and then implements a Quicksort to sort them aplhabetically writing to stdout",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--no-header", action="store_true", help="Specifies that the input_file does not contain a header row")
    parser.add_argument("input_file", help="CSV file of students (Format: first_name, second_name, score")
    args = parser.parse_args()
    config = vars(args)

    top_students = quicksort(get_top_students(read_csv(config['input_file'], not config['no_header'])))
    if len(top_students) < 1:
        sys.stdout.write("No students were found in \'" + config['input_file'] + "\'\n")
        sys.exit()
    for student in top_students:
        sys.stdout.write(student.first_name + " " + student.second_name + "\n")
    sys.stdout.write("Score: " + str(top_students[0].score) + "\n")

if __name__ == "__main__":
    main()