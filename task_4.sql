-- show table details
CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY NOT NULL,
    title VARCHAR(130),
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);
SHOW CREATE TABLE books;