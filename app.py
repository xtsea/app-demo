import asyncio
from akenoai import AkenoXToJs as js

js_st = js.stl()
js_st.title("Welcome to akenoai-lib APP")

js.hide_streamlit_watermark(unsafe_allow_html=True)

def run_async(func, *args):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(func(*args))

async def async_function():
    return "Hello from Async"

result = run_async(async_function)
st.write(result)
