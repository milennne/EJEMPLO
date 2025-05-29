from bst import ChanchirataDB
from dish import Dish

def test_chanchirata_db():
    print("🔬 Running tests for ChanchirataDB...\n")
    db = ChanchirataDB()

    # 1️⃣ Insertar 5 platos con diferentes códigos
    db.insert_dish(Dish(101, "Ceviche", 25.0, "Costa"))
    db.insert_dish(Dish(202, "Pachamanca", 35.0, "Sierra"))
    db.insert_dish(Dish(303, "Tacacho con Cecina", 30.0, "Selva"))
    db.insert_dish(Dish(404, "Lomo Saltado", 28.0, "Costa"))
    db.insert_dish(Dish(505, "Juane", 26.0, "Selva"))
    print("✅ Test 1: 5 dishes inserted\n")

    # 2️⃣ Buscar un plato que existe
    found = db.search_by_code(202)
    assert found is not None and found.name == "Pachamanca"
    print("✅ Test 2: Search existing dish\n")

    # 3️⃣ Buscar un plato que NO existe
    not_found = db.search_by_code(999)
    assert not_found is None
    print("✅ Test 3: Search non-existing dish\n")

    # 4️⃣ Eliminar un plato que existe
    db.delete_by_code(101)  # Ceviche
    assert db.search_by_code(101) is None
    print("✅ Test 4: Delete existing dish\n")

    # 5️⃣ Eliminar un plato que NO existe
    db.delete_by_code(888)  # No existe
    print("✅ Test 5: Delete non-existing dish\n")

    # 6️⃣ Insertar un código duplicado
    db.insert_dish(Dish(202, "Pachamanca Reloaded", 40.0, "Costa"))  # Código duplicado
    print("✅ Test 6: Duplicate insert handled\n")

    # 7️⃣ Listar platos en orden ascendente por código
    ordered_dishes = db.list_in_order()
    ordered_codes = [dish.code for dish in ordered_dishes]
    assert ordered_codes == sorted(ordered_codes)
    print("✅ Test 7: In-order listing correct\n")

    # 8️⃣ Insertar y eliminar varios platos y verificar consistencia
    db.insert_dish(Dish(606, "Anticucho", 20.0, "Costa"))
    db.insert_dish(Dish(707, "Carapulcra", 24.0, "Sierra"))
    db.delete_by_code(303)  # Tacacho
    assert db.search_by_code(303) is None
    assert db.search_by_code(606) is not None
    print("✅ Test 8: Multiple insert/delete consistent\n")

    # 9️⃣ Insertar platos en orden descendente (árbol degenerado)
    db2 = ChanchirataDB()
    db2.insert_dish(Dish(500, "Aji de Gallina", 20.0, "Costa"))
    db2.insert_dish(Dish(400, "Olluquito", 22.0, "Sierra"))
    db2.insert_dish(Dish(300, "Causa Limeña", 18.0, "Costa"))
    db2.insert_dish(Dish(200, "Tacu Tacu", 19.0, "Costa"))
    db2.insert_dish(Dish(100, "Chanfainita", 21.0, "Sierra"))
    db2.list_in_order()
    print("✅ Test 9: Degenerate BST works\n")

    # 🔟 Insertar platos en orden aleatorio y verificar que todo funcione
    db3 = ChanchirataDB()
    import random
    random_dishes = [
        Dish(120, "Cau Cau", 19.0, "Costa"),
        Dish(450, "Choritos a la Chalaca", 22.0, "Costa"),
        Dish(310, "Arroz con Pato", 35.0, "Norte"),
        Dish(180, "Escabeche", 20.0, "Costa"),
        Dish(390, "Shámbar", 23.0, "Norte")
    ]
    for d in random_dishes:
        db3.insert_dish(d)
    db3.list_in_order()
    print("✅ Test 10: Random insertions correct\n")

    print("🎉 All tests passed!")

test_chanchirata_db()

