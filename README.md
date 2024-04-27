# In-Memory Key-Value Database with Transaction Support

## Instructions

To run the code, simply copy the `InMemoryDB` class into a Python file (e.g., `inmemory_db.py`) and import it into your Python script or interpreter.

Example usage:

```python
from inmemory_db import InMemoryDB

db = InMemoryDB()
# ... (use the methods as per the examples provided)
```

No additional setup is required.

## Potential Improvements

This assignment could be improved in the following ways:

1. **Clarify the behavior for edge cases**:
   - What should happen if a transaction is started, and another transaction is attempted to be started before committing or rolling back the first one?
   - What should happen if a non-existent key is passed to `put` during a transaction?
   - How should the implementation handle non-string keys or non-integer values?

2. **Add more test cases**: The current examples cover the basic functionality, but more comprehensive test cases could be provided to ensure the robustness of the implementation.

3. **Implement a persistent storage option**: The current implementation is an in-memory database, which means all data is lost when the program terminates. An extension could be to add an option for persistent storage, such as writing the data to a file or connecting to a real database.

4. **Introduce concurrency handling**: In a real-world scenario, multiple transactions might be happening concurrently. The assignment could be extended to handle concurrent transactions, introducing concepts like locking and isolation levels.

5. **Grading with automated tests**: Instead of manually grading the submissions, an automated testing framework could be set up to run a suite of tests against the submitted code and provide immediate feedback to the students.
