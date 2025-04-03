from Linked_List import LinkedList


"Initial list: 5 -> 4 -> 3 -> None (Only for exercises: 7, 8 y 9)"

List = LinkedList
List.insert_at_beginning(3)
List.insert_at_beginning(4)
List.insert_at_beginning(5)



"#EXERCISE 9 (search())"

# Test searching for a value that exists in the list
result_1 = List.search(4)  # Expected output: 1 (since 4 is at position 1)
print("Position of 4:", result_1)

# Test searching for a value that does not exist in the list
result_2 = List.search(6)  # Expected output: -1 (since 6 is not in the list)
print("Position of 6:", result_2)
