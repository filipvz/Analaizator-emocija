import pandas as pd
import streamlit as st
from textblob import TextBlob
from deep_translator import GoogleTranslator

def set_background(url):
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("{url}");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Pozovi funkciju s linkom na sliku (mora biti direktan link na .jpg ili .png)
set_background('https://github.com/filipvz/Analaizator-emocija/blob/2b9681d3e6dd4179cb005611d53bb3b83ff15509/assets/Gemini_Generated_Image_vw0hr7vw0hr7vw0h.png')

st.set_page_config(page_title="Analizator teksta")

st.title("Analizator Emocija by Filip (20% Digital)")
st.subheader("Otkrij sentiment svog teksta na hrvatskom jeziku")

col1,col2=st.columns(2)

#Polje za unos teksta

with col1:
    st.info("Ovdje upišite ili copy/paste teksta: ")
    korisnik=st.text_area("Unos teksta", height=150)

#Logika aplikacije

if st.button("Analiziraj unešeni tekst"):
    if korisnik:
        with st.spinner("Analiziram..."):
            try:
                translator=GoogleTranslator(source="auto",target="en")
                prevedeni_tekst=translator.translate(korisnik)

                
                blob=TextBlob(prevedeni_tekst)
                rezultat=blob.sentiment.polarity

                with col2:
                    st.info("Rezultat analize: ")
                    if rezultat>0:
                        st.markdown("Pozitivno!!!!!!")
                        st.success(f"Ocjena: {round(rezultat,2)}")
                    elif rezultat<0:
                        st.markdown("Negativno!!!!!")
                        st.error(f"Ocjena: {round(rezultat,2)}")
                    else:
                        st.markdown("Neutralno!!!!!!!")
                        st.warning(f"Ocjena: {round(rezultat,2)}")
                    st.markdown("---------")
                    subjectivity=blob.sentiment.subjectivity
                    st.write("Analiza objektivnosti: ")

                    if subjectivity>0.5:
                            st.info(f"Ovo zvuči kao osobno mišljenje (Subjektivnost: {round(subjectivity,2)})")
                    else:
                            st.success(f"Ovo zvuči kao objektivna činjenica (Subjektivnost: {round(subjectivity,2)})")
                    st.markdown("----------")
                    st.write("Vizualni prikaz: ")
                    
                    tablica=pd.DataFrame(
                         {
                              "Vrijednost":[rezultat,subjectivity]
                         },
                         index=["Emocija (Polarity)","Subjektivnost"]

                    )
                    #graf
                    st.bar_chart(tablica)



            except Exception as e:
                st.error(f" Došlo je do greške u prijevodu: {e}")


    else:
        st.warning("Upišite neki tekst")






