from dish import Dish

class BSTNode:
    def __init__(self, dish):
        self.dish = dish
        self.left = None
        self.right = None

class ChanchirataDB:
    def __init__(self):
        self.root = None

    def insert_dish(self, dish):
        def _insert(node, dish):
            if node is None:
                return BSTNode(dish)
            if dish.code < node.dish.code:
                node.left = _insert(node.left, dish)
            elif dish.code > node.dish.code:
                node.right = _insert(node.right, dish)
            else:
                print(f"❌ Error: Dish with code {dish.code} already exists.")
            return node

        self.root = _insert(self.root, dish)

    def search_by_code(self, code):
        def _search(node, code):
            if node is None:
                return None
            if code == node.dish.code:
                return node.dish
            elif code < node.dish.code:
                return _search(node.left, code)
            else:
                return _search(node.right, code)

        result = _search(self.root, code)
        if result:
            print(f"✅ Found: {result}")
        else:
            print(f"📭 Dish with code {code} not found.")
        return result

    def delete_by_code(self, code):
        def _min_value_node(node):
            current = node
            while current.left:
                current = current.left
            return current

        def _delete(node, code):
            if node is None:
                print(f"📭 Dish with code {code} not found.")
                return None
            if code < node.dish.code:
                node.left = _delete(node.left, code)
            elif code > node.dish.code:
                node.right = _delete(node.right, code)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                min_larger_node = _min_value_node(node.right)
                node.dish = min_larger_node.dish
                node.right = _delete(node.right, min_larger_node.dish.code)
            return node

        self.root = _delete(self.root, code)

    def list_in_order(self):
        def _inorder(node, result):
            if node:
                _inorder(node.left, result)
                result.append(node.dish)
                _inorder(node.right, result)

        result = []
        _inorder(self.root, result)
        print("📋 Menu (in-order):")
        for dish in result:
            print(dish)
        return result

    def search_by_name(self, name):
        """Search for dishes by full or partial name (case insensitive)."""

        def _search(node, name, results):
            if node:
                _search(node.left, name, results)
                if name.lower() in node.dish.name.lower():
                    results.append(node.dish)
                _search(node.right, name, results)

        results = []
        _search(self.root, name, results)

        if results:
            print(f"🔍 Found {len(results)} result(s) matching '{name}':")
            for dish in results:
                print(f"  - {dish}")
        else:
            print(f"📭 No dishes found matching '{name}'.")

        return results

    def search_by_region(self, region):
        """Search for dishes by region (case insensitive)."""

        def _search(node, region, results):
            if node:
                _search(node.left, region, results)
                if region.lower() == node.dish.region.lower():
                    results.append(node.dish)
                _search(node.right, region, results)

        results = []
        _search(self.root, region, results)

        if results:
            print(f"📍 Dishes from region '{region}':")
            for dish in results:
                print(f"  - {dish}")
        else:
            print(f"📭 No dishes found from region '{region}'.")

        return results

