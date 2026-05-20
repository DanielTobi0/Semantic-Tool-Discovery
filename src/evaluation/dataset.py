evaluation_dataset = [
    # ==========================================
    # 1. FILESYSTEM SERVER EVALUATIONS
    # ==========================================
    {
        "query": "Can you show me the first 50 lines of the server.log file?",
        "expected_server": "filesystem",
        "expected_tool": "read_text_file",
        "expected_parameters": {"path": "server.log", "head": 50},
        "intent_type": "partial_read"
    },
    {
        "query": "Create a new folder called 'assets' inside the public directory.",
        "expected_server": "filesystem",
        "expected_tool": "create_directory",
        "expected_parameters": {"path": "public/assets"},
        "intent_type": "directory_creation"
    },
    {
        "query": "Find all occurrences of the phrase 'TODO: refactor' inside the src folder.",
        "expected_server": "filesystem",
        "expected_tool": "search_file_content",
        "expected_parameters": {"path": "src", "query": "TODO: refactor"},
        "intent_type": "content_search"
    },
    {
        "query": "Which files are taking up the most space in the /var/log directory?",
        "expected_server": "filesystem",
        "expected_tool": "list_directory_sizes",
        "expected_parameters": {"path": "/var/log", "sort_by": "size"},
        "intent_type": "size_analysis"
    },
    {
        "query": "Replace 'API_V1' with 'API_V2' in the config.json file.",
        "expected_server": "filesystem",
        "expected_tool": "edit_file",
        "expected_parameters": {"path": "config.json", "old_text": "API_V1", "new_text": "API_V2"},
        "intent_type": "file_edit"
    },
    {
        "query": "Give me a visual breakdown of all the files and folders inside the project root.",
        "expected_server": "filesystem",
        "expected_tool": "directory_tree",
        "expected_parameters": {"path": "./"}, # or project root path
        "intent_type": "structural_overview"
    },
    {
        "query": "Make the script.sh file executable for everyone.",
        "expected_server": "filesystem",
        "expected_tool": "change_permissions",
        "expected_parameters": {"path": "script.sh", "mode": "+x"}, # or 755
        "intent_type": "permission_change"
    },
    {
        "query": "Copy the entire 'images' folder over to the 'backup' directory.",
        "expected_server": "filesystem",
        "expected_tool": "copy_directory",
        "expected_parameters": {"source": "images", "destination": "backup"},
        "intent_type": "directory_copy"
    },
    {
        "query": "When was the database.sqlite file last modified?",
        "expected_server": "filesystem",
        "expected_tool": "get_file_info",
        "expected_parameters": {"path": "database.sqlite"},
        "intent_type": "metadata_retrieval"
    },
    {
        "query": "Load the contents of main.py, utils.py, and models.py all at once.",
        "expected_server": "filesystem",
        "expected_tool": "read_multiple_files",
        "expected_parameters": {"paths": ["main.py", "utils.py", "models.py"]},
        "intent_type": "batch_read"
    },

    # ==========================================
    # 2. MYSQL DATABASE SERVER EVALUATIONS
    # ==========================================
    {
        "query": "Connect to the production database at 192.168.1.50 using user 'admin'.",
        "expected_server": "mysql",
        "expected_tool": "connect_database",
        "expected_parameters": {"host": "192.168.1.50", "user": "admin"},
        "intent_type": "connection"
    },
    {
        "query": "What are all the base tables in the 'ecommerce' schema?",
        "expected_server": "mysql",
        "expected_tool": "list_tables",
        "expected_parameters": {"database_name": "ecommerce"},
        "intent_type": "schema_exploration"
    },
    {
        "query": "Fetch the top 10 rows from the users table where status is 'active'.",
        "expected_server": "mysql",
        "expected_tool": "execute_read_query",
        "expected_parameters": {"query": "SELECT * FROM users WHERE status = 'active' LIMIT 10"},
        "intent_type": "data_read"
    },
    {
        "query": "Why is this query 'SELECT * FROM orders WHERE user_id = 5' taking so long?",
        "expected_server": "mysql",
        "expected_tool": "analyze_query_plan",
        "expected_parameters": {"query": "SELECT * FROM orders WHERE user_id = 5"},
        "intent_type": "performance_analysis"
    },
    {
        "query": "Show me the exact SQL statement used to create the 'transactions' table.",
        "expected_server": "mysql",
        "expected_tool": "get_table_schema",
        "expected_parameters": {"table_name": "transactions"},
        "intent_type": "ddl_retrieval"
    },
    {
        "query": "What tables does the 'invoices' table link to via foreign keys?",
        "expected_server": "mysql",
        "expected_tool": "list_foreign_keys",
        "expected_parameters": {"table_name": "invoices"},
        "intent_type": "relationship_mapping"
    },
    {
        "query": "Force stop thread ID 4509, it's locking the table.",
        "expected_server": "mysql",
        "expected_tool": "kill_process",
        "expected_parameters": {"process_id": 4509},
        "intent_type": "process_management"
    },
    {
        "query": "Run a select query for all products and export the results as a CSV.",
        "expected_server": "mysql",
        "expected_tool": "export_query_results",
        "expected_parameters": {"query": "SELECT * FROM products", "format": "csv"},
        "intent_type": "data_export"
    },
    {
        "query": "Update the price to 19.99 for product ID 104.",
        "expected_server": "mysql",
        "expected_tool": "execute_write_query",
        "expected_parameters": {"query": "UPDATE products SET price = 19.99 WHERE id = 104"},
        "intent_type": "data_mutation"
    },
    {
        "query": "List all the indexes on the 'customers' table.",
        "expected_server": "mysql",
        "expected_tool": "list_indexes",
        "expected_parameters": {"table_name": "customers"},
        "intent_type": "index_retrieval"
    },

    # ==========================================
    # 3. SLACK SERVER EVALUATIONS
    # ==========================================
    {
        "query": "Post a message in the #general channel saying 'Deploy is complete!'.",
        "expected_server": "slack",
        "expected_tool": "post_message",
        "expected_parameters": {"channel": "#general", "text": "Deploy is complete!"},
        "intent_type": "message_broadcast"
    },
    {
        "query": "Reply to the message with timestamp 1629837.002 in #devops saying 'Looking into it'.",
        "expected_server": "slack",
        "expected_tool": "reply_to_thread",
        "expected_parameters": {"channel": "#devops", "thread_ts": "1629837.002", "text": "Looking into it"},
        "intent_type": "thread_reply"
    },
    {
        "query": "What are all the public channels currently active in this workspace?",
        "expected_server": "slack",
        "expected_tool": "list_channels",
        "expected_parameters": {"types": "public_channel"},
        "intent_type": "channel_discovery"
    },
    {
        "query": "React with the 'eyes' emoji to the last message sent at timestamp 123456 in #alerts.",
        "expected_server": "slack",
        "expected_tool": "add_reaction",
        "expected_parameters": {"channel": "#alerts", "name": "eyes", "timestamp": "123456"},
        "intent_type": "reaction_addition"
    },
    {
        "query": "Upload the error.log file into the #engineering channel.",
        "expected_server": "slack",
        "expected_tool": "upload_file",
        "expected_parameters": {"channels": "#engineering", "filename": "error.log"},
        "intent_type": "file_sharing"
    },
    {
        "query": "Create a new user group for the marketing team with the handle @marketing-team.",
        "expected_server": "slack",
        "expected_tool": "create_user_group",
        "expected_parameters": {"name": "marketing team", "handle": "marketing-team"},
        "intent_type": "group_creation"
    },
    {
        "query": "Search Slack for any messages containing the phrase 'API outage' from the last week.",
        "expected_server": "slack",
        "expected_tool": "search_messages",
        "expected_parameters": {"query": "API outage"},
        "intent_type": "global_search"
    },
    {
        "query": "Find the Slack ID for the user with the email john.doe@company.com.",
        "expected_server": "slack",
        "expected_tool": "get_user_by_email",
        "expected_parameters": {"email": "john.doe@company.com"},
        "intent_type": "user_lookup"
    },
    {
        "query": "Fetch the last 20 messages from the #design channel to catch me up.",
        "expected_server": "slack",
        "expected_tool": "get_channel_history",
        "expected_parameters": {"channel": "#design", "limit": 20},
        "intent_type": "context_reading"
    },
    {
        "query": "Invite user U123456 to the #project-alpha channel.",
        "expected_server": "slack",
        "expected_tool": "invite_to_channel",
        "expected_parameters": {"channel": "#project-alpha", "users": "U123456"},
        "intent_type": "channel_admin"
    },

    # ==========================================
    # 4. GITHUB SERVER EVALUATIONS
    # ==========================================
    {
        "query": "Create a new private repository called 'internal-tools' with an initialized README.",
        "expected_server": "github",
        "expected_tool": "create_repository",
        "expected_parameters": {"name": "internal-tools", "private": True, "auto_init": True},
        "intent_type": "repo_creation"
    },
    {
        "query": "Open a PR from the 'feature-auth' branch into 'main' titled 'Add SSO Login'.",
        "expected_server": "github",
        "expected_tool": "create_pull_request",
        "expected_parameters": {"head": "feature-auth", "base": "main", "title": "Add SSO Login"},
        "intent_type": "pr_creation"
    },
    {
        "query": "Squash and merge pull request #42 in the facebook/react repository.",
        "expected_server": "github",
        "expected_tool": "merge_pull_request",
        "expected_parameters": {"owner": "facebook", "repo": "react", "pull_number": 42, "merge_method": "squash"},
        "intent_type": "pr_merge"
    },
    {
        "query": "Show me all open issues in the tensorflow/tensorflow repo that have the 'bug' label.",
        "expected_server": "github",
        "expected_tool": "list_issues",
        "expected_parameters": {"owner": "tensorflow", "repo": "tensorflow", "state": "open", "labels": "bug"},
        "intent_type": "issue_tracking"
    },
    {
        "query": "Add a comment saying 'Fix looks good to me' on issue #105 in my-org/my-repo.",
        "expected_server": "github",
        "expected_tool": "create_issue_comment",
        "expected_parameters": {"owner": "my-org", "repo": "my-repo", "issue_number": 105, "body": "Fix looks good to me"},
        "intent_type": "issue_comment"
    },
    {
        "query": "Get the contents of the package.json file from the 'v2-beta' branch of vercel/next.js.",
        "expected_server": "github",
        "expected_tool": "get_file_content",
        "expected_parameters": {"owner": "vercel", "repo": "next.js", "path": "package.json", "ref": "v2-beta"},
        "intent_type": "file_read"
    },
    {
        "query": "What are the diffs between the 'staging' and 'production' branches in the backend repo?",
        "expected_server": "github",
        "expected_tool": "compare_commits",
        "expected_parameters": {"repo": "backend", "base": "production", "head": "staging"},
        "intent_type": "diff_analysis"
    },
    {
        "query": "Search for Python repositories that mention 'machine learning' and have more than 1000 stars.",
        "expected_server": "github",
        "expected_tool": "search_repositories",
        "expected_parameters": {"query": "machine learning language:python stars:>1000"},
        "intent_type": "repo_search"
    },
    {
        "query": "Delete the 'hotfix-1.2' branch from the ui-components repository.",
        "expected_server": "github",
        "expected_tool": "delete_branch",
        "expected_parameters": {"repo": "ui-components", "ref": "heads/hotfix-1.2"},
        "intent_type": "branch_deletion"
    },
    {
        "query": "Lock issue #99 in the public API repo because the conversation is getting too heated.",
        "expected_server": "github",
        "expected_tool": "lock_issue",
        "expected_parameters": {"repo": "public-api", "issue_number": 99, "lock_reason": "too heated"},
        "intent_type": "issue_moderation"
    },

    # ==========================================
    # 5. TIME/WEATHER SERVER EVALUATIONS
    # ==========================================
    {
        "query": "What's the weather like right now in Tokyo in Celsius?",
        "expected_server": "time_weather",
        "expected_tool": "get_current_weather",
        "expected_parameters": {"location": "Tokyo", "units": "metric"},
        "intent_type": "current_weather"
    },
    {
        "query": "Will it rain in London at any point over the next 5 days?",
        "expected_server": "time_weather",
        "expected_tool": "get_weather_forecast",
        "expected_parameters": {"location": "London", "days": 5},
        "intent_type": "weather_forecast"
    },
    {
        "query": "Convert '2023-10-15 14:00:00' from America/New_York to Europe/Berlin time.",
        "expected_server": "time_weather",
        "expected_tool": "convert_timezone",
        "expected_parameters": {"time": "2023-10-15 14:00:00", "source_timezone": "America/New_York", "target_timezone": "Europe/Berlin"},
        "intent_type": "timezone_conversion"
    },
    {
        "query": "What is the exact current time in Sydney right now?",
        "expected_server": "time_weather",
        "expected_tool": "get_current_time",
        "expected_parameters": {"timezone": "Australia/Sydney"},
        "intent_type": "current_time"
    },
    {
        "query": "Check the PM2.5 and overall Air Quality Index for Los Angeles.",
        "expected_server": "time_weather",
        "expected_tool": "get_air_quality",
        "expected_parameters": {"location": "Los Angeles"},
        "intent_type": "air_quality"
    },
    {
        "query": "What time will the sun set in Paris today?",
        "expected_server": "time_weather",
        "expected_tool": "get_sunrise_sunset",
        "expected_parameters": {"lat": 48.8566, "lon": 2.3522}, # Can also check if model extracts coords first
        "intent_type": "astronomical_data"
    },
    {
        "query": "Get the exact latitude and longitude coordinates for '1600 Pennsylvania Avenue NW, Washington, DC'.",
        "expected_server": "time_weather",
        "expected_tool": "search_location_coordinates",
        "expected_parameters": {"query": "1600 Pennsylvania Avenue NW, Washington, DC"},
        "intent_type": "geocoding"
    },
    {
        "query": "Are there any active tornado watches or severe weather alerts for Miami, Florida?",
        "expected_server": "time_weather",
        "expected_tool": "get_weather_alerts",
        "expected_parameters": {"location": "Miami, Florida"},
        "intent_type": "weather_warnings"
    },
    {
        "query": "How hot did it get in Phoenix on July 4th, 2020?",
        "expected_server": "time_weather",
        "expected_tool": "get_historical_weather",
        "expected_parameters": {"location": "Phoenix", "date": "2020-07-04"},
        "intent_type": "historical_weather"
    },
    {
        "query": "Does the 'America/Phoenix' timezone observe Daylight Saving Time?",
        "expected_server": "time_weather",
        "expected_tool": "get_timezone_info",
        "expected_parameters": {"timezone": "America/Phoenix"},
        "intent_type": "timezone_metadata"
    }
]