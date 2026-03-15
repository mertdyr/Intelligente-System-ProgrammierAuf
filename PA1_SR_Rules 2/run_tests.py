#!/usr/bin/env python3

from is_sr.Tests import runTests
from is_sr.Levels import levels

from WallFollowAgent import WallFollowAgent

runTests(levels, WallFollowAgent)
