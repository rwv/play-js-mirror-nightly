import glob
import hashlib
import os.path
import base64
import json

files = glob.glob('dist/*')

sri = {}

for file in files:
    # Calculate subresource integrity

    # Read file
    with open(file, 'rb') as f:
        content = f.read()

    # Calculate sha256
    sha256 = hashlib.sha256(content).digest()
    sha256Base64 = base64.b64encode(sha256).decode('utf-8').strip()

    # Add to sri
    sri[os.path.basename(file)] = "sha256-" + sha256Base64

# read version from package.json
with open('package.json', 'r') as f:
    version = json.load(f)['version']

result = {
    "version": version,
    "sri": sri
}

print(result)

# Write SRI values to a JSON file
with open('dist/sri.json', 'w') as f:
    json.dump(result, f, indent=4)