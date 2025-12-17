#!/usr/bin/env python3
"""
Compress faal.json using gzip and base64 encoding for client-side decompression.
"""
import json
import gzip
import base64

# Read original JSON
with open('faal.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convert to a more compact format: array of poems (index = faal number - 1)
poems = []
for i in range(1, len(data) + 1):
    poems.append(data[str(i)]['شعر'])

# Create compact JSON (array instead of object with keys)
compact_json = json.dumps(poems, ensure_ascii=False, separators=(',', ':'))

# Compress with gzip
compressed = gzip.compress(compact_json.encode('utf-8'), compresslevel=9)

# Base64 encode for embedding in JS
b64_encoded = base64.b64encode(compressed).decode('ascii')

# Write compressed data to a JS file
with open('faal-data.js', 'w', encoding='utf-8') as f:
    f.write(f'const FAAL_DATA_COMPRESSED = "{b64_encoded}";\n')

# Print stats
original_size = len(json.dumps(data, ensure_ascii=False))
compact_size = len(compact_json)
compressed_size = len(compressed)
b64_size = len(b64_encoded)

print(f"Original JSON size: {original_size:,} bytes")
print(f"Compact JSON size: {compact_size:,} bytes ({100*compact_size/original_size:.1f}%)")
print(f"Gzip compressed: {compressed_size:,} bytes ({100*compressed_size/original_size:.1f}%)")
print(f"Base64 encoded: {b64_size:,} bytes ({100*b64_size/original_size:.1f}%)")
print(f"\nSaved to faal-data.js")
