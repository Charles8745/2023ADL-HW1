

#!/bin/bash
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <input_file> <output_file> <prediction_file>"
    exit 1
fi

# modify test json
python modify_test_json.py "$1" "$2" "$3"
python test_submission.py "$1" "$2" "$3"
