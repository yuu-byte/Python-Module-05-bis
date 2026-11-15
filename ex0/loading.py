
def main() -> None:
    print("REAGENT STATUS: Loading reagents...")
    print()
    print("Checking dependencies:")
    print()

    all_installed = True

    try:
        import pandas

        print(f"[OK] pandas ({pandas.__version__}) - Data manipulation ready")
    except ImportError:
        all_installed = False
        print("[MISSING] pandas is not installed")

    try:
        import numpy

        print(
            f"[OK] numpy ({numpy.__version__}) - Numerical computation ready"
        )
    except ImportError:
        all_installed = False
        print("[MISSING] numpy is not installed")

    print()
    print("pip vs Poetry:")
    print(
        "  requirements.txt declares what to install; "
        "pip resolves it at install time."
    )
    print(
        "  pyproject.toml declares the same constraints, "
        "and Poetry pins the resolved"
    )
    print("  versions in poetry.lock so every install is identical.")
    print()

    if all_installed:
        print("All reagents present and accounted for.")
    else:
        print("To install missing dependencies:")
        print("  Using pip:")
        print("    pip install -r ex0/requirements.txt")
        print("  Using Poetry:")
        print("    cd ex0")
        print("    poetry install")


if __name__ == "__main__":
    main()
