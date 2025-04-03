from Linked_List import LinkedList


"Initial list: 5 -> 4 -> 3 -> None (Only for exercises: 7, 8 y 9)"

List = LinkedList
List.insert_at_beginning(3)
List.insert_at_beginning(4)
List.insert_at_beginning(5)

"EXERCISE 8 (delete_from_position())"

# Test case: Delete the node at position 1 (which is '4' in this case)
deleted_value = List.delete_from_position(1)

# Display the updated list after deletion
print(f"Deleted value: {deleted_value}")
print("Updated list:", List.display())