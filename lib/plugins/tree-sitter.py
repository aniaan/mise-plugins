import sys
from pathlib import Path

parent_dir = Path(__file__).parent.parent.parent
if str(parent_dir) not in sys.path:
    sys.path.insert(0, str(parent_dir))

from lib.lib import GITHUB_CHECKER_FLAG, Plugin

PLUGIN = Plugin(
    name="tree-sitter",
    cmd="tree-sitter",
    repo_name="tree-sitter/tree-sitter",
    filename_template="tree-sitter-{platform}-{arch}.gz",
    platform_map={
        "darwin": "macos",
        "linux": "linux",
    },
    arch_map={
        "x86_64": "x64",
        "aarch64": "arm64",
    },
    checksum_filename_template=GITHUB_CHECKER_FLAG,
    bin_path=lambda kwargs: f"{kwargs['filename'].rstrip('.gz')}",
    recover_raw_version=lambda x: f"v{x}",
)
