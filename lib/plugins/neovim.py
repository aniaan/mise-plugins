import shutil
import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import GITHUB_CHECKER_FLAG, FormatKwargs, Plugin


def _copy(plugin: Plugin, src: Path, dst: Path, format_kwargs: FormatKwargs):
    src = src / f"{format_kwargs['filename'].rstrip('.tar.gz')}/"
    if not src.exists():
        raise Exception(f"Source path {src} does not exist")
    shutil.copytree(src, dst, dirs_exist_ok=True)
    cmd = dst / "bin" / plugin.cmd
    cmd.chmod(0o755)


PLUGIN = Plugin(
    name="neovim",
    cmd="nvim",
    repo_name="neovim/neovim",
    filename_template="nvim-{platform}-{arch}.tar.gz",
    platform_map={
        "darwin": "macos",
        "linux": "linux",
    },
    arch_map={
        "x86_64": "x86_64",
        "aarch64": "arm64",
    },
    checksum_filename_template=GITHUB_CHECKER_FLAG,
    bin_path=lambda kwargs: f"{kwargs['filename'].rstrip('.tar.gz')}/bin/nvim",
    recover_raw_version=lambda x: f"v{x}" if x[0].isdigit() else x,
    custom_copy=_copy,
)
