import os
import django
from datetime import date

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookstore.settings')
django.setup()

from books.models import Book

sample_books = [
    {
        'title': 'Artificial Intelligence: A Modern Approach',
        'author': 'Stuart Russell & Peter Norvig',
        'description': 'Comprehensive introduction to the theory and practice of artificial intelligence.',
        'price': 720,
        'publication_date': date(2020, 4, 28),
        'isbn': '9780134610993',
    },
    {
        'title': 'Machine Learning: The New AI',
        'author': 'Ethem Alpaydin',
        'description': 'Overview of machine learning, its evolution, and applications.',
        'price': 1500,
        'publication_date': date(2016, 10, 7),
        'isbn': '9780262529518',
    },
    {
        'title': 'Python Crash Course',
        'author': 'Eric Matthes',
        'description': 'A fast-paced, thorough introduction to Python programming.',
        'price': 800,
        'publication_date': date(2019, 5, 3),
        'isbn': '9781593279288',
    },
    {
        'title': 'Learning Python',
        'author': 'Mark Lutz',
        'description': 'In-depth introduction to the core Python language.',
        'price': 950,
        'publication_date': date(2013, 6, 12),
        'isbn': '9781449355739',
    },
    {
        'title': 'Effective Java',
        'author': 'Joshua Bloch',
        'description': 'Best practices for writing robust and maintainable Java code.',
        'price': 1100,
        'publication_date': date(2017, 12, 27),
        'isbn': '9780134685991',
    },
    {
        'title': 'Java: The Complete Reference',
        'author': 'Herbert Schildt',
        'description': 'Comprehensive guide to the Java programming language.',
        'price': 1200,
        'publication_date': date(2018, 11, 9),
        'isbn': '9781260440232',
    },
    {
        'title': 'The C Programming Language',
        'author': 'Brian W. Kernighan & Dennis M. Ritchie',
        'description': 'Classic introduction to the C programming language.',
        'price': 600,
        'publication_date': date(1988, 3, 22),
        'isbn': '9780131103627',
    },
    {
        'title': 'C++ Primer',
        'author': 'Stanley B. Lippman, Josée Lajoie, & Barbara E. Moo',
        'description': 'Comprehensive introduction to C++ programming.',
        'price': 1300,
        'publication_date': date(2012, 8, 16),
        'isbn': '9780321714114',
    },
    {
        'title': 'Discrete Mathematics and Its Applications',
        'author': 'Kenneth H. Rosen',
        'description': 'Comprehensive guide to discrete mathematics.',
        'price': 1400,
        'publication_date': date(2011, 6, 14),
        'isbn': '9780073383095',
    },
    {
        'title': 'Introduction to the Theory of Computation',
        'author': 'Michael Sipser',
        'description': 'Introduction to the fundamental concepts of computational theory.',
        'price': 1250,
        'publication_date': date(2012, 2, 15),
        'isbn': '9781133187790',
    },
    {
        'title': 'Django for Beginners',
        'author': 'William S. Vincent',
        'description': 'Learn to build web applications with Django.',
        'price': 700,
        'publication_date': date(2018, 6, 12),
        'isbn': '9781983172662',
    },
    {
        'title': 'Two Scoops of Django',
        'author': 'Daniel Roy Greenfeld & Audrey Roy Greenfeld',
        'description': 'Best practices for the Django web framework.',
        'price': 1600,
        'publication_date': date(2015, 5, 15),
        'isbn': '9780981467344',
    },
    {
        'title': 'Web Development with Django',
        'author': 'Ben Shaw, Saurabh Badhwar, Andrew Bird, & Aidas Bendoraitis',
        'description': 'Comprehensive guide to web development using Django.',
        'price': 1800,
        'publication_date': date(2021, 3, 26),
        'isbn': '9781801072724',
    },
    {
        'title': 'Deep Learning',
        'author': 'Ian Goodfellow, Yoshua Bengio, & Aaron Courville',
        'description': 'Comprehensive introduction to deep learning.',
        'price': 1900,
        'publication_date': date(2016, 11, 18),
        'isbn': '9780262035613',
    },
    {
        'title': 'Pattern Recognition and Machine Learning',
        'author': 'Christopher M. Bishop',
        'description': 'Introduction to pattern recognition and machine learning.',
        'price': 1700,
        'publication_date': date(2006, 8, 17),
        'isbn': '9780387310732',
    },
    {
        'title': 'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow',
        'author': 'Aurélien Géron',
        'description': 'Practical guide to machine learning with Python.',
        'price': 1500,
        'publication_date': date(2019, 10, 15),
        'isbn': '9781492032649',
    },
    {
        'title': 'Introduction to Algorithms',
        'author': 'Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, & Clifford Stein',
        'description': 'Comprehensive introduction to algorithms.',
        'price': 2000,
        'publication_date': date(2009, 7, 31),
        'isbn': '9780262033848',
    },
    {
        'title': 'Computer Networking: A Top-Down Approach',
        'author': 'James F. Kurose & Keith W. Ross',
        'description': 'Introduction to computer networking principles.',
        'price': 1350,
        'publication_date': date(2016, 3, 10),
        'isbn': '9780133594140',
    },
    {
        'title': 'Operating System Concepts',
        'author': 'Abraham Silberschatz, Peter B. Galvin, & Greg Gagne',
        'description': 'Comprehensive guide to operating system principles.',
        'price': 1450,
        'publication_date': date(2018, 6, 12),
        'isbn': '9781983172662',
    },
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel García Márquez',
        'description': 'A landmark novel that tells the multi-generational story of the Buendía family, whose patriarch, José Arcadio Buendía, founded the town of Macondo.',
        'price': 1499,
        'publication_date': date(1967, 5, 30),
        'isbn': '9780060883287',
    },
    {
        'title': 'Moby-Dick',
        'author': 'Herman Melville',
        'description': 'A novel about the voyage of the whaling ship Pequod, commanded by Captain Ahab, who seeks revenge on the white whale Moby Dick.',
        'price': 1299,
        'publication_date': date(1851, 10, 18),
        'isbn': '9780142437247',
    },
    {
        'title': 'The Picture of Dorian Gray',
        'author': 'Oscar Wilde',
        'description': 'A philosophical novel about a man who sells his soul for eternal youth and beauty, while his portrait ages and records his sins.',
        'price': 1099,
        'publication_date': date(1890, 7, 1),
        'isbn': '9780141439570',
    },
    {
        'title': 'Frankenstein',
        'author': 'Mary Shelley',
        'description': 'A Gothic novel about a young scientist who creates a sapient creature in an unorthodox scientific experiment.',
        'price': 1149,
        'publication_date': date(1818, 1, 1),
        'isbn': '9780141439471',
    },
    {
        'title': 'The Grapes of Wrath',
        'author': 'John Steinbeck',
        'description': 'A novel set during the Great Depression, focusing on the Joads, a poor family of tenant farmers driven from their Oklahoma home by drought and economic hardship.',
        'price': 1399,
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
