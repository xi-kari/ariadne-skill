from __future__ import annotations

import argparse
import shutil
from pathlib import Path


SHARED_ASSETS = ("readme-hero.svg", "lattice-kernel-map.svg")


def _is_within(path: Path, parent: Path) -> bool:
    return path == parent or parent in path.parents


def _validate_output_path(repo_root: Path, source: Path, output_root: Path) -> None:
    git_dir = repo_root / ".git"
    build_dir = repo_root / "build"

    if output_root == Path(output_root.anchor):
        raise ValueError("unsafe site output path: filesystem root")
    if output_root == repo_root or output_root in repo_root.parents:
        raise ValueError("unsafe site output path: repository or its ancestor")
    if _is_within(output_root, source):
        raise ValueError("unsafe site output path: site source")
    if _is_within(output_root, git_dir):
        raise ValueError("unsafe site output path: Git metadata")
    if _is_within(output_root, repo_root) and not _is_within(output_root, build_dir):
        raise ValueError("unsafe site output path: repository source tree")


def _validate_source_path(repo_root: Path, source: Path, label: str) -> None:
    if source.is_symlink():
        raise ValueError(f"unsafe site source: symbolic link at {label}")
    resolved = source.resolve(strict=True)
    if not _is_within(resolved, repo_root):
        raise ValueError(f"unsafe site source: outside repository at {label}")


def _validate_source_tree(repo_root: Path, source: Path) -> None:
    _validate_source_path(repo_root, source, "site")
    for path in source.rglob("*"):
        _validate_source_path(repo_root, path, path.relative_to(repo_root).as_posix())


def build_site(repo_root: Path, output_root: Path) -> Path:
    """Build the dependency-free site into an explicitly selected directory."""

    repo_root = repo_root.resolve(strict=True)
    source = repo_root / "site"
    _validate_source_tree(repo_root, source)
    output_candidate = output_root.expanduser()
    if output_candidate.is_symlink():
        raise ValueError("unsafe site output path: symbolic link")
    output_root = output_candidate.resolve()
    _validate_output_path(repo_root, source, output_root)

    shared_assets = [repo_root / "docs" / "assets" / name for name in SHARED_ASSETS]
    for shared_asset in shared_assets:
        if not shared_asset.is_file():
            raise FileNotFoundError(f"missing shared site asset: {shared_asset}")
        _validate_source_path(
            repo_root,
            shared_asset,
            shared_asset.relative_to(repo_root).as_posix(),
        )

    if output_root.exists():
        if not output_root.is_dir():
            raise ValueError("site output path exists and is not a directory")
        if not _is_within(output_root, repo_root / "build"):
            raise ValueError("unsafe site output path: existing external directory")
        shutil.rmtree(output_root)

    shutil.copytree(source, output_root)
    assets = output_root / "assets"
    for shared_asset in shared_assets:
        name = shared_asset.name
        shutil.copy2(shared_asset, assets / name)

    return output_root


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build the Ariadne static website.")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("build/site"),
        help="repository-relative output directory (default: build/site)",
    )
    return parser.parse_args()


def main() -> int:
    args = _parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    output_root = args.output
    if not output_root.is_absolute():
        output_root = repo_root / output_root
    output_root = output_root.resolve()

    if not _is_within(output_root, repo_root):
        raise SystemExit("--output must stay inside the repository")

    try:
        built = build_site(repo_root, output_root)
    except (FileNotFoundError, ValueError) as error:
        raise SystemExit(f"site build failed: {error}") from None
    print(f"Built Ariadne site: {built}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
