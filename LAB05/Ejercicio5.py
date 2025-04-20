class Node:
    """Represent a node in a linked list."""
    
    def __init__(self, data):
        """Initialize a node with data and next reference."""
        self.data = data  # Store data in this node
        self.next = None 
class LinkedQueue:
    """Queue implementation using a linked list."""

    def __init__(self):
        """Initialize an empty queue."""
        self.front = None  # For dequeue operations ⬅️
        self.rear = None   # For enqueue operations ➡️
        self.size_count = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def enqueue(self, item):
        """Add an item to the rear of the queue."""
        new_node = Node(item)

        # If queue is empty, both front and rear point to the new node 🏁
        if self.is_empty():
            self.front = new_node
        else:
            # Link the new node at the end 🔗
            self.rear.next = new_node

        # Update rear to the new node ➡️
        self.rear = new_node
        self.size_count += 1
        return True

    def dequeue(self):
        """Remove and return the front item from the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")

        # Store the front node's data 📦
        item = self.front.data

        # Move front pointer to the next node ⬅️
        self.front = self.front.next

        # If queue becomes empty, update rear pointer too
        if self.front is None:
            self.rear = None

        self.size_count -= 1
        return item

    def peek(self):
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty! 🚫")
        return self.front.data

    def size(self):
        """Return the number of items in the queue."""
        return self.size_count

    def __str__(self):
        """Return a string representation of the queue."""
        if self.is_empty():
            return "Queue: []"

        result = []
        current = self.front
        while current:
            result.append(str(current.data))
            current = current.next

        return f"Queue: [{', '.join(result)}]"
class Customer:
    """Represent a customer in a supermarket."""

    def __init__(self, id, items_count):
        """Initialize a customer with ID and number of items."""
        self.id = id
        self.items_count = items_count
        self.arrival_time = 0  # Will be set when customer arrives ⏱️
        self.checkout_time = 0  # Will be set when customer completes checkout ⏱️

    def __str__(self):
        """Return a string representation of the customer."""
        return f"Customer #{self.id} ({self.items_count} items)"


class CheckoutLane:
    """Represent a checkout lane in a supermarket."""

    def __init__(self, id, processing_rate):
        """Initialize a checkout lane with ID and processing rate (items per time unit)."""
        self.id = id
        self.processing_rate = processing_rate  # Items processed per time unit ⚡
        self.queue = LinkedQueue()  # Queue of customers waiting in this lane
        self.current_customer = None  # Customer being processed
        self.time_remaining = 0  # Time until current customer is finished ⏱️
        self.customers_processed = 0  # Counter for statistics

    def is_busy(self):
        """Check if the checkout lane is currently processing a customer."""
        return self.current_customer is not None

    def queue_length(self):
        """Return the number of customers waiting in this lane."""
        return self.queue.size()

    def total_items_waiting(self):
        """Return the total number of items from all customers in the queue."""
        total = 0

        # Create a temporary queue to count items
        temp_queue = LinkedQueue()

        # Move all customers to temp queue while counting
        while not self.queue.is_empty():
            customer = self.queue.dequeue()
            total += customer.items_count
            temp_queue.enqueue(customer)

        # Move them back to original queue
        while not temp_queue.is_empty():
            self.queue.enqueue(temp_queue.dequeue())

        return total

    def add_customer(self, customer):
        """Add a customer to this checkout lane."""
        self.queue.enqueue(customer)
        return True

    def start_next_customer(self, current_time):
        """Start processing the next customer in the queue."""
        if self.queue.is_empty():
            return False

        # Get next customer from queue
        self.current_customer = self.queue.dequeue()

        # Calculate time to process this customer's items
        self.time_remaining = self.current_customer.items_count / self.processing_rate

        print(
            f"Lane #{self.id}: Started checkout for {self.current_customer} ⏳")
        return True

    def process_time_unit(self, current_time):
        """Process one time unit for this checkout lane."""
        if not self.is_busy():
            return False

        # Reduce remaining time
        self.time_remaining -= 1

        # Check if customer checkout is complete
        if self.time_remaining <= 0:
            # Record checkout completion time
            self.current_customer.checkout_time = current_time

            wait_time = self.current_customer.checkout_time - \
                self.current_customer.arrival_time
            print(
                f"Lane #{self.id}: Completed checkout for {self.current_customer} (waited {wait_time} time units) ✅")

            self.customers_processed += 1
            self.current_customer = None
            return True  # A customer finished checkout

        return False  # Customer still being processed


class Supermarket:
    """Simulate a supermarket with multiple checkout lanes."""

    def __init__(self):
        """Initialize the supermarket with checkout lanes."""
        # Create checkout lanes with different processing rates
        self.lanes = [
            CheckoutLane(1, 5),  # 5 items per time unit
            CheckoutLane(2, 3),  # 3 items per time unit
            CheckoutLane(3, 7)   # 7 items per time unit (express lane) ⚡
        ]

        self.current_time = 0
        self.customers_processed = 0
        self.total_wait_time = 0

    def select_best_lane(self, customer):
        """Select the best checkout lane for a customer."""
        best_lane = None
        min_wait_time = float('inf')

        for lane in self.lanes:
            # Estimate wait time by considering both current customer and queue
            estimated_wait = 0

            # Consider current processing customer
            if lane.is_busy():
                estimated_wait += lane.time_remaining

            # Consider total items in queue
            estimated_wait += lane.total_items_waiting() / lane.processing_rate

            # Select lane with minimum estimated wait time
            if estimated_wait < min_wait_time:
                min_wait_time = estimated_wait
                best_lane = lane

        return best_lane

    def add_customer(self, customer):
        """Add a customer to the best checkout lane."""
        # Set customer arrival time ⏱️
        customer.arrival_time = self.current_time

        # Find the best lane
        best_lane = self.select_best_lane(customer)

        # Add customer to the lane
        best_lane.add_customer(customer)
        print(f"Customer #{customer.id} joined Lane #{best_lane.id} (estimated wait: {customer.items_count / best_lane.processing_rate:.1f} time units) 🛒")

        return best_lane.id

    def simulate_time_unit(self):
        """Simulate one time unit for the supermarket."""
        self.current_time += 1

        # Process each checkout lane
        for lane in self.lanes:
            # If lane is not busy, start next customer
            if not lane.is_busy():
                lane.start_next_customer(self.current_time)

            # Process time unit for this lane
            customer_finished = lane.process_time_unit(self.current_time)

            # Update statistics if a customer finished
            if customer_finished:
                self.customers_processed += 1

        # Print status every 5 time units
        if self.current_time % 5 == 0:
            self.print_status()

    def print_status(self):
        """Print the current status of all checkout lanes."""
        print(f"\nTime: {self.current_time} ⏱️")
        for lane in self.lanes:
            if lane.is_busy():
                print(
                    f"Lane #{lane.id}: Processing {lane.current_customer}, {lane.queue_length()} waiting")
            else:
                print(f"Lane #{lane.id}: Idle, {lane.queue_length()} waiting")

    def all_lanes_empty(self):
        """Check if all checkout lanes are empty (no customers being processed or waiting)."""
        for lane in self.lanes:
            if lane.is_busy() or not lane.queue.is_empty():
                return False
        return True

    def get_statistics(self):
        """Calculate and return supermarket statistics."""
        total_processed = sum(lane.customers_processed for lane in self.lanes)

        # Calculate total wait time and average
        total_wait_time = 0
        processed_count = 0

        # We don't have the actual customers, this would need to be tracked differently
        # in a real implementation, but here we'll just return the processed count

        return {
            'total_time': self.current_time,
            'customers_processed': total_processed,
            'lanes_statistics': [
                {'lane_id': lane.id, 'customers_processed': lane.customers_processed}
                for lane in self.lanes
            ]
        }




def test_case_1():
    print("EXAMPLE 1")
    supermarket = Supermarket()
    customers = [
        Customer(1, 10),
        Customer(2, 10),
        Customer(3, 10)
    ]
    for customer in customers:
        supermarket.add_customer(customer)

    while not supermarket.all_lanes_empty():
        supermarket.simulate_time_unit()

    stats = supermarket.get_statistics()
    print(f"\nTotal time: {stats['total_time']} time units ⏱️")
    print(f"Total customers processed: {stats['customers_processed']} 👥")


def test_case_2():
    print("EXAMPLE 2")
    supermarket = Supermarket()
    customers = [
        Customer(1, 5),
        Customer(2, 20),
        Customer(3, 15)
    ]
    for customer in customers:
        supermarket.add_customer(customer)

    while not supermarket.all_lanes_empty():
        supermarket.simulate_time_unit()

    stats = supermarket.get_statistics()
    print(f"\nTotal time: {stats['total_time']} time units ⏱️")
    print(f"Total customers processed: {stats['customers_processed']} 👥")

def test_case_3():
    print("EXAMPLE 3")
    import random;
    supermarket = Supermarket()
    customers = [Customer(i, random.randint(1, 30)) for i in range(1, 6)] 

    print("Starting supermarket checkout simulation... 🛒")

    for customer in customers:
        supermarket.add_customer(customer)

    time_limit = 50
    for t in range(1, time_limit + 1):
        supermarket.simulate_time_unit()
        if supermarket.all_lanes_empty():
            print(f"\nAll customers processed at time {t}! 🎉")
            break

    stats = supermarket.get_statistics()
    print(f"\nTotal time: {stats['total_time']} time units ⏱️")
    print(f"Total customers processed: {stats['customers_processed']} 👥")


test_case_1()
test_case_2()
test_case_3()

