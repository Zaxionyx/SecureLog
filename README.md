# 🔐 SecureLog: A Structured Logging System in Python

A secure and organized logging utility designed to handle, categorize, and analyze log entries for Python applications. SecureLog provides a clean, class-based structure for managing application logs, enabling segregation, security checks, and powerful analysis.

## ⚙️ Project Structure & Technology

This project is built using core Python data structures to ensure efficiency and clarity:

* **Dictionaries (`dict`)**: Used as the primary structure to categorize logs, where keys are log categories.
* **Lists (`list`)**: Used to store individual log entries within each category.
* **Tuples (`tuple`)**: Used for immutable, timestamped log entries `(timestamp, message, level)`.
* **Sets (`set`)**: Used for fast and unique management of authorized user IDs.

---

## ✨ Features

### 🧱 Core Initialization

| Function | Description |
| :--- | :--- |
| **`init_secure_log()`** | Initializes the main log dictionary structure, setting up initial categories (e.g., "error", "info", "access") as lists. |

### 📜 Logging Functions

| Function | Description |
| :--- | :--- |
| **`add_log_entry(category, message, level)`** | Adds a new log entry as a tuple `(timestamp, message, level)` to the corresponding category list. |
| **`get_logs_by_category(category)`** | Retrieves the list of log entries for a specified category. |
| **`get_recent_logs(limit)`** | Retrieves the latest `n` log entries from all categories combined. |

### 🔒 Security & Uniqueness

This module manages access control using Python **Sets** for rapid lookups.

| Function | Description |
| :--- | :--- |
| **`register_authorized_user(user_id)`** | Adds a user’s ID to the internal set of authorized users. |
| **`check_user_access(user_id)`** | Returns `True` if the user ID is in the authorized users set, `False` otherwise. |
| **`remove_user_access(user_id)`** | Removes a user ID from the authorized users set. |

### 🔍 Search & Analysis

| Function | Description |
| :--- | :--- |
| **`find_logs_by_keyword(keyword)`** | Scans all log messages for a given keyword and returns a list of matching log entries. |
| **`get_unique_log_levels()`** | Returns a set of all distinct log levels found across all entries (e.g., `{'CRITICAL', 'INFO', 'WARNING'}`). |
| **`summarize_log_counts()`** | Returns a dictionary where keys are log categories and values are the total count of entries in that category. |

### 🧹 Maintenance & Utility

| Function | Description |
| :--- | :--- |
| **`clear_logs(category=None)`** | Clears logs for a specific category. If `None` is specified, all logs are cleared. |
| **`export_logs_to_file(filename)`** | Prepares all log data into a structured list of tuples for backup purposes, ready for writing to the specified `filename`. |

---

## 🏗️ Current Progress

The project is currently in its initial development phase.

* **`Logging_Functions`**: The core class has been defined.
* **`add_log_entry`**: This function is **fully implemented and functional**, allowing for successful addition and categorization of new log entries.

We are now focused on completing the remaining methods across the `Security_and_Uniqueness`, `SearchAndAnalysis`, and `Maintenance_and_Utiltiy` modules.
