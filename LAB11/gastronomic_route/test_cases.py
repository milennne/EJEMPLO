from gastronomic_route import GastronomicRoute

print("🔍 Running test cases for GastronomicRoute...\n")

# Initialize route
route = GastronomicRoute()

# 1. Add 3 branches in different regions
route.add_branch("Chanchirata Arequipa", "Sierra", "Rocoto Relleno")
route.add_branch("Chanchirata Lima", "Costa", "Ceviche")
route.add_branch("Chanchirata Iquitos", "Selva", "Juane")

# 2. Add a branch with same region but different specialty
route.add_branch("Chanchirata Trujillo", "Costa", "Cabrito")

# 3. Preorder traversal
print("🧭 Preorder traversal:")
route.preorder()

# 4. Inorder traversal
print("\n📝 Inorder traversal:")
route.inorder()

# 5. Postorder traversal
print("\n🔁 Postorder traversal:")
route.postorder()

# 6–8. Show summary (total branches, unique specialties, regions)
print("\n📊 Summary:")
route.summary()

# 9. Insert nodes to simulate a balanced tree
balanced_route = GastronomicRoute()
branches_balanced = [
    ("Chanchirata Cusco", "Sierra", "Adobo"),
    ("Chanchirata Arequipa", "Sierra", "Rocoto Relleno"),
    ("Chanchirata Lima", "Costa", "Ceviche"),
]
for name, region, dish in branches_balanced:
    balanced_route.add_branch(name, region, dish)
print("\n🌿 Balanced tree - Inorder:")
balanced_route.inorder()

# 10. Insert nodes to simulate a degenerate (linked-list-like) tree
degenerate_route = GastronomicRoute()
branches_degenerate = [
    ("Chanchirata A", "Costa", "Dish A"),
    ("Chanchirata B", "Costa", "Dish B"),
    ("Chanchirata C", "Costa", "Dish C"),
]
for name, region, dish in branches_degenerate:
    degenerate_route.add_branch(name, region, dish)
print("\n🌵 Degenerate tree - Preorder:")
degenerate_route.preorder()

print("\n✅ All test cases executed.\n")
