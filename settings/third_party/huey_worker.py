from settings import DATABASES

HUEY = {
    "huey_class": "huey.PriorityRedisHuey",  # Huey's implementation to use.
    "name": DATABASES["default"]["NAME"],  # Use db name for huey.
    "results": True,  # Store return values of tasks.
    "store_none": False,  # If a task returns None, do not save to results.
    "immediate": False,  # If DEBUG=True, run synchronously.
    "utc": True,  # Use UTC for all times internally.
    "blocking": True,  # Perform blocking pop rather than poll Redis.
    "connection": {
        "host": "localhost",
        "port": 6379,
        "db": 1,
        "connection_pool": None,  # Definitely you should use pooling!
        # ... tons of other options, see redis-py for details.
        # huey-specific connection parameters.
        "read_timeout": 1,  # If not polling (blocking pop), use timeout.
        "url": None,  # Allow Redis config via a DSN.
    },
    "consumer": {
        "workers": 1,
        "worker_type": "thread",
        "initial_delay": 0.1,  # Smallest polling interval, same as -d.
        "backoff": 1.15,  # Exponential backoff using this rate, -b.
        "max_delay": 10.0,  # Max possible polling interval, -m.
        "scheduler_interval": 1,  # Check schedule every second, -s.
        "periodic": True,  # Enable crontab feature.
        "check_worker_health": True,  # Enable worker health checks.
        "health_check_interval": 1,  # Check worker health every second.
    },
}
