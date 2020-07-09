<template>
    <div>
        <table>
            <thead>
                <tr>
                    <th>Order Name</th>
                    <th>Customer Company</th>
                    <th>Customer Name</th>
                    <th>Order Date</th>
                    <th>Delivered Amount</th>
                    <th>Total Amount</th>
                </tr>
            </thead>
            <tbody>
                <order-list-item v-for="order in orders" :key="order.id" v-bind:order="order"/>
            </tbody>
        </table>
    </div>
</template>

<script>
import OrderListItem from './OrderListItem'

export default {
    name: 'OrderList',
    components: {
        OrderListItem
    },
    props: {
        orders: Array
    }
}
</script>
<style scoped>
    table{
        border-spacing: 2em 0.2em;
    }
</style>