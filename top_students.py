import sys, argparse


class Student:
    def __init__(self, fn, sn, s):
        self.first_name = fn
        self.second_name = sn
        self.score = s


def read_csv(file_name, header=True):
    """
    Reads a CSV file containing student information and returns a list of Student objects.

    :param file_name: The name of the CSV file to read.
    :param header: Whether the file contains a header line. Defaults to True.
    :return: A list of Student objects representing the data in the CSV file.
    :raises IOError: If the specified file does not exist or cannot be opened.
    :raises ValueError: If the format of the data in the file is incorrect.
    """
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
    """
    Returns a list of the top scoring students in a given list of Student objects.

    :param list_of_students: A list of Student objects to be processed.
    :return: A list of the top scoring Student objects. If there are ties for the top score,
             all the tied students are included in the list.
    """
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
    """
    Sorts a list of Student objects using the quicksort algorithm.

    :param list_of_students: A list of Student objects to be sorted.
    :return: A sorted list of Student objects.
    """
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
    """
    Parses command-line arguments and runs the program to find and sort the top-performing students
    in a given CSV file. The program reads the file and creates a list of Student objects, then uses
    a max algorithm to find the students with the highest score(s). The list of top students is then
    sorted alphabetically by first and second name, and the results are written to standard output.
    
    Command-line arguments:
    -h, --help: show this help message and exit
    -n, --no-header: specifies that the input file does not contain a header row
    -q, --quicksort: uses Quicksort instead of the default Python sorting algorithm. No duplicates allowed.
    input_file: required positional argument; specifies the CSV file of students to read (Format: first_name, second_name, score (integer))

    Returns: None
    """
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