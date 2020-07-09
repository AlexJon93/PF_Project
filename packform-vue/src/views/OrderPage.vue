<template>
    <div>
        <input type="text" placeholder="Search" v-on:keyup="setSearch($event)"/>
        <label>From: <input type="date" id="from" v-bind:max="this.dates.to" v-on:change="setDate($event)"/></label>
        <label>To: <input type="date" id="to" v-bind:min="this.dates.from" v-on:change="setDate($event)" /></label>

        <div v-if="loading"><spinner/></div>
        <div v-else><order-list v-bind:orders="orders"/></div>
        <paginator v-bind:current-page="this.currentPage" v-bind:total-pages="this.pages" v-on:change-page="this.setPage"/>
    </div>
</template>

<script>
import OrderList from '../components/OrderList'
import Spinner from '../components/Spinner'
import Paginator from '../components/Paginator'

export default {
    name: 'OrderPage',
    components: {
        OrderList,
        Spinner,
        Paginator
    },
    data(){
        return {
            orders: [],
            loading: true,
            dates: {
                from: '',
                to: ''
            },
            search: '',
            pages: 0,
            currentPage: 0
        }
    },
    created() {
        this.getOrders()
    },
    methods: {
        getOrders(){
            const url = this.generateUrl()
            fetch(url, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(res => res.json())
            .then(data => {
                this.orders = data.orders
                this.pages = data.pages
                this.loading = false
            })
            .catch(error => {
                console.error(error)
                this.loading = false
            })
        },
        generateUrl(){
            const params = {
                search: this.search === '' ? undefined : this.search,
                from: this.dates.from === '' ? undefined : this.dates.from,
                to: this.dates.to === '' ? undefined : this.dates.to,
                page: this.currentPage === 0 ? undefined : this.currentPage
            }

            Object.keys(params).forEach(key => params[key] === undefined ? delete params[key] : null)
            
            var url = new URL('http://localhost:5000')
            var params_query = new URLSearchParams(params)
            url.search = params_query
            return url
        },
        setSearch(event){
            this.search = event.target.value
            this.getOrders()            
        },
        setDate(event){
            this.dates[event.target.id] = event.target.value
            this.getOrders()
        },
        setPage(position){
            this.currentPage = position
            this.getOrders()
        }
        
    }
}
</script>