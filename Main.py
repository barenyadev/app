import numpy as np
import pandas as pd
import streamlit as st

def main():
  st.title("Finding largest number")
  n1=st.number_input("1st number")
  n2=st.number_input("2nd number")
  n3=st.number_input("3rd number")
  
  if(n1 > n2 and n3):
    r=n1
  if(n2>n1 and n3):
    r=n2
  else:
    r=n3
  st.success('the output is {}'.format(r))
