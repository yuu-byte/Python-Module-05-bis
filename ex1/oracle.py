import os

from dotenv import load_dotenv


def main() -> None:
    print("ORACLE STATUS: Consulting the configuration...")
    print()

    load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")

    if matrix_mode:
        print(f"Mode: {matrix_mode}")
    else:
        matrix_mode = "development"
        print("Mode: development (default) [WARNING]")

    if database_url:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured [WARNING]")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Not configured [WARNING]")

    if log_level:
        print(f"Log Level: {log_level}")
    else:
        log_level = "INFO"
        print("Log Level: INFO (default) [WARNING]")

    if zion_endpoint:
        print("Remote Network: Online")
    else:
        print("Remote Network: Not configured [WARNING]")

    print()

    if matrix_mode == "development":
        print("Development diagnostics:")
        print(f"Log Level: {log_level}")
        print(f"Database configured: {bool(database_url)}")
    elif matrix_mode == "production":
        print("Production mode: Diagnostic details hidden")
    else:
        print("Unknown mode [WARNING]")


if __name__ == "__main__":
    main()
