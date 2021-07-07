create database bookstoredb


CREATE table books
(
 isbn text primary key,
 name text,
 author text,
 year int

)

create table authors
(
id serial primary key,
name text,
book text[]
)