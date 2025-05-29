from bst import ChanchirataDB
from dish import Dish
from helpers import save_database, load_database, is_valid_price, is_valid_region, format_region

def show_menu():
    print("\n=== ChanchirataDB CLI ===")
    print("1. Insert dish")
    print("2. Search dish by code")
    print("3. Delete dish by code")
    print("4. Show all dishes (in-order)")
    print("5. Exit")
    print("6. Save database")
    print("7. Load database")
    print("8. Search dish by name")
    print("9. Search dishes by region")


def main():
    db = ChanchirataDB()

    while True:
        show_menu()
        option = input("Choose an option: ")

        if option == "1":
            try:
                code = int(input("🔢 Enter dish code (integer): "))
                if db.search(code):
                    print("❌ A dish with that code already exists.")
                    continue

                name = input("🍽️ Enter dish name: ").strip()
                if not name:
                    print("❌ Dish name cannot be empty.")
                    continue

                region = input("🌍 Enter region (Costa, Sierra, Selva): ").strip()
                if not is_valid_region(region):
                    print("❌ Invalid region. Must be: Costa, Sierra, or Selva.")
                    continue

                price_input = input("💰 Enter dish price (e.g., 15.50): ").strip()
                if not is_valid_price(price_input):
                    print("❌ Invalid price. Must be a number > 0.")
                    continue

                price = float(price_input)
                region = format_region(region)

                dish = Dish(code, name, region, price)
                db.insert(dish)

            except ValueError:
                print("❌ Invalid input. Please try again.")


        elif option == "2":
            try:
                code = int(input("Enter code to search: "))
                db.search_by_code(code)
            except ValueError:
                print("❌ Invalid code.")

        elif option == "3":
            try:
                code = int(input("Enter code to delete: "))
                db.delete_by_code(code)
            except ValueError:
                print("❌ Invalid code.")

        elif option == "4":
            db.list_in_order()

        elif option == "5":
            print("👋 Goodbye!")
            break

        elif option == "6":
            save_database(db)

        elif option == "7":
            loaded_db = load_database()
            if loaded_db:
                db = loaded_db

        elif option == "8":
            name = input("🔤 Enter dish name (or part of it): ")
            db.search_by_name(name)

        elif option == "9":
            region = input("🌍 Enter region (e.g., Costa, Sierra, Selva): ")
            db.search_by_region(region)


        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
