import pickle

VALID_REGIONS = ["Costa", "Sierra", "Selva"]

def is_valid_region(region):
    return region.capitalize() in VALID_REGIONS

def is_valid_price(price_str):
    try:
        price = float(price_str)
        return price > 0
    except ValueError:
        return False

def format_region(region):
    """Normalize region with first letter capitalized (e.g., 'selva' -> 'Selva')"""
    return region.capitalize()

def save_database(db, filename="chanchirata_db.pkl"):
    try:
        with open(filename, "wb") as file:
            pickle.dump(db, file)
        print("💾 Database saved successfully.")
    except Exception as e:
        print(f"❌ Error saving database: {e}")

def load_database(filename="chanchirata_db.pkl"):
    try:
        with open(filename, "rb") as file:
            db = pickle.load(file)
        print("📂 Database loaded successfully.")
        return db
    except FileNotFoundError:
        print("⚠️ No saved database found. Starting new one.")
        return None
    except Exception as e:
        print(f"❌ Error loading database: {e}")
        return None

