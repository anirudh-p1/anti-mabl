class BaselineProfileManager:
    def __init__(self):
        self.bone_metrics = {}
        self.training_baselines = {}
        self.session_log = []

    def add_bone_metrics(self, user_id, metrics):
        self.bone_metrics[user_id] = metrics

    def add_training_baseline(self, user_id, baseline):
        self.training_baselines[user_id] = baseline

    def log_session(self, user_id, session_data):
        self.session_log.append({'user_id': user_id, 'session_data': session_data})

    def get_bone_metrics(self, user_id):
        return self.bone_metrics.get(user_id, 'No metrics found')

    def get_training_baseline(self, user_id):
        return self.training_baselines.get(user_id, 'No baseline found')

    def get_session_log(self, user_id):
        return [session for session in self.session_log if session['user_id'] == user_id]

# Example Usage
# profile_manager = BaselineProfileManager()
# profile_manager.add_bone_metrics('user1', {'metric': 10})
# profile_manager.add_training_baseline('user1', {'baseline': 5})
# profile_manager.log_session('user1', {'duration': 30, 'type': 'strength training'})
# print(profile_manager.get_bone_metrics('user1'))
# print(profile_manager.get_training_baseline('user1'))
# print(profile_manager.get_session_log('user1'))