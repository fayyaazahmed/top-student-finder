import sys, argparse


class Student:
    def __init__(self, fn, sn, s):
        self.first_name = fn
        self.second_name = sn
        self.score = s


def read_csv(file_name, header=True):
    try:
        with open(file_name, "r") as f:
            csv_file = f.readlines()
    except IOError:
        # catches erroneous file names
        sys.stdout.write("Could not read file \'" + file_name + "\'\n")
        sys.exit()

    students = []

    # checks if file contains header and skips over it
    if header:
        csv_file = csv_file[1:]

    for line in csv_file:
        try:
            # splits on commas creates Student object
            first_name, second_name, score = line.strip().split(',')
            score = int(score)
            student = Student(first_name, second_name, score)
            students.append(student)
        except ValueError:
            # Throws error if split elements do not match <str>,<str>,<int>
            sys.stdout.write("Format mismatch. Check that the input_file matches the required format. Check help using -h\n")
            sys.exit()

    return students


def get_top_students(list_of_students):
    top_students = []
    max_score = float('-inf')

    # basic max algorithm
    for student in list_of_students:
        if student.score > max_score:
            # updates max_score with new max_score and resets top_students list
            top_students = [student]
            max_score = student.score
        elif student.score == max_score:
            # if scores are equal adds them to the top_students list
            top_students.append(student)
    
    return top_students


def quicksort(list_of_students):
    # returns if list is empty or contains single Student
    if len(list_of_students) <= 1:
        return list_of_students

    # quick sort algorithm using the first element as a pivot
    pivot = list_of_students[0]

    # sorts by first_name and then second_name if tie breaks ocur.
    try:
        less_than_pivot = [student for student in list_of_students[1:] if (student.first_name < pivot.first_name) or (student.first_name == pivot.first_name and student.last_name < pivot.last_name)]
        greater_than_pivot = [student for student in list_of_students[1:] if (student.first_name >= pivot.first_name) or (student.first_name == pivot.first_name and student.last_name >= pivot.last_name)]
    except AttributeError:
        sys.stdout.write("The input_file contains a duplicate Student. Remove and retry.\n")
        sys.exit()

    # recursively sorts each of the 3 sets.
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)


def main():
    # basic CLI interface for better accessiblity
    parser = argparse.ArgumentParser(
        description="Top Perfoming Student Finder - Uses a max algorthim to find top students and then implements a Quicksort to sort them aplhabetically. Writes to STDOUT.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-n", "--no-header", action="store_true", help="Specifies that the input_file does not contain a header row")
    parser.add_argument("-q", "--quicksort", action="store_true", help="Uses Quicksort instead of the default python sorting algorithm. No duplicates allowed.")
    parser.add_argument("input_file", help="CSV file of students (Format: first_name, second_name, score (integer)")
    args = parser.parse_args()
    config = vars(args)

    # this is where the magic happens
    top_students = get_top_students(read_csv(config['input_file'], not config['no_header']))

    # returns and exits for empty set
    if len(top_students) < 1:
        sys.stdout.write("No students were found in \'" + config['input_file'] + "\'\n")
        sys.exit()

    # choose sorting algorithm...more coming soon.
    if config['quicksort']:
        sorted_list = quicksort(top_students)
    else:
        sorted_list = sorted(top_students, key=lambda student: (student.first_name, student.second_name))
    
    # outputs the results to stdout
    for student in sorted_list:
        sys.stdout.write(student.first_name + " " + student.second_name + "\n")
    sys.stdout.write("Score: " + str(top_students[0].score) + "\n")

if __name__ == "__main__":
    main()