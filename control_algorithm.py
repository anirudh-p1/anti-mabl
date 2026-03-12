class AdaptiveResistanceController:
    def __init__(self, base_resistance, fatigue_threshold, form_quality_threshold, safety_constraints):
        self.base_resistance = base_resistance
        self.fatigue_threshold = fatigue_threshold
        self.form_quality_threshold = form_quality_threshold
        self.safety_constraints = safety_constraints

    def adjust_brake_current(self, current_fatigue, current_form_quality):
        if current_fatigue > self.fatigue_threshold:
            adjustment_factor = (self.fatigue_threshold / current_fatigue)
            new_resistance = self.base_resistance * adjustment_factor
        elif current_form_quality < self.form_quality_threshold:
            adjustment_factor = (self.form_quality_threshold / current_form_quality)
            new_resistance = self.base_resistance * adjustment_factor
        else:
            new_resistance = self.base_resistance  # Maintain base resistance if conditions are good

        if self.is_within_safety_constraints(new_resistance):
            return new_resistance
        else:
            raise ValueError("Adjusted resistance exceeds safety constraints.")

    def is_within_safety_constraints(self, resistance):
        return resistance <= self.safety_constraints['max_resistance'] and resistance >= self.safety_constraints['min_resistance']