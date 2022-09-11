# Task from https://exercism.org/tracks/python/exercises/currency-exchange

def exchange_money(budget, exchange_rate):
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    actual_exchange_rate = exchange_rate * (1 + spread / 100)
    exchange_value = exchange_money(budget, actual_exchange_rate)
    number_of_bills = get_number_of_bills(exchange_value, denomination)
    return get_value_of_bills(denomination, number_of_bills)


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    exchange_value = budget // (exchange_rate * (1 + spread / 100))
    return exchange_value - exchangeable_value(budget, exchange_rate, spread, denomination)
