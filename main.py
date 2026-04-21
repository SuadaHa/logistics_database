from db_setup import create_database


def main():
    print("Starting application...")
    create_database()
    print("Database is ready!")


if __name__ == "__main__":
    main()