#!/bin/bash -e

cd $(dirname "${BASH_SOURCE[0]}")

function help_message
{
    echo "Trigger unittests"
    echo "  - You can just run tests with no arguments"
    echo "    In such case all test cases will run"
    echo ""
    echo "  - Or you can add test file name as a parameter"
    echo "    then only tests within that file will run"
    echo ""
    echo "        Examples:"
    echo "              $0 tests/test_teamtry.py"
    echo ""
    echo "  - You can select specific test class/module to run by adding its name with '::' symbols"
    echo ""
    echo "        Examples:"
    echo "              $0 tests/test_teamtry.py::TestTeamtry"
    echo "              $0 tests/test_teamtry.py::TestTeamtry::test_main__just_a_test__returns_0"
    echo ""
    echo "List of available test files:"
    echo ""

    ls -1 -d tests/* | grep 'test_.*.py$' | sed -n 's/^/         - /p'

    echo ""
    exit 1
}

test=""
for arg in "$@"; do
    case $arg in
    "-h"|"--help")
        help_message
        ;;
    "-s"|"--nocapture" )
        echo "NO CAPTURE"
        capture="-s"
        ;;
    "-v"|"--verbose" )
        echo "VERBOSE"
        verbose="-vv"
        ;;
    * )
        test+=" $arg"
        ;;
    esac
done

VirtualEnvPath="virtualenv"

if [[ ! -d ${VirtualEnvPath} ]]; then
    echo "Virtual Env is not setup. Lets fix that"
    ./build.sh "$@"
fi

. "${VirtualEnvPath}/bin/activate" root

${VirtualEnvPath}/bin/pytest -v --import-mode=append $capture $verbose $test
RESULT=$?

echo "Result = ${RESULT}"
