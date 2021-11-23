import pandas as pd

class Library:
    data=pd.DataFrame()
    
    def add_book(self, name:str, author: str, year: int, genre: str):
        data_dictionary={"Name":name, "Author": author, "Year": year, "Genre": genre}
        self.data=self.data.append(data_dictionary, ignore_index=True)
        print(self.data)
    def delete_book(self, book_id: int):
        if len(self.data) == 0:
            print("No books in the library")
        else:
            self.data=self.data.drop(book_id)
            print(self.data)

    def find_book(self, book_id: int):
        all_indexes = self.data.head()
        for i in all_indexes.index:
            if all_indexes.index[i] == book_id:
                print(pd.DataFrame(self.data.iloc[book_id]))
l=Library()
print("Add a first book:")
l.add_book("Faust","Johann Wolfgang Goethe", 1831,"dramatic poem")

print("Add a second book:")
l.add_book("Divine Comedy","Dante Alegueri",1310 ,"philosophy poem") 

print("Delete the book number 0:")
l.delete_book(0)

print("Find the book number  1:")
l.find_book(1)
