import streamlit as st

st.set_page_config(page_title="Calculator",page_icon="",layout="centered")

st.sidebar.title(" Calculator")
st.sidebar.write("Basic arithmetic operations")

st.title(" Smart Calculator")
st.write("Enter two numbers and choose an operation.")

left,right=st.columns(2)
with left:
    a=st.number_input("First Number",value=0.0)
with right:
    b=st.number_input("Second Number",value=0.0)

ops={
    "Addition (+)":"+",
    "Subtraction (-)":"-",
    "Multiplication (×)":"*",
    "Division (÷)":"/"
}

operation=st.radio("Operation",list(ops.keys()),horizontal=True)

col1,col2=st.columns(2)
calc=col1.button("Calculate",use_container_width=True)
reset=col2.button("Reset",use_container_width=True)

if reset:
    st.rerun()

if calc:
    symbol=ops[operation]
    if symbol=="+":
        result=a+b
    elif symbol=="-":
        result=a-b
    elif symbol=="*":
        result=a*b
    else:
        if b==0:
            st.error("Division by zero is not allowed.")
            st.stop()
        result=a/b

    result=round(result,2)
    if result==int(result):
        result=int(result)

    st.success("Calculation Successful")
    st.info(f"{a} {symbol} {b} = {result}")
    st.metric("Result",result)

st.divider()
st.caption("Developed using Python & Streamlit")
