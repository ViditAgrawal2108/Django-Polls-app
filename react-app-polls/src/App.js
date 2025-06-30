import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import QuestionList from './components/QuestionList';
import QuestionDetail from './components/QuestionDetail';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<QuestionList />} />
        <Route path="/questions/:id" element={<QuestionDetail />} />
      </Routes>
    </Router>
  );
}

export default App;
