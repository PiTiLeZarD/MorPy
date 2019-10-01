#!/usr/bin/env python3

from coder import play_string
import sys
from codes.sanitizer import sanitize
from codes.intl import code

string = " ".join(sys.argv[1:])

play_string(sanitize(string, code), code)