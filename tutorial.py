import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','Fill Form','Download'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/cropped-Untitled_design__6_-removebg-preview-1.png')
st.title('onlie technology')
st.header('by Sandhya Tiwari')
st.text('this is a tutorial on streamlit library')
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/5848152fcef1014c0b5e4967-2.png')
if (mymenu=='Home'):
    st.markdown('<center><h1>welcome</h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=EjY2gUFVwZE')
elif(mymenu=='Fill Form'):
    with st.form('My Form'):
        name=st.text_input('enter name')
        dob=st.date_input("choose date of birth")
        marks=st.slider('choose marks')
        k=st.form_submit_button("submit form")
        if k:
            st.write('Name=',name,'DOB:',dob,'Marks:',marks)

elif(mymenu=='Download'):
    st.header("Download")
    st.download_button('Download Now','hello this is the downloaded data','onlei.txt')
            

                           
            
                           
        


