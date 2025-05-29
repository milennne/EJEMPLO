class Branch:
    def __init__(self, name, region, specialty):
        self.name = name                # Branch name 📍
        self.region = region            # Region in Peru 🇵🇪
        self.specialty = specialty      # Signature dish 🍽️
        self.left = None                # Left-connected branch ↩️
        self.right = None               # Right-connected branch ↪️
