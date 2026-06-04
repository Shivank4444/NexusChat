import streamlit as st
from langchain_core.messages import HumanMessage,AIMessage,ToolMessage
import json


class DisplayResultStreamlit:
    def __init__(self,usecase,graph,user_message):
        self.usecase= usecase
        self.graph = graph
        self.user_message = user_message

    def _render_history(self):
        """Render all previous turns from session state above the current input."""
        for entry in st.session_state.chat_history:
            with st.chat_message("user"):
                st.write(entry["user"])
            with st.chat_message("assistant"):
                st.write(entry["assistant"])

    def display_result_on_ui(self):
        usecase= self.usecase
        graph = self.graph
        user_message = self.user_message
        print(user_message)
        if usecase =="Basic Chatbot":
            # --- render all previous turns ---
            self._render_history()

            # Build full message list: history + new user message
            history_messages = []
            for entry in st.session_state.chat_history:
                history_messages.append(HumanMessage(content=entry["user"]))
                history_messages.append(AIMessage(content=entry["assistant"]))
            history_messages.append(HumanMessage(content=user_message))

            # Stream the graph with full history so the LLM has memory
            ai_response = ""
            for event in graph.stream({'messages': history_messages}):
                print(event.values())
                for value in event.values():
                    ai_response = value["messages"].content
                    print(value['messages'])

            # Render the current turn
            with st.chat_message("user"):
                st.write(user_message)
            with st.chat_message("assistant"):
                st.write(ai_response)

            # Persist to session state
            st.session_state.chat_history.append({
                "user": user_message,
                "assistant": ai_response,
            })
                

        elif usecase=="Chatbot With Web":
            # --- render all previous turns ---
            self._render_history()

            # Build full message list: history + new user message
            history_messages = []
            for entry in st.session_state.chat_history:
                history_messages.append(HumanMessage(content=entry["user"]))
                history_messages.append(AIMessage(content=entry["assistant"]))
            history_messages.append(HumanMessage(content=user_message))

            res = graph.invoke({"messages": history_messages})

            # Render the current turn (only new messages, not the history we injected)
            ai_response = ""
            with st.chat_message("user"):
                st.write(user_message)
            for message in res["messages"]:
                if isinstance(message, ToolMessage):
                    with st.chat_message("ai"):
                        st.write("🔧 Tool Call")
                        st.write(message.content)
                elif isinstance(message, AIMessage) and message.content:
                    ai_response = message.content
                    with st.chat_message("assistant"):
                        st.write(message.content)

            # Persist to session state (store only the final AI text)
            if ai_response:
                st.session_state.chat_history.append({
                    "user": user_message,
                    "assistant": ai_response,
                })
                        