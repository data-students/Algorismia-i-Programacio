import sys
from dataclasses import dataclass

@dataclass
class CreditCard:
    number: str
    transactions: list[tuple[str, float]] # day, amount
    
    def is_candidate(self) -> bool:

        # Minim 3 transaccions
        if len(self.transactions) < 3:
            return False
        
        # Més tard del 2024/03
        last_transacion_date = self.transactions[-1][0]
        if last_transacion_date[:6] < "202403":
            return False

        # Suma total de 200€ o més
        total_sum = 0.0
        for transaction in self.transactions:
            total_sum += transaction[1]
        if total_sum < 200:
            return False
        
        return True

def read_credit_cards() -> dict[str, CreditCard]:

    credit_cards: dict[str, CreditCard] = {}

    for line in sys.stdin:
        line = line.split()
        date = str(line[0])
        number = str(line[1])
        ammount = float(line[2])
        if not line[1] in credit_cards:
            credit_cards[number] = CreditCard(number, [(date, ammount)])
        else:
            credit_cards[number].transactions.append((date, ammount))
    
    return credit_cards

def main() -> None:

    credit_cards = read_credit_cards()

    candidates = [card for card in credit_cards.values() if card.is_candidate()]

    for candidate in sorted(candidates, key= lambda x: x.number):
        print(candidate.number)

if __name__ == "__main__":
    main()
