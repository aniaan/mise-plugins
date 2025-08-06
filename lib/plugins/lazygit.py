import sys
from pathlib import Path


parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import Plugin

PLUGIN = Plugin(
    name="lazygit",
    cmd="lazygit",
    repo_name="jesseduffield/lazygit",
    filename_template="lazygit_{normalize_version}_{platform}_{arch}.tar.gz",
    platform_map={
        "darwin": "darwin",
        "linux": "linux",
    },
    arch_map={
        "x86_64": "x86_64",
        "aarch64": "arm64",
    },
    checksum_filename_template="checksums.txt",
    bin_path="lazygit",
    recover_raw_version=lambda x: f"v{x}",
)
