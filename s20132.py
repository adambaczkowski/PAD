import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Wczytanie danych z pliku CSV
data = pd.read_csv('googleplaystore.csv')

# Analiza zależności między Rating a kategorią aplikacji
st.subheader('Rating w zależności od kategorii')
fig1, ax1 = plt.subplots(figsize=(12, 8))
sns.barplot(x='Rating', y='Category', data=data, ax=ax1)
plt.title('Rating w zależności od kategorii')
st.pyplot(fig1)
plt.close()

# Zależność między liczbą recenzji a oceną aplikacji
st.subheader('Zależność między liczbą recenzji a oceną aplikacji')
data['Reviews'] = data['Reviews'].astype(str).str.replace(',', '')
data['Reviews'] = data['Reviews'].astype(int)
fig2, ax2 = plt.subplots(figsize=(12, 8))
sns.scatterplot(x='Reviews', y='Rating', data=data, ax=ax2)
plt.title('Zależność między liczbą recenzji a oceną aplikacji')
plt.xlabel('Liczba recenzji')
plt.ylabel('Ocena')
plt.xscale('log')
st.pyplot(fig2)
plt.close()

# Zależność między rozmiarem aplikacji a oceną aplikacji
st.subheader('Zależność między rozmiarem aplikacji a oceną aplikacji')
data['Size'] = data['Size'].str.replace('M', '').str.replace('k', '')
data['Size'] = data['Size'].replace('Varies with device', float('NaN')).astype(float)
fig3, ax3 = plt.subplots(figsize=(12, 8))
sns.scatterplot(x='Size', y='Rating', data=data, ax=ax3)
plt.title('Zależność między rozmiarem aplikacji a oceną aplikacji')
plt.xlabel('Rozmiar aplikacji (w megabajtach)')
plt.ylabel('Ocena aplikacji')
st.pyplot(fig3)
plt.close()

# Zależność między liczbą pobrań a oceną aplikacji
st.subheader('Zależność między liczbą pobrań a oceną aplikacji')
data['Installs'] = data['Installs'].str.replace('+', '').str.replace(',', '')
data['Installs'] = data['Installs'].astype(int)
fig4, ax4 = plt.subplots(figsize=(12, 8))
sns.scatterplot(x='Installs', y='Rating', data=data, ax=ax4)
plt.title('Zależność między liczbą pobrań a oceną aplikacji')
plt.xlabel('Liczba pobrań')
plt.ylabel('Ocena aplikacji')
plt.xscale('log')
st.pyplot(fig4)
plt.close()

# Średnia ocena aplikacji w zależności od typu
st.subheader('Średnia ocena aplikacji w zależności od typu')
rating_by_type = data.groupby('Type')['Rating'].mean().reset_index()
fig5, ax5 = plt.subplots(figsize=(12, 8))
sns.barplot(x='Type', y='Rating', data=rating_by_type, ax=ax5)
plt.title('Średnia ocena aplikacji w zależności od typu')
st.pyplot(fig5)
plt.close()

# Średnia ocena aplikacji w zależności od ceny
st.subheader('Średnia ocena aplikacji w zależności od ceny')
data['Price'] = data['Price'].apply(lambda x: float(x.strip('$')) if x != '0' else 0)
avg_rating_by_price = data.groupby('Price')['Rating'].mean()
fig6, ax6 = plt.subplots(figsize=(20, 12))
avg_rating_by_price.plot(kind='bar', ax=ax6)
plt.title('Średnia ocena aplikacji w zależności od ceny')
plt.xlabel('Cena (w dolarach)')
plt.ylabel('Średnia ocena')
plt.xticks(rotation=90)
st.pyplot(fig6)
plt.close()

# Zależność między Content Rating a oceną aplikacji
st.subheader('Zależność między Content Rating a oceną aplikacji')
content_rating_categories = ['Everyone', 'Everyone 10+', 'Teen', 'Mature 17+', 'Adults only 18+']
filtered_data = data[data['Content Rating'].isin(content_rating_categories)]
rating_means = filtered_data.groupby('Content Rating')['Rating'].mean().reset_index()
fig7, ax7 = plt.subplots(figsize=(12, 12))
ax7.bar(rating_means['Content Rating'], rating_means['Rating'])
plt.title('Zależność między Content Rating a oceną aplikacji')
plt.xlabel('Content Rating')
plt.ylabel('Średnia ocena aplikacji')
st.pyplot(fig7)
plt.close()

# Zależność między Genres a oceną aplikacji
st.subheader('Zależność między Genres a oceną aplikacji')
data_cleaned = data.dropna(subset=['Rating'])
fig8, ax8 = plt.subplots(figsize=(30, 30))
sns.barplot(x='Rating', y='Genres', data=data_cleaned, ax=ax8)
plt.title('Zależność między Genres a oceną aplikacji')
plt.xlabel('Genres')
plt.ylabel('Ocena aplikacji')
plt.xticks(rotation=90)
st.pyplot(fig8)
plt.close()

# Zależność między Last Updated a oceną aplikacji
st.subheader('Zależność między Last Updated a oceną aplikacji')
data['Last Updated'] = pd.to_datetime(data['Last Updated'], format='%B %d, %Y')
fig9, ax9 = plt.subplots(figsize=(12, 12))
plt.scatter(data['Last Updated'], data['Rating'], alpha=0.5)
plt.title('Zależność między Last Updated a oceną aplikacji')
plt.xlabel('Last Updated')
plt.ylabel('Ocena aplikacji')
plt.xticks(rotation=45)
st.pyplot(fig9)
plt.close()

# Zależność między Android Ver a oceną aplikacji
st.subheader('Zależność między Android Ver a oceną aplikacji')
rating_by_androidver = data.groupby('Android Ver')['Rating'].mean().reset_index()
rating_by_androidver = rating_by_androidver.sort_values('Rating', ascending=False)
fig10, ax10 = plt.subplots(figsize=(12, 8))
sns.barplot(x='Rating', y='Android Ver', data=rating_by_androidver, ax=ax10)
plt.title('Zależność między Android Ver a oceną aplikacji')
plt.xlabel('Ocena aplikacji')
plt.ylabel('Android Ver')
st.pyplot(fig10)
plt.close()
