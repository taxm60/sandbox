from fastapi import FastAPI
app = FastAPI()

books = [
    {
        "id": 1,
        "name": "The Book Name",
        "isbn": "abcd-1234",
        "_type": "Fiction",
        "publish": "2023-10-20",
        "price": 120,
    },
    {
        "id": 2,
        "name": "The Great Adventure",
        "isbn": "efgh-5678",
        "_type": "Adventure",
        "publish": "2022-05-15",
        "price": 250
    },
    {
        "id": 3,
        "name": "Coding Masterclass",
        "isbn": "ijkl-9012",
        "_type": "Technology",
        "publish": "2024-01-01",
        "price": 450
    },
    {
        "id": 4,
        "name": "Mysteries of the Deep",
        "isbn": "mnop-3456",
        "_type": "Mystery",
        "publish": "2023-11-30",
        "price": 180
    },
    {
        "id": 5,
        "name": "A History of Time",
        "isbn": "qrst-7890",
        "_type": "Non-Fiction",
        "publish": "2021-08-01",
        "price": 320
    },
    {
        "id": 6,
        "name": "Galactic War",
        "isbn": "uvwx-1122",
        "_type": "Science Fiction",
        "publish": "2024-03-10",
        "price": 280
    },
    {
        "id": 7,
        "name": "The Love Letter",
        "isbn": "yzab-3344",
        "_type": "Romance",
        "publish": "2022-12-25",
        "price": 150
    },
    {
        "id": 8,
        "name": "Financial Freedom",
        "isbn": "cdef-5566",
        "_type": "Business",
        "publish": "2023-04-18",
        "price": 380
    },
    {
        "id": 9,
        "name": "Cooking Simplified",
        "isbn": "ghij-7788",
        "_type": "CookBook",
        "publish": "2024-06-05",
        "price": 220
    },
    {
        "id": 10,
        "name": "Ancient Legends",
        "isbn": "klmn-9900",
        "_type": "Fantasy",
        "publish": "2021-11-11",
        "price": 290
    },
    {
        "id": 11,
        "name": "Mindfulness Guide",
        "isbn": "opqr-0011",
        "_type": "Self-Help",
        "publish": "2023-07-07",
        "price": 199
    }
]




@app.get('/api/books')
def get_books(type_=None):
    if type_:
        return [x for x in books if x['_type']==type_]
    return(books)