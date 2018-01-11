# Python Grader

This script clones multiple students' assignments from a git server, runs tests on them, and generates a series of good/bad reports to indicate whether the student passed all of the tests. For students that did
not pass all of the tests, a report will be generated that provides all test output.

This script is provided for educational purposes and does not necessarily demonstrate best engineering practices, etc.

## Use

Suppose you have:
  * students:
    * github.com/student1
    * github.com/student2
    * github.com/student3
  * an assignment named my-assignment
  * that each student has their own repo:
    * github.com/student1/my-assignment
    * etc.
  * that my-assignment has a directory named `tests` with a test file named
    `tests.py`
  * that you can run the project's tests with `python tests/test.py`
  * that you have created a `users.txt` file alongside this script
  * that `users.txt` contains the github usernames of your students:
    ```
    student1
    student2
    student3
    ```

Given the above, you would run the script with `python main.py my-assignment users.txt`

Successful execution of this script would create the following directories:
  * `reports/my-assignment/good`
  * `reports/my-assignment/bad`

The good and bad report directories would be populated with the results of the students' tests.

The contents and path of the `users.txt` file and also the name of the assignment repository are configurable without code changes. You can change the server that repositories are cloned from, as well as make other changes, by editing the code.

## Example

For a concrete example, you can run this script on its own home repository:

`python main.py PythonGrader users.txt.example`

This will clone [https://github.com/JASchilz/PythonGrader](https://github.com/JASchilz/PythonGrader) into `users/jaschilz`, run `tests/test.py` and produce output in `reports/PythonGrader`. Specifically, the report generated will be in `reports/PythonGrader/bad/jaschilz.txt` because `tests/test.py` contains a failing test.

## Security Notice

By running this script you're giving your students arbitrary execution under your user on your machine. It might be wise to run this script under a new user on your machine, or within a virtual machine. In this case, be sure to set up ssh credentials for this new user.
