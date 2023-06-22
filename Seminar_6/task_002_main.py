import sys
from package import guess_f

init_numbers = list(map(int, [i for i in sys.argv][1:]))
guess_f(*init_numbers)

