import streamlit as st

from servicehelper import get_premium

st.title('Calculate Your Premium')


def get_label_for_option(inp):
    if inp == 0:
        return 'No Surgery'
    elif inp == 1:
        return 'One Surgery'
    elif inp == 2:
        return 'Two Surgery'
    else:
        return 'Three or More Surgery'


with st.container():
    col1, col2 = st.columns(2, gap='large')
    with col1:
        st.subheader('Enter Basic Details')
        age = st.number_input('Age', 18)
        height = st.number_input('Height', 130)
        weight = st.number_input('Weight', 50)
    with col2:
        st.subheader('Enter details related to Health Issues')
        is_diabetic = st.toggle('Are you Diabetic?')
        is_bp = st.toggle('Do you have blood pressure issues?')
        is_transplant = st.toggle('Have you gone through any transplants?')
        is_chronic = st.toggle('Do you have any chronic illness?')
        is_allergy = st.toggle('Do you have any allergies?')
        is_cancer = st.toggle('Do you have any history of cancer in your family?')
        surgeries = st.selectbox('How many major surgeries did you have?', options=[0, 1, 2, 3],
                                 format_func=get_label_for_option)
st.markdown('##')
with st.container():
    col11, col12 = st.columns(2, gap='large')
    premium = 0
    with col11:
        if st.button('Get premium'):
            premium = get_premium(age, height, weight, is_diabetic,
                                  is_bp, is_transplant,
                                  is_chronic, is_allergy, is_cancer, surgeries)

    with col12:
        st.write(f'Your premium is Rs {premium}')
