# Top Performing Student Finder
This program reads in a CSV file of students with their first and last names, and scores, then finds the student(s) with the highest score and sorts them alphabetically by first and second names. It outputs the top student(s) to the command line.

## Usage
`python top_students.py [-h] [-n] input_file`

## Arguments
### Required Arguments
`input_file`: Specifies the path to the CSV file to be processed.
### Optional Arguments
`-h`, `--help`: Shows help message and exit.

`-n`, `--no-header`: Specifies that the input_file does not contain a header row.

## Input Format
The input file must be in CSV format and contain the following fields:

`first_name`: First name of the student (string).
`second_name`: Second name of the student (string).
`score`: Score of the student (integer).

## Output Format
The program outputs the top student(s) in the following format:
```
<first_name> <second_name>
Score: <score>
```

## Example Usage
The following command processes students.csv and outputs the top student(s) to the command line:

`python top_students.py TestData.csv`

The following command processes students.csv with no header and outputs the top student(s) to the command line:

`python top_students.py -n TestData_NoHeader.csv`


## Limitations

Requires a unique list of students as input. Exception thrown if duplicate is among top students.
