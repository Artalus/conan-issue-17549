python -m venv .venv
source .venv/bin/activate
python -m pip install git+https://github.com/memsharded/conan@feature/workspace_install

export CONAN_HOME=`pwd`/.conan2/
rm -rf $CONAN_HOME/profiles/
rm -rf $CONAN_HOME/editable_packages.json
conan profile detect

export BUILDDIR=`pwd`/3BigProject/build/
