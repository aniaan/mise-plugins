import sys
from pathlib import Path


parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="zellij",
    cmd="zellij",
    repo_name="zellij-org/zellij",
    filename_template="zellij-{arch}-{platform}.tar.gz",
    platform_map={
        "darwin": "apple-darwin",
        "linux": "unknown-linux-musl",
    },
    bin_path="zellij",
    checksum_stage="extract",
    checksum_filename_template="zellij-{arch}-{platform}.sha256sum",
    recover_raw_version=lambda x: f"v{x}",

)
