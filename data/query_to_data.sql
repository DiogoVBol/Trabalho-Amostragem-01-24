-- Criar tabela CSV com todos os dados para fazer amostragem

select  t1.order_id,
        t1.price,
        t3.seller_state

from tb_order_items as t1

left join tb_products as t2
on t1.product_id = t2.product_id

left join tb_sellers as t3
on t1.seller_id = t3.seller_id

left join tb_orders as t4
on t1.order_id = t4.order_id

where t4.order_status = 'delivered'
