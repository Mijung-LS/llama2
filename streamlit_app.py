import streamlit as st
import openai
###################################################################################################
# 0. page config & title
st.set_page_config(layout="centered", page_title="GPT test ver", page_icon="⚡")
st.title("⚡ GPT test ver")
st.text("Version : GPT-4-turbo-0125-preview")
###################################################################################################

user = st.radio(
    "What's your name",
    [":rainbow[MIJUNG BANG]"],
    captions = ["전략금융|mjbang@lsholdings.com"])

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#if user == ':rainbow[Comedy]':
#    st.write('You are' + user)
#else:
#    st.write("You didn\'t select USER NAME")

def chat_with_gpt():
    openai.api_key = "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"
    with st.container():
        if "openai_model" not in st.session_state:
            st.session_state["openai_model"] = "gpt-4-0125-preview"

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                
        try:
            if prompt := st.chat_input():
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.write("**User**")
                    st.markdown(prompt)

                with st.chat_message("assistant"):
                    st.write("**GPT**")
                    message_placeholder = st.empty()
                    full_response = ""
                    for response in openai.ChatCompletion.create(
                        model=st.session_state["openai_model"],
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        stream=True,
                    ):
                        full_response += response.choices[0].delta.get("content", "")
                        message_placeholder.markdown(full_response + "▌")
                    message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
        except:
            st.info("입력하신 API KEY를 다시 확인해주세요!")
            
chat_with_gpt()
