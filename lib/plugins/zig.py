import shutil
import sys
from pathlib import Path

from packaging import version

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import FormatKwargs, Plugin, verify_by_minisign

_PUBLIC_KEY = "RWSGOq2NVecA2UPNdBUZykf1CCb147pkmdtYxgb3Ti+JO/wCYvhbAb/U"


def _copy(plugin: Plugin, src: Path, dst: Path, format_kwargs: FormatKwargs):
    src = src / Path(f"{format_kwargs['filename'].rstrip('.tar.xz')}").name
    if not src.exists():
        raise Exception(f"Source path {src} does not exist")
    dst = dst / "bin"
    shutil.copytree(src, dst, dirs_exist_ok=True)
    cmd = dst / plugin.cmd
    cmd.chmod(0o755)


PLUGIN = Plugin(
    name="zig",
    cmd="zig",
    repo_name="ziglang/zig",
    filename_template="https://ziglang.org/download/{version}/zig-{platform}-{arch}-{version}.tar.xz",
    checksum_filename_template="{filename}.minisig",
    bin_path="zig",
    platform_map={
        "darwin": "macos",
        "linux": "linux",
    },
    custom_checker=lambda file_path, checksum_path, format_kwargs: verify_by_minisign(
        public_key=_PUBLIC_KEY,
        file_path=file_path,
        signature_path=checksum_path,
        format_kwargs=format_kwargs,
    ),
    custom_copy=_copy,
    sort_version_key=lambda x: version.parse(x["tag_name"].lstrip("v")),
)
