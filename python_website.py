import streamlit as st

# Page config
st.set_page_config(page_title="My Streamlit Website", page_icon="🌐", layout="wide")

# Custom CSS Styling
st.markdown(
    """
    <style>
    body {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }

    /* Sidebar */
    .stSidebar {
        background-color: #f5f5f5;
        border-right: 2px solid #e0e0e0;
    }

    
    h1, h2, h3 {
        color: #333;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 12px;
        padding: 0.6em 1.2em;
        font-size: 16px;
        transition: 0.3s;
    }

    div.stButton > button:hover {
        background-color: #ff7b7b;
        color: #fff;
        transform: scale(1.05);
    }

    /* Text inputs and Text area */
    input, textarea {
        border: 2px solid #4a90e2;
        border-radius: 10px;
        padding: 0.5em;
    }

    /* Footer Styling */
    footer {
        visibility: hidden;
    }

    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f5f5f5;
        color: #333;
        text-align: center;
        padding: 10px;
        font-size: 16px;
        border-top: 2px solid #e0e0e0;
    }

    /* Links Styling */
    a {
        color: #ff4b4b;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
        color: #ff7b7b;
    }

    /* Form Submit Button */
    .stForm button {
        background-color: #4a90e2;
        color: white;
        border-radius: 10px;
        padding: 0.5em 1em;
        font-size: 16px;
        transition: 0.3s;
    }

    .stForm button:hover {
        background-color: #1c6cd9;
        transform: scale(1.05);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar navigation
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "📖 About", "📬 Contact"])

# Main page
if page == "🏠 Home":
    st.title("🌟 Welcome to My Streamlit Website! 🚀")
    st.markdown(
        """
        ### ⚡ Simple, Fast, and Beautiful Web App
        Streamlit makes it easy to create apps for data science and more! 🧩
        """
    )
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=400)

    if st.button("✨ Click Me!"):
        st.success("🎉 You clicked the button! 🎊")

    name = st.text_input("📝 What's your name?")
    if name:
        st.write(f"👋 Hello, {name}! Nice to meet you!")

elif page == "📖 About":
    st.title("📖 About This App")
    st.markdown(
        """
        This is a simple multi-page app built with Streamlit. 🎈
        
        - 🐍 **Built in Python**
        - 🚀 **Deployed in minutes**
        - ⚡ **Interactive and fast**
        - 🌐 **Easy to share with the world**
        """
    )
    st.balloons()  # Fun animation 🎈

elif page == "📬 Contact":
    st.title("📬 Contact Me")
    st.markdown(
        """
        📧 **Email:** rahatbano142@gmail.com  
        🐙 **GitHub:** [Rahat Bano](https://github.com/RahatBano58)  
        🧩 **LinkedIn:** [Rahat Bano](https://www.linkedin.com/in/rahat-bano-5b78b41b3/)
        """
    )
    with st.form("contact_form"):
        name = st.text_input("🧑‍💻 Your Name")
        message = st.text_area("💌 Your Message")
        submitted = st.form_submit_button("📨 Send")
        if submitted:
            st.success("🎉 Thanks for your message! I'll get back to you soon. 🚀")

# Footer
st.markdown(
    """
    <div class="footer">
        Created with ❤️ by Rahat Bano 🚀 | 🌐 Streamlit App
    </div>
    """,
    unsafe_allow_html=True
)
