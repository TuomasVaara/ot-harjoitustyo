from initialize_database import initialize_database

def build():
    initialize_database()


# Makes calling the build function from command prompt possible!
if __name__ == "__main__":
    build()