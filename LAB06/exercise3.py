import random
import time

class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            return False  # Se descarta el auto si el carril está lleno
        self.queue[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None
        item = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item

    def current_size(self):
        return self.size

class TrafficSimulation:
    def __init__(self, capacity=10, cycle_time=5):
        #creacion de carriles 
        self.lane_ns = CircularQueue(capacity)
        self.lane_ew = CircularQueue(capacity)
        
        self.cycle_time = cycle_time
        self.time = 0
        self.wait_times = []
        self.max_queue_lengths = {"NS": 0, "EW": 0}

    def simulate_step(self):
        # Llegada aleatoria de autos
        if random.random() < 0.7:
            self.lane_ns.enqueue({"time": self.time})
        if random.random() < 0.6:
            self.lane_ew.enqueue({"time": self.time})

        # Semáforo en verde para una dirección a la vez
        if (self.time // self.cycle_time) % 2 == 0:
            vehicle = self.lane_ns.dequeue()
            if vehicle:
                self.wait_times.append(self.time - vehicle["time"])
        else:
            vehicle = self.lane_ew.dequeue()
            if vehicle:
                self.wait_times.append(self.time - vehicle["time"])

        # Actualizamos métricas
        self.max_queue_lengths["NS"] = max(self.max_queue_lengths["NS"], self.lane_ns.current_size())
        self.max_queue_lengths["EW"] = max(self.max_queue_lengths["EW"], self.lane_ew.current_size())
        self.time += 1

    def run_simulation(self, duration=30):
        for _ in range(duration):
            self.simulate_step()

        avg_wait = sum(self.wait_times) / len(self.wait_times) if self.wait_times else 0
        return {
            "average_wait_time": avg_wait,
            "max_queue_lengths": self.max_queue_lengths,
            "total_vehicles": len(self.wait_times)
        }

    
def test_traffic_simulation():
    print("Running basic traffic simulation test...\n")
    
    sim1 = TrafficSimulation(capacity=10, cycle_time=5)
    result1 = sim1.run_simulation(duration=60)
    print("Test 1 - 60 seconds")
    print(result1)
    print()

    sim2 = TrafficSimulation(capacity=15, cycle_time=4)
    result2 = sim2.run_simulation(duration=100)
    print("Test 2 - 100 seconds, bigger capacity and shorter cycles")
    print(result2)
    print()

    sim3 = TrafficSimulation(capacity=5, cycle_time=6)
    result3 = sim3.run_simulation(duration=30)
    print("Test 3 - 30 seconds, small buffer and longer cycles")
    print(result3)
    print()

    print("Tests completed.")

test_traffic_simulation()
