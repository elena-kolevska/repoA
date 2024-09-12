import os
import sys
from packaging.version import Version, InvalidVersion

def compare_versions(new_version, existing_version):
    try:
        new_ver = Version(new_version)
        existing_ver = Version(existing_version)
    except InvalidVersion:
        print("Invalid version format")
        sys.exit(1)

    if new_ver > existing_ver:
        print("New version is greater than existing version.")
        with open(os.getenv("GITHUB_ENV"), "a") as github_env:
            github_env.write("UPDATE_REQUIRED=true\n")
        sys.exit(0)
    else:
        print("New version is not greater. Skipping update.")
        with open(os.getenv("GITHUB_ENV"), "a") as github_env:
            github_env.write("UPDATE_REQUIRED=false\n")
        sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: compare_versions.py <new_version> <existing_version>")
        sys.exit(1)

    new_version = sys.argv[1]
    existing_version = sys.argv[2]

    compare_versions(new_version, existing_version)
