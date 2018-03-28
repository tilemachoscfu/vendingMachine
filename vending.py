class VendingMachine:

	def __init__(self, coins):
		self.coins = coins

	def give_change(self, payment, inserted):
		self.change = round(inserted - payment,2)
		self.pos = 0

		while self.change > 0:
			if not self.valid_coin_value():
				break
			self.give_coin()

	def give_coin(self):
		print("coin", self.current_coin())
		self.change -= self.current_coin()
		self.decrease_quantity()

	def decrease_quantity(self):
		self.coins[self.pos][1] -= 1

	def valid_coin_value(self):
		while self.change < self.current_coin() or self.current_coin_quantity() == 0:
			if self.last_coin():
				print("Unable to give amount")
				return False
			self.pos += 1
		return True

	def current_coin(self):
		return self.coins[self.pos][0]

	def current_coin_quantity(self):
		return self.coins[self.pos][1]


	def last_coin(self):
		return self.pos == len(self.coins)-1
if __name__ == "__main__":
	coins = [
				[2,20], [1,20], [0.5,40],
				[0.2,40], [0.1,40], [0.05,40]
			]

	vm = VendingMachine(coins)
	answer = 'y'
	while answer == 'y':
		payment = float(input("Payment: "))
		inserted = float(input("Value inserted: "))

		vm.give_change(payment, inserted)

		answer = input("Continue? ")