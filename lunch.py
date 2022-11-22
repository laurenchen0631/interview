import base64
import msgpack
from datetime import datetime

with open('lunch.log', 'rb') as f:
    for l in f:
        b = base64.b64decode(l)
        msg = msgpack.unpackb(b)
        address = []
        for part in msg["ipAddress"]:
            address.append(str(int(part)))
        msg["ipAddress"] = ".".join(address)
        msg["date"] = datetime.fromtimestamp(msg["date"]).strftime('%Y-%m-%d %H:%M:%S')
