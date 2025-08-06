import sys
from pathlib import Path


parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="rust-analyzer",
    cmd="rust-analyzer",
    repo_name="rust-lang/rust-analyzer",
    filename_template="rust-analyzer-{arch}-{platform}.gz",
    platform_map={
        "darwin": "apple-darwin",
        "linux": "unknown-linux-gnu",
    },
    bin_path="rust-analyzer",
)
