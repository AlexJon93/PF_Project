<template>
    <div>
        <table>
            <thead>
                <tr>
                    <th>Customer Company</th>
                    <th>Customer Name</th>
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