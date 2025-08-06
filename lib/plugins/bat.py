import sys
from pathlib import Path


parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="bat",
    cmd="bat",
    repo_name="sharkdp/bat",
    filename_template="bat-{version}-{arch}-{platform}.tar.gz",
    platform_map={
        "darwin": "apple-darwin",
        "linux": "unknown-linux-gnu",
    },
    bin_path=lambda kwargs: f"{kwargs['filename'].rstrip('.tar.gz')}/bat",
    recover_raw_version=lambda x: f"v{x}",
)
