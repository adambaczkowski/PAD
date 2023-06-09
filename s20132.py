import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Wczytanie danych z pliku CSV
data = pd.read_csv('googleplaystore.csv')

# Analiza zależności między Rating a kategorią aplikacji

st.subheader('Zależność między Rating a oceną aplikacji')
fig1, ax1 = plt.subplots(figsize=(20, 20))
sns.barplot(x='Rating', y='Category', data=data, ax=ax1)
plt.title('Rating w zależności od kategorii')
st.pyplot(fig1)
plt.close()

avg_rating_by_category = data.groupby('Category')['Rating'].mean()
highest_avg_rating_category = avg_rating_by_category.idxmax()
highest_avg_rating = avg_rating_by_category.max()

lowest_avg_rating_category = avg_rating_by_category.idxmin()
lowest_avg_rating = avg_rating_by_category.min()
st.write('Najwyższa średnia ocena:', highest_avg_rating, ' w kategorii:', highest_avg_rating_category)
st.write('Najniższa średnia ocena:', lowest_avg_rating, ' w kategorii:', lowest_avg_rating_category)


# Zależność między liczbą recenzji a oceną aplikacji
highest_avg_reviews = data.groupby('Category')['Reviews'].mean().idxmax()
highest_avg_reviews_category = data.groupby('Category')['Reviews'].mean().max()
lowest_avg_reviews = data.groupby('Category')['Reviews'].mean().idxmin()
lowest_avg_reviews_category = data.groupby('Category')['Reviews'].mean().min()

st.subheader('Zależność między liczbą recenzji a oceną aplikacji')
data['Reviews'] = data['Reviews'].astype(str).str.replace(',', '')
data['Reviews'] = data['Reviews'].astype(int)
fig2, ax2 = plt.subplots(figsize=(20, 20))
sns.scatterplot(x='Reviews', y='Rating', data=data, ax=ax2)
plt.title('Zależność między liczbą recenzji a oceną aplikacji')
plt.xlabel('Liczba recenzji')
plt.ylabel('Ocena')
plt.xscale('log')
st.pyplot(fig2)
plt.close()

st.write('Najwyższa średnia liczba recenzji:', highest_avg_reviews_category, ' w kategorii:', highest_avg_reviews)
st.write('Najniższa średnia liczba recenzji:', lowest_avg_reviews_category, ' w kategorii:', lowest_avg_reviews)


# Zależność między rozmiarem aplikacji a oceną aplikacji
st.subheader('Zależność między rozmiarem aplikacji a oceną aplikacji')
data['Size'] = data['Size'].str.replace('M', '').str.replace('k', '')
data['Size'] = data['Size'].replace('Varies with device', float('NaN')).astype(float)
fig3, ax3 = plt.subplots(figsize=(20, 20))
sns.scatterplot(x='Size', y='Rating', data=data, ax=ax3)
plt.title('Zależność między rozmiarem aplikacji a oceną aplikacji')
plt.xlabel('Rozmiar aplikacji (w megabajtach)')
plt.ylabel('Ocena aplikacji')
st.pyplot(fig3)
plt.close()

highest_avg_rating_size = data.groupby('Size')['Rating'].mean().idxmax()
highest_avg_rating_size_value = data.groupby('Size')['Rating'].mean().max()
lowest_avg_rating_size = data.groupby('Size')['Rating'].mean().idxmin()
lowest_avg_rating_size_value = data.groupby('Size')['Rating'].mean().min()

st.write('Najwyższa średnia ocena w zależności od rozmiaru aplikacji:', highest_avg_rating_size, ' z wartością:', highest_avg_rating_size_value)
st.write('Najniższa średnia ocena w zależności od rozmiaru aplikacji:', lowest_avg_rating_size, ' z wartością:', lowest_avg_rating_size_value)


# Zależność między liczbą pobrań a oceną aplikacji
st.subheader('Zależność między liczbą pobrań a oceną aplikacji')
data['Installs'] = data['Installs'].str.replace(',', '').str.replace('+', '').astype(int)
fig4, ax4 = plt.subplots(figsize=(20, 20))
sns.scatterplot(x='Installs', y='Rating', data=data, ax=ax4)
plt.title('Zależność między liczbą pobrań a oceną aplikacji')
plt.xlabel('Liczba pobrań')
plt.ylabel('Ocena aplikacji')
plt.xscale('log')
st.pyplot(fig4)
plt.close()

highest_avg_rating_installs = data.groupby('Installs')['Rating'].mean().idxmax()
highest_avg_rating_installs_value = data.groupby('Installs')['Rating'].mean().max()
lowest_avg_rating_installs = data.groupby('Installs')['Rating'].mean().idxmin()
lowest_avg_rating_installs_value = data.groupby('Installs')['Rating'].mean().min()

st.write('Najwyższa średnia ocena w zależności od liczby pobrań:', highest_avg_rating_installs, ' z wartością:', highest_avg_rating_installs_value)
st.write('Najniższa średnia ocena w zależności od liczby pobrań:', lowest_avg_rating_installs, ' z wartością:', lowest_avg_rating_installs_value)


# Średnia ocena aplikacji w zależności od typu
rating_by_type = data.groupby('Type')['Rating'].mean().reset_index()
highest_avg_rating_type = rating_by_type['Type'].iloc[0]
highest_avg_rating_type_value = rating_by_type['Rating'].iloc[0]
lowest_avg_rating_type = rating_by_type['Type'].iloc[1]
lowest_avg_rating_type_value = rating_by_type['Rating'].iloc[1]

st.subheader('Średnia ocena aplikacji w zależności od typu')
rating_by_type = data.groupby('Type')['Rating'].mean().reset_index()
fig5, ax5 = plt.subplots(figsize=(20, 20))
sns.barplot(x='Type', y='Rating', data=rating_by_type, ax=ax5)
plt.title('Średnia ocena aplikacji w zależności od typu')
st.pyplot(fig5)
st.write(rating_by_type)
plt.close()

st.write('Najwyższa średnia ocena w typie:', highest_avg_rating_type, ' z wartością:', highest_avg_rating_type_value)
st.write('Najniższa średnia ocena w typie:', lowest_avg_rating_type, ' z wartością:', lowest_avg_rating_type_value)


# Średnia ocena aplikacji w zależności od ceny
avg_rating_by_price = data.groupby('Price')['Rating'].mean()
highest_avg_rating_price = avg_rating_by_price.idxmax()
highest_avg_rating_price_value = avg_rating_by_price.max()
lowest_avg_rating_price = avg_rating_by_price.idxmin()
lowest_avg_rating_price_value = avg_rating_by_price.min()

st.subheader('Średnia ocena aplikacji w zależności od ceny')
data['Price'] = data['Price'].apply(lambda x: float(x.strip('$')) if x != '0' else 0)
avg_rating_by_price = data.groupby('Price')['Rating'].mean()
fig6, ax6 = plt.subplots(figsize=(20, 20))
avg_rating_by_price.plot(kind='bar', ax=ax6)
plt.title('Średnia ocena aplikacji w zależności od ceny')
plt.xlabel('Cena (w dolarach)')
plt.ylabel('Średnia ocena')
plt.xticks(rotation=90)
st.pyplot(fig6)
st.write(avg_rating_by_price)
plt.close()

st.write('Najwyższa średnia ocena przy cenie:', highest_avg_rating_price, ' z wartością:', highest_avg_rating_price_value)
st.write('Najniższa średnia ocena przy cenie:', lowest_avg_rating_price, ' z wartością:', lowest_avg_rating_price_value)


# Zależność między Content Rating a oceną aplikacji
st.subheader('Zależność między Content Rating a oceną aplikacji')
content_rating_categories = ['Everyone', 'Everyone 10+', 'Teen', 'Mature 17+', 'Adults only 18+']
filtered_data = data[data['Content Rating'].isin(content_rating_categories)]
rating_means = filtered_data.groupby('Content Rating')['Rating'].mean().reset_index()
highest_avg_rating_content = rating_means['Content Rating'].iloc[0]
highest_avg_rating_content_value = rating_means['Rating'].iloc[0]
lowest_avg_rating_content = rating_means['Content Rating'].iloc[4]
lowest_avg_rating_content_value = rating_means['Rating'].iloc[4]
rating_means = filtered_data.groupby('Content Rating')['Rating'].mean().reset_index()
fig7, ax7 = plt.subplots(figsize=(20, 20))
ax7.bar(rating_means['Content Rating'], rating_means['Rating'])
plt.title('Zależność między Content Rating a oceną aplikacji')
plt.xlabel('Content Rating')
plt.ylabel('Średnia ocena aplikacji')
st.pyplot(fig7)
st.write(rating_means)
plt.close()

st.write('Najwyższa średnia ocena w Content Rating:', highest_avg_rating_content, ' z wartością:', highest_avg_rating_content_value)
st.write('Najniższa średnia ocena w Content Rating:', lowest_avg_rating_content, ' z wartością:', lowest_avg_rating_content_value)

# Zależność między Genres a oceną aplikacji
st.subheader('Zależność między Genres a oceną aplikacji')
data_cleaned = data.dropna(subset=['Rating'])
highest_avg_rating_genre = data_cleaned.groupby('Genres')['Rating'].mean().idxmax()
highest_avg_rating_genre_value = data_cleaned.groupby('Genres')['Rating'].mean().max()
lowest_avg_rating_genre = data_cleaned.groupby('Genres')['Rating'].mean().idxmin()
lowest_avg_rating_genre_value = data_cleaned.groupby('Genres')['Rating'].mean().min()
fig8, ax8 = plt.subplots(figsize=(12, 30))
sns.barplot(x='Rating', y='Genres', data=data_cleaned, ax=ax8)
plt.title('Zależność między Genres a oceną aplikacji')
plt.xlabel('Genres')
plt.ylabel('Ocena aplikacji')
plt.xticks(rotation=90)
st.pyplot(fig8)
plt.close()

st.write('Najwyższa średnia ocena w gatunku:', highest_avg_rating_genre, ' z wartością:', highest_avg_rating_genre_value)
st.write('Najniższa średnia ocena w gatunku:', lowest_avg_rating_genre, ' z wartością:', lowest_avg_rating_genre_value)

# Zależność między Last Updated a oceną aplikacji
st.subheader('Zależność między Last Updated a oceną aplikacji')
data['Last Updated'] = pd.to_datetime(data['Last Updated'], format='%B %d, %Y')
fig9, ax9 = plt.subplots(figsize=(20, 20))
plt.scatter(data['Last Updated'], data['Rating'], alpha=0.5)
plt.title('Zależność między Last Updated a oceną aplikacji')
plt.xlabel('Last Updated')
plt.ylabel('Ocena aplikacji')
plt.xticks(rotation=45)
st.pyplot(fig9)
plt.close()

highest_avg_rating_last_updated = data.groupby('Last Updated')['Rating'].mean().idxmax()
highest_avg_rating_last_updated_value = data.groupby('Last Updated')['Rating'].mean().max()
lowest_avg_rating_last_updated = data.groupby('Last Updated')['Rating'].mean().idxmin()
lowest_avg_rating_last_updated_value = data.groupby('Last Updated')['Rating'].mean().min()

st.write('Najwyższa średnia ocena w dniu aktualizacji:', highest_avg_rating_last_updated, ' z wartością:', highest_avg_rating_last_updated_value)
st.write('Najniższa średnia ocena w dniu aktualizacji:', lowest_avg_rating_last_updated, ' z wartością:', lowest_avg_rating_last_updated_value)


# Zależność między Android Ver a oceną aplikacji
st.subheader('Zależność między Android Ver a oceną aplikacji')
rating_by_androidver = data.groupby('Android Ver')['Rating'].mean().reset_index()
rating_by_androidver = rating_by_androidver.sort_values('Rating', ascending=False)

highest_avg_rating_last_updated = data.groupby('Last Updated')['Rating'].mean().idxmax()
highest_avg_rating_last_updated_value = data.groupby('Last Updated')['Rating'].mean().max()
lowest_avg_rating_last_updated = data.groupby('Last Updated')['Rating'].mean().idxmin()
lowest_avg_rating_last_updated_value = data.groupby('Last Updated')['Rating'].mean().min()

fig10, ax10 = plt.subplots(figsize=(20, 20))
sns.barplot(x='Rating', y='Android Ver', data=rating_by_androidver, ax=ax10)
plt.title('Zależność między Android Ver a oceną aplikacji')
plt.xlabel('Ocena aplikacji')
plt.ylabel('Android Ver')
st.pyplot(fig10)
st.write(rating_by_androidver)
plt.close()

st.write('Najwyższa średnia ocena w dniu aktualizacji:', highest_avg_rating_last_updated, ' z wartością:', highest_avg_rating_last_updated_value)
st.write('Najniższa średnia ocena w dniu aktualizacji:', lowest_avg_rating_last_updated, ' z wartością:', lowest_avg_rating_last_updated_value)
