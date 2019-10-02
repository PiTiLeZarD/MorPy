#!/usr/bin/env python3

from coder import play_string
import sys
from codes.sanitizer import sanitize
from codes.intl import code

string = " ".join([sanitize(a, code) for a in sys.argv[1:]])

play_string(string, code)