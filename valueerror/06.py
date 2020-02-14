import json


nan = float("NaN")
json.dumps(nan, allow_nan=False)
