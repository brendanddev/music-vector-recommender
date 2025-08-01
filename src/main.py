
from config.config import Config

# Validate environment variables
try:
    Config.validate()
    print("Config validated successfully.")
except ValueError as e:
    print("Validation failed:", e)

Config._debug_print()
