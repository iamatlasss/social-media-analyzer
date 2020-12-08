import asyncio
import functools
import inspect
import threading

from pyrogram import types
from pyrogram.methods import Methods
from pyrogram.methods.utilities import idle as idle_module


def async_to_sync(obj, name):
    function = getattr(obj, name)
    main_loop = asyncio.get_event_loop()

    async def consume_generator(coroutine):
        return [i async for i in coroutine]

    @functools.wraps(function)
    def async_to_sync_wrap(*args, **kwargs):
        coroutine = function(*args, **kwargs)

        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = main_loop

        if loop.is_running():
            if threading.current_thread() is threading.main_thread():
                return coroutine
            else:
                if inspect.iscoroutine(coroutine):
                    return asyncio.run_coroutine_threadsafe(coroutine, loop).result()

                if inspect.isasyncgen(coroutine):
                    return asyncio.run_coroutine_threadsafe(consume_generator(coroutine), loop).result()

        if inspect.iscoroutine(coroutine):
            return loop.run_until_complete(coroutine)

        if inspect.isasyncgen(coroutine):
            return loop.run_until_complete(consume_generator(coroutine))

    setattr(obj, name, async_to_sync_wrap)


def wrap(source):
    for name in dir(source):
        method = getattr(source, name)

        if not name.startswith("_"):
            if inspect.iscoroutinefunction(method) or inspect.isasyncgenfunction(method):
                async_to_sync(source, name)


# Wrap all Client's relevant methods
wrap(Methods)

# Wrap types' bound methods
for class_name in dir(types):
    cls = getattr(types, class_name)

    if inspect.isclass(cls):
        wrap(cls)

# Special case for idle, because it's not inside Methods
async_to_sync(idle_module, "idle")
idle = getattr(idle_module, "idle")