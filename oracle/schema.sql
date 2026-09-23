create table if not exists documents (
    id integer primary key,
    source text not null,
    content text not null,
    embedding F32_BLOB(1536)
);

create index if not exists documents_source_idx on documents (source);

create index if not exists documents_embedding_idx
    on documents (libsql_vector_idx(embedding));
