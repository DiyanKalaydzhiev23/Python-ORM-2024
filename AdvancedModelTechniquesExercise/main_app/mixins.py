class RechargeEnergyMixin:
    def recharge_energy(self, amount: int) -> None:
        self.energy = min(100, self.energy + amount)
        self.save()
