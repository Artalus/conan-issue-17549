from conan import ConanFile


class C(ConanFile):
    name = "Subproject"
    requires = ("Wrappers/editable",)
    python_requires = "pyreq/editable"
    python_requires_extend = "pyreq.PkgBase"
