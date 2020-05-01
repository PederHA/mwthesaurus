import asyncio
from dataclasses import asdict

from mwthesaurus import MWClient


KEY = "YOUR-KEY-HERE"
client = MWClient(key=KEY)


if __name__ == "__main__":
    w1 = client.get("python")
    w2 = asyncio.run(client.aget("python"))
    assert w1 == w2
    print(w1)
    
    w_dict = [asdict(w) for w in w1]
    print(w_dict)



