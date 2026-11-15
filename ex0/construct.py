import os
import sys
import site


def main() -> None:

    python_path = sys.executable
    current_prefix = sys.prefix
    base_prefix = sys.base_prefix
    environment_name = os.path.basename(current_prefix)
    site_packages_paths = site.getsitepackages()
    is_venv = current_prefix != base_prefix

    if is_venv:
        print("LABORATORY STATUS: The laboratory is sealed")
        print()
        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {environment_name}")
        print(f"Environment Path: {current_prefix}")
        print()
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system.")
        print("Reagent installation path:")
        for path in site_packages_paths:
            print(path)

    else:
        print("LABORATORY STATUS: You are working in the open")
        print()
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected")
        print()
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.")
        print()
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows")
        print()
        print("Then run this program again.")


if __name__ == "__main__":
    main()
