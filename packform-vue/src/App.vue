<template>
  <div id="app">
    <OrderList v-bind:customers="customers"/>
  </div>
</template>

<script>
import OrderList from './components/OrderList'

export default {
  name: 'App',
  components: {
    OrderList
  },
  data: () => {
    return {
      customers : [
      { id: 0, customer_name: 'Alex', customer_company: 'Packform' },
      { id: 1, customer_name: 'Phoebe', customer_company: 'Packform' },
      { id: 2, customer_name: 'Jane', customer_company: 'Packform' },
      { id: 3, customer_name: 'Steve', customer_company: 'Packform' },
      { id: 4, customer_name: 'Alan', customer_company: 'Packform' }
    ]
    }
  }
}
</script>
