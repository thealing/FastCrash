import os
import shutil
from pathlib import Path

name = "RivetRival"

def publish_builds():
    base_build_dir = Path("Build/bin")
    publish_dir = Path("publish")
    
    if publish_dir.exists():
        shutil.rmtree(publish_dir)
    publish_dir.mkdir(parents=True)

    archs = ["arm", "arm64", "x64", "x86"]
    for arch in archs:
        release_path = base_build_dir / arch / "Release"
        
        if not release_path.exists():
            print(f"Skipping {arch}: Path not found ({release_path})")
            continue

        found_target = False
        
        for extension in ["*.exe", "*.apk"]:
            for file_path in release_path.glob(extension):
                new_name = f"{name}-{arch}{file_path.suffix}"
                dest_path = publish_dir / new_name
                
                try:
                    shutil.copy2(file_path, dest_path)
                    print(f"Copied: {arch} -> {new_name}")
                    found_target = True
                except Exception as e:
                    print(f"Error copying {file_path.name}: {e}")

        if not found_target:
            print(f"No targets found in {release_path}")

if __name__ == "__main__":
    publish_builds()
		