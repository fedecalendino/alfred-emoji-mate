BUNDLEID=$(plutil -extract bundleid raw -o - ./info.plist)
NAME=${BUNDLEID##*.}

VERSION=${1:-$(poetry version --short)}

FILENAME="$NAME.v$VERSION.alfredworkflow"

poetry version $VERSION
plutil -replace version -string $VERSION info.plist

echo "NAME: $NAME"
echo "BUNDLE ID: $BUNDLEID"
echo "CURRENT VERSION: v$(poetry version --short)"
echo "NEW VERSION: v$VERSION"
echo


echo "Building binaries..."
echo
./scripts/build.sh > /dev/null
echo


echo "Building release..."
echo

echo "Clean up non-exportable variables"
echo

# backup info.plist
cp info.plist old.plist

# find amount of variables to not export
VARIABLES_DONT_EXPORT_AMOUNT=$(plutil -extract variablesdontexport raw -o - ./info.plist)

for i in $(seq 0 $(expr "$VARIABLES_DONT_EXPORT_AMOUNT" - 1))
do
  VARIABLE=$(plutil -extract "variablesdontexport.$i" raw -o - ./info.plist)
  plutil -replace "variables.$VARIABLE" -string "" ./info.plist

  echo " * $VARIABLE: cleared"
done
echo

mkdir releases 2> /dev/null
zip "releases/$FILENAME" -r dist img *.png info.plist
echo


echo "Released $NAME v$VERSION"
echo " * releases/$FILENAME"
echo

# restore original info.plist
rm info.plist
mv old.plist info.plist
