from conan import ConanFile


class C(ConanFile):
    name = "BigProject"
    requires = (
        "Subproject/editable",
    )

    python_requires = "pyreq/editable"
    python_requires_extend = "pyreq.PkgBase"
