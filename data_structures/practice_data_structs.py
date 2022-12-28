import array
import collections
import logging
import sys
from types import MappingProxyType

logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def use_dict():
    logging.info("\nUsing dict")
    d1 = {"one": 1, "two": 2, "three": 3}
    logging.info(d1)
    logging.info(d1["one"])


def use_ordered_dict():
    logging.info("\nUsing ordered dict")
    # remembers the insertion order of keys
    d2 = collections.OrderedDict(one=1, two=2, three=3)
    logging.info(d2)


def use_default_dict():
    logging.info("\nUsing default dict")
    # returns the default values for missing keys
    d3 = collections.defaultdict(list)
    d3["cities"].append("Warsaw")
    d3["cities"].append("Lviv")
    d3["countries"].append("Ukraine")
    logging.info(d3)
    logging.info(d3["cities"])
    logging.info(d3["continents"])


def use_chain_map():
    logging.info("\nUsing chain map")
    # used to search multiple dictionaries as a single mapping
    dict1 = {"one": 1, "two": 2}
    dict2 = {"three": 3, "four": 4, "five": 5}
    chain = collections.ChainMap(dict1, dict2)
    logging.info(chain)
    logging.info(chain["one"])
    logging.info(chain["five"])


def use_mapping_proxy_type():
    logging.info("\nUsing proxy type")
    # used to make a read-only dictionary
    writable_dict = {"three": 3, "four": 4, "five": 5}
    read_only = MappingProxyType(writable_dict)
    logging.info(read_only)
    logging.info("Trying to change one value in read-only dict: ")
    try:
        read_only["five"] = 55
    except TypeError as e:
        logging.error(e)


def use_array():
    logging.info("\nUsing simple array/list")
    arr = [1, 2, 3, 4, 5]
    logging.info(arr)
    logging.info(arr[0])
    arr.append(7)
    logging.info("New element appended, updated array: " + str(arr))


def use_tuple():
    logging.info("\nUsing immutable tuple")
    my_tuple = (1, 2, 3, 4, 5)
    logging.info(my_tuple)
    logging.info(my_tuple[0])
    # my_tuple[0] = 0


def use_named_tuple():
    logging.info("\nUsing immutable named tuple")
    # tuple object with names for each position which the ordinary tuples lack
    cities = collections.namedtuple("Cities", ["name", "country"])
    c = cities("Lviv", "Ukraine")
    logging.info(cities)
    logging.info(c[0])
    logging.info(c.country)


def use_array_array():
    logging.info("\nUsing basic typed array")
    # basic typed array - constrained to a single data type
    # type code can be only must be one of those: b, B, u, h, H, i, I, l, L, q, Q, f or d.
    arr = array.array("d", (1, 2, 3, 4, 5))
    logging.info(arr)
    logging.info(arr[0])
    logging.info(arr[1])
    logging.info(arr.append(7))


def use_str():
    logging.info("\nUsing str")
    # immutable
    my_str = "abc"
    logging.info(my_str[1])


def use_bytes():
    logging.info("\nUsing bytes")
    # immutable, for integers between 0 and 255
    arr = bytes((0, 1, 2, 3))
    logging.info(arr)
    logging.info(arr[1])


def use_bytearray():
    logging.info("\nUsing bytearray")
    # mutable, for integers between 0 and 255
    arr = bytearray((0, 1, 2, 3))
    logging.info(arr)
    logging.info(arr[1])
    arr.append(5)
    logging.info(arr)


def use_deque():
    logging.info("\nUsing deque")
    # doubly ended queue - optimized list
    deque = collections.deque([1, 2, 3])
    logging.info(deque)
    deque.append(7)
    logging.info(deque)
    deque.appendleft(4)
    logging.info(deque)
    deque.pop()
    logging.info(deque)
    deque.popleft()
    logging.info(deque)


def use_different_dict_structs():
    logging.info("Different dictionary structures:")
    use_dict()
    use_ordered_dict()
    use_default_dict()
    use_chain_map()
    use_mapping_proxy_type()
    logging.info("\n\n\n")


def use_different_array_structs():
    logging.info("Different array structures:")
    use_array()
    use_tuple()
    use_named_tuple()
    use_array_array()
    use_str()
    use_bytes()
    use_bytearray()
    use_deque()
    logging.info("\n\n\n")


if __name__ == '__main__':
    use_different_dict_structs()
    use_different_array_structs()
