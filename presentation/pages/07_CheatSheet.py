import streamlit as st

st.title("Cheat Sheet")
st.caption("Inspirado en https://docs.streamlit.io/library/cheatsheet")


col1, col2, col3 = st.columns(3)

# Display text
with col1.expander('Texto'):
    st.code('''
st.write('Similar a print') # texto, datos, ...
st.write(['st', 'is <', 3]) # ver *
st.markdown('_Markdown_') # ver *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')
st.text('Fixed width text')
st.caption('Globos. Cientos de globos...')
st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
* optional kwarg unsafe_allow_html = True
    ''')

# Display data
with col1.expander('Datos'):
    st.code('''
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
st.json({'foo':'bar','fu':'ba'})
st.metric(label="Temp", value="273 K", delta="1.2 K")
    ''')

# Display charts
with col1.expander('Gráficos'):
    st.code('''
st.line_chart(data)
st.area_chart(data)
st.bar_chart(data)
st.pyplot(fig)
st.altair_chart(data)
st.vega_lite_chart(data)
st.plotly_chart(data)
st.bokeh_chart(data)
st.pydeck_chart(data)
st.deck_gl_chart(data)
st.graphviz_chart(data)
st.map(data)
    ''')

# Display media
with col1.expander('Imágenes, audio y videos'):
    st.code('''
st.image('my_picture.png')
st.audio('my_picture.wav')
st.video('my_picture.mp4')
    ''')

# Display interactive widgets
with col2.expander('Widgets interactivos'):
    st.code('''
st.button('Click')
st.download_button('Descargar', data)
st.checkbox('Mi opción')
st.radio('Radio', [1,2,3])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('Cargar archivo')
st.color_picker('Elige un color')
''')
    st.write('Los widgets regresan valores de python')

# Control flow
with col2.expander('Flujo de control'):
    st.code('''
st.stop()
    ''')

# Lay out your app
with col2.expander('Layout'):
    st.code('''
st.form('my_form_identifier')
st.form_submit_button('Submit to me')
st.container()
st.columns(spec)
>>> col1, col2 = st.columns(2)
>>> col1.subheader('Columna 1')
st.expander('Expander')
>>> with st.expander('Expand'):
>>>     st.write('Juicy deets')
''')
    st.write('Juntar widgets en una form:')
    st.code('''
>>> with st.form(key='my_form'):
>>> 	text_input = st.text_input(label='Ingresar nombre')
>>> 	submit_button = st.form_submit_button(label='Submit')
    ''')

# Display code
with col2.expander('Código'):
    st.code('''
st.code("#some python code")
st.echo()
>>> with st.echo():
>>>     st.write('Code will be executed and printed')
    ''')

# Display progress and status
with col3.expander('Mostrar progreso y estados'):
    st.code('''
st.progress(progress_variable_1_to_100)
st.spinner()
>>> with st.spinner(text='In progress'):
>>>     time.sleep(5)
>>>     st.success('Done')
st.balloons()
st.error('Error message')
st.warning('Warning message')
st.info('Info message')
st.success('Success message')
st.exception(e)
    ''')

# Placeholders, help, and options
with col3.expander('Placeholders, ayuda y opciones'):
    st.code('''
st.empty()
>>> my_placeholder = st.empty()
>>> my_placeholder.text('Replaced!')
st.help(pandas.DataFrame)
st.get_option(key)
st.set_option(key, value)
st.set_page_config(layout='wide')
    ''')

# Mutate data
with col3.expander('Cambiar datos'):
    st.code('''
DeltaGenerator.add_rows(data)
>>> my_table = st.table(df1)
>>> my_table.add_rows(df2)
>>> my_chart = st.line_chart(df1)
>>> my_chart.add_rows(df2)
    ''')

# Optimize performance
with col3.expander('Optimizando rendimiento'):
    st.code('''
@st.cache
>>> @st.cache
... def fetch_and_clean_data(url):
...     # Mutate data at url
...     return data
>>> # Executes d1 as first time
>>> d1 = fetch_and_clean_data(ref1)
>>> # Does not execute d1; returns cached value, d1==d2
>>> d2 = fetch_and_clean_data(ref1)
>>> # Different arg, so function d1 executes
>>> d3 = fetch_and_clean_data(ref2)
''')

