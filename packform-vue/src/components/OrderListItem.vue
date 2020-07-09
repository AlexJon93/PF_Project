<template>
    <tr>
        <td>{{ order.order_name }}</td>
        <td>{{ order.customer_company }}</td>
        <td>{{ order.customer_name }}</td>
        <td>{{ this.order_date }}</td>
        <td>{{ this.delivered_amount }}</td>
        <td>{{ this.total_amount }}</td>
    </tr>
</template>

<script>
import dayjs from 'dayjs'

export default {

    name: "OrderListItem",
    props: {
        order: Object
    },
    computed: {
        delivered_amount: function(){
            return this.order.delivered_amount === '-' ? '-' : '$'+Number(this.order.delivered_amount).toFixed(2)
        },
        total_amount: function(){
            return this.order.total_amount === '-' ? '-' : '$'+Number(this.order.total_amount).toFixed(2)
        },
        order_date: function(){
            return dayjs(this.order.created_at).format('MMM D, h:mm A')
        }
    }
}
</script>