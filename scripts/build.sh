function build() {
  echo "Generating $1 binary"
  echo

  poetry run pyinstaller --onedir --paths ./src/ "src/$1.py" 1> /dev/null

  echo "Workspace cleanup"
  echo

  rm "./$1.spec"
  rm -rf "./build/"

  echo
	echo "Finished generating bin file for $1"
	echo
}


rm -rf "./dist/"

build main

echo "Finished"
echo
