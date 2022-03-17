function install() {
  NAME="$1"

  if [ "$2" == "" ]
    then
      pip3 install "$NAME" --target .tmp
    else
      pip3 install "$NAME==$2" --target .tmp
  fi

  mv ".tmp/$NAME" "./$NAME"
}


install emoji
install fuzzywuzzy
install Levenshtein

rm -rf .tmp
