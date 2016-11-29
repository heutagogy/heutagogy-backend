DROP TABLE IF EXISTS bookmarks;
CREATE TABLE bookmarks (
  timestamp text,
  url text not null,
  title text
);
