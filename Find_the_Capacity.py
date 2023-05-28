s, t, b = map(int, input().split())

capacity_bytes = 2 * s * t * b * 512

capacity_kb = capacity_bytes / 1024
print(str(int(capacity_kb)) + "KB")