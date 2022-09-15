import logging

logging.basicConfig(level=logging.INFO)


class Calculator:
    def __init__(self, a=0.0, b=0.0):
        self.a = a
        self.b = b

    def add(self):
        try:
            return float(self.a + self.b)
        except ValueError:
            logging.error("Attributes are of the bad type - can take numeric values only")

    def substitute(self):
        try:
            return abs(self.a - self.b)
        except TypeError:
            logging.error("Attributes are of the bad type - cannot perform substitution")

    def multiply(self):
        try:
            return self.a * self.b
        except TypeError:
            logging.error("Attributes are of the bad type - cannot multiply")

    def divide(self):
        try:
            return self.a / self.b
        except ZeroDivisionError:
            logging.error("Cannot divide by 0, second attribute cannot be 0")
        except TypeError:
            logging.error("Attributes are of the bad type - cannot divide a by b")


def main():
    # for add()
    logging.info(Calculator(6, 3).add())
    logging.info(Calculator(6.4, 3.33).add())
    logging.info(Calculator("45", "54").add())
    # for substitute()
    logging.info(Calculator().substitute())
    logging.info(Calculator(6.4, 3.33).substitute())
    logging.info(Calculator("45", "54").substitute())
    # for multiply()
    logging.info(Calculator(2).multiply())
    # for divide()
    logging.info(Calculator().divide())
    logging.info(Calculator(6, 3.1).divide())
    logging.info(Calculator("8", "2").divide())


if __name__ == "__main__":
    main()
