poetry run pyinstaller --onefile --paths ./src/ src/main.py

rm -rf ./build
rm *.spec
