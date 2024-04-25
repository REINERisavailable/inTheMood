import streamlit as st

def page1():
    st.header("Page 1")
    st.write("You are on page 1")

def page2():
    st.header("Page 2")
    st.write("You are on page 2")

def page3():
    st.header("Page 3")
    st.write("You are on page 2")

def main():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ["Page 1", "Page 2"])

    if selection == "Page 1":
        page1()
    elif selection == "Page 2":
        page2()
    elif selection == "Page 2":
        page3()

if __name__ == "__main__":
    main()
