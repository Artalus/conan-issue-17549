from pathlib import Path

from conan.api.output import ConanOutput
from conan.internal.workspace import _UserWorkspaceAPI

name = "KdMonoRepo"


# global variable initialized automatically by conan internals
workspace_api: _UserWorkspaceAPI


_editables_result = {}


def editables() -> dict:
    # editables() gets called multiple times while conan executes; avoid traversing
    # filesystem again and again for same results
    global _editables_result
    if _editables_result:
        return _editables_result

    folder = Path(workspace_api.folder)

    for f in [(folder / "pyreq.py"), *folder.glob("./*/conanfile.py")]:
        f = f.as_posix()
        ConanOutput().info(f"-- workspace processing {f}")
        conanfile = workspace_api.load(f)
        # FIXME: would use /{conanfile.version} , but it is None
        _editables_result[f"{conanfile.name}/editable"] = {"path": f}

    return _editables_result
