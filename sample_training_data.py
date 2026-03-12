# sample_training_data.py

class SimulatedSession:
    def __init__(self, session_id, initial_fatigue=0):
        self.session_id = session_id
        self.initial_fatigue = initial_fatigue
        self.current_fatigue = initial_fatigue
        self.scenario_data = []

    def generate_scenario(self, duration):
        fatigue_increment = self.calc_fatigue_increment(duration)
        self.current_fatigue += fatigue_increment
        self.scenario_data.append(self.current_fatigue)
        return self.current_fatigue

    def calc_fatigue_increment(self, duration):
        # Assuming a linear model of fatigue progression
        return duration * 0.1  # Example increment value

    def reset_session(self):
        self.current_fatigue = self.initial_fatigue
        self.scenario_data = []

    def get_fatigue_level(self):
        return self.current_fatigue

# Example of usage
if __name__ == '__main__':
    session = SimulatedSession(session_id=1)
    print(f'Initial Fatigue: {session.get_fatigue_level()}')
    session.generate_scenario(duration=30)
    print(f'Fatigue after 30 minutes: {session.get_fatigue_level()}')