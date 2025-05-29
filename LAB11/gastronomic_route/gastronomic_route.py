from branch import Branch

class GastronomicRoute:
    def __init__(self):
        self.root = None

    def add_branch(self, name, region, specialty):
        new_branch = Branch(name, region, specialty)
        if not self.root:
            self.root = new_branch
        else:
            self._insert(self.root, new_branch)

    def _insert(self, current, new_branch):
        if new_branch.name < current.name:
            if current.left is None:
                current.left = new_branch
            else:
                self._insert(current.left, new_branch)
        else:
            if current.right is None:
                current.right = new_branch
            else:
                self._insert(current.right, new_branch)

    def preorder(self):
        print("🧭 Visiting Order:")
        self._preorder(self.root)

    def _preorder(self, node):
        if node:
            print(f"👉 {node.name} – {node.specialty} ({node.region})")
            self._preorder(node.left)
            self._preorder(node.right)

    def inorder(self):
        print("📝 Regional Order:")
        self._inorder(self.root)

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(f"👉 {node.name} – {node.specialty} ({node.region})")
            self._inorder(node.right)

    def postorder(self):
        print("🔁 Visit Summary:")
        self._postorder(self.root)

    def _postorder(self, node):
        if node:
            self._postorder(node.left)
            self._postorder(node.right)
            print(f"👉 {node.name} – {node.specialty} ({node.region})")

    def summary(self):
        total = self._count_branches(self.root)
        specialties = set()
        regions = set()
        self._collect_info(self.root, specialties, regions)
        print("✅ Total branches:", total)
        print("🍲 Unique specialties:", ", ".join(sorted(specialties)))
        print("🗺️ Regions represented:", ", ".join(sorted(regions)))

    def _count_branches(self, node):
        if node is None:
            return 0
        return 1 + self._count_branches(node.left) + self._count_branches(node.right)

    def _collect_info(self, node, specialties, regions):
        if node:
            specialties.add(node.specialty)
            regions.add(node.region)
            self._collect_info(node.left, specialties, regions)
            self._collect_info(node.right, specialties, regions)
