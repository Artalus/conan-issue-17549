from conan import ConanFile


class C(ConanFile):
    name = "Wrappers"

    def requirements(self):
        # rttr headers are exposed in Wrappers.hpp
        self.requires("rttr/0.9.6", transitive_headers=True)

    python_requires = "pyreq/editable"
    python_requires_extend = "pyreq.PkgBase"
