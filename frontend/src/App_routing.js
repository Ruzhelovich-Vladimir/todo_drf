import React from 'react';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js'
import BookList from './components/Book.js'
import AuthorBookList from './components/AuthorBook.js'
import axios from 'axios'
import {HashRouter, BrowserRouter, Route, Router, Link, Switch, Redirect} from 'react-router-dom'

const NotFound404 = ({ location }) =>{
    return(
        <div>
            <h1>404:Страница не найдена по адресу: '{location.pathname}' :(</h1>
        </div>
    )
}

class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'authors': [],
           'books': []
       }
   }

   componentDidMount() {
       const author1 = {id: 1, name: 'Грин', birthday_year: 1880}
       const author2 = {id: 2, name: 'Пушкин', birthday_year: 1799}
       const authors = [author1, author2]
       const book1 = {id: 1, name: 'Алые паруса', author: author1}
       const book2 = {id: 2, name: 'Золотая цепь', author: author1}
       const book3 = {id: 3, name: 'Пиковая дама', author: author2}
       const book4 = {id: 4, name: 'Руслан и Людмила', author: author2}
       const books = [book1, book2, book3, book4]

       this.setState(
           {
               'authors': authors,
               'books': books
           }
       )
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
               <BrowserRouter>
                   <nav>
                       <ul>
                           <li>
                               <Link to='/'>Main</Link>
                           </li>
                           <li>
                               <Link to='/books'>Books</Link>
                           </li>
                           <li>
                               <Link to='/authors'>Authors</Link>
                           </li>
                       </ul>
                   </nav>
                   <Switch>
                       <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />} />
                       <Route exact path='/books' component={() => <BookList books={this.state.books} />} />
                      <Redirect from='/authors' to='/' />
                       <Route path="/author/:id">
                           <AuthorBookList items={this.state.books} />
                       </Route>
                       <Route component={NotFound404} />
                   </Switch>

               </BrowserRouter>
               {/*<AuthorList authors={this.state.authors} />*/}
               {/*<BookList books={this.state.books} />*/}
           </div>
       )
   }
}


export default App;