import streamlit as st

st.title("Моята библиотека")
st.write("Добре дошли в моята дигитална библиотека!")

# Инициализиране на сесията за запазване на списъка
if "books" not in st.session_state:
  st.session_state.books = [
      "Хари Потър",
      "Малкият принц",
      "Хобит",
      "1984",
      "Под игото",
  ]

# 1. Показване на всички книги
st.subheader("📖 Всички книги")
for book in st.session_state.books:
  st.write("-", book)

# 2. Добавяне на нова книга
st.subheader("Добавяне на нова книга")
new_book = st.text_input("Въведете заглавие на книга")

if st.button("Добави книга"):
  if new_book != "":
    st.session_state.books.append(new_book)
    st.success("Книгата е добавена!")
    st.rerun()
  else:
    st.warning("Моля, въведете заглавие!")

# 3. Търсене на книга
st.subheader("Търсене на книга")
search = st.text_input("Каква книга търсите?")
if st.button("Търси"):
  found = False
  for book in st.session_state.books:
    if search.lower() in book.lower():
      st.success("Намерена книга: " + book)
      found = True
  if not found:
    st.warning("Няма такава книга!")

# 4. Изтриване на книга
st.subheader("Изтриване на книга")
if len(st.session_state.books) > 0:
  selected_book = st.selectbox("Изберете книга за изтриване:", st.session_state.books)
  if st.button("Изтрий"):
    st.session_state.books.remove(selected_book)
    st.success("Книгата е изтрита!")
    st.rerun()
else:
  st.info("Библиотеката е празна!")

# 5. Сортиране по азбучен ред
st.subheader("Сортиране")
if st.button("Сортирай по азбучен ред"):
  st.session_state.books.sort()
  st.rerun()

# 6. Статистика
st.subheader("Статистика")
total = len(st.session_state.books)
st.metric("Общ брой книги", total)

# 7. Препоръчани книги (Галерия)
st.subheader("Препоръчани книги")
col1, col2, col3 = st.columns(3)
with col1:
  st.image("https://covers.openlibrary.org/b/isbn/9780747532699-M.jpg")
  st.write("Хари Потър")
with col2:
  st.image("https://covers.openlibrary.org/b/isbn/9780156012195-M.jpg")
  st.write("Малкият принц")
with col3:
  st.image("https://covers.openlibrary.org/b/isbn/9780547928227-M.jpg")
  st.write("Хобит")
