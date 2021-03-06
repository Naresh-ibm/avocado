#!/usr/bin/env python

import os

from avocado import Test
from avocado import main


class GenDataTest(Test):

    """
    Simple test that generates data to be persisted after the test is run
    """

    def test_json(self):
        import json
        output_path = os.path.join(self.outputdir, "test.json")
        output = {"basedir": self.basedir,
                  "outputdir": self.outputdir}
        with open(output_path, "w") as output_file:
            json.dump(output, output_file)


if __name__ == "__main__":
    main()
