<template>
    <main class="wrapper">
        <div class="container orderpage">
            <input class="row" type="text" placeholder="Search" v-on:keyup="setSearch($event)"/>
            <div class="row">
                <label class="fromdate">From: <input type="date" id="from" v-bind:max="this.dates.to" v-on:change="setDate($event)"/></label>
                <label class="todate">To: <input type="date" id="to" v-bind:min="this.dates.from" v-on:change="setDate($event)" /></label>
            </div>
    
            <div class="row" v-if="loading"><spinner/></div>
            <div class="row" v-else><order-list v-bind:orders="orders"/></div>
            <paginator class="row" v-bind:current-page="this.currentPage" v-bind:total-pages="this.pages" v-on:change-page="this.setPage"/>
        </div>
        <div class="gap"></div>
        <order-footer/>
    </main>
</template>

<script>
import OrderList from '../components/OrderList'
import Spinner from '../components/Spinner'
import Paginator from '../components/Paginator'
import OrderFooter from '../components/OrderFooter'

export default {
    name: 'OrderPage',
    components: {
        OrderList,
        Spinner,
        Paginator,
        OrderFooter
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
            this.currentPage = 0
            this.getOrders()            
        },
        setDate(event){
            this.dates[event.target.id] = event.target.value
            this.currentPage = 0
            this.getOrders()
        },
        setPage(position){
            this.currentPage = position
            this.getOrders()
        }
        
    }
}
</script>
<style>
    .wrapper{
        display: flex;
        flex-direction: column;
        height: 100vh;
    }
    .orderpage{
        margin-top: 10vh;
    }
    .fromdate{
        padding-right: 1vw;
    }
    .gap{
        flex-grow: 1 !important;
    }
</style>