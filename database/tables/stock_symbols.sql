-- Table: public.stock_symbols

-- DROP TABLE public.stock_symbols;

CREATE TABLE public.stock_symbols
(
    id integer NOT NULL DEFAULT nextval('stock_symbols_id_sq'::regclass),
    "longname" character varying(255) COLLATE pg_catalog."default",
    "shortname" character varying(11) COLLATE pg_catalog."default",
    CONSTRAINT "PK_stockSymbolsID" PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.stock_symbols
    OWNER to postgres;

GRANT ALL ON TABLE public."stock_symbols" TO postgres;