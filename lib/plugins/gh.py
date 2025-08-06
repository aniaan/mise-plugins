import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

import shutil

from lib.lib import FormatKwargs, Plugin


def _copy(plugin: Plugin, src: Path, dst: Path, format_kwargs: FormatKwargs):
    folder = format_kwargs["filename"].removesuffix(".tar.gz").removesuffix(".zip")
    src = src / folder
    if not src.exists():
        raise Exception(f"Source path {src} does not exist")
    shutil.copytree(src, dst, dirs_exist_ok=True)
    cmd = dst / "bin" / plugin.cmd
    cmd.chmod(0o755)


def _filename_template(kwargs: FormatKwargs):
    suffix = "zip"
    if kwargs["platform"] == "linux":
        suffix = "tar.gz"

    return f"gh_{kwargs['normalize_version']}_{kwargs['platform']}_{kwargs['arch']}.{suffix}"


PLUGIN = Plugin(
    name="gh",
    cmd="gh",
    repo_name="cli/cli",
    filename_template=_filename_template,
    platform_map={
        "darwin": "macOS",
        "linux": "linux",
    },
    arch_map={
        "x86_64": "amd64",
        "aarch64": "arm64",
    },
    checksum_filename_template="gh_{normalize_version}_checksums.txt",
    bin_path="gh",
    recover_raw_version=lambda x: f"v{x}",
    custom_copy=_copy,
)
