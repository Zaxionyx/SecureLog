# SecureLog: A Structured Logging System in Python

A secure and organized logging utility designed to handle, categorize, and analyze log entries for Python applications.

## Project Description

SecureLog provides a clean, class-based structure for managing application logs. It allows for segregating logs into different categories (e.g., "error", "info", "access"), adding security by managing authorized users, and includes functions for searching, analyzing, and maintaining log data.

This project is built using core Python data structures:
* **Dictionaries** for the main log structure.
* **Lists** for storing entries within each category.
* **Tuples** for immutable, timestamped log entries.
* **Sets** for fast and unique management of authorized users.

## Features

### 🧱 Core Structure
* **`init_secure_log()`**: Initializes the main log structure as a dictionary where keys are log categories (like “error”, “info”, “access”), and values are lists of log entries.

### 📜 Logging Functions
* **`add_log_entry(category, message, level)`**: Adds a new log entry as a tuple (timestamp, message, level) to the corresponding list in the dictionary.
* **`get_logs_by_category(category)`**: Returns the list of log entries for a given category.
* **`get_recent_logs(limit)`**: Retrieves the latest `n` log entries from all categories combined.

### 🔒 Security & Uniqueness
* **`register_authorized_user(user_id)`**: Adds a user’s ID to a set of authorized users.
* **`check_user_access(user_id)`**: Checks if a user is in the authorized users set before allowing access to logs.
* **`remove_user_access(user_id)`**: Removes a user from the authorized users set.

### 🔍 Search & Analysis
* **`find_logs_by_keyword(keyword)`**: Scans through all log messages and returns a list of tuples (category, timestamp, message) matching the keyword.
* **`get_unique_log_levels()`**: Returns a set of all distinct log levels found in the logs (like INFO, WARNING, ERROR).
* **`summarize_log_counts()`**: Returns a dictionary mapping each category to the number of log entries it contains.

### 🧹 Maintenance & Utility
* **`clear_logs(category=None)`**: Clears logs for a specific category or all categories if none specified.
* **`export_logs_to_file(filename)`**: Prepares log data for export (as a list of tuples) for backup.

## Current Progress

This project is in its initial development phase. The core `Logging_Functions` class has been created, and the `add_log_entry` function is implemented and functional, allowing for new log entries to be added.
