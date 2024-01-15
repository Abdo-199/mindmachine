import os
from pathlib import Path
import secrets
import base64

# Path to the .env file
env_path = Path('.env')

# Check if the .env file already exists
if not env_path.is_file():
    # Generate a 256-bit (32 bytes) random key
    secret_key = secrets.token_bytes(32)
    # Encode the key in base64
    encoded_key = base64.b64encode(secret_key).decode()

    # Write the .env file
    with env_path.open('w') as env_file:
        env_file.write(f'JWT_SECRET_KEY={encoded_key}\n')
        # Add other necessary environment variables here
        # env_file.write('ANOTHER_VARIABLE=value\n')
