import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="stylua",
    cmd="stylua",
    repo_name="JohnnyMorganz/StyLua",
    filename_template="stylua-{platform}-{arch}.zip",
    platform_map={
        "darwin": "macos",
        "linux": "linux",
    },
    bin_path="stylua",
    recover_raw_version=lambda x: f"v{x}",
)
