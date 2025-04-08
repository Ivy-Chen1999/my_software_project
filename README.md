# A time management application ⭐
 
The Time Management application is designed to help users manage their time efficiently by combining a To-Do list with task timing and statistical analysis features. Users can plan, track, and review their tasks to improve productivity. 
This application's functions include: User Authentication, Task Management, Task Status Tracking, Time Tracking, Statistics & Visualization.

## Current Function
- User management
- Task list view, creation, marking, deletion
  
## Documentation  

- [Requirements specification](https://github.com/Ivy-Chen1999/my_software_project/blob/main/documentation/Requirements%20specification.md) 

- [Timesheet ](https://github.com/Ivy-Chen1999/my_software_project/blob/main/documentation/timesheet.md)

- [Changelog](https://github.com/Ivy-Chen1999/my_software_project/blob/main/documentation/changelog.md)

- [Architecture](https://github.com/Ivy-Chen1999/my_software_project/blob/main/documentation/architecture.md)
****
## Testing 

*Basic requirement:  python version >= 3.9*

First initial the database with:

```bash
poetry run invoke build
```

Start the application with:

```bash
poetry run invoke start
```
Run all tests with:

```bash
poetry run invoke test
```
Generate a test coverage report with:
```bash
poetry run invoke coverage-report
```
