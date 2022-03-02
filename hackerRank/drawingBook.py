# A teacher asks the class to open their books to a page number. A student can either start turning pages 
# from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, 
# page  is always on the right side:

# When they flip page , they see pages  and . Each page except the last page will always be printed on both sides. 
# The last page may only be printed on the front, given the length of the book. 
# If the book is  pages long, and a student wants to turn to page , what is the minimum number of pages to turn? 
# They can start at the beginning or the end of the book.

# Given  and , find and print the minimum number of pages that must be turned in order to arrive at page .


def pageCount(n, p):
    your_page = p // 2
    book_pages = n // 2
    # print(your_page)
    # print(book_pages)
    #
    from_front = your_page
    from_back = book_pages - your_page

    # print(from_front)
    # print(from_back)

    return min(from_front, from_back)

    

# print(pageCount(5,4))
print(pageCount(6,2))