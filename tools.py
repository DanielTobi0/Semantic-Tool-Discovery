filesystem_mcp_tools = {
    "read_text_file": {
        "Tool": "read_text_file",
        "Purpose": "Read complete or partial contents of a text file.",
        "Capabilities": "Retrieves file content as UTF-8 text. Supports reading the entire file, or extracting just the beginning (head) or end (tail) of large files to save token context.",
        "Parameters": "path (string): File location; head (int, optional): Number of lines from start; tail (int, optional): Number of lines from end."
    },
    "read_media_file": {
        "Tool": "read_media_file",
        "Purpose": "Read binary or media files.",
        "Capabilities": "Reads image, audio, or binary files and converts them to base64 encoded strings along with their MIME types for safe transmission and vision-model processing.",
        "Parameters": "path (string): File location."
    },
    "read_multiple_files": {
        "Tool": "read_multiple_files",
        "Purpose": "Read multiple files simultaneously.",
        "Capabilities": "Batch operation to retrieve the contents of multiple files in a single request. Partial failures on one file do not stop the successful reads of others.",
        "Parameters": "paths (array of strings): List of file locations."
    },
    "write_file": {
        "Tool": "write_file",
        "Purpose": "Create a new file or overwrite an existing one.",
        "Capabilities": "Writes string content directly to the specified file path. Overwrites any existing data destructively.",
        "Parameters": "path (string): File location; content (string): The data to write."
    },
    "append_file": {
        "Tool": "append_file",
        "Purpose": "Append content to an existing file.",
        "Capabilities": "Adds new text content to the end of a file without overwriting the existing data. Useful for updating logs or appending variables.",
        "Parameters": "path (string): File location; content (string): The data to append."
    },
    "edit_file": {
        "Tool": "edit_file",
        "Purpose": "Make selective edits to a file.",
        "Capabilities": "Uses pattern matching to replace specific multi-line blocks of text. Supports dry-run previews, preserves whitespace/indentation, and generates git-style diffs.",
        "Parameters": "path (string): File location; old_text (string): Text to search for; new_text (string): Replacement text; dry_run (bool, optional): Preview without saving."
    },
    "delete_file": {
        "Tool": "delete_file",
        "Purpose": "Delete a specific file.",
        "Capabilities": "Permanently removes a file from the filesystem. Action is destructive and cannot be undone.",
        "Parameters": "path (string): File location."
    },
    "copy_file": {
        "Tool": "copy_file",
        "Purpose": "Copy a file to a new location.",
        "Capabilities": "Duplicates a file while preserving its content. Safely fails if the destination already exists unless explicitly forced.",
        "Parameters": "source (string): Original file path; destination (string): Target file path; overwrite (bool, optional): Overwrite if destination exists."
    },
    "move_file": {
        "Tool": "move_file",
        "Purpose": "Move or rename files and directories.",
        "Capabilities": "Transfers a file or directory to a new path or changes its name. Will fail if the target destination already exists.",
        "Parameters": "source (string): Current path; destination (string): New path."
    },
    "get_file_info": {
        "Tool": "get_file_info",
        "Purpose": "Get detailed metadata for a file or directory.",
        "Capabilities": "Retrieves system metadata including size, creation time, modification time, access time, file type, and read/write/execute permissions.",
        "Parameters": "path (string): File or directory location."
    },
    "search_files": {
        "Tool": "search_files",
        "Purpose": "Search for files by name.",
        "Capabilities": "Recursively scans directories to find files or folders matching specific glob patterns or regular expressions. Ignores hidden files by default.",
        "Parameters": "path (string): Directory to search; pattern (string): Glob pattern to match; exclude_patterns (array of strings, optional): Patterns to ignore."
    },
    "search_file_content": {
        "Tool": "search_file_content",
        "Purpose": "Search for text inside multiple files.",
        "Capabilities": "Acts as a grep equivalent, scanning file contents across a directory to find lines matching a specific string or regex pattern.",
        "Parameters": "path (string): Directory to search; query (string): Text or regex to find; file_pattern (string, optional): Filter specific extensions to search."
    },
    "create_directory": {
        "Tool": "create_directory",
        "Purpose": "Create a new directory.",
        "Capabilities": "Creates a new folder. Automatically creates missing parent directories recursively (equivalent to mkdir -p). Succeeds silently if it already exists.",
        "Parameters": "path (string): Directory location."
    },
    "list_directory": {
        "Tool": "list_directory",
        "Purpose": "List the immediate contents of a directory.",
        "Capabilities": "Returns files and subdirectories located directly within the specified path, categorized with prefixes like [FILE] or [DIR].",
        "Parameters": "path (string): Directory location."
    },
    "list_directory_sizes": {
        "Tool": "list_directory_sizes",
        "Purpose": "List directory contents along with their file sizes.",
        "Capabilities": "Retrieves files and folders in a directory, calculating byte sizes and providing summary statistics. Supports sorting entries by name or size.",
        "Parameters": "path (string): Directory location; sort_by (string, optional): 'name' or 'size'."
    },
    "directory_tree": {
        "Tool": "directory_tree",
        "Purpose": "Retrieve a recursive representation of a directory.",
        "Capabilities": "Generates a deep, structured JSON tree of all files and folders nested within a directory, providing spatial understanding of project structures.",
        "Parameters": "path (string): Starting directory; depth (int, optional): Maximum recursion depth."
    },
    "delete_directory": {
        "Tool": "delete_directory",
        "Purpose": "Delete a directory.",
        "Capabilities": "Removes a folder. Can perform recursive deletion to forcefully delete a folder and all of its sub-contents if it is not empty.",
        "Parameters": "path (string): Directory location; recursive (bool, optional): Delete contents if not empty."
    },
    "copy_directory": {
        "Tool": "copy_directory",
        "Purpose": "Copy a directory and its contents.",
        "Capabilities": "Recursively duplicates an entire folder structure, including all nested files and subdirectories, to a new destination.",
        "Parameters": "source (string): Original directory path; destination (string): Target directory path."
    },
    "touch_file": {
        "Tool": "touch_file",
        "Purpose": "Update file timestamps or create an empty file.",
        "Capabilities": "Creates a zero-byte file if the target does not exist, or seamlessly updates the modification and access timestamps of an existing file.",
        "Parameters": "path (string): File location."
    },
    "change_permissions": {
        "Tool": "change_permissions",
        "Purpose": "Modify file or directory access permissions.",
        "Capabilities": "Changes the read, write, and execute permissions of a file (e.g., chmod), utilizing standard numeric (755) or symbolic (+x) modes.",
        "Parameters": "path (string): File or directory location; mode (string): Permission mode."
    },
    "change_owner": {
        "Tool": "change_owner",
        "Purpose": "Change the owner and group of a file or directory.",
        "Capabilities": "Modifies system ownership metadata (chown). Usually requires elevated administrative privileges to execute successfully.",
        "Parameters": "path (string): File or directory location; user (string): New owner username; group (string, optional): New group name."
    },
    "create_symlink": {
        "Tool": "create_symlink",
        "Purpose": "Create a symbolic link to a file or directory.",
        "Capabilities": "Generates a shortcut reference pointing from a target path back to a specified source path, aiding in modular file organization.",
        "Parameters": "target (string): The original file/folder; link_path (string): The path for the new symlink."
    },
    "list_allowed_directories": {
        "Tool": "list_allowed_directories",
        "Purpose": "Check which directories the server is permitted to access.",
        "Capabilities": "Returns the sandbox root paths that the current MCP server session is configured to safely read from or write to.",
        "Parameters": "None."
    }
}


mysql_database_mcp_tools = {
    "connect_database": {
        "Tool": "connect_database",
        "Purpose": "Establish a connection to a MySQL server.",
        "Capabilities": "Authenticates and creates a session with the MySQL database instance. Can connect via TCP/IP or local sockets. Handles connection pooling and returns a session token or ID.",
        "Parameters": "host (string): Database hostname or IP; port (int): Connection port; user (string): Username; password (string): Password; database (string, optional): Default schema to use."
    },
    "disconnect_database": {
        "Tool": "disconnect_database",
        "Purpose": "Close an active database connection.",
        "Capabilities": "Safely terminates the connection to the MySQL server, releasing socket resources and clearing session data.",
        "Parameters": "connection_id (string, optional): Specific session to close, defaults to current."
    },
    "ping_database": {
        "Tool": "ping_database",
        "Purpose": "Check the health of the database connection.",
        "Capabilities": "Executes a lightweight heartbeat query (e.g., 'SELECT 1') to verify the database is reachable and the session has not timed out.",
        "Parameters": "None."
    },
    "execute_read_query": {
        "Tool": "execute_read_query",
        "Purpose": "Execute a SELECT query safely.",
        "Capabilities": "Executes read-only SQL statements. Automatically limits result sets to prevent memory overflow and returns rows as structured JSON arrays.",
        "Parameters": "query (string): The SELECT SQL statement; limit (int, optional): Max rows to return."
    },
    "execute_write_query": {
        "Tool": "execute_write_query",
        "Purpose": "Execute DML statements (INSERT, UPDATE, DELETE).",
        "Capabilities": "Performs data manipulation operations. Returns metadata about the operation, such as the number of affected rows and any generated auto-increment IDs. Destructive action.",
        "Parameters": "query (string): The DML SQL statement."
    },
    "execute_transaction": {
        "Tool": "execute_transaction",
        "Purpose": "Execute multiple queries atomically within a transaction.",
        "Capabilities": "Wraps an array of SQL statements in a BEGIN...COMMIT block. If any query fails, automatically issues a ROLLBACK to maintain data integrity.",
        "Parameters": "queries (array of strings): List of SQL statements to execute in order."
    },
    "list_databases": {
        "Tool": "list_databases",
        "Purpose": "List all available schemas/databases.",
        "Capabilities": "Executes 'SHOW DATABASES' to return a list of all schemas accessible by the current user on the MySQL server.",
        "Parameters": "None."
    },
    "select_database": {
        "Tool": "select_database",
        "Purpose": "Change the active working database.",
        "Capabilities": "Executes a 'USE database_name' statement to switch the default schema context for subsequent queries in the session.",
        "Parameters": "database_name (string): Name of the database to switch to."
    },
    "list_tables": {
        "Tool": "list_tables",
        "Purpose": "List all base tables in the database.",
        "Capabilities": "Executes 'SHOW FULL TABLES WHERE Table_type = \"BASE TABLE\"' to enumerate standard data tables, ignoring views.",
        "Parameters": "database_name (string, optional): Target schema, defaults to active database."
    },
    "list_views": {
        "Tool": "list_views",
        "Purpose": "List all views in the database.",
        "Capabilities": "Executes 'SHOW FULL TABLES WHERE Table_type = \"VIEW\"' to list logical view structures in the specified schema.",
        "Parameters": "database_name (string, optional): Target schema, defaults to active database."
    },
    "get_table_schema": {
        "Tool": "get_table_schema",
        "Purpose": "Retrieve the exact DDL used to create a table.",
        "Capabilities": "Executes 'SHOW CREATE TABLE' to retrieve the raw SQL statement defining the table structure, including character sets, collations, and constraints.",
        "Parameters": "table_name (string): Name of the table."
    },
    "list_columns": {
        "Tool": "list_columns",
        "Purpose": "Get detailed column information for a table.",
        "Capabilities": "Queries 'information_schema.columns' to extract column names, data types, nullability, defaults, and character maximum lengths.",
        "Parameters": "table_name (string): Name of the table."
    },
    "get_primary_key": {
        "Tool": "get_primary_key",
        "Purpose": "Identify the primary key(s) of a table.",
        "Capabilities": "Specifically extracts the column or composite columns designated as the PRIMARY KEY, essential for understanding row uniqueness.",
        "Parameters": "table_name (string): Name of the table."
    },
    "list_indexes": {
        "Tool": "list_indexes",
        "Purpose": "List all indexes on a table.",
        "Capabilities": "Executes 'SHOW INDEX FROM' to return information about unique and non-unique indexes, cardinality, and indexed column sequences.",
        "Parameters": "table_name (string): Name of the table."
    },
    "list_foreign_keys": {
        "Tool": "list_foreign_keys",
        "Purpose": "Identify foreign key constraints and relationships.",
        "Capabilities": "Queries 'information_schema.key_column_usage' to map relationships between the target table and other tables, identifying referential integrity constraints.",
        "Parameters": "table_name (string): Name of the table."
    },
    "list_triggers": {
        "Tool": "list_triggers",
        "Purpose": "List triggers associated with tables.",
        "Capabilities": "Executes 'SHOW TRIGGERS' to list database events (BEFORE/AFTER INSERT/UPDATE/DELETE) and their corresponding procedural logic.",
        "Parameters": "table_name (string, optional): Filter by a specific table."
    },
    "list_routines": {
        "Tool": "list_routines",
        "Purpose": "List stored procedures and functions.",
        "Capabilities": "Queries 'information_schema.routines' to list programmable functions and procedures, including their return types and definitions.",
        "Parameters": "routine_type (string, optional): Filter by 'PROCEDURE' or 'FUNCTION'."
    },
    "get_table_statistics": {
        "Tool": "get_table_statistics",
        "Purpose": "Get physical table metrics and metadata.",
        "Capabilities": "Executes 'SHOW TABLE STATUS' to retrieve the storage engine type, estimated row count, data length (size in bytes), and index length.",
        "Parameters": "table_name (string): Name of the table."
    },
    "analyze_query_plan": {
        "Tool": "analyze_query_plan",
        "Purpose": "Explain the execution plan for a SQL query.",
        "Capabilities": "Prepends 'EXPLAIN' to a given query to expose how MySQL resolves it, including index usage, join types, and rows examined. Crucial for optimization.",
        "Parameters": "query (string): The SELECT statement to analyze."
    },
    "show_running_processes": {
        "Tool": "show_running_processes",
        "Purpose": "List active connections and running queries.",
        "Capabilities": "Executes 'SHOW PROCESSLIST' to display current user threads, execution states, and queries currently running on the server.",
        "Parameters": "full (bool, optional): If true, executes SHOW FULL PROCESSLIST to prevent query truncation."
    },
    "kill_process": {
        "Tool": "kill_process",
        "Purpose": "Terminate a long-running query or connection.",
        "Capabilities": "Executes the 'KILL' command against a specific thread ID to force-stop locked or inefficient queries.",
        "Parameters": "process_id (int): The thread ID to terminate."
    },
    "export_query_results": {
        "Tool": "export_query_results",
        "Purpose": "Export data sets to standard formats.",
        "Capabilities": "Executes a SELECT query and formats the result set entirely into a CSV or JSON string format for easy external parsing and data extraction.",
        "Parameters": "query (string): The SELECT statement; format (string): Target format ('csv' or 'json')."
    },
    "show_variables": {
        "Tool": "show_variables",
        "Purpose": "Inspect MySQL server configuration variables.",
        "Capabilities": "Executes 'SHOW VARIABLES' to retrieve system settings like max_connections, wait_timeout, or innodb_buffer_pool_size.",
        "Parameters": "pattern (string, optional): A LIKE clause to filter specific variables."
    }
}


slack_mcp_tools = {
    "post_message": {
        "Tool": "post_message",
        "Purpose": "Send a message to a channel or direct message.",
        "Capabilities": "Posts a standard or rich-text block message to a specified Slack channel, private group, or direct message conversation.",
        "Parameters": "channel (string): Channel ID or name; text (string): Message content; blocks (array, optional): Block Kit UI components."
    },
    "post_ephemeral_message": {
        "Tool": "post_ephemeral_message",
        "Purpose": "Send a temporary, user-specific message.",
        "Capabilities": "Posts a transient message to a channel that is only visible to a specific user. Ideal for silent confirmations or interactive errors.",
        "Parameters": "channel (string): Channel ID; user (string): User ID to show message to; text (string): Message content."
    },
    "update_message": {
        "Tool": "update_message",
        "Purpose": "Edit a previously sent message.",
        "Capabilities": "Modifies the text or block structure of an existing message sent by the bot. Requires the original message timestamp identifier.",
        "Parameters": "channel (string): Channel ID; ts (string): Timestamp of original message; text (string): New message content."
    },
    "delete_message": {
        "Tool": "delete_message",
        "Purpose": "Delete an existing message.",
        "Capabilities": "Removes a specific message from a channel or conversation permanently using its timestamp identifier.",
        "Parameters": "channel (string): Channel ID; ts (string): Timestamp of the message to delete."
    },
    "reply_to_thread": {
        "Tool": "reply_to_thread",
        "Purpose": "Send a message as a reply in a specific thread.",
        "Capabilities": "Posts a response explicitly bound to a parent message's thread. Optionally broadcasts the reply to the main channel.",
        "Parameters": "channel (string): Channel ID; thread_ts (string): Parent message timestamp; text (string): Reply content; reply_broadcast (bool, optional): Share in channel."
    },
    "add_reaction": {
        "Tool": "add_reaction",
        "Purpose": "Add an emoji reaction to a message.",
        "Capabilities": "Attaches a specified emoji (e.g., 'thumbsup') to a message to provide lightweight feedback or acknowledge receipt.",
        "Parameters": "channel (string): Channel ID; name (string): Emoji name without colons; timestamp (string): Message timestamp."
    },
    "remove_reaction": {
        "Tool": "remove_reaction",
        "Purpose": "Remove a previously added emoji reaction.",
        "Capabilities": "Detaches a specific emoji reaction from a message that was previously added by the authenticated bot.",
        "Parameters": "channel (string): Channel ID; name (string): Emoji name without colons; timestamp (string): Message timestamp."
    },
    "get_message_permalink": {
        "Tool": "get_message_permalink",
        "Purpose": "Get a shareable URL for a specific message.",
        "Capabilities": "Generates a direct web link (permalink) to a specific message within a channel for sharing or reference purposes.",
        "Parameters": "channel (string): Channel ID; message_ts (string): Message timestamp."
    },
    "list_channels": {
        "Tool": "list_channels",
        "Purpose": "List all public and joined private channels.",
        "Capabilities": "Retrieves a paginated list of channels in the workspace, including metadata like member count and creation date.",
        "Parameters": "limit (int, optional): Max results to return; types (string, optional): Comma-separated channel types (e.g., public_channel, private_channel)."
    },
    "create_channel": {
        "Tool": "create_channel",
        "Purpose": "Create a new Slack channel.",
        "Capabilities": "Initializes a new public or private channel in the workspace. Will fail if the channel name is already taken.",
        "Parameters": "name (string): Name of the new channel; is_private (bool, optional): Create as a private channel."
    },
    "join_channel": {
        "Tool": "join_channel",
        "Purpose": "Join an existing channel.",
        "Capabilities": "Adds the bot or authenticated user to a specified public channel to enable reading and sending messages.",
        "Parameters": "channel (string): Channel ID to join."
    },
    "leave_channel": {
        "Tool": "leave_channel",
        "Purpose": "Leave a channel.",
        "Capabilities": "Removes the bot or authenticated user from a specified channel, ceasing notifications and active participation.",
        "Parameters": "channel (string): Channel ID to leave."
    },
    "archive_channel": {
        "Tool": "archive_channel",
        "Purpose": "Archive a channel.",
        "Capabilities": "Changes the status of a channel to archived, freezing its history and preventing new messages from being sent.",
        "Parameters": "channel (string): Channel ID to archive."
    },
    "unarchive_channel": {
        "Tool": "unarchive_channel",
        "Purpose": "Unarchive a previously archived channel.",
        "Capabilities": "Restores an archived channel to active status, allowing members to resume sending messages.",
        "Parameters": "channel (string): Channel ID to unarchive."
    },
    "rename_channel": {
        "Tool": "rename_channel",
        "Purpose": "Change the name of a channel.",
        "Capabilities": "Updates the alphanumeric handle of a channel. Subject to workspace naming rules and permissions.",
        "Parameters": "channel (string): Channel ID; name (string): New channel name."
    },
    "invite_to_channel": {
        "Tool": "invite_to_channel",
        "Purpose": "Invite a user to a channel.",
        "Capabilities": "Adds a specific workspace user to an existing public or private channel.",
        "Parameters": "channel (string): Channel ID; users (string): Comma-separated list of User IDs to invite."
    },
    "kick_from_channel": {
        "Tool": "kick_from_channel",
        "Purpose": "Remove a user from a channel.",
        "Capabilities": "Forcibly removes a user from a specific channel. Requires appropriate admin or channel manager permissions.",
        "Parameters": "channel (string): Channel ID; user (string): User ID to remove."
    },
    "set_channel_topic": {
        "Tool": "set_channel_topic",
        "Purpose": "Set the topic of a channel.",
        "Capabilities": "Updates the brief description that appears in the channel header, typically used for current focus or status.",
        "Parameters": "channel (string): Channel ID; topic (string): New channel topic."
    },
    "set_channel_purpose": {
        "Tool": "set_channel_purpose",
        "Purpose": "Set the purpose of a channel.",
        "Capabilities": "Updates the longer descriptive text explaining what the channel is used for, visible in channel details.",
        "Parameters": "channel (string): Channel ID; purpose (string): New channel purpose."
    },
    "get_channel_info": {
        "Tool": "get_channel_info",
        "Purpose": "Get metadata about a specific channel.",
        "Capabilities": "Retrieves detailed information about a channel, including its creator, creation date, topic, purpose, and member count.",
        "Parameters": "channel (string): Channel ID."
    },
    "get_channel_history": {
        "Tool": "get_channel_history",
        "Purpose": "Fetch recent messages from a channel.",
        "Capabilities": "Retrieves a paginated list of chronological messages from a channel's history, essential for context reading.",
        "Parameters": "channel (string): Channel ID; limit (int, optional): Max messages to return; oldest (string, optional): Start timestamp."
    },
    "get_thread_replies": {
        "Tool": "get_thread_replies",
        "Purpose": "Fetch all replies within a specific thread.",
        "Capabilities": "Retrieves the entire sequence of replies attached to a parent message, enabling reading of localized conversations.",
        "Parameters": "channel (string): Channel ID; ts (string): Timestamp of the parent message."
    },
    "list_users": {
        "Tool": "list_users",
        "Purpose": "List all users in the Slack workspace.",
        "Capabilities": "Retrieves a paginated directory of workspace members, including their names, statuses, and profile information.",
        "Parameters": "limit (int, optional): Max users to return."
    },
    "get_user_info": {
        "Tool": "get_user_info",
        "Purpose": "Get detailed profile information for a user.",
        "Capabilities": "Fetches specific metadata for a single user ID, including real name, display name, timezone, and avatar URLs.",
        "Parameters": "user (string): User ID."
    },
    "get_user_by_email": {
        "Tool": "get_user_by_email",
        "Purpose": "Find a user's Slack ID using their email address.",
        "Capabilities": "Looks up a workspace member by their registered email address to retrieve their internal Slack ID for mapping and tagging.",
        "Parameters": "email (string): Email address of the user."
    },
    "list_channel_members": {
        "Tool": "list_channel_members",
        "Purpose": "List all users currently in a channel.",
        "Capabilities": "Returns an array of User IDs representing everyone who is currently a member of the specified channel.",
        "Parameters": "channel (string): Channel ID."
    },
    "upload_file": {
        "Tool": "upload_file",
        "Purpose": "Upload a file to a channel or thread.",
        "Capabilities": "Uploads document, image, or code snippet files directly to Slack, optionally sharing them in a specific conversation.",
        "Parameters": "channels (string): Comma-separated Channel IDs; file_content (string): Base64 or text content; filename (string): Name of the file."
    },
    "delete_file": {
        "Tool": "delete_file",
        "Purpose": "Delete an uploaded file.",
        "Capabilities": "Permanently removes a previously uploaded file from the Slack workspace to free up storage or remove sensitive data.",
        "Parameters": "file (string): File ID to delete."
    },
    "list_files": {
        "Tool": "list_files",
        "Purpose": "List files across the workspace or in a channel.",
        "Capabilities": "Retrieves a paginated list of files uploaded to Slack, filterable by user, channel, or file type.",
        "Parameters": "channel (string, optional): Channel ID to filter by; types (string, optional): File type filter (e.g., images, pdfs)."
    },
    "search_messages": {
        "Tool": "search_messages",
        "Purpose": "Search for messages matching a query string.",
        "Capabilities": "Executes a global search across the workspace for messages matching specific keywords or modifiers (e.g., from:user).",
        "Parameters": "query (string): Search query string; sort (string, optional): Sort by 'score' or 'timestamp'."
    },
    "search_files": {
        "Tool": "search_files",
        "Purpose": "Search for files matching a query string.",
        "Capabilities": "Executes a global search for files matching keyword queries in their name, content, or file type.",
        "Parameters": "query (string): Search query string; sort (string, optional): Sort by 'score' or 'timestamp'."
    },
    "list_custom_emojis": {
        "Tool": "list_custom_emojis",
        "Purpose": "List all custom emojis in the workspace.",
        "Capabilities": "Retrieves a key-value mapping of all custom emoji names and their corresponding image URLs installed in the workspace.",
        "Parameters": "None."
    },
    "create_user_group": {
        "Tool": "create_user_group",
        "Purpose": "Create a new Slack user group.",
        "Capabilities": "Generates a new user group (e.g., @engineering-team) that can be mentioned to ping multiple members at once.",
        "Parameters": "name (string): Name of the user group; handle (string): The mention handle."
    },
    "update_user_group_users": {
        "Tool": "update_user_group_users",
        "Purpose": "Update the members of a user group.",
        "Capabilities": "Overwrites the list of active members belonging to a specific user group, replacing the old member list entirely.",
        "Parameters": "usergroup (string): User Group ID; users (string): Comma-separated list of User IDs to include."
    }
}


github_mcp_tools = {
    "create_repository": {
        "Tool": "create_repository",
        "Purpose": "Create a new GitHub repository.",
        "Capabilities": "Initializes a new GitHub repository under the authenticated user's account or a specified organization. Supports setting visibility, adding a README, and applying an open-source license during creation.",
        "Parameters": "name (string): Repository name; description (string, optional): Short description; private (bool, optional): Set to true for private; auto_init (bool, optional): Initialize with README."
    },
    "get_repository": {
        "Tool": "get_repository",
        "Purpose": "Retrieve detailed information about a repository.",
        "Capabilities": "Fetches repository metadata including description, star count, language, default branch, clone URLs, visibility, and open issue counts.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name."
    },
    "list_repositories": {
        "Tool": "list_repositories",
        "Purpose": "List repositories for a user or organization.",
        "Capabilities": "Returns a paginated list of repositories accessible to the authenticated user. Can filter by visibility (public/private), affiliation, or sort by creation/update times.",
        "Parameters": "affiliation (string, optional): owner, collaborator, or organization member; sort (string, optional): created, updated, pushed; per_page (int, optional): Results per page."
    },
    "search_repositories": {
        "Tool": "search_repositories",
        "Purpose": "Search for repositories across GitHub.",
        "Capabilities": "Executes a global search across GitHub to find repositories matching specific keywords, topics, or language filters. Sorts results by stars, forks, or recent updates.",
        "Parameters": "query (string): The search query; sort (string, optional): stars, forks, or updated; order (string, optional): asc or desc."
    },
    "update_repository": {
        "Tool": "update_repository",
        "Purpose": "Update repository settings.",
        "Capabilities": "Modifies the configuration of an existing repository. Can change the repository name, description, default branch, visibility, or toggle features like wikis and issues.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; description (string, optional): New description; private (bool, optional): Change visibility."
    },
    "fork_repository": {
        "Tool": "fork_repository",
        "Purpose": "Fork a repository.",
        "Capabilities": "Creates a personal or organizational fork of an existing repository. Useful for contributing to upstream open-source projects safely.",
        "Parameters": "owner (string): Upstream account owner; repo (string): Upstream repository name; organization (string, optional): Target organization for the fork."
    },
    "list_branches": {
        "Tool": "list_branches",
        "Purpose": "List all branches in a repository.",
        "Capabilities": "Retrieves a paginated list of branches within a specific repository, including the latest commit SHA for each branch and branch protection status.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; per_page (int, optional): Results per page."
    },
    "get_branch": {
        "Tool": "get_branch",
        "Purpose": "Get detailed information about a specific branch.",
        "Capabilities": "Fetches details for a single branch, including branch protection rules, required reviews, and the commit object pointing to the tip of the branch.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; branch (string): Name of the branch."
    },
    "create_branch": {
        "Tool": "create_branch",
        "Purpose": "Create a new branch.",
        "Capabilities": "Creates a new Git reference (branch) pointing to a specific commit SHA. Essential for starting new feature work or bug fixes securely without affecting the default branch.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; ref (string): Name of new branch (e.g., refs/heads/new-feature); sha (string): Source commit SHA."
    },
    "delete_branch": {
        "Tool": "delete_branch",
        "Purpose": "Delete a branch.",
        "Capabilities": "Deletes a specific Git reference (branch) from the repository. Typically used to clean up branches after a pull request has been successfully merged.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; ref (string): Name of branch to delete (e.g., heads/feature-branch)."
    },
    "list_commits": {
        "Tool": "list_commits",
        "Purpose": "List commits on a repository.",
        "Capabilities": "Retrieves a chronological history of commits for a repository. Can filter commits by author, branch, file path, or date range.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; sha (string, optional): Branch or commit SHA to list from; path (string, optional): Filter by file path."
    },
    "get_commit": {
        "Tool": "get_commit",
        "Purpose": "Retrieve a specific commit.",
        "Capabilities": "Fetches detailed information about a single commit, including the author, message, timestamp, and a complete diff of the files added, modified, or deleted.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; ref (string): Commit SHA."
    },
    "compare_commits": {
        "Tool": "compare_commits",
        "Purpose": "Compare two commits or branches.",
        "Capabilities": "Analyzes the differences between a base and a head commit. Returns the merge base, a list of commits unique to the head, and a unified diff of file changes.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; base (string): Base branch or SHA; head (string): Head branch or SHA."
    },
    "get_file_content": {
        "Tool": "get_file_content",
        "Purpose": "Read the contents of a file in a repository.",
        "Capabilities": "Retrieves the Base64-encoded content of a specific file at a given commit or branch. Useful for inspecting code, configurations, or documentation.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; path (string): File path; ref (string, optional): Branch or commit SHA."
    },
    "create_or_update_file": {
        "Tool": "create_or_update_file",
        "Purpose": "Create or modify a file.",
        "Capabilities": "Commits a new file or updates an existing one directly via the API. Requires providing the new content, a commit message, and the blob SHA if updating an existing file.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; path (string): File path; message (string): Commit message; content (string): Base64 encoded file content; sha (string, optional): Blob SHA of existing file."
    },
    "delete_file": {
        "Tool": "delete_file",
        "Purpose": "Delete a file from a repository.",
        "Capabilities": "Removes a file from the repository and creates a commit logging the deletion. Requires the current blob SHA of the file to prevent race conditions.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; path (string): File path; message (string): Commit message; sha (string): Blob SHA of the file to delete."
    },
    "create_pull_request": {
        "Tool": "create_pull_request",
        "Purpose": "Create a new pull request.",
        "Capabilities": "Opens a new pull request to merge changes from a head branch into a base branch. Allows specifying the PR title, detailed description body, and drafting status.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; title (string): PR title; head (string): Branch containing changes; base (string): Target branch; body (string, optional): Description."
    },
    "update_pull_request": {
        "Tool": "update_pull_request",
        "Purpose": "Update an existing pull request.",
        "Capabilities": "Modifies the title, body, state (open/closed), or base branch of an existing pull request. Useful for managing PR lifecycle and updating descriptions.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; pull_number (int): PR number; title (string, optional): New title; state (string, optional): open or closed."
    },
    "list_pull_requests": {
        "Tool": "list_pull_requests",
        "Purpose": "List pull requests in a repository.",
        "Capabilities": "Retrieves open or closed pull requests. Can filter by base branch, sort by creation/update time, and page through results to review ongoing integrations.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; state (string, optional): open, closed, or all; sort (string, optional): created, updated, popularity."
    },
    "merge_pull_request": {
        "Tool": "merge_pull_request",
        "Purpose": "Merge a pull request.",
        "Capabilities": "Executes the merge of a pull request into its base branch. Supports different merge methods (merge commit, squash, rebase) and enforces branch protection rules.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; pull_number (int): PR number; commit_title (string, optional): Title for the merge commit; merge_method (string, optional): merge, squash, or rebase."
    },
    "get_pull_request": {
        "Tool": "get_pull_request",
        "Purpose": "Get details of a single pull request.",
        "Capabilities": "Fetches comprehensive metadata for a PR, including review status, mergeability, addition/deletion line counts, changed files count, and assignee information.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; pull_number (int): PR number."
    },
    "list_issues": {
        "Tool": "list_issues",
        "Purpose": "List repository issues.",
        "Capabilities": "Retrieves a paginated list of issues for a repository. Filters can be applied for issue state, assignee, labels, or milestone to triage and track bugs or tasks.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; state (string, optional): open, closed, or all; labels (string, optional): Comma-separated label names."
    },
    "get_issue": {
        "Tool": "get_issue",
        "Purpose": "Get details of a single issue.",
        "Capabilities": "Fetches the full context of a specific issue, including the title, body description, author, current status, labels, and assignment details.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; issue_number (int): Issue ID number."
    },
    "create_issue": {
        "Tool": "create_issue",
        "Purpose": "Create a new issue.",
        "Capabilities": "Opens a new issue in a repository for bug tracking or task management. Supports applying assignees, milestones, and specific categorical labels upon creation.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; title (string): Issue title; body (string, optional): Markdown description; labels (array of strings, optional): Tags to apply."
    },
    "update_issue": {
        "Tool": "update_issue",
        "Purpose": "Update an existing issue.",
        "Capabilities": "Modifies the properties of an open or closed issue. Used to update the description body, change the title, add labels, assign users, or toggle the open/closed state.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; issue_number (int): Issue ID number; title (string, optional): New title; state (string, optional): open or closed."
    },
    "lock_issue": {
        "Tool": "lock_issue",
        "Purpose": "Lock an issue from further comments.",
        "Capabilities": "Freezes an issue or pull request, preventing non-collaborators from adding new comments. Useful for archiving resolved discussions or stopping heated debates.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; issue_number (int): Issue ID number; lock_reason (string, optional): off-topic, resolved, too heated, spam."
    },
    "create_issue_comment": {
        "Tool": "create_issue_comment",
        "Purpose": "Add a comment to an issue or pull request.",
        "Capabilities": "Posts a new Markdown-formatted text comment to an ongoing issue discussion or pull request timeline to provide updates or feedback.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; issue_number (int): Issue ID number; body (string): Comment content in Markdown."
    },
    "list_issue_comments": {
        "Tool": "list_issue_comments",
        "Purpose": "List comments on an issue.",
        "Capabilities": "Retrieves a chronological, paginated list of comments made on a specific issue or PR, essential for reading discussion history and context.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; issue_number (int): Issue ID number; since (string, optional): Only comments updated at or after this time."
    },
    "update_issue_comment": {
        "Tool": "update_issue_comment",
        "Purpose": "Edit an existing issue comment.",
        "Capabilities": "Modifies the text of a previously posted comment. Often used for correcting typos or updating status checkboxes in issue descriptions.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; comment_id (int): The unique ID of the comment; body (string): New comment content."
    },
    "delete_issue_comment": {
        "Tool": "delete_issue_comment",
        "Purpose": "Delete a comment from an issue.",
        "Capabilities": "Permanently removes a specific comment from an issue or pull request timeline. Helps moderate spam or remove irrelevant chatter.",
        "Parameters": "owner (string): Account owner; repo (string): Repository name; comment_id (int): The unique ID of the comment to delete."
    },
    "search_issues": {
        "Tool": "search_issues",
        "Purpose": "Search issues and pull requests.",
        "Capabilities": "Executes advanced queries across GitHub to find issues or PRs matching specific criteria like author, text content, label, or repository. Sorts by interactions or creation date.",
        "Parameters": "query (string): Search query with qualifiers (e.g., 'repo:owner/repo is:open bug'); sort (string, optional): comments, created, updated; order (string, optional): asc or desc."
    }
}


time_weather_mcp_tools = {
    "get_current_time": {
        "Tool": "get_current_time",
        "Purpose": "Retrieve the current local time for a specific timezone.",
        "Capabilities": "Returns the current date, exact time, and timezone offset for a requested IANA timezone (e.g., 'America/New_York') or the system's local UTC time.",
        "Parameters": "timezone (string, optional): The IANA timezone database name. Defaults to UTC."
    },
    "convert_timezone": {
        "Tool": "convert_timezone",
        "Purpose": "Convert a specific date and time between two timezones.",
        "Capabilities": "Translates a given datetime string from a source timezone to a target timezone. Automatically handles daylight saving time (DST) adjustments.",
        "Parameters": "time (string): The datetime string to convert; source_timezone (string): Original IANA timezone; target_timezone (string): Destination IANA timezone."
    },
    "get_timezone_info": {
        "Tool": "get_timezone_info",
        "Purpose": "Get detailed information about a specific timezone.",
        "Capabilities": "Retrieves metadata for a timezone, including its current UTC offset, whether it currently observes daylight saving time, and standard region abbreviations.",
        "Parameters": "timezone (string): The IANA timezone database name."
    },
    "get_current_weather": {
        "Tool": "get_current_weather",
        "Purpose": "Get the current weather conditions for a specific location.",
        "Capabilities": "Retrieves real-time meteorological data including temperature, humidity, wind speed, barometric pressure, and weather condition descriptions (e.g., clear, raining) using geographic coordinates or city name.",
        "Parameters": "location (string, optional): City name or zip code; lat (float, optional): Latitude; lon (float, optional): Longitude; units (string, optional): 'metric' or 'imperial'."
    },
    "get_weather_forecast": {
        "Tool": "get_weather_forecast",
        "Purpose": "Retrieve the upcoming weather forecast for a location.",
        "Capabilities": "Fetches predicted weather conditions for the upcoming days or hours, providing expected high/low temperatures, precipitation probability, and general weather trends.",
        "Parameters": "location (string, optional): City name or zip code; days (int, optional): Number of days for forecast; units (string, optional): 'metric' or 'imperial'."
    },
    "get_historical_weather": {
        "Tool": "get_historical_weather",
        "Purpose": "Retrieve past weather data for a specific date and location.",
        "Capabilities": "Fetches historical meteorological records, allowing analysis of past temperatures, precipitation, and general conditions for a specific date in the past.",
        "Parameters": "location (string): City name or zip code; date (string): Target date (YYYY-MM-DD); units (string, optional): 'metric' or 'imperial'."
    },
    "get_air_quality": {
        "Tool": "get_air_quality",
        "Purpose": "Get current air quality index (AQI) and pollutant data.",
        "Capabilities": "Retrieves the overall Air Quality Index and specific concentrations of pollutants like PM2.5, PM10, Carbon Monoxide, and Ozone for a specified location.",
        "Parameters": "location (string, optional): City name or zip code; lat (float, optional): Latitude; lon (float, optional): Longitude."
    },
    "get_weather_alerts": {
        "Tool": "get_weather_alerts",
        "Purpose": "Retrieve severe weather warnings and alerts.",
        "Capabilities": "Fetches active meteorological hazard warnings (e.g., tornado watches, flood warnings, heat advisories) issued by local or national government weather agencies.",
        "Parameters": "location (string, optional): City name or zip code; lat (float, optional): Latitude; lon (float, optional): Longitude."
    },
    "search_location_coordinates": {
        "Tool": "search_location_coordinates",
        "Purpose": "Convert a city or address into geographic coordinates.",
        "Capabilities": "Performs forward geocoding to translate a human-readable location name into exact latitude and longitude coordinates, which are required for precise API weather lookups.",
        "Parameters": "query (string): City name, zip code, or address."
    },
    "get_sunrise_sunset": {
        "Tool": "get_sunrise_sunset",
        "Purpose": "Get sunrise, sunset, and twilight times for a location.",
        "Capabilities": "Calculates astronomical data including sunrise, sunset, solar noon, and civil/nautical twilight times for a specific geographical point on a given date.",
        "Parameters": "lat (float): Latitude; lon (float): Longitude; date (string, optional): Target date (YYYY-MM-DD), defaults to current date."
    }
}

