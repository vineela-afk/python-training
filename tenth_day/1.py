class Player:
    def __init__(self, name, is_impostor):
        self.name = name
        self.is_impostor = is_impostor
        self.tasks = []
        self.is_alive = True

    def complete_task(self, task):
        if not self.is_impostor and task in self.tasks:
            self.tasks.remove(task)
            print(f"{self.name} completed task: {task.name}")
        else:
            print(f"{self.name} cannot complete this task.")

    def sabotage(self, system):
        if self.is_impostor:
            system.sabotage()
            print(f"{self.name} sabotaged {system.name}")

    def is_suspected(self):
        # Implement logic to determine if the player is suspected
        pass

class Task:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Spaceship:
    def __init__(self, systems):
        self.systems = systems

    def sabotage_system(self, system):
        system.sabotage()
        print(f"System {system.name} sabotaged!")

class System:
    def __init__(self, name):
        self.name = name
        self.is_sabotaged = False

    def sabotage(self):
        self.is_sabotaged = True
        print(f"System {self.name} has been sabotaged!")

# Create players
player1 = Player("Player1", False)
player2 = Player("Player2", True)

# Create tasks
task1 = Task("Fix Wiring", "Electrical")
task2 = Task("Prime Shields", "Security")

# Assign tasks to crewmate player
player1.tasks = [task1, task2]

# Create spaceship systems
system1 = System("Reactor")
system2 = System("Oxygen")

# Create a spaceship
spaceship = Spaceship([system1, system2])

# Simulate interactions
player1.complete_task(task1)
player2.sabotage(system1)
spaceship.sabotage_system(system2)
