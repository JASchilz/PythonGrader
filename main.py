import subprocess
import os
import time
import sys

# The server for cloning student files and your username on that server.
# For example, you usually clone files from github as 'git@github.com'
git_user = "git"
git_server = "github.com"

if len(sys.argv) is not 3:
    print("usage: python {} project-name users-file.txt".format(sys.argv[0]))
    exit(1)

project_name = sys.argv[1]
users_file = sys.argv[2]

with open(users_file) as f:
    users = f.read().splitlines()

# Create the reports directories
os.makedirs(os.path.join("reports", project_name, "good"), exist_ok=True)
os.makedirs(os.path.join("reports", project_name, "bad"), exist_ok=True)

for user in users:
    # The path to this user's homework submission
    repo_path = os.path.join('users', user, project_name)

    # Remove any existing submission that we've downloaded; we're going to test
    # whatever is in the repo right now.
    subprocess.call(
        [
            "rm",
            "-rf",
            repo_path,
        ]
    )

    # Clone down the user's submission into repo_path
    result = subprocess.call(
        [
            "git",
            "clone",
            "{}@{}:{}/{}".format(git_user, git_server, user, project_name),
            repo_path,
        ]
    )

    # Did we successfully clone down the project?
    clone_successful = result is 0

    # If not, then skip this student
    if not clone_successful:
        continue

    try:
        time.sleep(3)

        # Run the tests, collecting stdout and stderr
        stdout = b""
        stderr = b""
        test_process = subprocess.Popen(
            [
                "python",
                os.path.join("tests", "test.py"),
            ],
            cwd=os.path.join(repo_path, "homework"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        # Hope for the best
        success = True
        try:
            # Retrieve stdout and stderr
            stdout, stderr = test_process.communicate(timeout=10)
        except subprocess.TimeoutExpired:
            # If the tests took too long, then kill the process, record tests as failed
            test_process.kill()
            success = False

        if test_process.returncode is None or test_process.returncode is not 0:
            # If the tests failed, mark them as failed
            success = False

        # Build the paths for this student's good/bad reports
        good_result_path = os.path.join("reports", project_name, "good", "{}.txt".format(user))
        bad_result_path = os.path.join("reports", project_name, "bad", "{}.txt".format(user))

        # Reformat stderr and stdout
        contents = (stderr.decode().replace("\r\n", "\n") + "\n\n" + stdout.decode().replace("\r\n", "\n"))

        # Remove any existing good/bad reports
        subprocess.call(["rm", bad_result_path])
        subprocess.call(["rm", good_result_path])

        if success:
            result_path = good_result_path
        else:
            result_path = bad_result_path

        with open(result_path, "w") as f:
            f.write(contents)

    finally:
        # In any case, kill the test process
        test_process.kill()

