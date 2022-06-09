# This assumes that you have this checked out in a sibling directory to pact, and will "deploy" (just copy) all of the code to ../pact/myplugins.

DESTDIR="../pact/myplugins/pact_osx_dict"

mkdir -p $DESTDIR
cp -R . $DESTDIR 2>/dev/null

# Remove unneeded stuff.
pushd $DESTDIR
rm -rf .git
rm *.sh
rm .gitignore
popd
