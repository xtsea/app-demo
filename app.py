import asyncio
import requests
import json
import time
from akenoai.streamlit import StreamlitToJs as js

class GithubUsername:
    def __init__(self, username):
        self.username = username

    def get_github_data(self):
        req = requests.get(f"https://api.github.com/users/{self.username}").json()
        try:
            return req
        except Exception as e:
            base_msg = f"**Error!** \n\n**Traceback:** \n `{e}` \n\n`Make sure that you've sent the command with the correct username!`"
            return base_msg

js_st = js.stl()
js_st.title("Welcome to akenoai-lib APP")
js_st.write("Developed by RandyDev")
js_st.write("GitHub User Information")

with js_st.form("github"):
    username = js_st.text_input("Enter GitHub username:")
    submit_checkbox = js_st.checkbox("allow users", value=False)
    submitted = js_st.form_submit_button("Submit")
    if submitted and submit_checkbox:
        js_st.spinner("Fetching GitHub data...")
        github_data = GithubUsername(username).get_github_data()
        if isinstance(github_data, dict):
            js_st.json(github_data)
        else:
            js_st.error(github_data)

js_st.title("Examples JSON by AkenoX API")

with js_st.form("json"):
    submitted = js_st.form_submit_button("Submit")
    if submitted:
        js_st.spinner("Loading......")
        try:
            js_st.json(
                js.no_async_randydev("json/all", is_obj=False)
            )
        except Exception as e:
            js_st.error(str(e))

js_st.title("ChatGPT AI")

with js_st.form("openai"):
    text = js_st.text_area('Enter text:', 'How to JavaScript code?')
    submitted = js_st.form_submit_button('Submit')
    placeholder = js_st.empty()
    free_api_key_on = js_st.toggle("Free Api Key")
    if submitted:
        try:
            if free_api_key_on:
                with placeholder, js_st.spinner("Processing......"):
                    time.sleep(5)
                js_st.write(
                    js.no_async_randydev("ai/openai/gpt-old", is_obj=True, query=text).results
                )
                js_st.success("Join Channel telegram : @RendyProjects")
            else:
                js_st.warning('Use button Free API Key', icon="⚠️")
        except Exception as e:
            js_st.error(str(e))
                            
js.hide_streamlit_watermark(unsafe_allow_html=True)
