import React from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios'
import {HashRouter, BrowserRouter, Route, Router, Link, Switch, Redirect} from 'react-router-dom'
import ProjectList from "./components/Projects";
import NoteList from "./components/Notes";
import DevelopmentList from "./components/Developments";
import ParticipantList from "./components/Participants";
// import BookList from "./components/Book";
// import AuthorBookList from "./components/AuthorBook";
// import AuthorList from './components/Author.js'

class App extends React.Component {

   constructor(props) {
       super(props)
       this.state = {
           'participants': [],  /*Участники*/
           'projects':[],
           'notes':[]
       }
   }

   componentDidMount() {
       // axios.get('http://localhost:8080/participants/?limit=100&isActivate=true').then(response => {
       //     const participants = response.data.results
       //     this.setState({'participants': participants})
       // }).catch(error => console.log(error));
       axios.get('http://localhost:8080/projects/?limit=100&isActivate=true').then(response => {
           const projects = response.data.results
           this.setState({'projects': projects})
       }).catch(error => console.log(error))
       axios.get('http://localhost:8080/notes/?limit=100&isActivate=true').then(response => {
           const notes = response.data.results
           this.setState({'notes': notes})
       }).catch(error => console.log(error))
       axios.get('http://localhost:8080/developments/?limit=100&isActivate=true').then(response => {
           const developments = response.data.results
           this.setState({'developments': developments})
       }).catch(error => console.log(error))
       axios.get('http://localhost:8080/participants/?limit=100&isActivate=true').then(response => {
           const participants = response.data.results
           this.setState({'participants': participants})
       }).catch(error => console.log(error))
   }

   render () {
       return (
           <div>
               <BrowserRouter>
                   <nav>
                       <ul>
                           <li>
                               <Link to='/'>Проекты</Link>
                           </li>
                           <li>
                               <Link to='/notes'>Заметки</Link>
                           </li>
                           <li>
                               <Link to='/developments'>Разработчики</Link>
                           </li>
                           <li>
                               <Link to='/participants'>Участники проекта</Link>
                           </li>
                       </ul>
                   </nav>
                   <Switch>
                       <Route exact path='/' component={() => <ProjectList projects={this.state.projects} />} />
                       <Route exact path='/notes' component={() => <NoteList notes={this.state.notes} />} />
                       <Route exact path='/developments' component={() => <DevelopmentList developments={this.state.developments} />} />
                       <Route exact path='/participants' component={() => <ParticipantList participants={this.state.participants} />} />
                       <Route path="/developments/:id">
                            <DevelopmentList developments={this.state.developments} />
                        </Route>
                       <Route path="/nodes/:id">
                            <NoteList notes={this.state.notes} />
                        </Route>
                       {/*<Route exact path='/participants' component={() => <ParticipantList books={this.state.participants} />} />*/}
                       {/*<Redirect from='/authors' to='/' />*/}
                       {/* <Route path="/developments/:uid">*/}
                       {/*     <DevelopmentList developments={this.state.developments} />*/}
                       {/* </Route>*/}
                       {/*<Route path="/notes/:uid">*/}
                       {/*     <DevelopmentList developments={this.state.developments} />*/}
                       {/* </Route>*/}
                       {/*<Route component={NotFound404} />*/}
                   </Switch>
               </BrowserRouter>
               {/*<AuthorList authors={this.state.authors} />*/}
               {/*<BookList books={this.state.books} />*/}
           </div>
       )
   }
}


export default App;