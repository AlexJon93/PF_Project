<template>
    <div>
        <order-list v-bind:orders="orders"/>
    </div>
</template>

<script>
import OrderList from '../components/OrderList'

export default {
    name: 'OrderPage',
    components: {
        OrderList
    },
    data(){
        return {
            orders: [],
            loading: false
        }
    },
    created() {
        this.getOrders()
    },
    methods: {
        getOrders(){
            this.loading = true
            fetch('http://localhost:5000/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(res => res.json())
            .then(orders => {
                console.log(orders)
                this.orders = orders
                this.loading = false
            })
            .catch(error => {
                console.error(error)
                this.loading = false
            })
        }
    }
}
</script>