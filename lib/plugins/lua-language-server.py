import sys
from pathlib import Path
import shutil


parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin, FormatKwargs


def _copy(plugin: Plugin, src: Path, dst: Path, format_kwargs: FormatKwargs):
    # src = src / f"{format_kwargs['filename'].removesuffix('.tar.gz')}/"
    if not src.exists():
        raise Exception(f"Source path {src} does not exist")
    shutil.copytree(src, dst, dirs_exist_ok=True)
    cmd = dst / "bin" / plugin.cmd
    cmd.chmod(0o755)


PLUGIN = Plugin(
    name="lua-language-server",
    cmd="lua-language-server",
    repo_name="LuaLS/lua-language-server",
    filename_template="lua-language-server-{version}-{platform}-{arch}.tar.gz",
    arch_map={
        "x86_64": "x64",
        "aarch64": "arm64",
    },
    bin_path=lambda kwargs: f"{kwargs['filename'].removesuffix('.tar.gz')}/bin/lua-language-server",
    custom_copy=_copy,
)
