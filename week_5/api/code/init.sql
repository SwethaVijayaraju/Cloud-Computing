-- Table: public.meals

-- DROP TABLE IF EXISTS public.meals;

CREATE TABLE IF NOT EXISTS public.meals
(
    id integer NOT NULL,
    name text COLLATE pg_catalog."default" NOT NULL,
    price numeric NOT NULL,
    CONSTRAINT meals_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.meals
    OWNER to root;


--
INSERT INTO public.meals VALUES (1, 'Masala Dosa', 9.99);
INSERT INTO public.meals VALUES (2, 'Ramen', 13.50);
INSERT INTO public.meals VALUES (3, 'Pop Corn Chicken', 11.99);
INSERT INTO public.meals VALUES (4, 'Chilli Chicken', 12.99);
INSERT INTO public.meals VALUES (5, 'Biriyani', 12.99);
INSERT INTO public.meals VALUES (6, 'Beans Parupu Usuli', 7.99);
INSERT INTO public.meals VALUES (7, 'Medu Vada', 6.50);
INSERT INTO public.meals VALUES (8, 'Grilled Chicken Burger', 8.99);
INSERT INTO public.meals VALUES (9, 'South Indian Filter Coffee', 5.00);
INSERT INTO public.meals VALUES (10, 'Chicken Buritto', 9.99);
INSERT INTO public.meals VALUES (11, 'Basil Pasta', 10.99);
INSERT INTO public.meals VALUES (12, 'Idly Vada Pongal Combo', 10.99);
INSERT INTO public.meals VALUES (13, 'Fried Rice', 9.99);
INSERT INTO public.meals VALUES (14, 'Apple Pie', 9.99);
INSERT INTO public.meals VALUES (15, 'Enchilada', 10.50);