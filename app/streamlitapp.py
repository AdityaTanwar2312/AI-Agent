import streamlit as st


# Frontend of AI Agent using RAG flow using streamlit
def main():
    st.title("Chat Interface")

    message = st.text_area("Message", placeholder="Ask Something...")
    if st.button("Run Flow"):
        if not message.strip():
            st.error("Please enter a message!")
            return 1
        
        try:
            with st.spinner("Running Flow...."):
                response = run_flow(message)

            response = response["outputs"][0]["outputs"][0]["results"]["message"]["text"]
            st.markdown(response)
        except Exception as e:
            st.error(str(e))

if __name__ == "__main__":
    main()