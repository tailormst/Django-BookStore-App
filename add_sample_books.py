import os
import django
from datetime import date

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from books.models import Book

# Sample books data - 25 popular books
sample_books = [
    {
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'description': 'A novel about the decadence and excess of the Jazz Age, following the mysterious millionaire Jay Gatsby and his obsession with beautiful Daisy Buchanan.',
        'price': 12.99,
        'publication_date': date(1925, 4, 10),
        'isbn': '9780743273565',
    },
    {
        'title': 'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'description': 'A novel about racial injustice and moral growth in the American South during the 1930s, told through the eyes of young Scout Finch.',
        'price': 14.99,
        'publication_date': date(1960, 7, 11),
        'isbn': '9780061120084',
    },
    {
        'title': '1984',
        'author': 'George Orwell',
        'description': 'A dystopian novel set in a totalitarian society where critical thought is suppressed under a regime of surveillance and propaganda.',
        'price': 11.99,
        'publication_date': date(1949, 6, 8),
        'isbn': '9780451524935',
    },
    {
        'title': 'Pride and Prejudice',
        'author': 'Jane Austen',
        'description': 'A romantic novel about manners and marriage in early 19th-century England, focusing on the strong-willed Elizabeth Bennet and the proud Mr. Darcy.',
        'price': 9.99,
        'publication_date': date(1813, 1, 28),
        'isbn': '9780141439518',
    },
    {
        'title': 'The Hobbit',
        'author': 'J.R.R. Tolkien',
        'description': 'A fantasy novel about the adventures of Bilbo Baggins, who is swept into an epic quest to reclaim the lost Dwarf Kingdom of Erebor from the fearsome dragon Smaug.',
        'price': 15.99,
        'publication_date': date(1937, 9, 21),
        'isbn': '9780547928227',
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J.K. Rowling',
        'description': 'The first novel in the Harry Potter series, following a young wizard who discovers his magical heritage on his eleventh birthday.',
        'price': 16.99,
        'publication_date': date(1997, 6, 26),
        'isbn': '9780747532743',
    },
    {
        'title': 'The Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'description': 'An epic high-fantasy novel that follows the quest to destroy the One Ring, which was created by the Dark Lord Sauron.',
        'price': 24.99,
        'publication_date': date(1954, 7, 29),
        'isbn': '9780618640157',
    },
    {
        'title': 'The Catcher in the Rye',
        'author': 'J.D. Salinger',
        'description': 'A novel about teenage alienation and loss of innocence, narrated by the cynical Holden Caulfield.',
        'price': 10.99,
        'publication_date': date(1951, 7, 16),
        'isbn': '9780316769488',
    },
    {
        'title': 'The Alchemist',
        'author': 'Paulo Coelho',
        'description': 'A philosophical novel about a young Andalusian shepherd who dreams of finding a worldly treasure and embarks on a journey to find it.',
        'price': 13.99,
        'publication_date': date(1988, 1, 1),
        'isbn': '9780061122415',
    },
    {
        'title': 'Brave New World',
        'author': 'Aldous Huxley',
        'description': 'A dystopian novel set in a futuristic World State, inhabited by genetically modified citizens and an intelligence-based social hierarchy.',
        'price': 12.49,
        'publication_date': date(1932, 1, 1),
        'isbn': '9780060850524',
    },
    {
        'title': 'The Hunger Games',
        'author': 'Suzanne Collins',
        'description': 'A dystopian novel set in a post-apocalyptic nation where young people must participate in a televised death match called the Hunger Games.',
        'price': 14.49,
        'publication_date': date(2008, 9, 14),
        'isbn': '9780439023481',
    },
    {
        'title': 'The Da Vinci Code',
        'author': 'Dan Brown',
        'description': 'A mystery thriller novel that follows symbologist Robert Langdon as he investigates a murder in the Louvre Museum and discovers a battle between the Priory of Sion and Opus Dei.',
        'price': 15.49,
        'publication_date': date(2003, 3, 18),
        'isbn': '9780307474278',
    },
    {
        'title': 'The Kite Runner',
        'author': 'Khaled Hosseini',
        'description': 'A novel about friendship, betrayal, and redemption set against the backdrop of Afghanistan\'s tumultuous history.',
        'price': 13.99,
        'publication_date': date(2003, 5, 29),
        'isbn': '9781594631931',
    },
    {
        'title': 'Gone with the Wind',
        'author': 'Margaret Mitchell',
        'description': 'A historical novel set in Clayton County, Georgia, and Atlanta during the American Civil War and Reconstruction era.',
        'price': 18.99,
        'publication_date': date(1936, 6, 30),
        'isbn': '9781451635621',
    },
    {
        'title': 'The Fault in Our Stars',
        'author': 'John Green',
        'description': 'A novel about two teenagers with cancer who fall in love after meeting at a cancer support group.',
        'price': 12.99,
        'publication_date': date(2012, 1, 10),
        'isbn': '9780142424179',
    },
    {
        'title': 'The Shining',
        'author': 'Stephen King',
        'description': 'A horror novel about a family staying at an isolated hotel for the winter where a sinister presence influences the father into violence.',
        'price': 14.99,
        'publication_date': date(1977, 1, 28),
        'isbn': '9780307743657',
    },
    {
        'title': 'The Chronicles of Narnia',
        'author': 'C.S. Lewis',
        'description': 'A series of fantasy novels set in the fictional realm of Narnia, a place where magic exists, mythical beasts roam, and animals talk.',
        'price': 29.99,
        'publication_date': date(1950, 10, 16),
        'isbn': '9780066238500',
    },
    {
        'title': 'The Girl with the Dragon Tattoo',
        'author': 'Stieg Larsson',
        'description': 'A psychological thriller novel about a journalist and a young computer hacker investigating a wealthy family\'s dark secrets.',
        'price': 16.99,
        'publication_date': date(2005, 8, 1),
        'isbn': '9780307454546',
    },
    {
        'title': 'The Odyssey',
        'author': 'Homer',
        'description': 'An ancient Greek epic poem that follows the Greek hero Odysseus on his journey home after the fall of Troy.',
        'price': 9.99,
        'publication_date': date(1800, 1, 1),  # Approximate date
        'isbn': '9780140268867',
    },
    {
        'title': 'Crime and Punishment',
        'author': 'Fyodor Dostoevsky',
        'description': 'A novel that explores the mental anguish and moral dilemmas of Rodion Raskolnikov, an impoverished ex-student in Saint Petersburg who formulates a plan to kill an unscrupulous pawnbroker.',
        'price': 11.99,
        'publication_date': date(1866, 1, 1),
        'isbn': '9780143107637',
    },
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel García Márquez',
        'description': 'A landmark novel that tells the multi-generational story of the Buendía family, whose patriarch, José Arcadio Buendía, founded the town of Macondo.',
        'price': 14.99,
        'publication_date': date(1967, 5, 30),
        'isbn': '9780060883287',
    },
    {
        'title': 'Moby-Dick',
        'author': 'Herman Melville',
        'description': 'A novel about the voyage of the whaling ship Pequod, commanded by Captain Ahab, who seeks revenge on the white whale Moby Dick.',
        'price': 12.99,
        'publication_date': date(1851, 10, 18),
        'isbn': '9780142437247',
    },
    {
        'title': 'The Picture of Dorian Gray',
        'author': 'Oscar Wilde',
        'description': 'A philosophical novel about a man who sells his soul for eternal youth and beauty, while his portrait ages and records his sins.',
        'price': 10.99,
        'publication_date': date(1890, 7, 1),
        'isbn': '9780141439570',
    },
    {
        'title': 'Frankenstein',
        'author': 'Mary Shelley',
        'description': 'A Gothic novel about a young scientist who creates a sapient creature in an unorthodox scientific experiment.',
        'price': 11.49,
        'publication_date': date(1818, 1, 1),
        'isbn': '9780141439471',
    },
    {
        'title': 'The Grapes of Wrath',
        'author': 'John Steinbeck',
        'description': 'A novel set during the Great Depression, focusing on the Joads, a poor family of tenant farmers driven from their Oklahoma home by drought and economic hardship.',
        'price': 13.99,
        'publication_date': date(1939, 4, 14),
        'isbn': '9780143039433',
    },
]

# Add books to the database
for book_data in sample_books:
    book, created = Book.objects.get_or_create(
        isbn=book_data['isbn'],
        defaults=book_data
    )
    if created:
        print(f"Added: {book.title}")
    else:
        print(f"Already exists: {book.title}")

print(f"\nAdded {len(sample_books)} sample books to the database.")
