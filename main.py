import random
import sys

from app import CafeApp
from logic import Cafe


def main():
    app = CafeApp(Cafe(random.choice), print)
    app.buy(sys.argv[1], float(sys.argv[2]))


if __name__ == "__main__":
    main()
