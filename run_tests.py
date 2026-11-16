"""The one command this repository is tested with.

    python run_tests.py

Standard library only, so it runs anywhere Python 3.8+ runs and needs no installation. This is the
command to put in AGENTS.md, because it is the command that actually works here.

Exit code 0 means every test passed; 1 means at least one failed. An agent that cannot read the
output can still read the exit code.
"""
import os, sys, unittest

HERE = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    suite = unittest.defaultTestLoader.discover(os.path.join(HERE, "tests"), top_level_dir=HERE)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print("\n%d tests, %d failures, %d errors" % (result.testsRun, len(result.failures), len(result.errors)))
    sys.exit(0 if result.wasSuccessful() else 1)
