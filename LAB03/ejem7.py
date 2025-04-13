from Linked_List import LinkedList


"Initial list: 5 -> 4 -> 3 -> None (Only for exercises: 7, 8 y 9)"

List = LinkedList
List.insert_at_beginning(3)
List.insert_at_beginning(4)
List.insert_at_beginning(5)




"EXERCISE 7 (delete_from_end())"

#Call delete_from_end() to remove the last element
List.delete_from_end()

# Call display() to check the updated list
print(List.display())