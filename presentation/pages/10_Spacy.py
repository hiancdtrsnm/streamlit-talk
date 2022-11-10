from spacy_streamlit.util import LOGO, load_model
from spacy_streamlit import visualize_parser, visualize_ner, process_text, visualize_tokens
import streamlit as st

NER_ATTRS = ["text", "label_", "start", "end", "start_char", "end_char"]
TOKEN_ATTRS = ["idx", "text", "lemma_", "pos_", "tag_", "dep_", "head", "morph",
               "ent_type_", "ent_iob_", "shape_", "is_alpha", "is_ascii",
               "is_digit", "is_punct", "like_num", "is_sent_start"]

models = ["es_core_news_sm", "es_core_news_md"]
default_text = "Sundar Pichai es el CEO de Google."
spacy_model = "es_core_news_md"

st.markdown(LOGO, unsafe_allow_html=True)

model_load_state = st.info(f"Loading model '{spacy_model}'...")
nlp = load_model(spacy_model)
model_load_state.empty()

text = st.text_area("Texto a Analizar", default_text, key=f"visualize_text")

text

doc = process_text(spacy_model, text)

visualize_parser(doc, title="Parser de Despendencias", key="visualize_parser")
visualize_ner(doc, title="Entidades Nombradas", attrs=NER_ATTRS, key="visualize_ner")
visualize_tokens(doc, title="Tokens", attrs=TOKEN_ATTRS, key="visualize_tokens")

st.header("Información del Pipeline")
json_doc_exp = st.expander("JSON Doc")
json_doc_exp.json(doc.to_json())

meta_exp = st.expander("Pipeline meta.json")
meta_exp.json(nlp.meta)

config_exp = st.expander("Pipeline config.cfg")
config_exp.code(nlp.config.to_str())

if st.checkbox("Mostrar código"):
    st.code("""
from spacy_streamlit.util import LOGO, load_model
from spacy_streamlit import visualize_parser, visualize_ner, process_text, visualize_tokens
import streamlit as st

NER_ATTRS = ["text", "label_", "start", "end", "start_char", "end_char"]
TOKEN_ATTRS = ["idx", "text", "lemma_", "pos_", "tag_", "dep_", "head", "morph",
               "ent_type_", "ent_iob_", "shape_", "is_alpha", "is_ascii",
               "is_digit", "is_punct", "like_num", "is_sent_start"]

models = ["es_core_news_sm", "es_core_news_md"]
default_text = "Sundar Pichai es el CEO de Google."
spacy_model = "es_core_news_md"

st.markdown(LOGO, unsafe_allow_html=True)

model_load_state = st.info(f"Loading model '{spacy_model}'...")
nlp = load_model(spacy_model)
model_load_state.empty()

text = st.text_area("Texto a Analizar", default_text, key=f"visualize_text")

text

doc = process_text(spacy_model, text)

visualize_parser(doc, title="Parser de Despendencias", key="visualize_parser")
visualize_ner(doc, title="Entidades Nombradas", attrs=NER_ATTRS, key="visualize_ner")
visualize_tokens(doc, title="Tokens", attrs=TOKEN_ATTRS, key="visualize_tokens")

st.header("Información del Pipeline")
json_doc_exp = st.expander("JSON Doc")
json_doc_exp.json(doc.to_json())

meta_exp = st.expander("Pipeline meta.json")
meta_exp.json(nlp.meta)

config_exp = st.expander("Pipeline config.cfg")
config_exp.code(nlp.config.to_str())

""")