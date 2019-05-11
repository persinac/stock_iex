CREATE SEQUENCE public.stock_symbols_id_sq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE public.stock_symbols_id_sq
    OWNER TO postgres;