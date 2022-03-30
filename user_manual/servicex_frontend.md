(ch-controlling-sx)=

# Working in a group

- the query cache yaml file that one can use for everyone.
- What to check into a repo what not to check into a repo

# Controlling ServiceX

Advanced configuration options and usage of `servicex`.

* You have to restart the engine once the first call has been made to `servicex` - servicex.yaml is loaded only once.
* details about how the cache works and how to clear it, etc.

## Caching

## Logging

The ServiceX libraries use the standard python logging libraries. If you want to see what is going on sometimes the first thing to do is turn
on logging. In this example we check to see what the `func_adl` is that is being sent back to `servicex`.

(sec-async)=
## Async Interface
