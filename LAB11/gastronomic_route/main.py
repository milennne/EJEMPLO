from gastronomic_route import GastronomicRoute
from helpers import validate_non_empty_string

def print_menu():
    print("\n🌐 Welcome to Chanchirata's Gastronomic Route!")
    print("1. Add new branch")
    print("2. Show route (Preorder)")
    print("3. Show route (Inorder)")
    print("4. Show route (Postorder)")
    print("5. Show summary")
    print("0. Exit")

def main():
    route = GastronomicRoute()

    while True:
        print_menu()
        option = input("👉 Choose an option: ").strip()

        if option == "1":
            try:
                name = input("📍 Branch name: ").strip()
                region = input("🗺️ Region: ").strip()
                specialty = input("🍽️ Specialty: ").strip()

                validate_non_empty_string(name, "Branch name")
                validate_non_empty_string(region, "Region")
                validate_non_empty_string(specialty, "Specialty")
                
                route.add_branch(name, region, specialty)
                print("✅ Branch added successfully!")
            except ValueError as e:
                print(f"⚠️ Error: {e}")

        elif option == "2":
            print("\n🧭 Route in Preorder:")
            route.preorder()

        elif option == "3":
            print("\n📝 Route in Inorder:")
            route.inorder()

        elif option == "4":
            print("\n🔁 Route in Postorder:")
            route.postorder()

        elif option == "5":
            print("\n📊 Route Summary:")
            route.summary()

        elif option == "0":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
