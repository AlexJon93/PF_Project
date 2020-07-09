<template>
    <div>
        <ul>
            <li v-for="customer in customers" :key="customer.id">
                <OrderListItem v-bind:customer="customer"/>
            </li>
        </ul>
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
        customers: Array
    }
}
</script>