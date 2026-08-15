# StrBcrypt
A Wrapper for the bcrypt python library that acts as a lazy shortcut
for fastapi and other applications that need to hash password and
verify them.

## Why
- the python bcrypt developers do not have any intrest in adding lazy 
    string support so I went ahead and did it with very minimal time
    spent.

- Too many users wind up using bcrypt with in their favorite
    server wrappers together. Most post requests wind up using
    passwords in string format. This libary attempts to eliminate a problem
    with needing to encode absolutely everything under the sun keeping
    your code nice and clean. You can inject StrBcrypt as a dependency
    in your litestar projects as well as fastapi very easily.





## Installation
```
pip install strbcrypt
```


## Using StrBcrypt

To utilize it is written in an object oriented format to make up for the different
settings a user may wind up utilitizing.

```python
from strbcrypt import StrBcrypt

utf8_bcrypt = StrBcrypt("utf-8", errors="surrogateescape", rounds=11)


def main():
    pwd = "password"

    bcrypt_hash = utf8_bcrypt.hashpw(pwd)

    if utf8_bcrypt.checkpw(pwd, bcrypt_hash):
        print("success")
    else:
        print("WRONG!")


if __name__ == "__main__":
    main()
```


## Going Async
This library also provides an asynchronous wrapper if that in any way is important
to you.

```
pip install strbcrypt[anyio]
```

```python
import anyio

from strbcrypt.anyio import AsyncStrBcrypt

utf8_bcrypt = AsyncStrBcrypt("utf-8", errors="surrogateescape", rounds=11)


async def main():
    pwd = "password"

    bcrypt_hash = await utf8_bcrypt.hashpw(pwd)

    if await utf8_bcrypt.checkpw(pwd, bcrypt_hash):
        print("success")
    else:
        print("WRONG!")


if __name__ == "__main__":
    anyio.run(main)
```



