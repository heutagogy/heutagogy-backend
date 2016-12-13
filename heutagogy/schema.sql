DROP TABLE IF EXISTS bookmarks;
CREATE TABLE bookmarks (
  user text,
  timestamp text,
  url text not null,
  title text,
  read bool
);
