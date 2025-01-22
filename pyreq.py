from pathlib import Path

from conan import ConanFile, conan_version
from conan.tools.cmake import CMake, CMakeToolchain


class PkgBase(object):
    generators = ("CMakeDeps",)
    settings = ("os", "compiler", "build_type", "arch")
    options = {
        "shared": [False, True],
    }
    default_options = {
        "shared": False,
    }

    def set_version(self):
        self.version = "editable"

    def init(self):
        # Conan does not inherit options by default, so docs and Slack suggest this instead
        base = self.python_requires["pyreq"].module.PkgBase
        if conan_version.major == 1:
            self.options = {**base.options, **self.options}
            self.default_options = {**base.default_options, **self.default_options}
        else:
            self.options.update(base.options, base.default_options)

    def layout(self):
        self.folders.build = "build"
        self.folders.generators = f"{self.folders.build}/Conan/"
        self.folders.source = "."

    def generate(self):
        tc = CMakeToolchain(self, generator="Ninja")
        tc.generate()

    def build(self):
        # build directory persists for editable packages from monorepo;
        # wipe cmake cache before building, just in case
        cache = Path(self.build_folder) / "CMakeCache.txt"
        if cache.is_file():
            self.output.info(f"** {cache} exists, removing")
            cache.unlink()

        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package_info(self):
        # libdirs defaults to [lib]; editable packages do not package anything
        self.cpp_info.libdirs = [self.folders.build]
        # collect_libs() returns empty list since there is no `package_folder`
        self.cpp_info.libs = [self.name]


class C(ConanFile):
    name = "pyreq"
    version = "editable"
