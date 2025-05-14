#!/bin/sh

PATH_TO_FILE_REQUIREMENTS=""

# PARSE PARAMETERS
while [ "$#" -gt 0 ]; do
    case $1 in
        --file)
            PATH_TO_FILE_REQUIREMENTS="$2"
            shift 2
            ;;
        *)

        echo "UNKNOWN PARAMETER: $1"
        exit 1
        ;;
    esac
done

if [ -n "$PATH_TO_FILE_REQUIREMENTS" ]; then
    echo "A file path to \"requirements.txt\" has been provided: $PATH_TO_FILE_REQUIREMENTS"
else
    echo "No file path to \"requirements.txt\" has been provided (use --file <PATH>)."

    exit 1
fi

python3 -m venv venv

. venv/bin/activate

pip install --no-cache-dir -r $PATH_TO_FILE_REQUIREMENTS
