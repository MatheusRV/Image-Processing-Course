#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse


def main(args):
    """ Main entry point of the app """
    print("hello world")
    print(args)


if __name__ == "__main__":
    """ This is executed when run from the command line """
    parser = argparse.ArgumentParser()

    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")

    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)

    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")

    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbosity (-v, -vv, etc)")

    # Specify output of "--version"
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s (version {version})".format(version=__version__))

    args = parser.parse_args()
    main(args)

python aritm.py noisy_fingerprint.tif noisy_fingerprint_ARITM.tif
python logic.py noisy_fingerprint.tif noisy_fingerprint_LOGIC.tif
python neg.py noisy_fingerprint.tif noisy_fingerprint_NEG.tif
python gama.py noisy_fingerprint.tif noisy_fingerprint_GAMA.tif 0.5
python cont.py noisy_fingerprint.tif noisy_fingerprint_CONT.tif
python hist.py noisy_fingerprint.tif
python eq.py noisy_fingerprint.tif noisy_fingerprint_EQ.tif
python media.py noisy_fingerprint.tif noisy_fingerprint_MEDIA.tif 5
python gauss.py noisy_fingerprint.tif noisy_fingerprint_GAUSS.tif 15
python med.py noisy_fingerprint.tif noisy_fingerprint_MED.tif 5
python maxmin.py noisy_fingerprint.tif noisy_fingerprint_MIN.tif noisy_fingerprint_MAX.tif 3
python lap.py noisy_fingerprint.tif noisy_fingerprint_LAP.tif
python nit.py noisy_fingerprint.tif noisy_fingerprint_NIT.tif
python grad.py noisy_fingerprint.tif noisy_fingerprint_GRAD.tif
python bordas_s.py noisy_fingerprint.tif noisy_fingerprint_BORDAS_S.tif 5
python bordas_l.py noisy_fingerprint.tif noisy_fingerprint_BORDAS_L.tif 5
python lim_it.py noisy_fingerprint.tif noisy_fingerprint_LIM_IT.tif <T_ini>
python otsu.py noisy_fingerprint.tif noisy_fingerprint_OTSU.tif
python lim_s.py noisy_fingerprint.tif noisy_fingerprint_LIM_S.tif 5