class Search:
    customer_name_query\
        ="""select customer_id
            from customer
            where first_name ilike %s 
                or last_name ilike %s"""

    customer_id_query\
        ="""select
                case when c.store_id = 1 then '🇨🇦 Lethbridge' else '🇦🇺 Woodridge' end as store ,
                c.first_name || ' ' || c.last_name as name,
                c.customer_id ,
                c.email ,
                '('||left(a.phone,4) ||') '|| substring(a.phone,5,4) ||'-'|| right(a.phone,4) as phone ,
                a.address,
                c.create_date ,
                case when n.customer_id is not null then 'Overdue' else 'Normal' end as status ,
                c.store_id
            from customer c
            inner join address a
                on c.address_id = a.address_id
            left join not_return_customer n
                on n.customer_id = c.customer_id
            where c.activebool is true
                and c.customer_id = ANY(%s)""" # ANY(%s) : 상자에 담겨있는 ID들을 전부 비교
    # <-- View Table Create -->
    # CREATE OR REPLACE VIEW public.not_return_customer as
    #  select distinct r.customer_id
    #  from rental r
    #  inner join inventory i
    #      on r.inventory_id = i.inventory_id
    #  inner join film f
    #      on i.film_id = f.film_id
    #  where r.return_date is null
    #      and r.rental_date + (f.rental_duration * INTERVAL '1 day') < now();

    film_title_query\
        ="""select distinct inventory_id
            from inventory_data
            where title ilike %s """

    inventory_id_query\
        ="""select
                inventory_id ,
                title ,
                case when store_id = 1 then '🇨🇦 Lethbridge' else '🇦🇺 Woodridge' end as store ,
                case when return_date is not null then 'In stock' else 'Checked out' end as status ,
                rental_date ,
                '$'||rental_rate ,
                store_id
            from inventory_data
            where status is not null
            and inventory_id = ANY(%s)""" # ANY(%s) : 상자에 담겨있는 ID들을 전부 비교
    # <-- View Table Create -->
    # CREATE OR REPLACE VIEW public.inventory_data as (
    # select
    #     i.inventory_id ,
    #     f.title ,
    #     i.store_id ,
    #     r.rental_date ,
    #     r.return_date ,
    #     case when rank() over (
    #         partition by i.inventory_id , i.store_id order by r.rental_date desc) = 1 then 1
    #     else null end as status ,
    #     f.rental_rate
    # from inventory i
    # inner join film f
    #     on i.film_id = f.film_id
    # inner join rental r
    #     on i.inventory_id = r.inventory_id);