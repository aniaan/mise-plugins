import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))


from lib.lib import FormatKwargs, Plugin


def _filename_template(kwargs: FormatKwargs):
    if kwargs["platform"] == "macos":
        return "marksman-macos"
    return f"marksman-linux-{kwargs['arch']}"


PLUGIN = Plugin(
    name="marksman",
    cmd="marksman",
    repo_name="artempyanykh/marksman",
    filename_template=_filename_template,
    platform_map={
        "darwin": "macos",
        "linux": "linux",
    },
    arch_map={
        "x86_64": "x64",
        "aarch64": "arm64",
    },
    bin_path="marksman",
    is_compressed=False,
)
