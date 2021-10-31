import os

import alfred


@alfred.command("twine", help="publish the package on pypi")
def twine():
    alfred.invoke_command("build")

    login = os.getenv("TWINE_USERNAME")
    password = os.getenv("TWINE_PASSWORD")

    if not login or not password:
        print("")
        print("The credentials for pypi are missing. You have to be defined through environment variables TWINE_USERNAME and TWINE_PASSWORD")
        print("export TWINE_USERNAME=__token__")
        print("export TWINE_PASSWORD=pypi-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        exit(1)

    twine = alfred.sh("twine")
    alfred.run(twine, ['upload', '--non-interactive', 'dist/*'])
