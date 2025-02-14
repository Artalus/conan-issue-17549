from pathlib import Path

from conan import Workspace
from conan.api.output import ConanOutput

name = "KdMonoRepo"


_editables_result = {}

class MyWorkspace(Workspace):
    def name(self):
        return "workspace"
    def add(self, ref, path, *args, **kwargs):
        self.output.info(f"Adding {ref} at {path}")
        super().add(ref, path, *args, **kwargs)
    def remove(self, path, *args, **kwargs):
        self.output.info(f"Removing {path}")
        return super().remove(path, *args, **kwargs)
    def editables(self) -> dict:
        # editables() gets called multiple times while conan executes; avoid traversing
        # filesystem again and again for same results
        ConanOutput().info("-- workspace editables")
        global _editables_result
        if _editables_result:
            return _editables_result

        folder = Path(self.folder)

        for f in folder.glob("./*/conanfile.py"):
            # conan automatically appends conanfile.py to `load`ed paths
            f = f.parent.as_posix()
            ConanOutput().info(f"-- workspace processing {f}")
            conanfile = self.load_conanfile(f)
            # FIXME: would use /{conanfile.version} , but it is None
            _editables_result[f"{conanfile.name}/editable"] = {"path": f}

        return _editables_result
