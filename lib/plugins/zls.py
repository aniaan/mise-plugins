import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin, verify_by_minisign

_PUBLIC_KEY = "RWR+9B91GBZ0zOjh6Lr17+zKf5BoSuFvrx2xSeDE57uIYvnKBGmMjOex"

PLUGIN = Plugin(
    name="zls",
    cmd="zls",
    repo_name="zigtools/zls",
    filename_template="zls-{arch}-{platform}.tar.xz",
    checksum_filename_template="{filename}.minisig",
    bin_path="zls",
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
)
