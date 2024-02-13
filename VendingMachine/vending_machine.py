class VendingMachine:
    def __init__(self):
        self.beverages = []
        self.cards = []
        self.columns = []

    def addBeverage(self, beverage):
        self.beverages.append(beverage)

    def rechargeCard(self, card_id, credit):
        card_exists = False
        for card in self.cards:
            if card['id'] == card_id:
                card['credit'] += credit
                card_exists = True
                break

        if not card_exists:
            self.cards.append({'id': card_id, 'credit': credit})

    def getCredit(self, card_id):
        for card in self.cards:
            if card['id'] == card_id:
                return card['credit']
        return -1.0

    def refillColumn(self, column_number, beverage_name, quantity):
        self.columns.append({'number': column_number, 'beverage': beverage_name, 'quantity': quantity})

    def availableCans(self, beverage_name):
        total_quantity = 0
        for column in self.columns:
            if column['beverage'] == beverage_name:
                total_quantity += column['quantity']
        return total_quantity

    def sell(self, beverage_name, card_id):
        for column in self.columns:
            if column['beverage'] == beverage_name and column['quantity'] > 0:
                for card in self.cards:
                    if card['id'] == card_id and card['credit'] >= self.getBeveragePrice(beverage_name):
                        card['credit'] -= self.getBeveragePrice(beverage_name)
                        column['quantity'] -= 1
                        return column['number']
        return -1.0

    def getBeveragePrice(self, beverage_name):
        for beverage in self.beverages:
            if beverage.name == beverage_name:
                return beverage.price
        return -1.0