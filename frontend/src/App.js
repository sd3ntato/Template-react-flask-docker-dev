import React from 'react';

function App() {

  fetch('/api/data').then(res => res.json()).then(data => {
    console.log(data);
  });

  return (
    <div style={{ textAlign: 'center' }}>
      <header>
        <p>
          Edist <code>src/App.js</code> and save to reload.d
        </p>
        <a href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
