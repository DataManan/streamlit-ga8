import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")
    st.subheader("I am Manan Jain, 22f1001259, and this is my week 8 graded assignment")
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")
    
    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.write(f"The largest number is: {largest}")

main()
