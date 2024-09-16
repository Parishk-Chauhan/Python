
# Python has the following data types built-in by default, in these categories:

# Text Type:	        str
# Numeric Types:	    int, float, complex
# Sequence Types:   	list, tuple, range
# Mapping Type:	        dict
# Set Types:	        set, frozenset
# Boolean Type:	        bool
# Binary Types:     	bytes, bytearray, memoryview
# None Type:	        NoneType

# text : 
x = "Hello"                                                   # str : Represents sequences of characters (e.g., words, sentences).

# Number : 
y = 5                                                         # int : Represents whole numbers (e.g., 1, 42, -7).

z = 5.2                                                       # float : Represents numbers with decimal points (e.g., 3.14, -0.001).

a = 4j                                                        # complex : Represents complex numbers with real and imaginary parts (e.g., 3 + 2j).

# sequence types : 
b = ["hello", "i", "am", "Paishk"]                            # list : An ordered, mutable collection of elements (e.g., [1, 2, 3]).

c = ("hello", "i", "am", "Paishk")                            # tuple : An ordered, immutable collection of elements (e.g., (1, 2, 3)).

d = range(6)                                                  # range : Represents a sequence of numbers, often used in loops (e.g., range(0, 10)).

# mapping :
e = {"name" : "John", "age" : 36}                             # dict : A collection of key-value pairs (e.g., {"name": "Alice", "age": 25}).

# set : 
f = {"apple", "banana", "cherry"}                             # set : An unordered collection of unique elements (e.g., {1, 2, 3}).

g = frozenset({"apple", "banana", "cherry"})                  # frozenset : An immutable version of a set (e.g., frozenset({1, 2, 3})).

# boolean : 
h = True                                                      # bool : Represents True or False values.

# binary type : 
i = b"Hello"                                                  #bytes : Immutable sequence of bytes (e.g., b'hello').

j = bytearray(5)                                              # bytearray : Mutable sequence of bytes (e.g., bytearray(b'hello')).

k = memoryview(bytes(5))                                      # memoryview : Provides a view into the memory of another binary object.

# none type : 
l = None                                                      #none type : Represents the absence of a value (None).