from abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def __init__(self):
        super().__init__()

    def compute_damage(self):
        return self.power
