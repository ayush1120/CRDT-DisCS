PROJECT_DIR=$1
PYTHONPATH=$2

SETUP_DIR="${PROJECT_DIR}/setup"
BASE_DIR="${PROJECT_DIR}/scarf"


command cd "$PROJECT_DIR"
command virtualenv -p "${PYTHONPATH}" envCRDT-DisCS
command source "${PROJECT_DIR}/envCRDT-DisCS/bin/activate"
command pip install -r "${PROJECT_DIR}/requirements.txt"
command deactivate
