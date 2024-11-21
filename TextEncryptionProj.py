#Programmer: Alexander Henriquez
#Purpose of this program is to do basic text encryption
#Data: 11/18/2024


import random

from numpy.lib.user_array import container

while True:

# Get user input
    userinput = input("Type anything: ")

    # Shuffle the list of characters
    char_list = list(userinput)

    # Convert the input into a list of characters
    random.shuffle(char_list)

    # Join the shuffled list back into a string
    scrambled_output = ''.join(char_list)

    if userinput:
        key = random.randint(-10000000000000000000000000000*10000000000000000000000000000,
                         10000000000000000000000000000 * 10000000000000000000000000000)
    print(key)
    print()
    print("Scrambled Output:", scrambled_output, "non scrambled input:", userinput)
    userinput


    again = input("Do you want to go again 1 = yes, 0 = no")



    if again == "1" :
        continue

    else:
        print("End")
        break


class Transaction:
    def __init__(self, platform, stock, price, action, date):
        self.platform = platform
        self.stock = stock
        self.price = price
        self.action = action
        self.date = date


class Portfolio:
    def __init__(self, name):
        self.name = name
        self.stocks = {}
        self.value = 0
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        if transaction.action == "Buy":
            self.stocks[transaction.stock] = self.stocks.get(transaction.stock, 0) + 1
            self.value += transaction.price
        elif transaction.action == "Sell":
            self.stocks[transaction.stock] = self.stocks.get(transaction.stock, 0) - 1
            self.value -= transaction.price

    def edit_transaction(self, index, transaction):
        old_transaction = self.transactions[index]
        if old_transaction.action == "Buy":
            self.stocks[old_transaction.stock] -= 1
            self.value -= old_transaction.price
        elif old_transaction.action == "Sell":
            self.stocks[old_transaction.stock] += 1
            self.value += old_transaction.price
        self.transactions[index] = transaction
        if transaction.action == "Buy":
            self.stocks[transaction.stock] += 1
            self.value += transaction.price
        elif transaction.action == "Sell":
            self.stocks[transaction.stock] -= 1
            self.value -= transaction.price

    def delete_transaction(self, index, old_transaction=None):
        transaction = self.transactions[index]
        if transaction.action == "Buy":
            self.stocks[transaction.stock] -= 1
            self.value -= transaction.price
        elif transaction.action == "Sell":
            self.stocks[transaction.stock] += 1
            self.value += old_transaction.price
        del self.transactions[index]

    def plot_allocation(self):
        labels = list(self.stocks.keys())
        sizes = list(self.stocks.values())
        plt.pie(sizes, labels=labels, autopct="%1.1f%%")
        plt.title(f"Allocation of {self.name}")
        plt.show()

    def plot_performance(self, index):
        dates = [t.date for t in self.transactions]
        start_date = min(dates)
        end_date = max(dates)
        symbols = list(self.stocks.keys())
        data = yf.download(symbols + [index], start=start_date, end=end_date)
        prices = data["Adj Close"]
        weights = np.array(list(self.stocks.values())) / sum(self.stocks.values())
        portfolio_returns = (prices[symbols] * weights).sum(axis=1)
        index_returns = prices[index]
        plt.plot(portfolio_returns, label="Portfolio")
        plt.plot(index_returns, label=index)
        plt.title(f"Performance of {self.name} vs {index}")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.show()

    def save_data(self, filename):
        df = pd.DataFrame([vars(t) for t in self.transactions])
        df.to_csv(filename)

    def load_data(self, filename):
        df = pd.read_csv(filename)
        for _, row in df.iterrows():
            transaction = Transaction(row["platform"], row["stock"], row["price"], row["action"], row["date"])
            self.add_transaction(transaction)


## need a way to see how the text was changed and track it




## maybe make an if statment that compares input vs scambled text aand that
## can be the bases for the decrypter


##w\whatif I make a program. It assigns where something should be encrypted or not. Then a key is generated that con
## I basically need to find out how to reverse back the text. And use a passcode to do that

## so key plus