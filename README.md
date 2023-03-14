# Top Performing Student Finder
This program reads in a CSV file of students with their first and last names, and scores, then finds the student(s) with the highest score and sorts them alphabetically by first and second names. It outputs the top student(s) to the command line.

## Design Choices
### Reading file & writing output
Used the `open()` method to read in the csv file and then used the `split()` to create Student objects. This simplified the task and increased maintainability and scope for future additions.

Used `sys.stdout.write()` to keeo to the spec requirement of using STDOUT only. Opted not to use `print()` as it gave better control of newline characters but this could easily adapt it.

### Sorting
Opted to use python's built in `sorted()` function as the default search behaviour. It implements Tim Sort and has a worst case time complexity of `O(n log n)`. This should be sufficient for what should be a relatively short list of top students.

I also included a quicksort for larger lists which has best case time complexity of `O(n)`. However this does not cater for duplicates like the default function.

### Max algorithm
This was a straightforward max algorithm that iterated over the list of students once and had time compplexity `O(n)`

## Usage
```
python top_students.py [-h] [-n] [-q] input_file
```

## Arguments
### Required Arguments
`input_file`: Specifies the path to the CSV file to be processed.
### Optional Arguments
`-h`, `--help`: Shows help message and exit.

`-n`, `--no-header`: Specifies that the input_file does not contain a header row.

`-q`, `--quicksort`: Uses Quicksort instead of the default python sorting algorithm. No duplicates allowed.

## Input Format
The input file must be in CSV format (.csv) and contain the following fields:

`first_name`: First name of the student (string).

`second_name`: Second name of the student (string).

`score`: Score of the student (integer).

## Output Format
The program outputs the top student(s) in the following format (see result_example.txt):
```
<first_name> <second_name>
Score: <score>
```

## Example Usage
The following command processes TestData.csv and outputs the top student(s) to the command line:

```
python top_students.py TestData.csv
```

The following command processes TestData_NoHeader.csv with no header and outputs the top student(s) to the command line:

```
python top_students.py -n TestData_NoHeader.csv
```

The following command processes TestData.csv using Quicksort and outputs the top student(s) to the command line:

```
python top_students.py -q TestData.csv
```


## Limitations

- Quicksort requires a unique list of students as input. Exception thrown if duplicate is among top students.
