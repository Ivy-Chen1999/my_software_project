## Week 3

- Users can now register, log in, log out, and view the current user through a simple text interface.  
- Initial environment and folder structure have been set up.  
- Add entity classes: User, Task, PomodoroSession, and Statistics for model used.  
- Add UserRepository to handle user data storage in database.  
- Add UserService for managing user-related logic.  
- Wrote unit tests for UserService with 98% coverage.  
- Implemented a text based interface for testing user features.

## Week 4

- Users can now see the list of tasks, create tasks, mark them as done, and delete them.
- Added TaskRepository to handle task-related database operations.
- Added TaskService to manage task logic including creation, completion, deletion.
- Settled SQLite database and build up, all features now operates on the database.
- Polished code according to Pylint
- Improved text based interfaced for better testing.
- Add unit tests for UserRepo.

  ## Week 5

- Users can now add pomodoro sessions related to specific task.
- Added PomodoroRepository to handle time-related database operations.
- Added PomodoroService to manage time log including starting time and end time.
- Added pomodoro table to SQLite database.
- Changed the entities to dataclass and polished code according to Pylint.
- Improved text based interfaced that enables time log functions.
- Add unit tests for Pomodoroservice.
