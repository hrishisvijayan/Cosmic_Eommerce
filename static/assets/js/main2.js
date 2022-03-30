
new Vue({
    el: '#app',
    data() {
                            
                return {
                    counter: 1
                }
            },
    methods: {
                changeCounter: function(num){
                    this.counter += +num
                    console.log(this.counter)
                    !isNaN(this.counter) && this.counter > 0 ? this.counter : this.counter = 0;
                
                }
            },
            computed: {
    
            }
    
        })
    
    
    
    