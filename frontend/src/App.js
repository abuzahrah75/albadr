import React from 'react';

import {Route, Switch,} from 'react-router-dom'

import './App.css';

import NavBar from './components/NavBar'
import Utama from './components/pages/Utama'
import Projek from './components/pages/Projek'
import About from './components/pages/About'

function App() {
  return (
    <div className="App">
     <NavBar />
     <Switch>
            <Route path="/" exact component={Utama} />
            <Route path="/projek" exact component={Projek} />
            <Route path="/about" exact component={About} />

            <Route path="*" component={ ()=> "404 NOT FOUND"}/>
      </Switch>
    </div>
  );
}

export default App;
