import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
import re
from spellchecker import SpellChecker

# Sayfa Ayarları
st.set_page_config(page_title="Advanced NLP Grader", layout="wide")
st.title("🚀 Advanced English Proficiency & Spell Checker")

# 1. Modeli ve Yazım Denetleyiciyi Yükle
@st.cache_resource
def load_tools():
    model = joblib.load('feedback_prize_model.pkl')
    spell = SpellChecker() # Varsayılan: İngilizce
    return model, spell

model, spell = load_tools()

def basit_temizleme(text):
    text = text.replace('\n', ' ')
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# 2. Kullanıcı Arayüzü
text_input = st.text_area("Analiz edilecek metni buraya girin:", height=250)

col_btn1, col_btn2 = st.columns(2)

if col_btn1.button("📊 Puanla ve Analiz Et"):
    if text_input:
        # Puanlama İşlemi
        cleaned = basit_temizleme(text_input)
        prediction = model.predict([cleaned])[0]
        target_cols = ['Cohesion', 'Syntax', 'Vocabulary', 'Phraseology', 'Grammar', 'Conventions']
        
        # Sonuçları Göster
        st.subheader("📈 Performans Analizi")
        res_df = pd.DataFrame({'Kriter': target_cols, 'Puan': prediction})
        
        c1, c2 = st.columns([1, 2])
        with c1:
            for i, row in res_df.iterrows():
                st.metric(row['Kriter'], f"{row['Puan']:.2f}/5.0")
        with c2:
            fig = px.bar(res_df, x='Kriter', y='Puan', color='Puan', range_y=[0, 5],
                         color_continuous_scale='RdYlGn', title="Kriter Bazlı Başarı")
            st.plotly_chart(fig, use_container_width=True)
            
    else:
        st.warning("Lütfen bir metin girin.")

if col_btn2.button("🔍 Yazım Hatalarını Bul"):
    if text_input:
        # Yazım Denetimi (Öneri yapmadan sadece tespit eder)
        words = re.findall(r'\b\w+\b', text_input)
        misspelled = spell.unknown(words)
        
        if misspelled:
            st.subheader("⚠️ Yazım Hataları Tespit Edildi")
            
            # Hataları metin içinde vurgula
            highlighted = text_input
            for word in misspelled:
                # Sadece kırmızıya boyar, yanına öneri eklemez
                highlighted = re.sub(f"\\b({word})\\b", f" :red[\\1] ", highlighted, flags=re.IGNORECASE)
            
            st.markdown(highlighted)
            
            st.info("Bilgi: Kırmızı ile işaretlenen kelimelerin yazımı hatalı olabilir. Lütfen sözlükten kontrol edin.")
            
            # Hatalı kelimelerin listesi (isteğe bağlı)
            with st.expander("Hatalı Kelime Listesi"):
                st.write(", ".join(misspelled))
        else:
            st.success("Tebrikler! Yazım hatası tespit edilmedi.")