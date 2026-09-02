create extension if not exists vector;

create table if not exists documents (
    id bigserial primary key,
    source text not null,
    content text not null,
    embedding vector(1536),
    created_at timestamptz default now()
);

create index if not exists documents_source_idx on documents (source);

create index if not exists documents_embedding_idx
    on documents using hnsw (embedding vector_cosine_ops);

create or replace function match_documents(
    query_embedding vector(1536),
    match_count int default 5
)
returns table (
    id bigint,
    source text,
    content text,
    similarity float
)
language sql stable
as $$
    select
        documents.id,
        documents.source,
        documents.content,
        1 - (documents.embedding <=> query_embedding) as similarity
    from documents
    order by documents.embedding <=> query_embedding
    limit match_count;
$$;
