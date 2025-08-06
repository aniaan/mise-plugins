import sys
from pathlib import Path


parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="starship",
    cmd="starship",
    repo_name="starship/starship",
    filename_template="starship-{arch}-{platform}.tar.gz",
    platform_map={
        "darwin": "apple-darwin",
        "linux": "unknown-linux-gnu",
    },
    bin_path="starship",
    checksum_filename_template="{filename}.sha256",
    recover_raw_version=lambda x: f"v{x}",
)
