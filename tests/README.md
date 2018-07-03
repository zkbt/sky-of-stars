If you run `pytest` from the command line, from this package's directory, then it will automatically call every function that starts with `test_` or ends with `_test` in `.py` files stored in this `tests/` directory.

It can be helpful to write small little tests that our code must be able to pass, so that we know we're not breaking any parts of it when we add new features. We can write a test for a new feature that we want to add, and then make sure we pass all our tests by running `pytest` regularly.
