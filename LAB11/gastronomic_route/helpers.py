
def validate_non_empty_string(value, field_name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string.")

def capitalize_each_word(text):
    return ' '.join(word.capitalize() for word in text.split())

def remove_duplicates(items):
    return list(set(items))

def format_output_list(title, items):
    print(f"\n🔹 {title}:")
    for item in items:
        print(f"   - {item}")
