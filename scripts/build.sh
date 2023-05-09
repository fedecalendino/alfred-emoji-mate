rm -rf "./dist/"

echo "Copy dependencies"
cp -r $(find .venv | egrep "site-packages$") ./dist

echo "Clean up dist folder"
cd dist

find . | grep __pycache__ | xargs rm -rf
ls -d */ | grep info | xargs rm -rf
ls | egrep "^\_.*" | xargs rm -rf

rm -rf *.so black blackd blib2to3 distutils* pkg_resources pip* setuptools* wheel*

cd ..

echo "Copy source code"
cp -r ./src/* dist

echo "Finished"
echo
