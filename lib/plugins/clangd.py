import shutil
import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import GITHUB_CHECKER_FLAG, FormatKwargs, Plugin


def _copy(plugin: Plugin, src: Path, dst: Path, format_kwargs: FormatKwargs):
    src = src / f"clangd_{format_kwargs['version']}/"
    if not src.exists():
        raise Exception(f"Source path {src} does not exist")
    shutil.copytree(src, dst, dirs_exist_ok=True)
    cmd = dst / "bin" / plugin.cmd
    cmd.chmod(0o755)


PLUGIN = Plugin(
    name="clangd",
    cmd="clangd",
    repo_name="clangd/clangd",
    filename_template="clangd-{platform}-{version}.zip",
    platform_map={
        "darwin": "mac",
        "linux": "linux",
    },
    checksum_filename_template=GITHUB_CHECKER_FLAG,
    bin_path="clangd_{version}/bin/nvim",
    custom_copy=_copy,
)
