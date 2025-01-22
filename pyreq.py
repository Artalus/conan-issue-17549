import os

from conan import ConanFile, conan_version
from conan.tools.cmake import CMakeToolchain


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


class C(ConanFile):
    name = "pyreq"
    version = "editable"
