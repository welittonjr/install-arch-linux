DIR_VENV="venv/"

if [ ! -d "$DIR_VENV" ]; then
    python3 -m venv venv
fi