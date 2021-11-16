<template>
<div>
    <ul>
        <li :key="card.id" v-for="card  in cards.data.allCards" >
        {{card.name}}
        </li>
    </ul>    
</div>
</template>
    

<script>

import gql from 'graphql-tag'

export default {
    name: 'CardList',    
    //definimos la variable que almacenara el listado de cards
    data () {
    return {
        cards: ''
    }
    },    

    //declaramos un metodo que vaya a leer los cards a GraphQl
    methods:
    {
      // sera un funcion asincrona pues debera esperar hasta recibir la respuesta externa
    async leercards(){
        
        //desde aquí se realiza la consulta a Graphql y el resultado se guarda en una constante
        const cardsGraphql = await this.$apollo.query({
        query: gql`query {
                allCards {
                id
                name
                    }
                }`,     
        })

        //El dato obtenido de Graphql se lo asignamos a la variable cards que se mostrara en el template
        this.cards = cardsGraphql
        

    }      

    },
    //el metodo leercards se ejecutara cada vez que los componentes de la pagina ya esten montados
    mounted () {
    this.leercards()
    }
    
}

</script>
