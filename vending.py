# Tasks
# Calculate the change first before giving them.


class Coin:
	def __init__(self, value, quantity):
		self.value = value
		self.quantity = quantity

	def isAvailable(self):
		return self.quantity > 0


class VendingMachine:
	def __init__(self, coins):
		self.coins = coins

	def transaction(self):
		self.payment = float(input("Payment amount: "))
		self.inserted = float(input("Inserted amount: "))
		self.change = round(self.inserted - self.payment, 2)
		self.giveChange()

	def giveChange(self):
		pos = 0
		while self.change > 0:
			if self.coins[pos].value > self.change or self.coins[pos].quantity == 0:
				if pos < len(self.coins) - 1:
					pos += 1
				else:
					print("Sorry, no more change")
					break
				continue

			print("Give ", self.coins[pos].value)
			self.change = round(self.change - self.coins[pos].value, 2)
			self.coins[pos].quantity -= 1



coins = []
coins.append(Coin(2, 20))
coins.append(Coin(1, 20))
coins.append(Coin(0.5, 20))
coins.append(Coin(0.2, 20))
coins.append(Coin(0.1, 20))
coins.append(Coin(0.05, 20))

vm = VendingMachine(coins)

answer = 'y'

while answer == 'y':
	vm.transaction()
	answer = input("Continue? ")

