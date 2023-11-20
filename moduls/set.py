import streamlit as st
import pandas as pd


st.set_page_config(page_title="set",layout="wide") #Сначала выставляем стиль для страницы
st.sidebar.subheader('Группировать по:') #Потом создаю боковую панель


Data_frame = pd.read_excel('C:\\Users\\kushhov\\Desktop\\test_app\\test_table.xlsx') #Оригинальная выгрузка

List_unic_link = list(Data_frame['Ссылка'].drop_duplicates()) #Список из уникальных ссылок
List_unic_otvet= list(Data_frame['Ответственный'].drop_duplicates()) #Список из уникальных ссылок
List_unic_project = list(Data_frame['Проектировщик'].drop_duplicates()) #Список из уникальных ссылок


check_col = [False]*len(List_unic_link)
Link_df = pd.DataFrame({'Ссылка':List_unic_link,'check':check_col})
check_col = [False]*len(List_unic_otvet)
otvet_df = pd.DataFrame({'Ответственный':List_unic_otvet,'check':check_col})
check_col = [False]*len(List_unic_project)
project_df = pd.DataFrame({'Проектировщик':List_unic_project,'check':check_col})


all_dis = ['Ссылка','Ответственный','Проектировщик']


with st.sidebar.expander("Cсылка"):
    edit_df_link = st.data_editor(
    Link_df,
    column_config={
        "Сгруппировать": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** widgets",
            default=None,
        )
    },
    disabled=all_dis,
    hide_index=True,
)

with st.sidebar.expander("Ответственный"):
    edit_df_otvet = st.data_editor(
    otvet_df,
    column_config={
        "Сгруппировать": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** widgets",
            default=None,
        )
    },
    disabled=all_dis,
    hide_index=True,
)

with st.sidebar.expander("Проектировщик"):
    edit_df_project = st.data_editor(
    project_df,
    column_config={
        "Сгруппировать": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** widgets",
            default=None,
        )
    },
    disabled=all_dis,
    hide_index=True,
)



#edit_df_link
#edit_df_otvet
#edit_df_project

#df = Data_frame.loc[Data_frame['Ссылка'] == '00000654212'] #- Пример вывода фрейма по условию
#df2 = Data_frame.loc[Data_frame['Ответственный'] == 'Бахтеев Павел Юрьевич'] #- Пример вывода фрейма по условию
#df = pd.concat([df,df2])
#st.dataframe(df)
#values_equipment = Data_frame[Number_Vector].values[i]

#Ищем поднятые флажки

#Списки ссылок и имён
list_link = []
list_otvet = []
list_project= []

#Немного оптимизирую процесс (Здесь много тестов)
nn = max(len(List_unic_link),len(List_unic_otvet),len(List_unic_project))

for i in range(nn):
    try:
        if edit_df_link['check'].values[i]:
            list_link.append(edit_df_link['Ссылка'].values[i])
    except:
        pass
    try:
        if edit_df_otvet['check'].values[i]:
            list_otvet.append(edit_df_otvet['Ответственный'].values[i])
    except:
        pass
    try:
        if edit_df_project['check'].values[i]:
            list_project.append(edit_df_project['Проектировщик'].values[i])
    except:
        pass


all_df = {}
all_df = pd.DataFrame(all_df) #Создаём пустой начальный df

for i in range(len(list_link)):
    temp_df = Data_frame.loc[Data_frame['Ссылка'] == list_link[i]]
    all_df = pd.concat([all_df,temp_df])

for i in range(len(list_otvet)):
    temp_df = Data_frame.loc[Data_frame['Ответственный'] == list_otvet[i]]
    all_df = pd.concat([all_df,temp_df])

for i in range(len(list_project)):
    temp_df = Data_frame.loc[Data_frame['Проектировщик'] == list_project[i]]
    all_df = pd.concat([all_df,temp_df])

st.dataframe(all_df)
