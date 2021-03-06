import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import axios from 'axios'


class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'authors': []
       }
   }

   componentDidMount() {
   axios.get('http://localhost:8080/api/authors')
       .then(response => {
           const authors = response.data
               this.setState(
               {
                   'authors': authors
               }
           )
       }).catch(error => console.log(error))
}
   // componentDidMount() {
   //     const authors = [
   //         {
   //             'first_name': 'Фёдор',
   //             'last_name': 'Достоевский',
   //             'birthday_year': 1821
   //         },
   //         {
   //             'first_name': 'Александр',
   //             'last_name': 'Грин',
   //             'birthday_year': 1880
   //         },
   //     ]
   //     this.setState(
   //         {
   //             'authors': authors
   //         }
   //     )
   // }

   render () {
       return (
           <div>
               <AuthorList authors={this.state.authors} />
           </div>
       )
   }
}


export default App;