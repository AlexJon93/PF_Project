<template>
    <div>
        <div v-if="loading"><spinner/></div>
        <div v-else><order-list v-bind:orders="orders"/></div>        
    </div>
</template>

<script>
import OrderList from '../components/OrderList'
import Spinner from '../components/Spinner'

export default {
    name: 'OrderPage',
    components: {
        OrderList,
        Spinner
    },
    data(){
        return {
            orders: [],
            loading: true
        }
    },
    created() {
        this.getOrders()
    },
    methods: {
        getOrders(){
            fetch('http://localhost:5000/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(res => res.json())
            .then(orders => {
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