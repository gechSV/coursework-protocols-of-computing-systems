# coursework-protocols-of-computing-systems
# Data base model
### NewsPosts(table)
* `id` - Primary key;
* `category` - Foreign key(Categories table);
* `date` (date - DateField) - date publication news;
* `title` (text - TextField);
* `text` (text - TextField);
* `image` (text - TextField) - address.

### Categories(table)
* `id` - Primary key;
* `category` (text - TextField)
  
